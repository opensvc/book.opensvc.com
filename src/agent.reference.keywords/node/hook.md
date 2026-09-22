# Driver `hook`

**Supported keywords:**

- command
- comment
- events

## Keyword `command`

	required:    false
	scopable:    false
	convert:     shlex

**Description:**

The command to execute on selected events.

The program is fed the json-formatted event data through stdin.


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


## Keyword `events`

	required:    false
	scopable:    false
	convert:     list

**Description:**

The list of events to execute the hook command on.

The special value `all` is also supported.


