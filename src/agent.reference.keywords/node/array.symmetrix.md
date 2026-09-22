# Driver `array.symmetrix`

**Minimal configlet:**

	[array#1]
	type = symmetrix

**Minimal setup command:**

	om node set --kw="type=symmetrix"

**Supported keywords:**

- comment
- name
- password
- schedule
- symcli_connect
- symcli_path
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


## Keyword `name`

	required:    false
	scopable:    false

**Example:**

	name=00012345

**Description:**

The name of the array. If not provided, fallback to the section name suffix.


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


## Keyword `symcli_connect`

	required:    false
	scopable:    false

**Example:**

	symcli_connect=MY_SYMAPI_SERVER

**Description:**

Set the `SYMCLI_CONNECT` environment variable to this value.

If not set, the SCSI communication channels are used.

The value set must be declared in the `/var/symapi/config/netcnfg` file.


## Keyword `symcli_path`

	required:    false
	scopable:    false
	default:     /usr/symcli

**Example:**

	symcli_path=/opt/symcli

**Description:**

Force use of a symcli programs installation, pointing the path of its head
directory.

For the case multiple symcli versions are installed and the default selector
does not select the version preferred for the array.


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


