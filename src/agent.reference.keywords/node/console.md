# Driver `console`

**Supported keywords:**

- comment
- port
- url

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


## Keyword `port`

	required:    false
	scopable:    false
	default:     1216
	convert:     int

**Description:**

The port the console listener of the node listens on, on the address the api listens on.

A console session is a websocket opened on this port with a ticket the api issued. The sessions are not served through the api port: each is a process of its own, which a daemon restart does not interrupt.

The nodes of a cluster reach each other's console on the same port, so the keyword is best set in the cluster configuration.


## Keyword `url`

	required:    false
	scopable:    false

**Example:**

	url=wss://access.example.com/opensvc-console/

**Description:**

The url clients open the console sessions on, when it is not the console port of the node they reach the api on.

Set it to the address a site access proxy publishes the console listener at. Any node accepts the sessions of any node, and relays the ones it does not serve itself, so the proxy can forward to whichever node it reaches.

The proxy has to forward the websocket upgrade and the query string, which holds the session ticket.


