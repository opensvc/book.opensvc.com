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


## Configure the listener

Set an appropriate cluster name in cluster.conf, then

```
export CLUSTERNAME=$(om cluster get --kw cluster.name)
```

<div class="warning">
Note: Changing the cluster name once the cluster is setup and used is hard.
</div>

The listener needs a TLS certificate to allow remote connections.

The cluster can generate this certificate, or an external PKI can be trusted by the cluster.

### With external PKI

Store the Certificate Authority certificate chain in a secret.

```
om system/sec/ca-external create
om system/sec/ca-external add --key certificate_chain --from ~/ca_crt_chain.pem
```

Create the Certificate for the TLS listener as a secret.

```
om system/sec/cert-$CLUSTERNAME create
om system/sec/cert-$CLUSTERNAME gen cert
```

Make the external CA sign this certificate and load the resulting certificate key.

```
om system/sec/cert-$CLUSTERNAME create --kw cn=vip.$CLUSTERNAME.mycorp
om system/sec/cert-$CLUSTERNAME decode --key certificate_signing_request >~/$CLUSTERNAME.csr

#### signing procedure ####

om system/sec/cert-clu add --key certificate --from ~/$CLUSTERNAME_crt.pem
om system/sec/cert-clu add --key certificate_chain --from ~/$CLUSTERNAME_crt_chain.pem
```


Declare this Certificate Authority for the TLS listener.

```
om cluster set --kw cluster.ca=system/sec/ca-external
```

If available, declare the Certificate Revokation List location, so the listener can refuse revoked certificates before their expiration.

```
om cluster set --kw cluster.crl=http://crl.mycorp
```

### With internal PKI

The v3 agent creates a default CA and listener certificate.

The following commands are only necessary to create custom certificates, or if the agent is v2.

Create the CA certificate.

```
om system/sec/ca-$CLUSTERNAME create
om system/sec/ca-$CLUSTERNAME set \
    --kw o=mycorp \
    --kw c=fr \
    --kw email=admin@mycorp
om system/sec/ca-$CLUSTERNAME gen cert
```

Create the Certificate for the TLS listener as a secret.

```
om system/sec/cert-$CLUSTERNAME create \
    --kw ca=system/sec/ca-$CLUSTERNAME \
    --kw cn=vip.$CLUSTERNAME.mycorp
om system/sec/cert-$CLUSTERNAME gen cert
```

## Create Users

```
om system/usr/root create
om system/usr/usr1 create
```

If the `system/sec/ca-$CLUSTERNAME` exists, the created users will automatically get populated with `certificate_chain`, `certificate` and `private_key` keys.
The client certificate data can be extracted with:

```
om system/usr/usr1 decode --key certificate_chain
om system/usr/usr1 decode --key certificate
om system/usr/usr1 decode --key private_key
```


## Grant

```
om system/usr/root set --kw grant+=root
om system/usr/usr1 set --kw grant+=squatter
om system/usr/usr1 set --kw grant+=admin:ns1
om system/usr/usr1 set --kw 'grant+=guest:*'
```

<div class="warning">

See Also:

* [Configure Client](agent.configure.client.md)
* [RBAC](agent.rbac)

</div>
