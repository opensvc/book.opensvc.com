# Driver `store.plakar`

**Minimal configlet:**

	[store#1]
	type = plakar
	passphrase = from system/sec/backup key passphrase
	url = /srv/plakar

**Minimal setup command:**

	om test/sec/foo set \
		--kw="type=plakar" \
		--kw="passphrase=from system/sec/backup key passphrase" \
		--kw="url=/srv/plakar"

**Supported keywords:**

- access_key
- ca
- comment
- disable_tls
- host_key
- keep
- passphrase
- region
- secret_key
- ssh_private_key
- token
- type
- url

## Keyword `access_key`

	required:    false
	scopable:    false
	group:       store
	secret:      true
	rbac:        An access key not written from . key <key>, a key of the sec declaring the store, requires the root grant.

**Example:**

	access_key=from system/sec/backup key access_key

**Description:**

The access key id a `s3://` store signs its requests with, written
`from <sec> key <key>`, the key holding one line. Required by a `s3://` url,
with `secret_key`, and refused with another: a store never signs with the
credentials of the node, as the role of its instance.

In a store declared in a sec, `from .` is that sec, a relative path is of its
namespace, and the key is read as the object using the store.

A namespace administrator writes it `from . key <key>`, a key of the sec
declaring the store: as the key is read as the object using the store, a key
of another datastore, which a store shared with other namespaces would read
for them, requires the root grant.


## Keyword `ca`

	required:    false
	scopable:    false
	group:       store
	rbac:        The certificate authorities not written from . key <key>, a key of the sec declaring the store, requires the root grant.

**Example:**

	ca=from system/cfg/backup key ca

**Description:**

The certificate authorities the server of a `https://` store is verified
with, written `from <datastore> key <key>`, the key of a cfg or a sec holding
their certificates in PEM. Refused with another url than `https://`.

Unset, the server is verified with the certificate authorities of the
system. Set, with these only: a server whose certificate one of the system
signed is refused.

A namespace administrator writes it `from . key <key>`, a key of the sec
declaring the store: as the key is read as the object using the store, a key
of another datastore, which a store shared with other namespaces would read
for them, requires the root grant.


## Keyword `comment`

	required:    false
	scopable:    false
	group:       identity

**Description:**

A free form text describing the role of the object, of the node, or of the
section it is set in.

The keyword is accepted in any section, so the DEFAULT section can document a
configuration as a whole, and a resource, pool, heartbeat, array or network
section can document itself.

The agent does not interpret the value.


## Keyword `disable_tls`

	required:    false
	scopable:    false
	group:       store
	default:     false
	convert:     bool
	rbac:        A store reached without TLS requires the root grant.

**Description:**

Set to true to reach a `s3://` store in plain http, as a S3-compatible
server of a private network serving no TLS: the `use_tls` option of the s3
package of plakar, given `false`. The access key of the store, the
signatures of its requests and its data, encrypted by plakar, then cross the
network with no TLS, and the server is not authenticated.

Unset or false, the store is reached with TLS, as the package does by
default, and its certificate verified with the certificate authorities of
the system. The driver never falls back to plain http by itself: a server
answering in plain http fails the call, with the hint to set this keyword.

Only root sets it: a namespace administrator may not, on a store declared in
a sec. Refused with a url of another scheme.


## Keyword `host_key`

	required:    false
	scopable:    false
	group:       store

**Example:**

	host_key=ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBc1nVQ6Ck8M6zKQ1dHoRcgYzBH9Cf2rBG7aJ1LGq2xp

**Description:**

The public key of the server of a `sftp://` store, as `ssh-keyscan` prints
it, with or without the host before it, or `from <datastore> key <key>` for
the key of a datastore holding it. Required by a `sftp://` url, refused
with another.

The server must present this key: a store is never written to, nor read from, a
server it did not recognize. The known hosts of root and of the node are not
read.


## Keyword `keep`

	required:    false
	scopable:    false
	group:       store

**Example:**

	keep=24h 7d 4w 6m

**Description:**

The retention of the runs of each object backed up into this store, when
its `sync.store` resource sets none. A list of rules, a run kept by any of
them being kept:

`<n>`
  The `<n>` latest runs.

`<n>h`, `<n>d`, `<n>w`, `<n>m`, `<n>y`
  The latest run of each of the `<n>` latest hours, days, weeks (Monday to
  Sunday), months or years holding a run.

The periods are counted among the ones holding a run, not back from now,
so an object whose runs stopped for a while keeps its last ones. They are
in UTC, of the time a run started, so runs written by different nodes
after a failover fall in the same periods. Without `keep`, no run is ever
deleted.

For example, `keep = 24h 7d 4w 6m` keeps 41 runs at most.


## Keyword `passphrase`

	required:    true
	scopable:    false
	group:       store
	secret:      true
	rbac:        A passphrase not written from . key <key>, a key of the sec declaring the store, requires the root grant.

**Example:**

	passphrase=from system/sec/backup key passphrase

**Description:**

The passphrase of the Kloset store, written `from <sec> key <key>`: a
passphrase is never written in the section.

plakar gets it from `om <sec> key decode -- <key>`, the `passphrase_cmd` of its
configuration: it is never in a file, a command line nor the environment. The
key holds one line, a trailing newline being ignored. Losing the passphrase
loses the runs of the store.

In a store declared in a sec, `from .` is that sec, a relative path is of its
namespace, and the key is read as the object using the store.

A namespace administrator writes it `from . key <key>`, a key of the sec
declaring the store: as the key is read as the object using the store, a key
of another datastore, which a store shared with other namespaces would read
for them, requires the root grant.


## Keyword `region`

	required:    false
	scopable:    false
	group:       store

**Example:**

	region=eu-west-3

**Description:**

The region a `s3://` store signs its requests with, as `eu-west-3`: the
`region` option of the s3 package of plakar. A value of the section, not a
secret. Refused with a url of another scheme.

Unset, the package is given no region and its s3 client finds one by
itself: the one the server tells for the bucket, or `us-east-1`. Set it for
a server refusing that discovery, or the requests signed for another region
than its own, as some S3-compatible providers do.


## Keyword `secret_key`

	required:    false
	scopable:    false
	group:       store
	secret:      true
	rbac:        A secret key not written from . key <key>, a key of the sec declaring the store, requires the root grant.

**Example:**

	secret_key=from system/sec/backup key secret_key

**Description:**

The secret access key of the `access_key` of a `s3://` store, written
`from <sec> key <key>`: a secret is never written in the section. The key
holds one line. Required by a `s3://` url, refused with another.

plakar reads it from the configuration the driver writes for the store, a
file of the private directory of the store only root reads, kept in memory:
it is never on a command line nor in the environment.

In a store declared in a sec, `from .` is that sec, a relative path is of its
namespace, and the key is read as the object using the store.

A namespace administrator writes it `from . key <key>`, a key of the sec
declaring the store: as the key is read as the object using the store, a key
of another datastore, which a store shared with other namespaces would read
for them, requires the root grant.


## Keyword `ssh_private_key`

	required:    false
	scopable:    false
	group:       store
	secret:      true
	rbac:        An ssh private key not written from . key <key>, a key of the sec declaring the store, requires the root grant.

**Example:**

	ssh_private_key=from system/sec/backup key ssh_private_key

**Description:**

The private key the user of a `sftp://` store logs in with, written
`from <sec> key <key>`: a key is never written in the section, nor read from a
file of the node. The key has no passphrase. Required by a `sftp://` url,
refused with another.

The sftp package of plakar runs the ssh of the node. The driver has it run
with this key only, written in the private directory of the store: neither
the keys, the agent nor the ssh configuration of root are used.

In a store declared in a sec, `from .` is that sec, a relative path is of its
namespace, and the key is read as the object using the store, so the
datastore holding it must share with its namespace.

A namespace administrator writes it `from . key <key>`, a key of the sec
declaring the store: as the key is read as the object using the store, a key
of another datastore, which a store shared with other namespaces would read
for them, requires the root grant.


## Keyword `token`

	required:    false
	scopable:    false
	group:       store
	secret:      true
	rbac:        A token not written from . key <key>, a key of the sec declaring the store, requires the root grant.

**Example:**

	token=from system/sec/backup key token

**Description:**

The token a `https://` store sends the plakar server, the one `plakar server
-token` requires, written `from <sec> key <key>`: a token is never written in
the section. The key holds one line. Refused with another url than
`https://`: a token is not sent in the clear.

plakar reads it from the configuration the driver writes for the store, a
file of the private directory of the store only root reads, kept in memory:
it is never on a command line nor in the environment.

In a store declared in a sec, `from .` is that sec, a relative path is of its
namespace, and the key is read as the object using the store.

A namespace administrator writes it `from . key <key>`, a key of the sec
declaring the store: as the key is read as the object using the store, a key
of another datastore, which a store shared with other namespaces would read
for them, requires the root grant.


## Keyword `type`

	required:    true
	scopable:    false
	group:       store
	candidates:  plakar, tar
	rbac:        Requires the root grant, except for the values plakar, tar.

**Description:**

The driver of the store, the tool keeping the backups the `sync.store`
resources of the objects write into it.

`plakar`
  A Kloset store, driven through the plakar binary of the node. It
  deduplicates, compresses and encrypts.

`tar`
  A directory holding a gzipped tar archive per member of a run. It
  neither deduplicates nor encrypts: a test and reference store.


## Keyword `url`

	required:    true
	scopable:    false
	group:       store
	rbac:        A keyword of the plakar driver, which needs the root grant to choose.

**Example:**

	url=/srv/plakar

**Description:**

The location of the Kloset store: an absolute path or a `fs://` url of one
for a directory of the node, or the `<scheme>://` url of a location plakar
reaches by itself. A relative path is refused.

A directory, a `sftp://` and a `s3://` store are created by the first run
written into them, never by a listing, a status, a check, a restore or a
deletion. A remote store is created only when plakar answers that its
location is reached, with the credentials of the store, and holds no
repository, the bucket of a `s3://` store being made when missing: a server
not reached, a login, a host key or a permission refused fails the run and
creates nothing. The store of another scheme, a plakar server `http://` or
`https://` included, is created by hand, with `plakar create`: a plakar
server serves a repository that exists.

A location found empty gets a new store, as a directory does: a server
whose storage is not mounted, or a url mistyped, shows as a store holding
none of the earlier runs, which are where they were. Two objects of a node
writing their first run at once create one store, and so do two nodes: the
store the other node created meanwhile is used as it is.

A directory is the same for every node, on storage none of them holds, as
an nfs mount: the runs kept on the disk of one node are lost with it, when
they are needed, and the node taking an object over finds none of them. A
node where the shared directory is not mounted lists no run, and creates no
store in the mount point until it writes a run.

The plakar of the node is of the 1.1 releases, from 1.1.8: the driver reads
what plakar prints, which another release, as 1.2, may print otherwise. A
plakar older or newer is refused, with its version, before the store is
called.

plakar reaches by itself a plakar server, `http://` or `https://`, as
`plakar server` runs, with `-allow-delete` for the retention to delete runs.
The other locations, as `sftp://` or `s3://`, need the plakar package of
their scheme on every node, installed by the operator with `plakar pkg add`
as the user om runs as, root: the stores use the data directory plakar
installs the packages in for that user, `~/.local/share/plakar` of its home.

A `sftp://`, `s3://` or `https://` store never reaches its location with
what the node holds for root. A `sftp://` store logs in with `ssh_private_key` and recognizes its server by
`host_key`, both required: the sftp package runs the ssh of the node, which
the driver keeps off the keys, the agent, the configuration and the known
hosts of root. A `s3://` store signs with `access_key` and `secret_key`,
both required, never with the role of the instance, for the `region` it is
given, or the one the s3 package finds by itself, over TLS unless root set
its `disable_tls`. A `https://` store may
send a `token`, and verify its server with the certificate authorities of
`ca` instead of the ones of the system. A credential keyword, a `region` or
a `disable_tls`, of another scheme than the one of the url is refused. A store with another scheme has
no credential keyword: plakar reaches it with what its url and the node
hold.

The store is never inside a head it backs up. A store declared in a sec is
reached over the network: the daemon reads and writes a store as root, and a
namespace does not choose a directory of the node. A namespace declares a
`sftp://` or `s3://` store in a sec, its passphrase and its credentials
written `from <sec> key <key>`: another scheme, `https://` included, requires
the root grant.

The retention deletes the snapshots of a run, then runs `plakar
maintenance`, which frees their space in two passes: the packs no snapshot
uses are marked, then removed by a maintenance run 7 days later or more. A
maintenance finding the store locked by a backup is skipped, the next
deletion running it again.


