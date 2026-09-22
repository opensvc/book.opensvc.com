# Driver `cni`

**Supported keywords:**

- comment
- config
- plugins

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


## Keyword `config`

	required:    false
	scopable:    false
	default:     /var/lib/opensvc/cni/net.d

**Example:**

	config=/var/lib/opensvc/cni/net.d

**Description:**

The directory hosting the CNI network configuration files.


## Keyword `plugins`

	required:    false
	scopable:    false
	default:     /usr/lib/cni

**Example:**

	plugins=/var/lib/opensvc/cni/bin

**Description:**

The directory hosting the CNI plugins.


