# Ingress Gateway

Services configured to obtain an IP address from a backend network are inaccessible to clients outside the cluster.

To expose them, the user or a cluster administrator can deploy an ingress gateway configured with a public IP address.

HAProxy is our recommended program to route layer 4 and layer 7 communications from the frontend to the backend servers.

## Behaviour

The backend composition is kept up to date by HAProxy the `resolvers` mechanism.

To declare the cluster dns in the HAProxy configuration:

    resolvers clusterdns
        accepted_payload_size 8192
        nameserver ns0 1.2.3.1:53
        nameserver ns1 1.2.3.2:53

Then this resolvers configuration can be referenced in every backend definition like:

    backend website1
        option httpchk GET /health
        server-template website1_ 1 svc1.ns1.svc.clu1:8080 resolvers clusterdns check init-addr none

## Configurations

* **Intra-Cluster Load-Balancing:** Run only one HAproxy on the cluster, in a failover topology svc.
* **Extra-Cluster Load-Balancing:** Every node runs a HAProxy exposing the same servers. The upstream load-balancer picks one.

## Intra-Cluster Load-Balancing Configuration

Listen on port 443, with a self-signed certificate.

    # Create a self signed key and certificate
    sudo om testigw/sec/haproxy create
    sudo om testigw/sec/haproxy gencert

    # Create a haproxy configuration as a cfg key
    sudo om testigw/cfg/haproxy create
    sudo om testigw/cfg/haproxy add --key haproxy.cnf --from https://raw.githubusercontent.com/opensvc/opensvc_templates/main/igw_haproxy/basic-cfg-haproxy.cnf

    # Deploy the Ingress Gateway svc
    sudo om testigw/svc/haproxy deploy --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/igw_haproxy/basic-svc.conf

A `ip#1` failover-capable public IP address should be added and started for this service to be useful to extra-cluster clients, but it can be tested from a cluster node already.

    # Store the IP address allocated on start
    eval IP=$(sudo om testigw/svc/haproxy resource ls -o json --rid ip --node $HOSTNAME| jq .items[].data.status.info.ipaddr)

    # Test
    curl -o- -k --resolve svc1.acme.com:443:$IP https://svc1.acme.com

Deploy a test webserver to populate the svc1.acme.com backend:

    sudo om testigw/svc/svc1 create --config https://raw.githubusercontent.com/opensvc/opensvc_templates/main/igw_haproxy/nginx.conf
    sudo om testigw/svc/svc1 provision --wait
    curl -o- -k --resolve svc1.acme.com:443:$IP https://svc1.acme.com
