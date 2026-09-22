# Driver `array.hp3par`

**Minimal configlet:**

	[array#1]
	type = hp3par

**Minimal setup command:**

	om node set --kw="type=hp3par"

**Supported keywords:**

- cli
- comment
- key
- manager
- method
- pwf
- schedule
- type
- username

## Keyword `cli`

	required:    false
	scopable:    false
	default:     3parcli

**Example:**

	cli=/path/to/pwf

**Description:**

The path of the executable hp3par CLI.


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

	required:    false
	scopable:    false

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in.


## Keyword `manager`

	required:    false
	scopable:    false

**Default:**

The name of the array

**Example:**

	manager=mymanager.mycorp

**Description:**

The array manager host name.


## Keyword `method`

	required:    false
	scopable:    false
	candidates:  proxy, cli, ssh
	default:     ssh

**Example:**

	method=ssh

**Description:**

The connection method to use.


## Keyword `pwf`

	required:    false
	scopable:    false

**Example:**

	pwf=/path/to/pwf

**Description:**

The path to the 3par password file to use to log in.


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

	required:    false
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in, if configured.


