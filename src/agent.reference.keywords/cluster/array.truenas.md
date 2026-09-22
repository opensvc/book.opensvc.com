# Driver `array.truenas`

**Minimal configlet:**

	[array#1]
	type = truenas
	api = https://array.opensvc.com/api/v1.0
	password = from system/sec/array1 key password
	username = root

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=truenas" \
		--kw="api=https://array.opensvc.com/api/v1.0" \
		--kw="password=from system/sec/array1 key password" \
		--kw="username=root"

**Supported keywords:**

- api
- comment
- insecure
- password
- schedule
- timeout
- type
- username

## Keyword `api`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	api=https://array.opensvc.com/api/v1.0

**Description:**

The array rest api url.


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


## Keyword `insecure`

	required:    false
	scopable:    false
	default:     false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Example:**

	insecure=true

**Description:**

Disable secure socket verification.


## Keyword `password`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	password=from system/sec/array1 key password

**Description:**

The password to use to log in, expressed as a datastore reference.

Value format:
- New format: `from <namespace>/<kind>/<name> key <key name>`
- Legacy format: `<namespace>/<kind>/<name>` (uses default key "password")

Array passwords are usually stored in sec datastores like `system/sec/<array name>`.


## Keyword `schedule`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `timeout`

	required:    false
	scopable:    false
	default:     120s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	timeout=10s

**Description:**

The api request timeout.


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


