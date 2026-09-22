# Driver `packages`

**Supported keywords:**

- comment
- schedule

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


## Keyword `schedule`

	required:    false
	scopable:    false
	default:     ~00:00-06:00
	rbac:        This driver group requires the root grant.

**Description:**

Schedule parameter for the `pushpkg` node action.

See `usr/share/doc/schedule` for the schedule syntax.


