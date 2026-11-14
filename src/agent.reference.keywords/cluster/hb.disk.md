# Driver `hb.disk`

**Minimal configlet:**

	[hb#1]
	type = disk
	dev = /dev/mapper/36589cfc000000e03957c51dabab8373a

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=disk" \
		--kw="dev=/dev/mapper/36589cfc000000e03957c51dabab8373a"

**Supported keywords:**

- comment
- dev
- interval
- max_slots
- timeout
- type

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


## Keyword `dev`

	required:    true
	scopable:    true
	group:       transport
	rbac:        This driver group requires the root grant.

**Example:**

	dev=/dev/mapper/36589cfc000000e03957c51dabab8373a

**Description:**

The device to write the heartbeats to and read from.

It must be,

* Dedicated to the daemon use.
* Named by a static path, as `/dev/mapper/<name>` or `/dev/disk/by-id/<id>`: a `/dev/dm-<n>` path is refused, its number changing across reboots, and a `/dev/sd<x>` path is warned of.
* Sized `max_slots` x 4 KiB for the metadata, plus 1 MiB per node, plus 1 MiB: 7 MiB for 2 nodes with the default `max_slots`. The streams of a smaller device fail to start.

Signing a device that is not a heartbeat disk yet (`om daemon hb sign`) zeroes its metadata area, its first `max_slots` x 4 KiB, and is refused on a device holding another signature, as a filesystem, unless forced.


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


## Keyword `max_slots`

	required:    false
	scopable:    false
	group:       transport
	default:     1024
	convert:     int
	rbac:        This driver group requires the root grant.

**Example:**

	max_slots=1024

**Description:**

The maximum number of slots that can be written to the HB disk device.

It should be set to at least twice the number of cluster nodes using the HB disk device.

Do not modify this value after first activation.
Do not modify default value if the hb disk is used by multiple clusters.


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


