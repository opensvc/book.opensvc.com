# Driver `syslog`

**Supported keywords:**

- comment
- facility
- host
- level
- port

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


## Keyword `facility`

	required:    false
	scopable:    false
	default:     daemon
	rbac:        This driver group requires the root grant.

**Description:**

The syslog facility to log to.


## Keyword `host`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Default:**

`localhost` if port is set.

**Description:**

The syslog server host to send logs to.

If neither `host` nor `port` are specified and if `/dev/log` exists, the
messages are posted to `/dev/log`.


## Keyword `level`

	required:    false
	scopable:    false
	candidates:  critical, error, warning, info, debug
	default:     info
	rbac:        This driver group requires the root grant.

**Description:**

The minimum message criticity to feed to syslog.

Setting to `critical` actually disables the syslog logging, as the
agent does not emit messages at this level.


## Keyword `port`

	required:    false
	scopable:    false
	default:     514
	rbac:        This driver group requires the root grant.

**Description:**

The syslog server port to send logs to.

If neither `host` nor `port` are specified and if `/dev/log` exists, the
messages are posted to `/dev/log`.


