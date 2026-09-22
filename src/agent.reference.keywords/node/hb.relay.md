# Driver `hb.relay`

**Minimal configlet:**

	[hb#1]
	type = relay
	relay = https://relay.acme.com:1215

**Minimal setup command:**

	om node set \
		--kw="type=relay" \
		--kw="relay=https://relay.acme.com:1215"

**Supported keywords:**

- comment
- insecure
- interval
- password
- relay
- timeout
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


## Keyword `insecure`

	required:    false
	scopable:    false
	default:     false
	convert:     bool

**Description:**

Set to `true` to disable the relay SSL certificate verification.

This should only be enabled for testing.


## Keyword `interval`

	required:    false
	scopable:    true
	default:     5s
	convert:     duration

**Description:**

The maximum interval between 2 heartbeat payload sends.

The actual interval is not fixed, because the daemon tries to send the
message as soon as it has something to notify. A minimum interval
protects the node from saturating the network and cpu with the daemon
synchronization workload.


## Keyword `password`

	required:    false
	scopable:    false
	default:     system/sec/relay

**Example:**

	password=from system/sec/relays key relay.acme.com/user1/password

**Description:**

A datastore key reference to a password used to authenticate with the relay API.

Value format:
- New format: `from <obj_path|obj_relpath> key <key name>`
- Legacy format: `<obj_path|obj_relpath>` (uses default key "password")

Where `<obj_relpath>` is the `./sec/<name>` notation. Node configuration is not
namespaced, so it resolves in the `system` namespace: `./sec/relays` is
`system/sec/relays`.


## Keyword `relay`

	required:    true
	scopable:    false

**Example:**

	relay=https://relay.acme.com:1215

**Description:**

The relay server uri.

If not specified, the port value is 1215, i.e. the default opensvc listener port.


## Keyword `timeout`

	required:    false
	scopable:    true
	default:     15s
	convert:     duration

**Description:**

The delay since the last received heartbeat from a node before considering this node is gone.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  unicast, multicast, disk, relay

**Description:**

The heartbeat driver name.


## Keyword `username`

	required:    false
	scopable:    false
	default:     relay

**Description:**

The username for login the relay api.


