# Driver `listener`

**Supported keywords:**

- acme_port
- addr
- comment
- crl
- dns_sock_gid
- dns_sock_uid
- openid_client_id
- openid_issuer
- port
- rate_limiter_burst
- rate_limiter_expires
- rate_limiter_rate
- tls_secs

## Keyword `acme_port`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	convert:     int
	rbac:        This driver group requires the root grant.

**Example:**

	acme_port=80

**Description:**

The port of the node the listener answers http-01 ACME challenges on, in
plain http, usually `80`: the port an ACME directory reads them from. No
challenge is answered when empty.

The listener answers only `/.well-known/acme-challenge/<token>`, from the
tokens a renewal of a sec of `listener.tls_secs` stores in that sec, and
every node answers them, so the names of the certificate may resolve to any
node of the cluster.


## Keyword `addr`

	required:    false
	scopable:    true
	aliases:     tls_addr
	rbac:        This driver group requires the root grant.

**Example:**

	addr=1.2.3.4

**Description:**

The ip addr the daemon tls listener must listen on.


## Keyword `comment`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

A free form text describing the role of the object, of the node, or of the
section it is set in.

The keyword is accepted in any section, so the DEFAULT section can document a
configuration as a whole, and a resource, pool, heartbeat, array or network
section can document itself.

The agent does not interpret the value.


## Keyword `crl`

	required:    false
	scopable:    false
	default:     /var/lib/opensvc/certs/ca_crl
	rbac:        This driver group requires the root grant.

**Example:**

	crl=https://crl.opensvc.com

**Description:**

The URL serving the certificate revocation list.

The default points to the path of the cluster CA CRL in `{var}/certs/ca_crl`.


## Keyword `dns_sock_gid`

	required:    false
	scopable:    false
	default:     953
	rbac:        This driver group requires the root grant.

**Description:**

The gid owning the unix socket serving the remote backend to the pdns authoritative server.


## Keyword `dns_sock_uid`

	required:    false
	scopable:    false
	default:     953
	rbac:        This driver group requires the root grant.

**Description:**

The uid owning the unix socket serving the remote backend to the pdns authoritative server.


## Keyword `openid_client_id`

	required:    false
	scopable:    false
	default:     om3
	rbac:        This driver group requires the root grant.

**Description:**

The openid client id used by om3-webapp.


## Keyword `openid_issuer`

	required:    false
	scopable:    false
	aliases:     openid_authority
	rbac:        This driver group requires the root grant.

**Example:**

	openid_issuer=https://keycloak.opensvc.com/auth/realms/clusters

**Description:**

The base URL of the identity issuer aka provider. It is used to detect the metadata location: `openid_issuer`/.well-known/openid-configuration.

If set, the http listener will try to validate the Bearer token provided in
the requests headers.

If the token is valid,

* the user name is fetched from the `preferred_username` claim (fallback on `name`)

* the user grant list is obtained by joining the multiple `entitlements` claims.

The keyword was named `openid_authority`, and that name is still accepted.

It replaced `openid_well_known`, which is not accepted anymore.
`openid_well_known` was the metadata endpoint itself, where `openid_issuer` is
the base URL that endpoint is derived from.

## Keyword `port`

	required:    false
	scopable:    true
	aliases:     tls_port
	default:     1215
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The port the daemon tls listener must listen on.

In pull action mode, the collector post request to notify
there are actions to unqueue. The opensvc daemon executes the
`dequeue actions` node action upon receive.

The `listener.port` value is sent to the collector on `om node push asset`.


## Keyword `rate_limiter_burst`

	required:    false
	scopable:    true
	default:     100
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The maximum number of inet listener requests to pass at the same moment.
It additionally allows a number of requests to pass when rate limit is reached.


## Keyword `rate_limiter_expires`

	required:    false
	scopable:    true
	default:     60s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

The duration after that a inet listener rate limiter is cleaned up.


## Keyword `rate_limiter_rate`

	required:    false
	scopable:    true
	default:     20
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The rate of inet listener requests allowed to pass per seconds.


## Keyword `tls_secs`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	convert:     list
	rbac:        This driver group requires the root grant.

**Example:**

	tls_secs=system/sec/public

**Description:**

The secs whose certificates the listener presents, besides the certificate
of `system/sec/cert`, to the clients asking one of their names: a name of the
cluster published on the internet, as the name of its virtual address, can
have a certificate browsers trust, from an ACME directory, while the nodes
keep reaching each other by their names, which only the cluster ca certifies.

A sec is named by its path, as `system/sec/public`, or by its name in the
`system` namespace. A client asking a name no listed certificate has gets the
certificate of `system/sec/cert`.

A certificate renewed is presented from the next connection, on every node.
`om <sec> certificate renew` obtains the certificate of a listed sec through
the listener, which serves the http-01 challenge on `listener.acme_port`.


