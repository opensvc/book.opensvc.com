# Driver `collector`

**Supported keywords:**

- action_batch
- action_log_timeout
- comment
- feeder
- ping_interval
- server
- status_delay
- timeout
- url

## Keyword `action_batch`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	default:     100
	convert:     int
	rbac:        This driver group requires the root grant.

**Example:**

	action_batch=200

**Description:**

The maximum number of instance action begins and ends the collector speaker
sends to the collector per batch, one batch at a time.
A batch stops at the first send failing, so a collector down costs one send
per batch whatever this value.
Minimum value: 1


## Keyword `action_log_timeout`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	default:     10s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	action_log_timeout=30s

**Description:**

The maximum time the collector speaker waits for the log lines of an ended
instance action, read from the journal of the node the action ran on.
An end whose log lines can not be read in time is sent without them.
Minimum value: 1s


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


## Keyword `feeder`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	rbac:        This driver group requires the root grant.

**Default:**

`collector.url`/feeder if collector.url is defined.

**Example:**

	feeder=https://collector.opensvc.com/feeder

**Description:**

The url of the OpenSVC Collector v3 feeder, the api the node feeds its data
to.


## Keyword `ping_interval`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	default:     60s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	ping_interval=120s

**Description:**

Set the minimum interval between 2 push alive status to collector.
It is called when there are no daemon status changes, but we want
to send alive status to collector.
Minimum value: 60s


## Keyword `server`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	rbac:        This driver group requires the root grant.

**Default:**

`collector.url`/server if collector.url is defined.

**Example:**

	server=https://collector.opensvc.com/server

**Description:**

The url of the OpenSVC Collector v3 server, the api the node registers on and
reads from.


## Keyword `status_delay`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	default:     10s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	status_delay=30s

**Description:**

Set the minimum delay before next push daemon status changes to collector.
Minimum value: 10s


## Keyword `timeout`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	default:     5s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	timeout=10s

**Description:**

The maximum time to wait for a collector v3 call, as the send of the begin
or the end of an instance action.
Minimum value: 1s. Maximum value: 20s.


## Keyword `url`

	required:    false
	scopable:    false
	since:       v3.0.0-rc44
	rbac:        This driver group requires the root grant.

**Example:**

	url=https://collector.opensvc.com

**Description:**

The url of the OpenSVC Collector v3. The node feeds it, and reaches its
server api, when the node is registered on it.
If collector.feeder or collector.server are not explicitly defined, they are
derived from this value.


