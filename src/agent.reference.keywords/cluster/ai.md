# Driver `ai`

**Supported keywords:**

- agent_url
- comment

## Keyword `agent_url`

	required:    false
	scopable:    false
	since:       v3.0.0-rc56
	rbac:        This driver group requires the root grant.

**Example:**

	agent_url=https://ai.example.com:8090

**Description:**

The url of the OpenSVC AI agent om3-webapp calls.

It is an https origin, the scheme, the host and the port only: another value
is refused when written, and an invalid one found in the file is reported
and left out of the cluster status.


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


