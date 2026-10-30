# Driver `array.eva`

**Minimal configlet:**

	[array#1]
	type = eva
	manager = evamanager.mycorp
	password = from system/sec/array1 key password
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=eva" \
		--kw="manager=evamanager.mycorp" \
		--kw="password=from system/sec/array1 key password" \
		--kw="username=root"

**Supported keywords:**

- bin
- comment
- manager
- password
- schedule
- type
- username

## Keyword `bin`

	required:    false
	scopable:    false

**Example:**

	bin=/opt/sssu/bin/sssu

**Description:**

The EVA manager executable to use.


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


## Keyword `manager`

	required:    true
	scopable:    false

**Example:**

	manager=evamanager.mycorp

**Description:**

The EVA manager to connect.


## Keyword `password`

	required:    true
	scopable:    false

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


