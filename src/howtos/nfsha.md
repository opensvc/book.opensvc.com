# NFS High Availability Setup

NFS is a tricky beast to set up for high availability. Without proper configuration, NFS clients tend to hang waiting for I/O completion on the shares. This guide covers the Linux NFS server configuration for smooth failover.

---

## OpenSVC HA Setup

Create the OpenSVC service and config for the NFS server using the name `nfssvc`, in the `test` namespace. The service will use `192.168.1.100` as the virtual IP address with mask `24` configured on interface named `eth0` and the shared storage will be mounted on `your/dev/path`.

**On the master node**
```bash
om test/svc/nfssvc create --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/nfs/nfs.conf \
--env dev=/your/dev/path \
--env ip=192.168.1.100 \
--env mask=24 \
--env nic=eth0
  
om test/cfg/nfssvc create
```

---

## NFS Configuration

Linux NFS service uses `/var/lib/nfs` to store both node-private and service-private data. The tricky part of the HA setup is to separate this data.

### NFS Server Startup

NFS startup will be handled by the OpenSVC service. Stop the NFS service and inhibit its launch at server startup.

**On both nodes:**

```bash
systemctl stop nfs-kernel-server
systemctl stop nfs-mountd
systemctl stop nfs-server
systemctl stop rpcbind

systemctl disable nfs-kernel-server
systemctl disable nfs-mountd
systemctl disable nfs-server
```

**On the master node:**

Add the OpenSVC service startup script to the config.

```bash
om test/cfg/nfssvc key add --name script --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/nfs/script
```

### Deploy the OpenSVC Service
**On the master node:**

```bash
om test/svc/nfssvc provision
```


### Node Private Data

The data that must remain local to each node is the RPC pipefs pseudo filesystem. It is mounted by default under `/var/lib/nfs/rpc_pipefs`. As `/var/lib/nfs` will be moved to the shared filesystem, we need to change the location of this mount point.

Create the new mount point.

**On both nodes:**

```bash
mkdir /var/lib/rpc_pipefs
```

Change these system configuration files to use this new mount point.

**On both nodes:**

```
/etc/modprobe.d/modprobe.conf.dist
/etc/idmapd.conf
```

### Service Private Data

`/var/lib/nfs` contains data essential for NFS client session takeover. Thus, this directory must follow the service in case of failover.

**On the master node:**

```bash
mkdir -p /nfssvc/var/lib
mv /var/lib/nfs /nfssvc/var/lib/nfs
```

The exports list should also move with the service, to avoid configuration drift between the two nodes.

**On the master node:**

```bash
mkdir -p /nfssvc/etc
mv /etc/exports /nfssvc/etc/exports
```

**On both nodes:**

```bash
ln -sf /nfssvc/var/lib/nfs /var/lib/nfs
ln -sf /nfssvc/etc/exports /etc/exports
```

Configure NFS to listen on the service IP address.

**On both nodes:**

#### On RedHat-based distros:

`/etc/sysconfig/nfs`
```bash
STATD_HOSTNAME=<ip>
```

#### On Debian / Ubuntu:

`/etc/default/nfs-common`
```bash
STATDOPTS="--name <IP>"
```

`/etc/default/nfs-kernel-server`
```bash
RPCNFSDOPTS="--host <IP>"
RPCMOUNTDOPTS="--manage-gids --bind-addr <IP>"
```

---

## Epilog

Reboot the nodes to activate the new `rpc_pipefs` location and start testing failovers.