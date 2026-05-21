# NFS4 High Availability Setup - Traditional Integration

This howto describes a NFS4-only HA service setup using the least possible virtualization layers (no persistent volume, no cluster backend network IP address, no ingress gateway, no container), to maximize efficiency and simplicity.

It has been tested on Red Hat Enterprise Linux 8.7 nodes.

---

## Prerequisites

| Prerequisite                              | Example                                     |
|-------------------------------------------|---------------------------------------------|
| 2 nodes                                   | node1 `5.196.34.132` / node2 `5.196.34.133` |
| A failover IP address for the NFS4 server | nfsv4.opensvc.com `5.196.34.141`            |
| Shared storage (SAN, iSCSI, ...) or DRBD  |                                             |
| OpenSVC agent 2.1+ installed              |                                             |

---

## Setup LVM2

Configure an LVM2 volume group to host an LVM2 logical volume, used as the DRBD backing device.

```bash
dnf -y install lvm2
pvcreate /dev/vdb
vgcreate datavg /dev/vdb
```

---

## Setup DRBD

### Kernel Module & Utils

[Linbit](https://www.linbit.com/) DRBD kernel modules for RHEL are available on [ElRepo](https://www.elrepo.org/).

```bash
dnf -y install https://www.elrepo.org/elrepo-release-8.el8.elrepo.noarch.rpm
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
sed -i 's/^mirrorlist/#mirrorlist/' /etc/yum.repos.d/elrepo.repo
dnf -y install kmod-drbd90 drbd90-utils
```

You can verify that DRBD is ready with the command below:

```
[root@node1 ~]# modinfo drbd | grep ^version
version:        9.1.13
```

---

## Setup the OpenSVC Cluster

### Install OpenSVC

**On both nodes:**

```bash
dnf -y install python3 python3-cryptography
curl -o opensvc-2.1-latest.rpm https://repo.opensvc.com/rpms/2.1/current
dnf -y install ./opensvc-2.1-latest.rpm
```

### Join Cluster Nodes

**On node1:**

```bash
[root@node1 ~]# om cluster set --kw hb#1.type=unicast
[root@node1 ~]# om cluster set --kw cluster.name=cluster1
[root@node1 ~]# om cluster get --kw cluster.secret
b26a1e28b84a11edab28525400d67af6
```

**On node2:**

```bash
[root@node2 ~]# om daemon join --node node1 --secret b26a1e28b84a11edab28525400d67af6
@ n:node2
local node is already frozen
join node node1
W local node is left frozen as it was already before join
```

**On node1** — unfreeze nodes and set up root SSH trust:

```bash
om node thaw
om node update ssh authorized keys --node='*'
```

> **Note:** Ensure that you can SSH as root from one node to another without being prompted for a password.

You should now have a configured cluster:

```
[root@node1 ~]# om mon
Threads                               node1        node2
 daemon         running             |
 hb#1.rx        running  [::]:10000 | /            O
 hb#1.tx        running             | /            O
 listener       running       :1214
 monitor        running
 scheduler      running

Nodes                                 node1        node2
 score                              | 69           69
  load 15m                          | 0.0          0.0
  mem                               | 12/98%:1.77g 11/98%:1.77g
  swap                              | -            -
 state                              |
```

---

## Deploy the Service

### Deploy with NFS4 Disabled

Create the OpenSVC service using the name `nfsv4`, in the `test` namespace, an ext4 filesystem, reachable using the public DNS name `nfsv4.opensvc.com` configured on interface `eth0`.

**On node1:**

```bash
om test/svc/nfsv4 deploy \
  --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/nfs/nfsv4-app-disabled.conf \
  --env dev=/dev/mapper/36001405102633e566cd41bebac415158 \
  --env fqdn=nfsv4.opensvc.com \
  --env nic=eth0
```

> **Note:** The config used in this command has all application resources (nfsdcld, rpc.idmapd, rpc.mountd, nfsd) disabled. Using that trick, we can configure NFS4 later and test core (IP, filesystem) failovers early.
>
> This is convenient for learning purposes, but in other situations you may want to use `--config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/nfs/nfsv4.conf` for a one-step deployment.

This command creates and configures the system resources needed by the service on both nodes
```
root@node1:~# om system/svc/nfsv4 print status -r
test/svc/nfsv4                    up                                               
└ instances                 
  ├ node2                            down  idle                                       
  └ node1                            up    idle started                               
    └ resources                                                                        
      ├ ip#1                ...../..  up    5.196.34.141/255.255.255.224 eth0 nfsv4.opensvc.com   
      ├ fs#1                ........  up    ext4 /dev/mapper/36001405102633e566cd41beba
      │                                     c415158@/srv/nfsv4.test.svc.cluster1   
      ├ app#0               ..D../..  n/a   forking app.forking                        
      ├ app#1               ..D../..  n/a   simple app.simple                          
      ├ app#2               ..D../..  n/a   simple app.simple                          
      ├ app#3               ..D../..  n/a   forking app.forking                        
      ├ app#4               ..D../..  n/a   simple app.simple                          
      └ sync#i0             ..D../..  n/a   rsync    

[root@node1 ~]# df -h /srv/nfsv4.test.svc.cluster1
Filesystem                                     Size  Used Avail Use% Mounted on
/dev/mapper/36001405102633e566cd41bebac415158  974M   96K  907M   1% /srv/nfsv4.test.svc.cluster1
```

### Test the Core Failover

This step only serves to ensure that the IP, and filesystem fail over back and forth between nodes before continuing with the NFS4 layer setup.

#### Initial Situation

The green `O` means that the service is currently running on `node1`.

**On node1 or node2:**

```
[root@node1 ~]# om test/svc/nfsv4 mon
test/svc/nfsv4                   node1 node2
 test/svc/nfsv4  up  ha  1/1   |  O^    S
```

#### Move Service to node2

The `switch` action will relocate the service to the other node. The `^` means that the service is not running on its preferred node.

**On node1 or node2:**

```
[root@node1 ~]# om test/svc/nfsv4 switch
@ n:node1 o:test/svc/nfsv4 sc:n
test/svc/nfsv4 defer target state set to placed@node2

[root@node1 ~]# om test/svc/nfsv4 mon
test/svc/nfsv4                   node1 node2
 test/svc/nfsv4  up^  ha  1/1  |  S^    O
```

#### Move Service Back to node1

You can use either the `switch` action or `giveback` to move the service to its preferred node.

**On node1 or node2:**

```
[root@node1 ~]# om test/svc/nfsv4 giveback
@ n:node1 o:test/svc/nfsv4 sc:n
test/svc/nfsv4 defer target state set to placed

[root@node1 ~]# om test/svc/nfsv4 mon
test/svc/nfsv4                   node1 node2
 test/svc/nfsv4  up  ha  1/1   |  O^    S
```

---

## Enable NFS4

We must make sure systemd will not manage NFS4 services — only OpenSVC must be in charge of these servers.

### Disable NFS4-Related systemd Unit Files

**On both nodes:**

```bash
systemctl mask --now rpc-statd.service \
                     rpcbind.service \
                     rpcbind.socket \
                     nfs-server.service \
                     nfs-mountd.service \
                     nfs-idmapd.service \
                     nfsdcld.service
```

### Download NFS4 Server Config Files

The NFS4 configuration files are stored in the replicated filesystem.

**On node1:**

```bash
curl -o /srv/nfsv4.test.svc.cluster1/etc/nfs.conf \
  https://raw.githubusercontent.com/opensvc/opensvc_templates/main/nfs/etc.nfs.conf

curl -o /srv/nfsv4.test.svc.cluster1/etc/exports \
  https://raw.githubusercontent.com/opensvc/opensvc_templates/main/nfs/etc.exports.conf
```

### Install NFS4 Server Config Files

**On both nodes:**

```bash
rm -f /etc/nfs.conf ; rm -f /etc/exports ; rmdir /etc/exports.d
ln -s /srv/nfsv4.test.svc.cluster1/etc/nfs.conf /etc/nfs.conf
ln -s /srv/nfsv4.test.svc.cluster1/etc/exports /etc/exports
```

### Adjust the Config Files

**On node1:**

```bash
sed -i 's@ROOTFS@/srv/nfsv4.test.svc.cluster1@' /srv/nfsv4.test.svc.cluster1/etc/nfs.conf
sed -i 's@FQDN@nfsv4.opensvc.com@' /srv/nfsv4.test.svc.cluster1/etc/nfs.conf
sed -i 's@ROOTFS@/srv/nfsv4.test.svc.cluster1@' /srv/nfsv4.test.svc.cluster1/etc/exports
```

### Enable & Start OpenSVC App Resources

**On node1:**

```
[root@node1 ~]# om test/svc/nfsv4 enable --rid app
@ n:node1 o:test/svc/nfsv4 sc:n
remove app#3.disable
remove app#2.disable
remove app#1.disable
remove app#4.disable

[root@node1 ~]# om test/svc/nfsv4 start --rid app
INF test/svc/nfsv4: >>> do start [om test/svc/nfsv4 start --rid app] (origin user, sid a00da93a-d513-4d89-8a42-19267b8146fa)             
INF test/svc/nfsv4: app#0: run: /usr/bin/om exec --pg /opensvc.slice/opensvc-ns.system.slice/opensvc-ns.system-svc.nfstrad.slice/opensvc-ns.system-svc.nfstrad-app.0.slice -- mount -t rpc_pipefs sunrpc /var/lib/nfs/rpc_pipefs          
INF test/svc/nfsv4: app#1: run: /usr/bin/om exec --pg /opensvc.slice/opensvc-ns.system.slice/opensvc-ns.system-svc.nfstrad.slice/opensvc-ns.system-svc.nfstrad-app.1.slice -- /usr/sbin/nfsdcld --foreground          
INF test/svc/nfsv4: app#2: run: /usr/bin/om exec --pg /opensvc.slice/opensvc-ns.system.slice/opensvc-ns.system-svc.nfstrad.slice/opensvc-ns.system-svc.nfstrad-app.2.slice -- /usr/sbin/rpc.idmapd -f          
INF test/svc/nfsv4: app#3: trigger non-blocking pre start: /usr/sbin/exportfs -r         
INF test/svc/nfsv4: app#3: run: /usr/bin/om exec --pg /opensvc.slice/opensvc-ns.system.slice/opensvc-ns.system-svc.nfstrad.slice/opensvc-ns.system-svc.nfstrad-app.3.slice -- /usr/sbin/rpc.nfsd 8          
INF test/svc/nfsv4: app#3: trigger non-blocking post start: /bin/sh -c 'if systemctl -q is-active gssproxy; then systemctl reload gssproxy; fi'         
INF test/svc/nfsv4: app#4: run: /usr/bin/om exec --pg /opensvc.slice/opensvc-ns.system.slice/opensvc-ns.system-svc.nfstrad.slice/opensvc-ns.system-svc.nfstrad-app.4.slice -- /usr/sbin/rpc.mountd --foreground          
INF test/svc/nfsv4: <<< done start [om test/svc/nfsv4 start --rid app] in 814.419694ms, instance status is now up        

[root@node1 ~]# om test/svc/nfsv4 print status -r
test/svc/nfsv4                    up                                               
└ instances                 
  ├ node2                            down  idle                                       
  └ node1                            up    idle started                               
    └ resources                                                                        
      ├ ip#1                ...../..  up    5.196.34.141/255.255.255.224 eth0 nfsv4.opensvc.com   
      ├ fs#1                ........  up    ext4 /dev/mapper/36001405102633e566cd41beba
      │                                     c415158@/srv/nfsv4.test.svc.cluster1   
      ├ app#0               ...../..  up    forking app.forking                                                                  
      ├ app#1               ...../..  up    simple app.simple                                                                    
      ├ app#2               ...../..  up    simple app.simple                                                                    
      ├ app#3               ...../..  up    forking app.forking                                                                  
      ├ app#4               ...../..  up    simple app.simple                           
      └ sync#i0             ..D../..  n/a   rsync    
```

---

## Test

### Connect Clients

You should be able to mount the NFS root share from any client:

```bash
[root@client ~]# mount -v -t nfs4 -o proto=tcp,port=2049 nfsv4.opensvc.com:/ /mnt
mount.nfs4: timeout set for Thu Mar  2 17:11:37 2023
mount.nfs4: trying text-based options 'proto=tcp,port=2049,vers=4.2,addr=5.196.34.141,clientaddr=37.59.71.10'

[root@client ~]# df -h /mnt
Filesystem           Size   Used  Avail Use% Mounted on
nfsv4.opensvc.com:/  4860M     0  4560M   0% /mnt
```

### Test the Failover

Start NFS client activity (fio runs, for example), then reboot the node hosting the active service instance.

---

> **Warning:** This howto uses the default NFS4 security and tuning configurations. You may now tune the NFS4 configuration to match your specific requirements.