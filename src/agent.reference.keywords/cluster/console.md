# Driver `console`

**Supported keywords:**

- comment
- insecure
- max_greet_timeout
- max_seats
- server

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


## Keyword `insecure`

	required:    false
	scopable:    false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

If set, don't verify the console server certificate.


## Keyword `max_greet_timeout`

	required:    false
	scopable:    false
	default:     20s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

This keyword sets the absolute upper limit (maximum duration) that an API user can request via the `greet_timeout` query parameter when calling the handler to start a service instance resource console.

The console handler accepts a `greet_timeout` query parameter, which specifies how long the service instance should wait for the first client connection to the generated console URL.

The `max_greet_timeout` acts as a security safeguard, preventing API users from setting excessively long `greet_timeout` values.

If `max_greet_timeout` is set to 30s, any user request for greet_timeout=60s will be refused.

Recommendation:

* Keep Short: The effective timeout should generally be kept to a few seconds (e.g., 5s to 10s). A shorter timeout minimizes the risk that a malicious actor could successfully guess the console URL through a brute-force attack before the link expires.

* Manual Testing: Users may occasionally need to set a slightly higher `greet_timeout` (e.g., 60s) for manual testing or debugging purposes, but this value will always be constrained by the `max_greet_timeout` defined here.


## Keyword `max_seats`

	required:    false
	scopable:    false
	default:     1
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

This keyword sets the absolute upper limit that an API user can request via the `seats` query parameter when calling the handler to start a service instance resource console.


## Keyword `server`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

The tty-proxy console server address. A TLS capable server is expected, so the value should be a TLS terminator reverse proxy.


