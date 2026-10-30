# Driver `uxgroup`

**Supported keywords:**

- comment
- grant

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


## Keyword `grant`

	required:    false
	scopable:    true
	convert:     listlowercase
	rbac:        This driver group requires the root grant.

**Example:**

	grant=operator:ns1 guest:ns2

**Description:**

The grants of the members of the unix group named by the section,
`[uxgroup#<group>]`, connected to the user socket of the node: the same
grants as the `grant` keyword of a `usr` object.

The members are the ones the name service lists for the group, whatever
groups the connected process holds. A process gets the grants of every
group it is a member of, and of the `usr` objects whose `uxuser` names its
login or uid.

Write it for one node with `grant@<node>`, where the accounts of a node
differ from the others'.


