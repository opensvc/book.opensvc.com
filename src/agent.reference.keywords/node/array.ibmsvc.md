# Driver `array.ibmsvc`

**Minimal configlet:**

	[array#1]
	type = ibmsvc
	key = /path/to/key
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=ibmsvc" \
		--kw="key=/path/to/key" \
		--kw="username=root"

**Supported keywords:**

- comment
- key
- schedule
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


## Keyword `key`

	required:    true
	scopable:    false

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in.


## Keyword `schedule`

	required:    false
	scopable:    false

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  freenas, hds, eva, nexenta, vioserver, centera, symmetrix, emcvnx, netapp, hp3par, ibmds, ibmsvc, xtremio, dorado, hoc, truenas

**Description:**

The storage array driver name.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in.


