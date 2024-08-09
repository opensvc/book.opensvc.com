# Cluster Domain Name Server

The agent daemon can act as a remote backend for PowerDNS, serving dynamic records for the services deployed. This is most interesting when services get their ip addresses on private backends with internal IPAM.

If set up, when the agent starts a container, it sets up its resolver (dns and search) so they make use of the internal name server.

This feature is not enabled by default.

## Records

* One A record `<hostname>.<svcname>.<namespace>.svc.<clustername>` for each resource embedding an ip address and a hostname in its "info".
* One round-robin A record for `<svcname>.<namespace>.svc.<clustername>`. Each resource embedding an ip address in its "info" gets a slot in the RR.
* One SRV record for `_<service>._<protocol>.<svcname>.<namespace>.svc.<clustername>`. Each resource with an expose keyword matching `<service>` and `<port>` gets a slot in the RR.

<div class="warning">

Note:

A service created without a specific namespace is assigned a `root` namespace value.

</div>

## Implementation

* A farmed (flex) service.
* Each instance runs a authoritative PowerDNS server, a PowerDNS recursor and a recursor cache janitoring daemon.
* Each component runs as a privileged docker instance to have r/w access to shared unix domain sockets.
* The DNS server and recursor share the node network namespace.
* The PowerDNS server uses the dns thread of the OpenSVC daemon as a remote backend. Communications go through the `<OSVCVAR>/dns/pdns.sock` unix domain socket.

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

```
om cluster set --kw cluster.dns+=192.168.100.11 --kw cluster.dns+=192.168.100.14
```

### Deploy the DNS service

```
om system/cfg/dns create
om system/cfg/dns add --key server --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/pdns.conf.template
om system/cfg/dns add --key recursor --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/recursor.conf.template
om system/cfg/dns add --key configure --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/configure
om system/svc/dns deploy --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/dns/dns.conf
```

<div class="warning">

Note:

Make sure `allow-from` in the `recursor` key of `system/cfg/dns` contains all the cluster backend networks allowed to request the DNS (the default is `127.0.0.1/32,10.0.0.0/8,fd00::/112,::1`).

</div>

## Verify

### Verify the backend

```
om daemon dns dump
```

```
echo '{"method": "lookup", "parameters": {"qname": "cluster1.", "qtype": "SOA"}}' | socat - /var/lib/opensvc/dns/pdns.sock

{"result": [{"ttl": 60, "qname": "cluster1.", "qtype": "SOA", "domain_id": -1, "content": "dns.cluster1. contact@opensvc.com 1 7200 3600 432000 86400"}]}
```

### Verify the DNS authoritative server

```
dig +short cluster1. SOA @192.168.100.11 -p 5300
```

### Verify the DNS recursor

```
dig +short cluster1. SOA @192.168.100.11
```

### Dump the zone contents asking DNS

```
dig +noall +answer cluster1. AXFR @192.168.100.11 -p 5300
```

### Dump the zone contents asking agent socket

Same as `om daemon dns dump`

```
echo '{"method": "list", "parameters": {"zonename": "cluster1."}}' | sudo socat - unix://var/lib/opensvc/dns/pdns.sock | jq
```

## Administration

### Add forwarding for the reverse zones

Either switch to `--forward-zones-file` or add new elements to `forward-zones` in the `recursor` key of `system/cfg/dns`.