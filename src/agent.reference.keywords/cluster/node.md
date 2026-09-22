# Driver `node`

**Supported keywords:**

- allowed_networks
- asset_env
- branch
- collector
- collector_feeder
- collector_ping_interval
- collector_server
- collector_status_delay
- collector_timeout
- comment
- dbcompliance
- dbinsecure
- dblog
- dbopensvc
- env
- loc_addr
- loc_building
- loc_city
- loc_country
- loc_floor
- loc_rack
- loc_room
- loc_zip
- maintenance_grace_period
- max_key_size
- max_parallel
- min_avail_mem_pct
- min_avail_swap_pct
- ready_period
- rejoin_grace_period
- repo
- repocomp
- repopkg
- ruser
- sec_zone
- secure_fetch
- split_action
- sshkey
- team_integ
- team_support

## Keyword `allowed_networks`

	required:    false
	scopable:    false
	default:     10.0.0.0/8 172.16.0.0/24 192.168.0.0/16
	convert:     list
	rbac:        This driver group requires the root grant.

**Description:**

The list of cidr blocks the agents allows creation of backend network into.

Should be restricted to match your site constraints.


## Keyword `asset_env`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	asset_env=Production

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `branch`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	branch=1.9

**Description:**

Set the targeted opensvc agent branch.

The downloaded upgrades will honor that branch.

If not set, the `repopkg` imposes the target branch via the current link.

It is recommended to set `branch` when `repopkg` points to a repository
you are not responsible for.


## Keyword `collector`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	collector=https://collector.opensvc.com

**Description:**

The system enables OpenSVC Collector 3 calls conditional upon the detection of
the Collector 3 environment.
If collector_feeder or collector_server are not explicitly defined, they are
derived from this value.


## Keyword `collector_feeder`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Default:**

`node.collector`/feeder if node.collector is defined.
**Example:**

	collector_feeder=https://collector.opensvc.com/feeder

**Description:**

OpenSVC enables Collector v3 feeder calls upon detection of a collector v3 instance.


## Keyword `collector_ping_interval`

	required:    false
	scopable:    false
	aliases:     db_min_ping_interval
	default:     60s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	collector_ping_interval=120s

**Description:**

Set the minimum interval between 2 push alive status to collector.
It is called when there are no daemon status changes, but we want
to send alive status to collector.
Minimum value: 60s


## Keyword `collector_server`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Default:**

`node.collector`/server if node.collector is defined.
**Example:**

	collector_server=https://collector.opensvc.com/server

**Description:**

OpenSVC enables Collector v3 server calls upon detection of a collector v3 instance.

## Keyword `collector_status_delay`

	required:    false
	scopable:    false
	aliases:     db_min_update_interval
	default:     10s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	collector_status_delay=30s

**Description:**

Set the minimum delay before next push daemon status changes to collector.
Minimum value: 10s

## Keyword `collector_timeout`

	required:    false
	scopable:    false
	default:     5s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

The maximum time to wait for a collector v3 call. Maximum allowed value 20.


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


## Keyword `dbcompliance`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Default:**

Same protocol, server and port as `dbopensvc`, but with a different path.

**Example:**

	dbcompliance=https://collector.opensvc.com

**Description:**

Set the uri of the collector's main rpc server.

The path part of the uri can be left unspecified.


## Keyword `dbinsecure`

	required:    false
	scopable:    false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

Set to `true` to disable the collector x509 certificate verification.

This should only be used for testing.


## Keyword `dblog`

	required:    false
	scopable:    false
	default:     true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

If `true` and `dbopensvc` is set, the objects action logs are reported to the
collector.

Set to `false` to disable log reporting to the collector, even if `dbopensvc`
is set.


## Keyword `dbopensvc`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	dbopensvc=https://collector.opensvc.com

**Description:**

Set the uri of the collector's feed rpc server.

The path part of the uri can be left unspecified.

If `dbopensvc` is not set, the agent does not try to communicate with a
collector.


## Keyword `env`

	required:    false
	scopable:    false
	default:     TST
	rbac:        This driver group requires the root grant.

**Description:**

A code like PRD, DEV, etc... the agent can use to enforce data protection policies:

* A non-PRD object instance can not be started on a PRD node
* A PRD object instance can be started on a non-PRD node (typically in a DRP situation)



## Keyword `loc_addr`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_addr=7 rue blanche

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `loc_building`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_building=Crystal

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `loc_city`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_city=Paris

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `loc_country`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_country=fr

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `loc_floor`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_floor=21

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `loc_rack`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_rack=R42

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `loc_room`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_room=102

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `loc_zip`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	loc_zip=75017

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `maintenance_grace_period`

	required:    false
	scopable:    false
	default:     60
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

A duration expression, like `1m30s`, defining how long the daemon keeps
remote node data while it is known to be in `maintenance`.

The maintenance state is announced to peers at the beginning of a `daemon
stop` and `daemon restart`, but not on daemon shutdown.

As long as the remote node data is kept, the local daemon won't takeover
the instances running on the node in maintenance.

This parameter should be adjusted to span the daemon restart time.


## Keyword `max_key_size`

	required:    false
	scopable:    false
	default:     1mb
	convert:     size
	rbac:        This driver group requires the root grant.

**Description:**

The maximum size of a value stored in a `cfg` or `sec` datastore key.

Adding or changing a key with a larger value is refused.


## Keyword `max_parallel`

	required:    false
	scopable:    false
	default:     10
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

Allow a maximum of `max_parallel` CRM commands to run simultaneously.

