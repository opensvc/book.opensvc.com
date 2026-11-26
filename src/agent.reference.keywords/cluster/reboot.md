# Driver `reboot`

**Supported keywords:**

- blocking_pre
- comment
- pre

## Keyword `blocking_pre`

	required:    false
	scopable:    false
	group:       triggers
	rbac:        This driver group requires the root grant.

**Example:**

	blocking_pre=yum upgrade -y

**Description:**

A command or script to execute before `om node reboot`, after `reboot.pre`.

Errors abort the reboot, as a patching command that failed would leave the
node half updated.


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


## Keyword `pre`

	required:    false
	scopable:    false
	group:       triggers
	rbac:        This driver group requires the root grant.

**Example:**

	pre=yum upgrade -y

**Description:**

A command or script to execute before `om node reboot`.

Errors are logged and ignored: the node reboots anyway.


