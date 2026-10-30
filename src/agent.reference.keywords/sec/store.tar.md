# Driver `store.tar`

**Minimal configlet:**

	[store#1]
	type = tar
	url = /srv/backups

**Minimal setup command:**

	om test/sec/foo set \
		--kw="type=tar" \
		--kw="url=/srv/backups"

**Supported keywords:**

- comment
- host_key
- keep
- ssh_private_key
- type
- url

## Keyword `comment`

	required:    false
	scopable:    false

**Description:**

A free form text describing the role of the object, of the node, or of the
section it is set in.

The keyword is accepted in any section, so the DEFAULT section can document a
configuration as a whole, and a resource, pool, heartbeat, array or network
section can document itself.

The agent does not interpret the value.


## Keyword `host_key`

	required:    false
	scopable:    false

**Example:**

	host_key=ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBc1nVQ6Ck8M6zKQ1dHoRcgYzBH9Cf2rBG7aJ1LGq2xp

**Description:**

The public key of the sftp server of the store, as `ssh-keyscan` prints it,
with or without the host before it.

The server must present this key: a store is never written to, nor read from, a
server it did not recognize.


## Keyword `keep`

	required:    false
	scopable:    false

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


## Keyword `ssh_private_key`

	required:    false
	scopable:    false
	secret:      true
	rbac:        An ssh private key not written from <sec> key <key> requires the root grant.

**Example:**

	ssh_private_key=from system/sec/backup key ssh_private_key

**Description:**

The private key the sftp user of the store authenticates with, written
`from <sec> key <key>`: a key is never written in the section, nor read from a
file of the node.

In a store declared in a sec, `from .` is that sec, a relative path is of its
namespace, and the key is read as the object using the store, so the
datastore holding it must share with its namespace.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  tar
	rbac:        Requires the root grant, except for the values tar.

**Description:**

The driver of the store, the tool keeping the backups the `sync.store`
resources of the objects write into it.

`tar`
  A directory holding a gzipped tar archive per member of a run. It
  neither deduplicates nor encrypts: a test and reference store.


## Keyword `url`

	required:    true
	scopable:    false
	rbac:        A store url other than sftp://, a directory of the node, requires the root grant.

**Example:**

	url=/srv/backups

**Description:**

The directory holding the store: an absolute path or a `file://` url for a
directory of the node, or `sftp://<user>@<host>[:<port>]/<path>` for a
directory of an sftp server.

A directory of the node is one per node, each holding the runs its node
writes, unless `shared` says it is the same on every node, as an nfs mount.
The store is never inside a head it backs up.

An sftp server is reached from every node by itself. Its user is authenticated
by `ssh_private_key`, and the server by `host_key`. A store declared in a sec is
an sftp store: the daemon reads and writes a store as root, and a namespace
does not choose a directory of the node.


