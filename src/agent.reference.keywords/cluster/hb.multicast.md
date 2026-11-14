# Driver `hb.multicast`

**Minimal configlet:**

	[hb#1]
	type = multicast

**Minimal setup command:**

	om test/ccfg/foo set --kw="type=multicast"

**Supported keywords:**

- addr
- comment
- interval
- intf
- port
- timeout
- type

## Keyword `addr`

	required:    false
	scopable:    true
	group:       transport
	default:     224.3.29.71
	rbac:        This driver group requires the root grant.

**Description:**

The multicast group to send to and listen on, IPv4 or IPv6.

An IPv6 group, as `ff02::1:4141`, requires `intf` on every node of the
heartbeat. The group names no zone, as `ff02::1:4141%eth0`: name the
interface with `intf`.


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


## Keyword `interval`

	required:    false
	scopable:    true
	group:       timing
	default:     5s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

The maximum interval between 2 heartbeat payload sends.

The actual interval is not fixed, because the daemon tries to send the
message as soon as it has something to notify. A minimum interval
protects the node from saturating the network and cpu with the daemon
synchronization workload.


## Keyword `intf`

	required:    false
	scopable:    true
	group:       transport
	rbac:        This driver group requires the root grant.

**Default:**

The natural interface for `<addr>`

**Example:**

	intf=eth0

**Description:**

The interface to join the multicast group on, and to send from.

Required for an IPv6 group, on every node of the heartbeat: use the scoping
syntax when the interface name differs between nodes.


## Keyword `port`

	required:    false
	scopable:    true
	group:       transport
	default:     10000
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The port for each node to send to or listen on.


## Keyword `timeout`

	required:    false
	scopable:    true
	group:       timing
	default:     15s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

The delay since the last received heartbeat from a node before considering this node is gone.


## Keyword `type`

	required:    true
	scopable:    false
	group:       identity
	candidates:  unicast, multicast, disk, relay
	rbac:        This driver group requires the root grant.

**Description:**

The heartbeat driver name.


