# Driver `task.host`

**Minimal configlet:**

	[task#1]
	type = host

**Minimal setup command:**

	om test/vol/foo set --kw="type=host"

**Supported keywords:**

- blocking_post_provision
- blocking_post_run
- blocking_post_unprovision
- blocking_pre_provision
- blocking_pre_run
- blocking_pre_unprovision
- check
- command
- comment
- configs_environment
- confirmation
- cwd
- disable
- encap
- environment
- group
- limit_as
- limit_core
- limit_cpu
- limit_data
- limit_fsize
- limit_memlock
- limit_nofile
- limit_nproc
- limit_rss
- limit_stack
- limit_vmem
- log
- max_parallel
- monitor
- on_error
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
- post_run
- post_unprovision
- pre_provision
- pre_run
- pre_unprovision
- provision
- provision_requires
- retcodes
- run_requires
- run_timeout
- schedule
- secrets_environment
- shared
- snooze
- standby
- stat_timeout
- stop
- stop_timeout
- subset
- tags
- timeout
- type
- umask
- unprovision
- unprovision_requires
- user

## Keyword `blocking_post_provision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `provision` action.

Errors interrupt the action.

This trigger is only executed on leaders.


## Keyword `blocking_post_run`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `run` action.

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


## Keyword `blocking_pre_run`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `run` action.

Errors interrupt the action.


## Keyword `blocking_pre_unprovision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `unprovision` action.

Errors interrupt the action.


## Keyword `check`

	required:    false
	scopable:    true
	candidates:  last_run, last_run_warn, 

**Example:**

	check=last_run

**Description:**

If set to `last_run`, the last run retcode is used to report a task resource
status.

If set to `last_run_warn`, the last run error retcode is displayed as a
resource warning.

If not set (default), the status of a task is always n/a.


## Keyword `command`

	required:    false
	scopable:    true

**Description:**

The shlex expression of the command to execute on `run` actions.


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


## Keyword `configs_environment`

	required:    false
	scopable:    true
	convert:     shlex

**Example:**

	configs_environment=PORT=http/port webapp/app1* {name}/* {name}-debug/settings

**Description:**

A whitespace-separated list of `<var>=<cfg name>/<key path>` or
`<cfg name>/<key matcher>`.

If the `cfg` or config key doesn't exist then `start` and `stop` actions on
the resource will fail with a non 0 exit code.

A shell expression splitter is applied, so double quotes can be around
`<cfg name>/<key path>` only or whole `<var>=<cfg name>/<key path>`.

Example with,

* `<ns>/cfg/nginx` a config having a `user` key with value `user1`.

* `<ns>/cfg/cfg1` a config having a `key1` key with value `val1`.

`configs_environment = NGINX_USER=nginx/user cfg1/*` creates the following
variables in the process execution environment:

	NGINX_USER=user1
	key1=val1



## Keyword `confirmation`

	required:    false
	scopable:    false
	convert:     bool

**Description:**

If set to `true`, ask for an interactive confirmation to run the task.

This flag can be used for dangerous tasks like data restoration.


## Keyword `cwd`

	required:    false
	scopable:    true

**Description:**

Change the working directory to the specified location instead of the default
`<pathtmp>`.


## Keyword `disable`

	required:    false
	scopable:    true
	convert:     bool

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

**Description:**

Set to `true` to ignore this resource in the nodes context and consider it in the encapnodes context. The resource is thus handled by agents deployed in the service containers.


## Keyword `environment`

	required:    false
	scopable:    true
	convert:     shlex

**Example:**

	environment=CRT=cert1/server.crt PEM=cert1/server.pem

**Description:**

A whitespace-separated list of `<var>=<value>`.

A shell expression splitter is applied, so double quotes can be around
`<value>` only or whole `<var>=<value>`.


## Keyword `group`

	required:    false
	scopable:    true

**Description:**

If the binary is owned by the `root` user, run it as the specified group
instead of `root`.


## Keyword `limit_as`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the total virtual memory that can be in use by a process (unit bytes)
(same as limit_vmem).

When both `limit_vmem` and `limit_as` is used, the max value is chosen.


## Keyword `limit_core`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the largest core dump size that can be produced (unit byte).


## Keyword `limit_cpu`

	required:    false
	scopable:    true
	convert:     duration

**Example:**

	limit_cpu=30s

**Description:**

The limit on CPU time (duration).


## Keyword `limit_data`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the data segment size of a process (unit byte).


## Keyword `limit_fsize`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the largest file that can be created (unit byte).


## Keyword `limit_memlock`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on how much memory a process can lock with mlock(2) (unit byte, no solaris support).


## Keyword `limit_nofile`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the number files a process can have open at once.


## Keyword `limit_nproc`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the number of processes this user can have at one time, no solaris support.


## Keyword `limit_rss`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the total physical memory that can be in use by a process
(unit byte, no solaris support).


## Keyword `limit_stack`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the stack size of a process (unit bytes).


## Keyword `limit_vmem`

	required:    false
	scopable:    true
	convert:     size

**Description:**

The limit on the total virtual memory that can be in use by a process (unit bytes).


## Keyword `log`

	required:    false
	scopable:    true
	default:     true
	convert:     bool

**Description:**

Log the task outputs in the service log.


## Keyword `max_parallel`

	required:    false
	scopable:    true
	default:     1
	convert:     int

**Example:**

	max_parallel=2

**Description:**

Support limited, concurrent runs of tasks.

The task#xx.max_parallel=2 setting limits the number of concurrent task runs to 2.

The default value is 1, ensuring backward compatibility.

The run count is determined based on PID files created in the <resource var>/run/ directories.

The PID file is normally removed when the task execution ends, but if the executor dies abruptly (e.g., due to a SIGKILL), the stale PID file is not considered when computing the resource status. It is removed before the count check of the next run.

Staleness is evaluated using the condition: (PID file mtime < process birth time).

A new status log message may appear to indicate that the maximum concurrency limit has been reached.


## Keyword `monitor`

	required:    false
	scopable:    true
	convert:     bool

**Description:**

A resource with `monitor=true` will trigger the `monitor_action`
(crash or reboot the node, freezestop or switch the service) if:

* The resource is `down`.

* The instance has `local_expect=started` in its daemon monitor data, which
  means the daemon considers this instance is and should remain started.

* All restart tentatives failed.


## Keyword `on_error`

	required:    false
	scopable:    true

**Example:**

	on_error=/srv/{name}/data/scripts/task_on_error.sh

**Description:**

A command to execute on `run` action if `command` returned an error.


## Keyword `optional`

	required:    false
	scopable:    true
	convert:     bool

**Description:**

Action errors on optional resources are logged but do not interrupt the action sequence.

The status of optional resources is not included in the instance availability status but is considered in the overall status.

The status of task and sync resources is always included in the overall status, regardless of whether they are marked as optional.

Resources tagged as `noaction` are considered optional by default.

Dump filesystems are a typical use case for optional=true.


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


## Keyword `post_provision`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `provision` action.

Errors do not interrupt the action.

This trigger is only executed on leaders.


## Keyword `post_run`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute after the resource `run` action.

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


## Keyword `pre_run`

	required:    false
	scopable:    true
	rbac:        Triggers require the root grant.

**Description:**

A command or script to execute before the resource `run` action.

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

**Example:**

	provision_requires=ip#0 fs#0(down,stdby down)

**Description:**

A whitespace-separated list of conditions to meet to accept a 'provision'
action.

A condition is expressed as `<rid>(<state>,...)`.

If states are omitted, `up,stdby up` is used as the default expected states.


## Keyword `retcodes`

	required:    false
	scopable:    true
	default:     0:up 1:down

**Example:**

	retcodes=0:up 1:down 3:warn 4: n/a 5:undef

**Description:**

The whitespace-separated list of `<retcode>:<status name>`.

All undefined retcodes are mapped to the `warn` status.

Valid `<status names>` are:

* `up`
* `down`
* `warn`
* `n/a`
* `undef`


## Keyword `run_requires`

	required:    false
	scopable:    false

**Example:**

	run_requires=ip#0 fs#0(down,stdby down)

**Description:**

A whitespace-separated list of conditions to meet to accept a 'run'
action.

A condition is expressed as `<rid>(<state>,...)`.

If states are omitted, `up,stdby up` is used as the default expected states.


## Keyword `run_timeout`

	required:    false
	scopable:    true
	convert:     duration

**Example:**

	run_timeout=1m30s

**Description:**

Wait for `<duration>` before declaring the action a failure.

Takes precedence over `timeout`.


## Keyword `schedule`

	required:    false
	scopable:    true

**Example:**

	schedule=00:00-01:00 mon

**Description:**

Set the task `run` schedule.

See `usr/share/doc/opensvc/schedule` for the schedule syntax reference.


## Keyword `secrets_environment`

	required:    false
	scopable:    true
	convert:     shlex

**Example:**

	secrets_environment=CRT=cert1/server.pem sec1/*

**Description:**

A whitespace-separated list of `<var>=<sec name>/<key path>` or
`<sec name>/<key matcher>`.

If the `sec` or secret key doesn't exist then `start` and `stop` actions on
the resource will fail with a non 0 exit code.

A shell expression splitter is applied, so double quotes can be around
`<sec name>/<key path>` only or whole `<var>=<sec name>/<key path>`.

Example with,

* `<ns>/sec/cert1` a secret having a `server.pem` key with value `mycrt`.

* `<ns>/sec/sec1` a secret having a `key1` key with value `val1`.

`secrets_environment = CRT=cert1/server.pem sec1/*` creates the following
variables in the process execution environment:

	CRT=mycrt
	key1=val1



## Keyword `shared`

	required:    false
	scopable:    true
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

> **Warning**: If admins want to submit `--local` provision or unprovision
  commands themselves, they have to set the `--leader` flag correctly.

Flex objects usually don't use shared resources. But if they do, only
the flex primary gets `--leader` commands.

> **Warning**: All resources depending on a shared resource must also be
  flagged as shared.


## Keyword `snooze`

	required:    false
	scopable:    true
	convert:     duration

**Example:**

	snooze=10m

**Description:**

Snooze the service before running the task, so if the command is cause a
status degradation the user can decide to snooze alarms for the duration
set as value.


## Keyword `standby`

	required:    false
	scopable:    true
	convert:     bool

**Description:**

If `true`, always start the resource, even on non-started instances.

The daemon is responsible for starting standby resources.

A resource can be set standby on a subset of nodes using keyword scoping.

A typical use-case is a synchronized filesystem on non-shared disks. The
remote filesystem must be mounted to not overflow the underlying filesystem.

> **Warning**: In most situation, don't set shared resources standby, a
  non-clustered fs on shared disks for example.


## Keyword `stat_timeout`

	required:    false
	scopable:    true
	convert:     duration

**Description:**

The fs resources status evaluation includes a stat syscall test.
This keyword defines the maximum wait time for those stat calls to respond.

When expired, the resource status is degraded is to warn, which can trigger
a monitor action (reboot or crash the node) if the resource is monitored.


## Keyword `stop`

	required:    false
	scopable:    true

**Example:**

	stop=/usr/bin/rm -f /tmp/{fqdn}.{rindex}

**Description:**

The shlex expression of the command to execute to stop a running task.

Without it, the task is stopped by killing the processes its `command` started.


## Keyword `stop_timeout`

	required:    false
	scopable:    true
	convert:     duration

**Example:**

	stop_timeout=180

**Description:**

Wait for `<duration>` before declaring the app launcher `stop` action a
failure.

Takes precedence over `timeout`.

If neither `timeout` nor `stop_timeout` is set, the agent waits indefinitely
for the app launcher to return.

A timeout can be coupled with `optional=true` to not abort a service instance
stop when an app launcher did not return.


## Keyword `subset`

	required:    false
	scopable:    true

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

**Example:**

	timeout=5m

**Description:**

Wait for `<duration>` before declaring the task `run` action a failure.

If no timeout is set, the agent waits indefinitely for the task command to exit.


## Keyword `type`

	required:    false
	scopable:    false
	rbac:        Requires the root grant, except for the values oci, docker, podman.

**Description:**

The resource driver name.


## Keyword `umask`

	required:    false
	scopable:    true
	convert:     umask

**Example:**

	umask=022

**Description:**

The umask to set for the application process.


## Keyword `unprovision`

	required:    false
	scopable:    false
	default:     true
	convert:     bool

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

**Example:**

	unprovision_requires=ip#0 fs#0(down,stdby down)

**Description:**

A whitespace-separated list of conditions to meet to accept a 'unprovision'
action.

A condition is expressed as `<rid>(<state>,...)`.

If states are omitted, `up,stdby up` is used as the default expected states.


## Keyword `user`

	required:    false
	scopable:    true

**Description:**

If the binary is owned by the `root` user, run it as the specified user
instead of `root`.


