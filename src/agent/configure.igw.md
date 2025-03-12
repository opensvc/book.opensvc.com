# Ingress Gateway

Services configured to obtain an IP address from a backend network are not naturally accessible to clients outside the cluster.

To expose them, the user or a cluster administrator can deploy a ingress gateway configured with a public IP address.

HAProxy is our recommended program to route layer 4 and layer 7 communications from the frontend to the backend servers.

## Behaviour

The backend composition is kept up to date by HAProxy the `resolvers` mechanism.

To declare the cluster dns in the HAProxy configuration:

    resolvers clusterdns
        parse-resolv-conf
        accepted_payload_size 8192

As the HAProxy server runs in a container resource started by OpenSVC, the `/etc/resolv.conf` file contains the cluster nameservers IP address.
The `parse-resolv-conf` tells HAProxy to read the nameservers from there.

This `resolvers` configuration can be referenced in every `backend` definition like:

    backend svc1
        option httpchk GET /health
        server-template svc1_ 1 svc1.ns1.svc.${CLUSTERNAME}:8080 resolvers clusterdns check init-addr none

## Configurations

* **Intra-Cluster Load-Balancing:** Run only one HAproxy on the cluster, in a failover topology svc.
* **Extra-Cluster Load-Balancing:** Every node runs a HAProxy exposing the same servers. The upstream load-balancer picks one.

## Intra-Cluster Load-Balancing Configuration

Listen on port 443, with a self-signed certificate.

Deploy a haproxy service using the basic example from the [igw_haproxy template](https://github.com/opensvc/opensvc_templates/tree/main/igw_haproxy) page on github.

    # Create a self signed key and certificate
    sudo om testigw/sec/haproxy create
    sudo om testigw/sec/haproxy certificate create

    # Create a haproxy configuration as a cfg key
    sudo om testigw/cfg/haproxy create
    sudo om testigw/cfg/haproxy key add --name haproxy.cfg --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/igw_haproxy/basic-cfg-haproxy.cfg

    # Deploy the Ingress Gateway svc
    # * change the network to a cluster spaning network if you have one setup
    # * make sure requests from this network are allowed by the nameservers
    sudo om testigw/svc/haproxy deploy --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/igw_haproxy/basic-svc.conf --kw ip#1.network=default

A `ip#1` failover-capable public IP address should be added and started for this service to be useful to extra-cluster clients, but it can be tested from a cluster node already.

    # Store the haproxy IP address allocated on start
    eval IP=$(sudo om testigw/svc/haproxy resource ls -o json --rid ip --node $HOSTNAME| jq .items[].data.status.info.ipaddr)

    # Test, faking a DNS resolution of svc1.opensvc.com to the haproxy ip address
    curl -o- -k --resolve svc1.opensvc.com:443:$IP https://svc1.opensvc.com

    # Deploy a test webserver to populate the svc1.opensvc.com backend:
    # * change the network to a cluster spaning network if you have one setup
    # * make sure requests from this network are allowed by the nameservers
    sudo om testigw/svc/svc1 deploy --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/igw_haproxy/nginx.conf --kw ip#1.network=default --wait

    # Retest until available
    curl -o- -k --resolve svc1.opensvc.com:443:$IP https://svc1.opensvc.com

## Automated Certificate Management Environment

The [igw_haproxy template](https://github.com/opensvc/opensvc_templates/tree/main/igw_haproxy) page on github also documents the deployment of a HAProxy cluster ingress gateway service implementing ACME.
