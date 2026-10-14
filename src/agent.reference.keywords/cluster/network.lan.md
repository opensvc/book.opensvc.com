# Driver `network.lan`

**Minimal configlet:**

	[network#1]
	type = lan

**Minimal setup command:**

	om test/ccfg/foo set --kw="type=lan"

**Supported keywords:**

- comment
- dev
- gateway
- mask_per_node
- network
- ranges
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
	scopable:    true
	rbac:        This driver group requires the root grant.

**Example:**

	dev=eth1

**Description:**

The interface of the node on the segment, which the addresses drawn from this
network are configured on, as `eth1`.

When not set, it is the interface holding an address of the segment, not
counting the addresses of the ranges. Set it when the nodes have no address
on the segment, or when several interfaces hold one.


## Keyword `gateway`

	required:    false
	scopable:    true
	rbac:        This driver group requires the root grant.

**Example:**

	gateway=192.168.10.254

**Description:**

The router of the segment, which the ip.netns resources drawing from this
network route the traffic of their namespace through, unless they set a
gateway of their own. The ip.host resources do not use it: their addresses
are configured on the node, which has its own routes.

It must be an address of the segment, and not one of the ranges om hands out.
When not set, the ip.netns resources set no gateway, and a namespace with no
default route of its own reaches the segment only.


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
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	network=192.168.10.0/24

**Description:**

The segment the nodes share, as `192.168.10.0/24`, which the addresses drawn
from this network are configured with the prefix length of. Its first
address, and the last of an ipv4 segment, are never handed out.

om hands out the addresses of the ranges keyword only. Every node draws from
all of them, so an address is the same wherever the object runs, and an
object moving to another node takes its address along.

A draw is made under the cluster lock of the network, and keeps clear of the
addresses the nodes hold: the ones each node alive has reserved, the ones the
cluster status reports, and the ones each node remembers the others last
reported holding, which outlive a node the cluster stops hearing from. A node
stopped cleanly, as for a restart, is waited for until its maintenance grace
period ends, for as long as the lease of the lock allows.

Two parts of a split cluster, each not hearing the other, draw blind to what
the other draws, and can hand out the same address twice. The ip.host
resources report such an address as held elsewhere too, and an administrator
gives one of them another address: unset the addr of the resource and
restart it, or unprovision and provision it.


## Keyword `ranges`

	required:    false
	scopable:    false
	convert:     list
	rbac:        This driver group requires the root grant.

**Example:**

	ranges=192.168.10.100-192.168.10.149 192.168.10.151-192.168.10.199

**Description:**

The addresses of the segment om hands out, as a list of subnets, as
`192.168.10.128/26`, and of spans from a first to a last address, as
`192.168.10.100-192.168.10.199`, the form nftables and ipset read.

Required: the segment holds the addresses of the nodes, of the router and of
the other hosts, which om knows nothing of. Keep the ranges clear of them,
leaving out a host in the middle of a span by writing the span in two:

    ranges = 192.168.10.100-192.168.10.149 192.168.10.151-192.168.10.199

The ranges must be in the segment, and must not overlap, nor overlap the
ranges of another lan network of the same segment.


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


