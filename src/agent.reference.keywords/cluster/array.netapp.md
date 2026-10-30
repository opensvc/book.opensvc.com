# Driver `array.netapp`

**Minimal configlet:**

	[array#1]
	type = netapp
	key = /path/to/key
	server = centera1
	username = root

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=netapp" \
		--kw="key=/path/to/key" \
		--kw="server=centera1" \
		--kw="username=root"

**Supported keywords:**

- comment
- key
- schedule
- server
- type
- username

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


## Keyword `key`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in.


## Keyword `schedule`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `server`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	server=centera1

**Description:**

The storage server to connect.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  freenas, hds, eva, nexenta, vioserver, centera, symmetrix, emcvnx, netapp, hp3par, ibmds, ibmsvc, xtremio, dorado, hoc, truenas
	rbac:        This driver group requires the root grant.

**Description:**

The storage array driver name.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in.


