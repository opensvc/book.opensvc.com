# Cluster API

The cluster API can be accessed remotely through any cluster node agent listener.

The cluster API URL servername can resolve as:

* A single floating IP address, usually handled by the `system/svc/vip` failover service
* Multiple floating IP addresses
* All of the cluster nodes IP addresses
* Some of the cluster nodes IP addresses

The listener supports the following authentication methods:

* basic

  The username is given by the client in every request header.

  The `system/usr/<username>` object must exist on the cluster and provide the grants.

* x509

  The username is the `cn` of the certificate.

  The `system/usr/<username>` object must exist on the cluster and provide the grants.

* JWT

  The username and grants are token claims.

  The `system/usr/<username>` object does not need to exist.

  Added in v3 agent.

## Create Users

Example:

    #
    # Create a cluster admin user
    # ---------------------------
    om system/usr/root create --kw grant=root

    #
    # Create a namespace ns1 admin user
    # with read permission on ns2
    # ---------------------------------
    om system/usr/usr1 create --kw grant="admin:ns1 guest:ns2"


## Testing the API

A demonstration agent exposes the API manifest at [https://relay3.opensvc.com/public/ui/](https://relay3.opensvc.com/public/ui/)

    $ TOKEN=$(sudo om daemon auth token --subject usr1 --duration 10m)
    $ curl -o- -k -s -H "Authorization: Bearer $TOKEN" https://localhost:1215/whoami
    {"auth":"jwt","grant":{"guest":["ns2"], "admin": ["ns1"]},"name":"usr1","namespace":"system","raw_grant":"admin:ns1 guest:ns2"}

## Configure the listener

A cluster-level self-signed certificate authority is automatically configured upon agent installation.

The listener needs a TLS certificate to allow remote connections. This certificate is also automatically generated.

The following steps are only necessary to resilver the CA or switch to an external PKI.


### With external PKI

    export CLUSTERNAME=$(om cluster get --kw cluster.name)

Store the Certificate Authority certificate chain in a secret.

    om system/sec/ca-external create
    om system/sec/ca-external add --key certificate_chain --from ~/ca_crt_chain.pem

Create the Certificate for the TLS listener as a secret.

    om system/sec/cert-$CLUSTERNAME create
    om system/sec/cert-$CLUSTERNAME gen cert

Make the external CA sign this certificate and load the resulting certificate key.

    om system/sec/cert-$CLUSTERNAME create --kw cn=vip.$CLUSTERNAME.mycorp
    om system/sec/cert-$CLUSTERNAME decode --key certificate_signing_request >~/$CLUSTERNAME.csr

#### signing procedure ####

    om system/sec/cert-clu add --key certificate --from ~/$CLUSTERNAME_crt.pem
    om system/sec/cert-clu add --key certificate_chain --from ~/$CLUSTERNAME_crt_chain.pem


Declare this Certificate Authority for the TLS listener.

    om cluster set --kw cluster.ca=system/sec/ca-external

If available, declare the Certificate Revokation List location, so the listener can refuse revoked certificates before their expiration.

    om cluster set --kw cluster.crl=http://crl.mycorp

### With internal PKI

Create the CA certificate.

    export CLUSTERNAME=$(om cluster get --kw cluster.name)
    om system/sec/ca-$CLUSTERNAME create
    om system/sec/ca-$CLUSTERNAME set \
        --kw o=mycorp \
        --kw c=fr \
        --kw email=admin@mycorp
    om system/sec/ca-$CLUSTERNAME gen cert

Create the Certificate for the TLS listener as a secret.

    om system/sec/cert-$CLUSTERNAME create \
        --kw ca=system/sec/ca-$CLUSTERNAME \
        --kw cn=vip.$CLUSTERNAME.mycorp
    om system/sec/cert-$CLUSTERNAME gen cert

### Recreate Users certificate

    om system/usr/root gencerts
    om system/usr/usr1 gencerts


    om system/usr/usr1 decode --key certificate_chain
    om system/usr/usr1 decode --key certificate
    om system/usr/usr1 decode --key private_key


<div class="warning">

See Also:

* [RBAC](agent.rbac)

</div>
