# Section `DEFAULT`

**Supported keywords:**

- access
- app
- children
- comment
- comp_schedule
- create_pg
- devices_from
- disable
- drpnodes
- env
- flex_max
- flex_min
- flex_primary
- flex_target
- hard_affinity
- hard_anti_affinity
- id
- info_schedule
- monitor_action
- monitor_schedule
- nodes
- parents
- pg_blkio_weight
- pg_cpu_quota
- pg_cpu_shares
- pg_cpus
- pg_mem_limit
- pg_mem_oom_control
- pg_mem_swappiness
- pg_mems
- pg_vmem_limit
- placement
- pool
- pre_monitor_action
- provision
- provision_timeout
- rollback
- run_schedule
- shared
- size
- soft_affinity
- soft_anti_affinity
- start_timeout
- stat_timeout
- status_schedule
- status_timeout
- stonith
- stop_timeout
- sync_schedule
- sync_timeout
- timeout
- topology
- type
- unprovision
- unprovision_timeout

## Keyword `access`

	required:    false
	scopable:    true
	candidates:  rwo, roo, rwx, rox
	default:     rwo
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The access mode of the volume.

* `rwo` is Read Write Once
* `roo` is Read Only Once
* `rwx` is Read Write Many
* `rox` is Read Only Many

`rox` and `rwx` modes are served by flex volume services.


## Keyword `app`

	required:    false
	scopable:    false
	default:     default
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

A user-defined code linking to:

* who is responsible for this service.
* who is billable.

This code thus provides a most useful object grouping and filtering key.

Short and simple codes, like ERP, are easier to work with.


## Keyword `children`

	required:    false
	scopable:    false
	convert:     listlowercase
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The list of services or instances expressed as `<path>[@<nodename>]` that must
be `down` or `stdby up` to allow this service to be stopped by the daemon.

The list is whitespace-separated.

Children are looked up in the same namespace first, so for a test/svc/svc1,
the `svc2` relation is interpreted as `test/svc/svc2`.

The `./svc/svc2` notation states that explicitly. It resolves in the namespace
of the object declaring it, so a set of objects cloned into another namespace
keeps referring to its own members.

To declare a relation to `svc2` in the root namespace, use the fully
qualified path notation `root/svc/svc2`.


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


## Keyword `comp_schedule`

	required:    false
	scopable:    true
	default:     ~00:00-06:00
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The instance compliance run schedule.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `create_pg`

	required:    false
	scopable:    true
	default:     true
	convert:     bool
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

Use process grouping when possible.

If turned on, the agent will create a container group for:

* the object
* each resource group (ie, the subset:drivergroup tuple)
* each resource

A container group allows capping the memory, swap and cpu usage.
These cappings can be defined using the `pg_*` keywords in the
DEFAULT, the subset or the resource section.


## Keyword `devices_from`

	required:    false
	scopable:    false
	convert:     list
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The list of resources that contribute their exposed devices to the volume exposed devices.

 If not specified, only the last disk contributes.


## Keyword `disable`

	required:    false
	scopable:    true
	convert:     bool

**Description:**

Disables the object instance:

* Instance and all resource statuses become `n/a`.
* Instance actions (e.g. start, stop, ...) are silently ignored.
* Resources stay disabled regardless of `DEFAULT.disable=false`.
* `disable=false` on a resource does not override `DEFAULT.disable=true`.


## Keyword `drpnodes`

	required:    false
	scopable:    true
	convert:     peers
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	drpnodes=n1 n2

**Description:**

A node selector expression specifying the list of cluster nodes hosting
object instances when all primary `nodes` are unavailable, like in a
DRP situation.

If not specified or left empty, the node evaluating the keyword is
assumed to be the only instance hosting node.

Labels can be used to define a list of nodes by an arbitrary property.
For example `cn=fr cn=kr` would be evaluated as `n1 n2 n3` if `n1` and
`n2` have the `cn=fr` label and `n3` has the `cn=kr` label.

The glob syntax can be used in the node selector expression. For
example `n1 n[23] n4*` would be expanded to `n1 n2 n3 n4` in a
`n1 n2 n3 n4 n5` cluster.

