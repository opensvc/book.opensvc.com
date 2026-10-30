# Driver `array.centera`

**Minimal configlet:**

	[array#1]
	type = centera
	java_bin = /opt/java/bin/java
	jcass_dir = /opt/centera/LIB
	password = from system/sec/array1 key password
	server = centera1
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=centera" \
		--kw="java_bin=/opt/java/bin/java" \
		--kw="jcass_dir=/opt/centera/LIB" \
		--kw="password=from system/sec/array1 key password" \
		--kw="server=centera1" \
		--kw="username=root"

**Supported keywords:**

- comment
- java_bin
- jcass_dir
- password
- schedule
- server
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


## Keyword `java_bin`

	required:    true
	scopable:    false

**Example:**

	java_bin=/opt/java/bin/java

**Description:**

The path to the java executable to use to run the Centera management program.


## Keyword `jcass_dir`

	required:    true
	scopable:    false

**Example:**

	jcass_dir=/opt/centera/LIB

**Description:**

The path of the directory hosting the `JCASScript.jar`.


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


## Keyword `server`

	required:    true
	scopable:    false

**Example:**

	server=centera1

**Description:**

The storage server to connect.


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


