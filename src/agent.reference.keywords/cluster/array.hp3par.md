# Driver `array.hp3par`

**Minimal configlet:**

	[array#1]
	type = hp3par

**Minimal setup command:**

	om test/ccfg/foo set --kw="type=hp3par"

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
	group:       tools
	default:     3parcli
	rbac:        This driver group requires the root grant.

**Example:**

	cli=/path/to/pwf

**Description:**

The path of the executable hp3par CLI.


## Keyword `comment`

	required:    false
	scopable:    false
	group:       identity
	rbac:        This driver group requires the root grant.

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
	group:       credentials
	rbac:        This driver group requires the root grant.

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in.


## Keyword `manager`

	required:    false
	scopable:    false
	group:       endpoint
	rbac:        This driver group requires the root grant.

**Default:**

The name of the array

**Example:**

	manager=mymanager.mycorp

**Description:**

The host name the commands are sent to: the array manager, or, with the `ssh` method, a bastion of the zone of the array whose authorized key forces a command passing the commands on to the array.


## Keyword `method`

	required:    false
	scopable:    false
	group:       endpoint
	candidates:  cli, ssh
	default:     ssh
	rbac:        This driver group requires the root grant.

**Example:**

	method=ssh

**Description:**

The connection method to use.

* `ssh`

  Run the commands on the array over ssh, as the `username` with the private `key`. The ssh client never prompts and gives up a `manager` it can not reach in 10 seconds.

* `cli`

  Run the commands through the 3PAR cli installed on this node, with the password file `pwf`.

The `proxy` method of v2, which served the commands of the nodes of a dmz from a node of the zone of the array, is not supported. Use the `ssh` method, its `manager` a bastion of the zone of the array whose authorized key forces a command passing on to the array the remote copy commands it allows.


## Keyword `pwf`

	required:    false
	scopable:    false
	group:       credentials
	rbac:        This driver group requires the root grant.

**Example:**

	pwf=/path/to/pwf

**Description:**

The path to the 3par password file to use to log in.


## Keyword `schedule`

	required:    false
	scopable:    false
	group:       scheduling
	rbac:        This driver group requires the root grant.

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `type`

	required:    true
	scopable:    false
	group:       identity
	candidates:  freenas, hds, symmetrix, hp3par, xtremio, hoc, pure, truenas
	rbac:        This driver group requires the root grant.

**Description:**

The storage array driver name.


## Keyword `username`

	required:    false
	scopable:    false
	group:       credentials
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in, if configured.