The drpnodes can be data synchronization targets for `sync` resources.


## Keyword `env`

	required:    false
	scopable:    false
	aliases:     service_type
	rbac:        A volume keyword other than size requires the root grant.

**Default:**

The same as the node `env`.

**Description:**

A code like PRD, DEV, etc... the agent can use to enforce data protection policies:

* A non-PRD object instance can not be started on a PRD node
* A PRD object instance can be started on a non-PRD node (typically in a DRP situation)

The default value is read from the node `env` keyword.



## Keyword `flex_max`

	required:    false
	scopable:    false
	aliases:     flex_max_nodes
	depends:     topology=flex
	default:     {#nodes}
	convert:     int
	rbac:        A volume keyword other than size requires the root grant.

**Default:**

The number of elements in `nodes`.

**Description:**

The maximum number of up instances of this object in the cluster.
Above this number the aggregated object status is degraded to warn.

The `0` value is interpreted as unlimited.


## Keyword `flex_min`

	required:    false
	scopable:    false
	aliases:     flex_min_nodes
	depends:     topology=flex
	default:     1
	convert:     int
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The minimum number of up instances of this object in the cluster.
Below this number the aggregated object status is degraded to warn.


## Keyword `flex_primary`

	required:    false
	scopable:    true
	depends:     topology=flex
	convert:     listlowercase
	rbac:        A volume keyword other than size requires the root grant.

**Default:**

The first node of `nodes`.

**Description:**

The node in charge of syncing the other nodes in a flex object.


## Keyword `flex_target`

	required:    false
	scopable:    false
	depends:     topology=flex
	default:     {flex_min}
	convert:     int
	rbac:        A volume keyword other than size requires the root grant.

**Default:**

The value of `flex_min`.

**Description:**

The optimal number of up instances of the object in the cluster.
The value must be between `flex_min` and `flex_max`.

If `orchestrate=ha`, the daemon is free to take action to reach the
`flex_target`.


## Keyword `hard_affinity`

	required:    false
	scopable:    false
	aliases:     affinity
	convert:     listlowercase
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	hard_affinity=svc1 svc2

**Description:**

A whitespace separated list of object paths.

These objects must be started on the local node to allow the local monitor
to start an instance of the service.


## Keyword `hard_anti_affinity`

	required:    false
	scopable:    false
	aliases:     anti_affinity
	convert:     listlowercase
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	hard_anti_affinity=svc1 svc2

**Description:**

A whitespace separated list of object paths.

These object must not be started on the local node to allow the local monitor
to start an instance of the object.


## Keyword `id`

	required:    false
	scopable:    false
	recorded:    written when what it names is made, and reset when the object is cloned
	rbac:        A volume keyword other than size requires the root grant.

**Default:**

A random generated UUID.

**Description:**

A rfc4122 random uuid generated by the agent.


## Keyword `info_schedule`

	required:    false
	scopable:    true
	aliases:     resinfo_schedule
	default:     @60m
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The instance resource info refresh schedule.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `monitor_action`

	required:    false
	scopable:    true
	candidates:  crash, freezestop, none, reboot, switch
	default:     none
	convert:     list
	rbac:        Requires the root grant, except for the values switch, freezestop, none.

**Example:**

	monitor_action=reboot

**Description:**

The action to trigger when a monitored resource is no longer in the "up" or
"standby up" state, and all restart attempts for the resource have failed.

The `reboot` and `crash` monitor actions do not attempt to cleanly stop any
processes. On Linux, they utilize system-level sysrq triggers.

This behavior is designed to ensure that the host stops writing to shared
disks as quickly as possible, minimizing the risk of data corruption. This
is critical because a failover node is likely preparing to write to the same
shared disks.

You can append a fallback monitor action to this keyword. A common example
is `freezestop reboot`. In this case, the reboot action will be executed
if the stop fails or times out.

Other monitor_actions values:
  - `none`: Is the No Operation monitor action (the default value).
  - `freezestop`: freeze and subsequently stop the monitored instance.
  - `switch`: try monitored instance stop to allow any other cluster nodes to
     takeover the instance.


## Keyword `monitor_schedule`

	required:    false
	scopable:    true
	default:     @1m
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The instance monitored resources status evaluation schedule.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `nodes`

	required:    false
	scopable:    true
	convert:     nodes
	rbac:        A volume keyword other than size requires the root grant.

**Default:**

The lowercased hostname of the evaluating node.

**Example:**

	nodes=n1 n*

**Description:**

A node selector expression specifying the list of cluster nodes hosting
object instances.

If not specified or left empty, the node evaluating the keyword is
assumed to be the only instance hosting node.

Labels can be used to define a list of nodes by an arbitrary property.
For example `cn=fr cn=kr` would be evaluated as `n1 n2 n3` if `n1` and
`n2` have the `cn=fr` label and `n3` has the `cn=kr` label.

The glob syntax can be used in the node selector expression. For
example `n1 n[23] n4*` would be expanded to `n1 n2 n3 n4` in a
`n1 n2 n3 n4 n5` cluster.


## Keyword `parents`

	required:    false
	scopable:    false
	convert:     listlowercase
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The list of services or instances expressed as `<path>[@<nodename>]` that must
be `up` to allow this service to be started by the daemon.

The list is whitespace-separated.

Parents are looked up in the same namespace first, so for a test/svc/svc1,
the `svc2` relation is interpreted as `test/svc/svc2`.

The `./svc/svc2` notation states that explicitly. It resolves in the namespace
of the object declaring it, so a set of objects cloned into another namespace
keeps referring to its own members.

To declare a relation to `svc2` in the root namespace, use the fully
qualified path notation `root/svc/svc2`.


## Keyword `pg_blkio_weight`

	required:    false
	scopable:    true

**Example:**

	pg_blkio_weight=50

**Description:**

Block IO relative weight. Value: between `10` and `1000`.

The kernel default is `100`.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `pg_cpu_quota`

	required:    false
	scopable:    true

**Example:**

	pg_cpu_quota=50%@all

**Description:**

The percentage of cpu time the processes of the group may use.

Accepted expressions:

* `50%`
  Half of one cpu.

* `50%@all`
  Half of every cpu the node has.

* `10%@2`
  A tenth of two cpus.

Unlike `pg_cpu_shares`, which only arbitrates when the node is cpu-bound, a
quota caps the group whether or not the node is busy.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `pg_cpu_shares`

	required:    false
	scopable:    true
	convert:     size

**Example:**

	pg_cpu_shares=512

**Description:**

The kernel default value is used, which usually is 1024 shares.

In a cpu-bound situation, this setting ensures the service does not use more
than its share of cpu resource. The actual percentile depends on shares
allowed to other services.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `pg_cpus`

	required:    false
	scopable:    true
	depends:     create_pg=true

**Example:**

	pg_cpus=0-2

**Description:**

Allow service process to bind only the specified cpus.

Cpus are specified as list or range : `0,1,2` or `0-2`.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `pg_mem_limit`

	required:    false
	scopable:    true
	convert:     size

**Example:**

	pg_mem_limit=512m

**Description:**

Ensures the service does not use more than specified memory (in bytes).

The Out-Of-Memory killer is triggered in case of tresspassing.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `pg_mem_oom_control`

	required:    false
	scopable:    true

**Example:**

	pg_mem_oom_control=1

**Description:**

A flag (0 or 1) that enables or disables the Out of Memory killer for the
processes of the group.

* If enabled (0), tasks that attempt to consume more memory than they are
  allowed are immediately killed by the OOM killer.
* If disabled (1), tasks are allowed to continue to try allocating memory,
  stressing the system.

The OOM killer is enabled by default in every cgroup using the memory
controller.

This keyword caps nothing on a node holding the unified cgroup hierarchy,
which has no `memory.oom_control`: that file is of the v1 hierarchy. Setting
it there is warned about, and ignored.


## Keyword `pg_mem_swappiness`

	required:    false
	scopable:    true

**Example:**

	pg_mem_swappiness=40

**Description:**

Set a swappiness percentile value for the process group.

This keyword caps nothing on a node holding the unified cgroup hierarchy,
which has no `memory.swappiness`: that file is of the v1 hierarchy. Setting
it there is warned about, and ignored.


## Keyword `pg_mems`

	required:    false
	scopable:    true

**Example:**

	pg_mems=0-2

**Description:**

Allow service process to bind only the specified memory nodes.

Memory nodes are specified as list or range : `0,1,2` or `0-2`.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `pg_vmem_limit`

	required:    false
	scopable:    true
	convert:     size

**Example:**

	pg_vmem_limit=1g

**Description:**

Ensures the service does not use more than specified memory+swap (in bytes).

The Out-Of-Memory killer is triggered in case of tresspassing.
The specified value must be greater than `pg_mem_limit`.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `placement`

	required:    false
	scopable:    false
	candidates:  , last start, load avg, nodes order, none, score, shift, spread
	default:     nodes order
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

Set a service instances placement policy:

* `none`

  No placement policy. a policy for dummy, observe-only, services.

* `nodes order`

  The left-most available node is allowed to start a service instance when
  necessary.

* `last start`

  The preferred instances is the one started last.

* `load avg`

  The least loaded node takes precedences.

* `shift`

  Shift the nodes order ranking by the service prefix converter to an integer.

* `spread`

  A spread policy tends to perfect leveling with many services.

* `score`

  The highest scoring node takes precedence (the score is a composite indice
  of load, mem and swap).


## Keyword `pool`

	required:    false
	scopable:    true
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The name of the pool this volume was allocated from.


## Keyword `pre_monitor_action`

	required:    false
	scopable:    true
	rbac:        Requires the root grant.

**Example:**

	pre_monitor_action=/bin/true

**Description:**

A callout to execute before the `monitor_action`.

For example, if `monitor_action = freezestop`, a `pre_monitor_action` script
may decide to crash the server if it detects a situation were `freezestop` can
not succeed (for example, a fs can not be umounted due to an unresponsive
storage array).


## Keyword `provision`

	required:    false
	scopable:    true
	default:     true
	convert:     bool

**Description:**

Set in the default section, `provision=false` cancels the instance provision action before looping over the resources.
In this case, the action returns an error.

This acts like a glass the user has to break to access the provision button.


## Keyword `provision_timeout`

	required:    false
	scopable:    true
	convert:     duration
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	provision_timeout=1m30s

**Description:**

Wait for `<duration>` before declaring the action a failure.

Takes precedence over `timeout`.


## Keyword `rollback`

	required:    false
	scopable:    true
	default:     true
	convert:     bool
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

If set to `false`, the default *rollback on start action error* behaviour is
disabled, leaving the instance in its half-started state (avail `warn`).

The daemon then refuses to failover a service if any instance is in `warn`
availabity state. It is highly recommended to not use `rollback=false` if
`orchestrate=ha`.


## Keyword `run_schedule`

	required:    false
	scopable:    true
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The instance tasks run action default schedule.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `shared`

	required:    false
	scopable:    true
	default:     true
	convert:     bool

**Description:**

If `true`, the resource will be considered shared during provision and
unprovision actions.

A shared resource driver can implement a different behaviour depending
on weither it is run from the leader instance, or not:

* When `--leader` is set, the driver creates and configures the system
  objects. For example the disk.disk driver allocates a SAN disk and
  discover its block devices.

* When `--leader` is not set, the driver does not redo the actions
  already done by the leader, but may do some. For example, the
  disk.disk driver skips the SAN disk allocation, but discovers the
  block devices.

The daemon takes care of setting the `--leader` flags on the commands
it submits during deploy, purge, provision and unprovision
orchestrations.

> *Warning*: If admins want to submit `--local` provision or unprovision
  commands themselves, they have to set the `--leader` flag correctly.

Flex objects usually don't use shared resources. But if they do, only
the flex primary gets `--leader` commands.


## Keyword `size`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The size used by this volume in its pool.


## Keyword `soft_affinity`

	required:    false
	scopable:    false
	convert:     listlowercase
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	soft_affinity=svc1 svc2

**Description:**

A whitespace separated list of services that must be started on the node to allow the monitor to start this service.

If the local node is the only candidate ignore this constraint and allow start.


## Keyword `soft_anti_affinity`

	required:    false
	scopable:    false
	convert:     listlowercase
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	soft_anti_affinity=svc1 svc2

**Description:**

A whitespace separated list of services that must not be started on the node to allow the monitor to start this service.

If the local node is the only candidate ignore this constraint and allow start.


## Keyword `start_timeout`

	required:    false
	scopable:    true
	convert:     duration
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	start_timeout=1m30s

**Description:**

Wait for `<duration>` before declaring the action a failure.

Takes precedence over `timeout`.


## Keyword `stat_timeout`

	required:    false
	scopable:    true
	convert:     duration

**Description:**

The fs resources status evaluation includes a stat syscall test.
This keyword defines the maximum wait time for those stat calls to respond.

When expired, the resource status is degraded is to warn, which can trigger
a monitor action (reboot or crash the node) if the resource is monitored.


## Keyword `status_schedule`

	required:    false
	scopable:    true
	default:     @10m
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The instance status evaluation schedule.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `status_timeout`

	required:    false
	scopable:    true
	default:     1m
	convert:     duration
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	status_timeout=10s

**Description:**

The maximum duration of the instance status evaluation.

For example, the total start action duration is constrained by different timeouts:

* the `start_timeout`
  Limiting the start action duration.

* the `stop_timeout`
  Limiting the start rollback duration triggered by start errors.

* the `status_timeout`
  Limiting the post-start instance status evaluation duration.


## Keyword `stonith`

	required:    false
	scopable:    false
	depends:     topology=failover
	default:     false
	convert:     bool
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

Enable the stonith callout for this object.

Shoot The Other Node In The Head, aka fence, using a callout.

The callout is triggered after a quorum vote won, when the surviving node is
about to start a local instance of a service that was known to be started on
a unreachable peer node.

The callout is meant to prevent the peer from writing to shared disks, remote
databases, and from responding to clients.

The callout itself is the `command` keyword of the peer `stonith#<nodename>`
section of the node configuration.


## Keyword `stop_timeout`

	required:    false
	scopable:    true
	convert:     duration
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	stop_timeout=1m30s

**Description:**

Wait for `<duration>` before declaring the action a failure.

Takes precedence over `timeout`.


## Keyword `sync_schedule`

	required:    false
	scopable:    true
	default:     04:00-06:00
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The instance sync default schedule.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `sync_timeout`

	required:    false
	scopable:    true
	convert:     duration
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	sync_timeout=1m30s

**Description:**

Wait for `<duration>` before declaring the action a failure.

Takes precedence over `timeout`.


## Keyword `timeout`

	required:    false
	scopable:    true
	default:     1h
	convert:     duration
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	timeout=2h

**Description:**

Wait for `<duration>` before declaring a state-changing action a failure.

A per-action `<action>_timeout` can override this value.


## Keyword `topology`

	required:    false
	scopable:    false
	aliases:     cluster_type
	candidates:  failover, flex
	default:     failover
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

* `failover`

  The service is allowed to be up on one node at a time.

* `flex`

  The service can be up on `flex_target` nodes, where `flex_target` must be in
  the `[flex_min, flex_max]` range.


## Keyword `type`

	required:    false
	scopable:    false
	rbac:        A volume keyword other than size requires the root grant.

**Description:**

The resource driver name.


## Keyword `unprovision`

	required:    false
	scopable:    true
	default:     true
	convert:     bool

**Description:**

Set in the default section, `unprovision=false` cancels the instance provision action before looping over the resources.
In this case, the action returns an error.

This acts like a glass the user has to break to access the unprovision button.


## Keyword `unprovision_timeout`

	required:    false
	scopable:    true
	convert:     duration
	rbac:        A volume keyword other than size requires the root grant.

**Example:**

	unprovision_timeout=1m30s

**Description:**

Wait for `<duration>` before declaring the action a failure.

Takes precedence over `timeout`.


