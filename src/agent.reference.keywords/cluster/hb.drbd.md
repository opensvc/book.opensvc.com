# Driver `hb.drbd`

**Minimal configlet:**

	[hb#1]
	type = drbd

**Minimal setup command:**

	om test/ccfg/foo set --kw="type=drbd"

**Supported keywords:**

- max_peers

## Keyword `max_peers`

	required:    false
	scopable:    false
	convert:     int
	rbac:        This driver group requires the root grant.

**Default:**

(nodes_count*2)-1

**Example:**

	max_peers=8

**Description:**

The integer value to use in `create-md --max-peers <n>`.

The driver ensures the value is not lesser than the number of instances.


