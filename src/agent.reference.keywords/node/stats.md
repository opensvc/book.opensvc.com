# Driver `stats`

**Supported keywords:**

- comment
- disable
- schedule

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


## Keyword `disable`

	required:    false
	scopable:    false
	convert:     list

**Example:**

	disable=blockdev mem_u

**Description:**

The statistics groups not to push to the collector, among `cpu`, `mem_u`,
`swap`, `proc`, `block`, `blockdev`, `netdev`, `netdev_err` and `fs_u`.


## Keyword `schedule`

	required:    false
	scopable:    false
	default:     ~00:00-06:00

**Description:**

Schedule parameter for the `pushstats` node action.

See `usr/share/doc/schedule` for the schedule syntax.


