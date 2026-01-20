# Cluster API

The Cluster API provides remote access to the OpenSVC cluster management and monitoring functionality. It is accessible through the **agent listener** on any running cluster node.

## Access and Network Resolution

The Cluster API URL (server name) can be configured to resolve to various network endpoints to ensure high availability and redundancy.

Possible Resolutions:

  * **Single Floating IP**

    A single virtual IP (VIP) address, typically managed by a failover service like `system/svc/vip`. This is the most common and robust approach.

  * **Multiple Floating IP Addresses**

    A set of VIPs for complex network routing or multi-site setups.

  * **All Cluster Node IPs**

    Every physical or virtual IP address of all nodes in the cluster.

  * **Subset of Cluster Node IPs**

    A selection of node IP addresses, often used in large clusters or specific network segments.


## Authentication Methods

The agent listener supports several industry-standard authentication methods to secure access to the API.

### Basic Authentication

  * **Mechanism:** The client provides the **username** and **password** in the request header of every API call and the password is compared to the `password` key of the `system/usr/<username>` object.
  * **Authorization:** The RBAC grants are read from the `system/usr/<username>` `grant` key.
  * **User Object:** The `system/usr/<username>` object **must exist** on the cluster.

### X.509 Certificate Authentication

  * **Mechanism:** Authentication is based on a client-side X.509 certificate.
  * **Username:** The username is derived from the **Common Name (`cn`)** field of the client certificate.
  * **Authorization:** The RBAC grants are read from the `system/usr/<username>` `grant` key.
  * **User Object:** The `system/usr/<username>` object **must exist** on the cluster.

### JSON Web Token (JWT)

  * **Mechanism:** Authentication is based on a JWT passed as a bearer token.
  * **Username:** The username is derived from the `sub` token claim.
  * **Authorization:** The RBAC grants are derived from the `grant` token claim.
  * **User Object:** The `system/usr/<username>` object **does not need to exist** on the cluster if the tokens are issued and managed by an external OpenID Connect (OIDC) server.
  * **Availability:** This method was **added in OpenSVC v3** agents.


## Managing API Users

### Creating Local Users (`system/usr/`)

Skip this step if you plan to use only OIDC-issued tokens for a user. Local user objects define the user's cluster grants for Basic and X.509 authentication.

```bash
# Create a cluster-wide administrator user
om system/usr/root create --kw grant=root

# Create user `usr1` with
#  `admin` rights on namespace `ns1`
#  `guest` (read-only) rights on namespace `ns2`
om system/usr/usr1 create --kw grant="admin:ns1 guest:ns2"
```


### Generating X.509 Certificates for Users

This step is only necessary if you require X.509 authentication for the user.

```bash
# Generate Certificate:
om system/usr/root certificate create
om system/usr/usr1 certificate create

# Download Keys (for client use):
om system/usr/usr1 key decode --name certificate_chain
om system/usr/usr1 key decode --name certificate
om system/usr/usr1 key decode --name private_key
```

These commands will print the PEM-encoded keys to standard output.


## Testing the API

The API manifest (documentation) is exposed by a demonstration agent for reference.

A practical test using a JWT:

```bash
# Generate a Temporary Token:
$ TOKEN=$(sudo om daemon auth token --subject usr1 --duration 10m)

# Call the `whoami` Endpoint:
$ curl -o- -k -s -H "Authorization: Bearer $TOKEN" https://localhost:1215/whoami
```

Example Output:

```json
{"auth":"jwt","grant":{"guest":["ns2"], "admin": ["ns1"]},"name":"usr1","namespace":"system","raw_grant":"admin:ns1 guest:ns2"}
```


## Configuring the Listener TLS Certificate

The agent listener requires a TLS certificate to accept remote connections securely.

Upon initial agent installation and daemon startup:

* A self-signed Certificate Authority (CA) is automatically created as `system/sec/ca`.
* A listener certificate, signed by this internal CA, is automatically created as `system/sec/cert`.

The following steps are only required if you need to **re-sign the internal CA** or **switch to an external PKI**.

### Option 1: Using the Internal PKI

The initial configuration is done automatically upon agent installation and daemon startup, creating:

  * The CA certificate at `system/sec/ca`.
  * The listener certificate at `system/sec/cert`.

1. **Import a valid certificate in `system/sec/ca`:**
    ```bash
    om system/sec/ca key change --name certificate --from ~/$CLUSTERNAME.pem
    om system/sec/ca key change --name certificate_chain --from ~/$CLUSTERNAME.chain
    om system/sec/ca key change --name private_key --from ~/$CLUSTERNAME.key
    ```
2. **Recreate the listener certificate:**
    ```bash
    om system/sec/cert certificate create
    ```

### Option 2: Using an External PKI

1.  **Adjust the Listener Certificate Subject:**

    Only the `cn` is strictly required by OpenSVC, but the signing certificate authority will surely require more.

    ```bash
    om system/sec/cert config update --set cn=vip.$CLUSTERNAME.mycorp \
        --set alt_names="node1.$CLUSTERNAME.mycorp node2.$CLUSTERNAME.mycorp" \
        --set c=FR \
        --set o=MyCorp \
        --set ou=Support \
        --set l=Paris \
        --set st=IDF \
        --set email=support@mycorp
    ```
2.  **Create the Listener Certificate Request:**
    ```bash
    om system/sec/cert certificate signing-request
    ```
3.  **Perform External Signing:** *(This is an external procedure to be done with your PKI tool using the generated csr.)*
4.  **Load the Signed Certificate:**
    ```bash
    om system/sec/cert key change --name certificate_chain --from ~/$CLUSTERNAME_crt_chain.pem
    ```
    The certificate is always first, then the CA certificate chain.
5.  **Configure Certificate Revocation List (Optional):**
    ```bash
    om cluster config update --set cluster.crl=http://crl.mycorp
    ```
6. **Restart the Daemons**
    ```bash
    om daemon restart --node="*"
    ```


> ➡️  See Also
> * [RBAC](agent.rbac) For detailed information on Role-Based Access Control and grant management.
