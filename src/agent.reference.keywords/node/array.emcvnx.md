# Driver `array.emcvnx`

**Minimal configlet:**

	[array#1]
	type = emcvnx
	spa = array1-a
	spb = array1-b

**Minimal setup command:**

	om node set \
		--kw="type=emcvnx" \
		--kw="spa=array1-a" \
		--kw="spb=array1-b"

**Supported keywords:**

- comment
- method
- password
- schedule
- scope
- spa
- spb
- type
- username

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


## Keyword `method`

	required:    false
	scopable:    false
	candidates:  secfile, credentials
	default:     secfile

**Example:**

	method=secfile

**Description:**

The authentication method to use.


## Keyword `password`

	required:    false
	scopable:    false

**Example:**

	password=system/sec/array1

**Description:**

The password to use to log in, expressed as a datastore reference.

Value format:
- New format: `from <namespace>/<kind>/<name> key <key name>`
- Legacy format: `<namespace>/<kind>/<name>` (uses default key "password")

Array passwords are usually stored in sec datastores like `system/sec/<array name>`.


## Keyword `schedule`

	required:    false
	scopable:    false

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `scope`

	required:    false
	scopable:    false
	default:     0

**Example:**

	scope=1

**Description:**

The VNC scope to work in.


## Keyword `spa`

	required:    true
	scopable:    false

**Example:**

	spa=array1-a

**Description:**

The name of the Service Processor A.


## Keyword `spb`

	required:    true
	scopable:    false

**Example:**

	spb=array1-b

**Description:**

The name of the Service Processor B.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  freenas, hds, eva, nexenta, vioserver, centera, symmetrix, emcvnx, netapp, hp3par, ibmds, ibmsvc, xtremio, dorado, hoc, truenas

**Description:**

The storage array driver name.


## Keyword `username`

	required:    false
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in, if configured.


