# Driver `network.bridge`

**Minimal configlet:**

	[network#1]
	type = bridge

**Minimal setup command:**

	om test/ccfg/foo set --kw="type=bridge"

**Supported keywords:**

- comment
- dev
- mask_per_node
- network
- public
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


## Keyword `dev`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

The network bridge device name. If not set the name will be `obr_<network name>`. Use this keyword if you need the network to use an already existing bridge.


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

## Keyword `network`

	required:    false
	scopable:    true
	rbac:        This driver group requires the root grant.

**Description:**

The cluster backend network.

The routed_bridge driver fragments this network into subnets with a prefix length given by`mask_per_nodes`.


## Keyword `public`

	required:    false
	scopable:    false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

Set to true if the network ip range is public and we must not configure masquerading rules.


## Keyword `type`

	required:    false
	scopable:    false
	candidates:  bridge, routed_bridge, lan
	default:     bridge
	rbac:        This driver group requires the root grant.

**Description:**

The type of network.

* `bridge`: a subnet on a bridge of each node, the same on every node, its
  traffic masqueraded out of the node.
* `routed_bridge`: a subnet cut into one range per node, routed between the
  nodes.
* `lan`: ranges of a segment the nodes share, the addresses of which an
  object takes along when it moves to another node, as the floating address
  of a failover service.

The traffic the nodes forward for the `bridge` and `routed_bridge` networks
is accepted in the om nft table, and, on a node running docker, whose
forward chain drops what docker did not accept, in a chain the docker
`DOCKER-USER` chain jumps to.