Applies to both:

* `om <selector> <action>` commands.
* commands executed by the daemon for orchestrations


## Keyword `min_avail_mem_pct`

	required:    false
	scopable:    false
	aliases:     min_avail_mem
	default:     2
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The minimum required available memory to allow orchestration.


## Keyword `min_avail_swap_pct`

	required:    false
	scopable:    false
	aliases:     min_avail_swap
	default:     10
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The minimum required available swap to allow orchestration.


## Keyword `ready_period`

	required:    false
	scopable:    false
	default:     5s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

A duration expression, like `10s`, defining how long the daemon waits before
starting a service instance in `ready` state.

A peer node can preempt the start during this period.

Usually set to allow at least a couple of heartbeats to be received.


## Keyword `rejoin_grace_period`

	required:    false
	scopable:    false
	default:     90s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

A duration expression, like `1m30s`, defining how long a starting daemon waits
in `rejoin` state.

The daemon normally exits the `rejoin` state when it has received a heartbeat
from all its peer nodes.

During this phase, the orchestration is not allowed, to give a chance to
place the services optimally when multiple daemon were restarted at the same
time.

But if a peer stays down, the other daemons have to stop waiting at some
point to let the service start, even if not on their natural placement leader.

This should be adjusted to:

	2s + <longest reboot duration>


The worse case of multiple nodes reboot is when the longest reboot node is
rebooted near the end of the reboot of the second longest rebooting node.

	|==========>
        n1 reboot
                    |--------------------|
                    n1 rejoin_grace_period
                    |================>
                    n1 in rejoin state
                                      |=====================
                                      n1 in idle state
                  |==================>
                  n2 reboot
                                      |--------------------|
                                      n2 rejoin_grace_period
                                      |=====================
                                      n2 in idle state
                                           
As a consequence, to minimize the `rejoin_grace_period`, prefer fast boot
nodes.


## Keyword `repo`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	repo=http://opensvc.repo.corp

**Description:**

Set the uri of the opensvc agent package repository and compliance modules
gzipped tarball repository.

This parameter is used by the `om node updatepkg` and `om node updatecomp`
commands.

Expected repository structure:

ROOT
+- compliance
|+- compliance-100.tar.gz
|+- compliance-101.tar.gz
|`- current -> compliance-101.tar.gz
+- packages
 +- deb
 +- depot
 +- pkg
 +- sunos-pkg
 +- rpms
 |+- current -> 2.0/current
 |+- 1.9
 | +- current -> opensvc-1.9-50.rpm
 | +- opensvc-1.9-49.rpm
 | `- opensvc-1.9-50.rpm
 |+- 2.0
 | +- current -> opensvc-2.0-90.rpm
 | `- opensvc-2.0-90.rpm
 `- tbz


## Keyword `repocomp`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	repocomp=http://compliance.repo.corp

**Description:**

Set the uri of the opensvc compliance modules repository.

A gzipped tarball is expected to be found there by the `om node updatecomp`
command.

Expected repository structure:

	ROOT
	+- compliance-100.tar.gz
	+- compliance-101.tar.gz
	`- current -> compliance-101.tar.gz


## Keyword `repopkg`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	repopkg=http://repo.opensvc.com

**Description:**

Set the uri of the opensvc agent package repository.

This parameter is used by the `om node updatepkg` command.

Expected repository structure:

ROOT
+- deb
+- depot
+- pkg
+- sunos-pkg
+- rpms
|+- current -> 2.0/current
|+- 1.9
| +- current -> opensvc-1.9-50.rpm
| +- opensvc-1.9-49.rpm
| `- opensvc-1.9-50.rpm
|+- 2.0
| +- current -> opensvc-2.0-90.rpm
| `- opensvc-2.0-90.rpm
`- tbz


## Keyword `ruser`

	required:    false
	scopable:    false
	default:     root
	rbac:        This driver group requires the root grant.

**Example:**

	ruser=root opensvc@node1

**Description:**

Set the remote user to use to login to a remote node with ssh and rsync.

The remote user must have the privileges to run as root the following commands
on the remote node:

* om
* rsync

The default ruser is root for all nodes.

`ruser` accepts a list of `user[@node]`.
If @node is omitted, user is considered the new default user.


## Keyword `sec_zone`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	sec_zone=dmz1

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `secure_fetch`

	required:    false
	scopable:    false
	default:     true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

If set to false, disable ssl authentication checks on all uri fetches.


## Keyword `split_action`

	required:    false
	scopable:    true
	candidates:  crash, reboot, disabled
	default:     crash
	rbac:        This driver group requires the root grant.

**Description:**

The node suicide method to use when a cluster split occurs and the node does
not have the quorum.

This opting-out is meant to avoid double-start situations when the cluster
is split.

Possible values are:

* `crash`

  Default.

* `reboot`

  May be preferred when the node power-on is not easy. No remote access via
  IPMI or equivalent for example.

* `disabled`

  May be used for test or training only (it does nothing).


## Keyword `sshkey`

	required:    false
	scopable:    false
	default:     opensvc
	rbac:        This driver group requires the root grant.

**Description:**

The basename of the ssh public key served by the GET /node/name/:nodename/ssh/key.
For example, the `opensvc` default value serves ~/.ssh/opensvc.pub.


## Keyword `team_integ`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	team_integ=TINT

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


## Keyword `team_support`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	team_support=TSUP

**Description:**

An asset information to push to the collector on `om node push asset`, overriding the currently stored value.


