# Driver `disk.sgcp_nfs_cg`

**Minimal configlet:**

	[disk#1]
	type = sgcp_nfs_cg
	uuid = 

**Minimal setup command:**

	om test/svc/foo set \
		--kw="type=sgcp_nfs_cg" \
		--kw="uuid="

**Supported keywords:**

- az
- blocking_post_provision
- blocking_post_start
- blocking_post_stop
- blocking_post_unprovision
- blocking_pre_provision
- blocking_pre_start
- blocking_pre_stop
- blocking_pre_unprovision
- comment
- disable
- encap
- endpoint
- failover
- monitor
- optional
- pg_blkio_weight
- pg_cpu_quota
- pg_cpu_shares
- pg_cpus
- pg_mem_limit
- pg_mem_oom_control
- pg_mem_swappiness
- pg_mems
- pg_vmem_limit
- post_provision
- post_start
- post_stop
- post_unprovision
- pre_provision
- pre_start
- pre_stop
- pre_unprovision
- provision
- provision_requires
- restart
- restart_delay
- secret
- shared
- standby
- start_requires
- stat_timeout
- stop_requires
- subset
- tags
- timeout
- type
- unprovision
- unprovision_requires
- uuid

## Keyword `az`

	required:    false
	scopable:    true
	default:     {node.labels.az}
	rbac:        This driver group requires the root grant.

**Description:**

The availability zone of the local node. Use a reference to a node label or a scoped value.

The default resolves the az node label, so a node where that label is unset
has to set this keyword. The resource refuses to configure without it: the
start action would then ask for a switchover to an empty availability zone.


## Keyword `blocking_post_provision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `provision` action.

Errors interrupt the action.

This trigger is only executed on leaders.


## Keyword `blocking_post_start`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `start` action.

Errors interrupt the action.


## Keyword `blocking_post_stop`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `stop` action.

Errors interrupt the action.


## Keyword `blocking_post_unprovision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `unprovision` action.

Errors interrupt the action.

This trigger is only executed on leaders.


## Keyword `blocking_pre_provision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `provision` action.

Errors interrupt the action.


## Keyword `blocking_pre_start`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `start` action.

Errors interrupt the action.


## Keyword `blocking_pre_stop`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `stop` action.

Errors interrupt the action.


## Keyword `blocking_pre_unprovision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `unprovision` action.

Errors interrupt the action.


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


## Keyword `disable`

	required:    false
	scopable:    true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

A disabled resource will be ignored on `start`, `stop`, `provision` and
`unprovision` actions.

A disabled resource status is `n/a`.

If set in the `DEFAULT` section of an object, the object is disabled and
ignores `start`, `stop`, `shutdown`, `provision` and `unprovision` actions.

These actions immediately return success.

`om <path> disable` sets `DEFAULT.disable=true`.

`om <path> enable` sets `DEFAULT.disable=false`.

> **Note**: The `enable` and `disable` actions preserve the individual
  resource `disable` state.


## Keyword `encap`

	required:    false
	scopable:    false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

Set to `true` to ignore this resource in the nodes context and consider it in the encapnodes context. The resource is thus handled by agents deployed in the service containers.


## Keyword `endpoint`

	required:    false
	scopable:    true
	rbac:        This driver group requires the root grant.

**Description:**

The fileaas api url.

By default, the api results are served from a local cache to the status
evaluations run by the daemon scheduler, and to the ones run by an action
with a resource selection that neither includes nor requires this resource,
like `om <path> app start`. Every other action, an operator status or an action
on or requiring this resource first of all, reads the api again. Set the
OSVC_SGCP_CACHE environment variable to override this default whatever the
action: `1` serves the cached values, `0` never does, the daemon scheduler
included. Any other value is ignored, with a warning in the resource status.

A cached value is only served while younger than the cache.ttl_seconds
value from the sgcp configuration file, and a zero ttl disables the cache.

## Keyword `failover`

	required:    false
	scopable:    true
	default:     true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

The failover keyword is used during the start action when --force is not specified.
When set to true, it enables fallback to the failover operation if the initial switchover operation fails with status code 412 and the action originates from the daemon.
When start --force is used, the failover operation is used directly, without first trying switchover, regardless of the failover keyword value.


## Keyword `monitor`

	required:    false
	scopable:    true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

A resource with `monitor=true` will trigger the `monitor_action`
(crash or reboot the node, freezestop or switch the service) if:

* The resource is `down`.

* The instance has `local_expect=started` in its daemon monitor data, which
  means the daemon considers this instance is and should remain started.

* All restart tentatives failed.


## Keyword `optional`

	required:    false
	scopable:    true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

Action errors on optional resources are logged but do not interrupt the action sequence.

The status of optional resources is not included in the instance availability status but is considered in the overall status.

The status of task and sync resources is always included in the overall status, regardless of whether they are marked as optional.

Resources tagged as `noaction` are considered optional by default.

Dump filesystems are a typical use case for optional=true.


## Keyword `pg_blkio_weight`

	required:    false
	scopable:    true
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

**Example:**

	pg_vmem_limit=1g

**Description:**

Ensures the service does not use more than specified memory+swap (in bytes).

The Out-Of-Memory killer is triggered in case of tresspassing.
The specified value must be greater than `pg_mem_limit`.

Setting this keyword to `default` puts the capping back where a node that
never capped anything leaves it. Removing the keyword does not: what was
written stays written, whether om wrote it or something else did.


## Keyword `post_provision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `provision` action.

Errors do not interrupt the action.

This trigger is only executed on leaders.


## Keyword `post_start`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `start` action.

Errors do not interrupt the action.


## Keyword `post_stop`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `stop` action.

Errors do not interrupt the action.


## Keyword `post_unprovision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `unprovision` action.

Errors do not interrupt the action.

This trigger is only executed on leaders.


## Keyword `pre_provision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `provision` action.

Errors do not interrupt the action.


## Keyword `pre_start`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `start` action.

Errors do not interrupt the action.


## Keyword `pre_stop`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `stop` action.

Errors do not interrupt the action.


## Keyword `pre_unprovision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `unprovision` action.

Errors do not interrupt the action.


## Keyword `provision`

	required:    false
	scopable:    false
	default:     true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

Set to `false` to ignore the `provision` and `unprovision` actions on the
resource.

> **Warning**: `provision` and `unprovision` use data-destructive operations
  like formatting.

It is recommended to set `provision=false` on long-lived critical objects,
to force administrators to remove this setting when they really want to
destroy data.


## Keyword `provision_requires`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	provision_requires=ip#0 fs#0(down,stdby down)

**Description:**

A whitespace-separated list of conditions to meet to accept a 'provision'
action.

A condition is expressed as `<rid>(<state>,...)`.

If states are omitted, `up,stdby up` is used as the default expected states.


## Keyword `restart`

	required:    false
	scopable:    true
	default:     0
	convert:     int
	rbac:        This driver group requires the root grant.

**Description:**

The daemon will try to restart a resource if:

* The resource is `down`, `stdby down` or `warn`.

* The instance has `local_expect=started` in its daemon monitor data, which
  means the daemon considers this instance is and should remain started.

* The node is not frozen

* The instance is not frozen

In this case, the daemon try `restart=<n>` times before falling back to the
monitor action.

The `restart_delay` keyword sets the interval after a failed restart before
the next tentative.

Resources with `standby=true` have `restart` forced to a minimum of 2, to
increase chances of a restart success.


## Keyword `restart_delay`

	required:    false
	scopable:    true
	default:     500ms
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

The minimum delay between two restart tentatives on the resource.


## Keyword `secret`

	required:    false
	scopable:    true
	rbac:        This driver group requires the root grant.

**Description:**

The name of the secret object in the same namespace containing the api access credentials.

## Keyword `shared`

	required:    false
	scopable:    true
	convert:     bool
	rbac:        This driver group requires the root grant.

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

> **Warning**: If admins want to submit `--local` provision or unprovision
  commands themselves, they have to set the `--leader` flag correctly.

Flex objects usually don't use shared resources. But if they do, only
the flex primary gets `--leader` commands.

> **Warning**: All resources depending on a shared resource must also be
  flagged as shared.


## Keyword `standby`

	required:    false
	scopable:    true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

If `true`, always start the resource, even on non-started instances.

The daemon is responsible for starting standby resources.

A resource can be set standby on a subset of nodes using keyword scoping.

A typical use-case is a synchronized filesystem on non-shared disks. The
remote filesystem must be mounted to not overflow the underlying filesystem.

> **Warning**: In most situation, don't set shared resources standby, a
  non-clustered fs on shared disks for example.


## Keyword `start_requires`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	start_requires=ip#0 fs#0(down,stdby down)

**Description:**

A whitespace-separated list of conditions to meet to accept a 'start'
action.

A condition is expressed as `<rid>(<state>,...)`.

If states are omitted, `up,stdby up` is used as the default expected states.


## Keyword `stat_timeout`

	required:    false
	scopable:    true
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

The fs resources status evaluation includes a stat syscall test.
This keyword defines the maximum wait time for those stat calls to respond.

When expired, the resource status is degraded is to warn, which can trigger
a monitor action (reboot or crash the node) if the resource is monitored.


## Keyword `stop_requires`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	stop_requires=ip#0 fs#0(down,stdby down)

**Description:**

A whitespace-separated list of conditions to meet to accept a 'stop'
action.

A condition is expressed as `<rid>(<state>,...)`.

If states are omitted, `up,stdby up` is used as the default expected states.


## Keyword `subset`

	required:    false
	scopable:    true
	rbac:        This driver group requires the root grant.

**Description:**

The name of the subset this resource is assigned to.

Resources of a same driver group and a same subset are ordered and acted upon
together, and are configured as a whole in a `[subset#<group>:<name>]` section,
or in a less precise `[subset#<name>]` one.

That section accepts `parallel`, to act on the members concurrently rather than
one after the other, and the `pg_*` keywords, to place the members in their own
process group.


## Keyword `tags`

	required:    false
	scopable:    true
	convert:     set
	rbac:        This driver group requires the root grant.

**Description:**

A whitespace-separated list of tags.

Tags can be used for resource selection by tag.

Some tags can influence the driver behaviour:

* `noaction`

  Skip any state changing action on the resource and imply `optional=true`.

* `nostatus`

  Force the status `n/a`.


## Keyword `timeout`

	required:    false
	scopable:    true
	convert:     duration
	rbac:        This driver group requires the root grant.

**Description:**

The maximum time to wait for a consistency group switchover.

## Keyword `type`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

The resource driver name.


## Keyword `unprovision`

	required:    false
	scopable:    false
	default:     true
	convert:     bool
	rbac:        This driver group requires the root grant.

**Description:**

Set to `false` to ignore the `unprovision` action on the resource.

> **Warning**: `unprovision` use data-destructive operations like
  formatting.

It is recommended to set `provision=false` on long-lived critical objects,
to force administrators to remove this setting when they really want to
destroy data.


## Keyword `unprovision_requires`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	unprovision_requires=ip#0 fs#0(down,stdby down)

**Description:**

A whitespace-separated list of conditions to meet to accept a 'unprovision'
action.

A condition is expressed as `<rid>(<state>,...)`.

If states are omitted, `up,stdby up` is used as the default expected states.


## Keyword `uuid`

	required:    true
	scopable:    true
	rbac:        This driver group requires the root grant.

**Description:**

The fileaas consistency group id.

