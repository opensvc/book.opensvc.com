# Cluster Domain Name Server

The OpenSVC agent daemon can act as a remote backend for PowerDNS, serving dynamic records for services deployed within the cluster. This functionality is particularly useful when services are assigned IP addresses on private backends with internal IPAM.

If enabled, the agent configures the container's resolver (`nameserver` and `search`) to use the internal name server when starting a container.

This feature is not enabled by default.

## Records

* **A record:** `<hostname>.<svcname>.<namespace>.svc.<clustername>` for each resource that includes `ipaddr` and `hostname` in the `info` map in its states.
* **Round-Robin A Record:** `<svcname>.<namespace>.svc.<clustername>` where each resource that includes `ipaddr` in the `info` map in its states is included in the round-robin.
* **Round-Robin SRV Record:** `_<service>._<protocol>.<svcname>.<namespace>.svc.<clustername>` where each resource with an `expose` keyword matching `<port>/<service>` is included in the round-robin.

<div class="warning">

Note:

A service created without a specific namespace defaults to the `root` namespace.

</div>

## Implementation

* A farmed (flex) service.
* Each instance runs a authoritative PowerDNS server, a PowerDNS recursor and a recursor cache janitoring daemon.
* Each component runs as a privileged docker instance to have r/w access to shared unix domain sockets.
* The DNS server and recursor share the node network namespace.
* The PowerDNS server uses the dns thread of the OpenSVC daemon as a remote backend. Communications go through the `/var/lib/opensvc/dns/pdns.sock` unix domain socket.

### Docker images

* ghcr.io/opensvc/pdns_server
* ghcr.io/opensvc/pdns_recursor
* ghcr.io/opensvc/pdns_janitor

## Configure

### Preliminary steps

* Make sure the cluster configuration :kw:`cluster.name` is set to a meaningful, unique site-wide, value. It can be a fqdn like `cluster1.my.org`, or just a basename like `cluster1`.
* Choose at least 2 cluster nodes that will act as DNS backends.
* Choose a free port for the DNS to listen on (default is `5300`).
* Identify the ip addresses you want the DNS to listen on (public or private). In the following examples, `192.168.100.11` and `192.168.100.14`.
* Make sure these ip addresses are resolved to the node name as declared in the :kw:`cluster.nodes` keyword (edit /etc/hosts if necessary).
* OpenSVC agent installed, minimum version 2.1-1651
* Make sure docker or podman is installed and running on selected dns nodes.
* Make sure CNI is installed
* Make sure you have access to pull from docker.io on selected dns nodes (you can pre-pull or save/load the images if not).

### Declare DNS backends

    om cluster config update --set cluster.dns+=192.168.100.11 --set cluster.dns+=192.168.100.14

### Deploy the DNS service

    om system/cfg/dns create
    om system/cfg/dns key add --name server --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/pdns.conf.template
    om system/cfg/dns key add --name recursor --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/recursor.conf.template
    om system/cfg/dns key add --name configure --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/configure
    om system/svc/dns deploy --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/dns.conf

<div class="warning">

Note:

Make sure `allow-from` in the `recursor` key of `system/cfg/dns` contains all the cluster backend networks allowed to request the DNS (the default is `127.0.0.1/32,10.0.0.0/8,fd00::/112,::1`).

</div>

### Configure the nodes resolver

On every node, execute:

    # create the resolved configlet directory if it doesn't exist yet
    $ mkdir -p /etc/systemd/resolved.conf.d

    # install a configlet routing all requests to the cluster domain to the cluster nameservers
    $ cat - <<EOF >/etc/systemd/resolved.conf.d/opensvc.conf
    [Resolve]
    Domains=$(om cluster config get --kw cluster.name)
    DNS=$(om cluster config get --kw cluster.dns)
    EOF

    # activate the new configuration
    $ systemctl restart systemd-resolved.service

## Verify

### Verify the backend

#### Dump the records served by opensvc to the PowerDNS server

```
om daemon dns dump
```

#### Test the unix socket served by opensvc for the PowerDNS server

```
echo '{"method": "list", "parameters": {"zonename": "cluster1."}}' | sudo socat - unix://var/lib/opensvc/dns/pdns.sock | jq
```

### Verify the DNS server

#### Dump the zone contents asking the PowerDNS server

```
dig +noall +answer cluster1. AXFR @192.168.100.11 -p 5300
```

### Verify the DNS recursor

```
dig +short cluster1. SOA @192.168.100.11
```

## Administration

### Add forwarding for the reverse zones

Either switch to `--forward-zones-file` or add new elements to `forward-zones` in the `recursor` key of `system/cfg/dns`.
