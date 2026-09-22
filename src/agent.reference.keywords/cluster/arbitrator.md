# Driver `arbitrator`

**Minimal configlet:**

	[arbitrator]
	uri = http://www.opensvc.com

**Minimal setup command:**

	om test/ccfg/foo set --kw="uri=http://www.opensvc.com"

**Supported keywords:**

- comment
- insecure
- uri
- weight

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
	default:     false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

Set to `true` to disable the arbitrator SSL certificate verification on the
https uri.

This should only be enabled for testing.


## Keyword `uri`

	required:    true
	scopable:    false
	aliases:     name
	rbac:        This driver group requires the root grant.

**Example:**

	uri=http://www.opensvc.com

**Description:**

The arbitrator uri used by cluster node to ask for a vote when the cluster is
split.

When the uri scheme is http or https, the vote checker is based on a GET
request, else it is based on a TCP connect.

For backward compatibility, when the port is not specified in a TCP connect
uri, the 1214 port is implied.

Arbitrators are tried in sequence, each reachable arbitrator gives a vote.

In case of a real split, all arbitrators are expected to be unreachable from
the lost segment. At least one of them is expected to be reachable from the
surviving segment.

Arbitrators of a cluster must thus be located close enough to each other, so a
subset of arbitrators can't be reachable from a split cluster segment, while
another subset of arbitrators is reachable from the other split cluster segment.

But not close enough so they can all fail together. Usually, this can be
interpreted as: same site, not same rack and power lines.

Arbitrators are verified every 60s to alert admins of the arbitrator failures.


## Keyword `weight`

	required:    false
	scopable:    false
	default:     1
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

During a quorum vote, this reachable arbitrator contributes <n> votes.


