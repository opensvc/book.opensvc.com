# Driver `compliance`

**Supported keywords:**

- auto_update
- comment
- schedule

## Keyword `auto_update`

	required:    false
	scopable:    false
	default:     false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

If set to `true`, execute `om node updatecomp` upon every scheduler-executed
`om node compliance check`.

These updates keep the compliance modules in sync with the reference
repository.

> *Warning*: the module repository security is critical. Attackers could
  insert malicious code in served modules.


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
	default:     02:00-06:00
	rbac:        This driver group requires the root grant.

**Description:**

Schedule parameter for the `compliance auto` node action, which check all
attached modules and fix only those flagged ``autofix``.

See `usr/share/doc/schedule` for the schedule syntax.


