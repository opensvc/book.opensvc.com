# Driver `network.lo`

**Minimal configlet:**

	[network#1]
	type = lo

**Minimal setup command:**

	om test/ccfg/foo set --kw="type=lo"

**Supported keywords:**

- comment
- mask_per_node
- type

## Keyword `comment`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

A free form text describing the role of the object, of the node, or of the
section it is set in.

The keyword is accepted in any section, so the DEFAULT section can document a
configuration as a whole, and a resource, pool, heartbeat, array or network
section can document itself.

The agent does not interpret the value.


## Keyword `mask_per_node`

	required:    false
	scopable:    false
	default:     0
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The prefix length of the subnets distributed to each node.
For example if the network is a x.x.x.x/16 you can distribute
- x.x.x.x/17 subnets to 2 nodes
- x.x.x.x/18 to 4 nodes
- etc...

If both `mask_per_node` and `ips_per_node` are set, `ips_per_node` is ignored.
If only `ips_per_node` is set, it is honored for backward compatibility.

The `ips_per_node` keyword is deprecated because its value is hard to manage for large ipv6 subnets (e.g a x.x.x.x/48 subnet has 281474976710656 ips).

## Keyword `type`

	required:    false
	scopable:    false
	candidates:  bridge, routed_bridge
	default:     bridge
	rbac:        This driver group requires the root grant.

**Description:**

The type of network.


