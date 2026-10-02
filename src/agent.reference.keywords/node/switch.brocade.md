# Driver `switch.brocade`

**Minimal configlet:**

	[switch#1]
	type = brocade
	username = admin

**Minimal setup command:**

	om node set \
		--kw="type=brocade" \
		--kw="username=admin"

**Supported keywords:**

- comment
- key
- method
- name
- password
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

	required:    false
	scopable:    false

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in the switch.


## Keyword `method`

	required:    false
	scopable:    false
	candidates:  telnet, ssh
	default:     ssh

**Example:**

	method=ssh

**Description:**

The method to use to connect to the switch.

* `ssh`
  Log in with the private key `key` points to, or with the password of the
  `password` secret.

* `telnet`
  Refused: telnet sends the password in clear, and the switches have it
  disabled by default. The value is accepted in the configuration of a node
  upgraded from v2, and the inventory of the switch fails with a message
  asking for `ssh`.

The key of the switch is trusted on the first connection, and recorded in
the known hosts of the root user: a later connection presenting another key
is refused.


## Keyword `name`

	required:    false
	scopable:    false

**Example:**

	name=sansw1.my.corp

**Description:**

The name to connect to the switch with (dns name or ip address), and
optionally the ssh port, as `sansw1.my.corp:2222`.

If not set, fallback to the section name suffix.


## Keyword `password`

	required:    false
	scopable:    false

**Example:**

	password=mysec/password

**Description:**

The password to use to log in, read from a secret.

The value is `from <path> key <name>`, or a `sec` name alone, in the `system`
namespace, whose `password` key is read.

Either `password` or `key` must be specified.


## Keyword `schedule`

	required:    false
	scopable:    false

**Description:**

Schedule parameter for the `pushswitch` node action, which inventories the
switch and reports its configuration to the collector.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  brocade

**Description:**

The SAN switch driver name.

A node with a `switch#<name>` section inventories the switch on the section
`schedule`, or with `om node push switch`, and reports its configuration to
the collector.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=admin

**Description:**

The username to use to log in the switch.


