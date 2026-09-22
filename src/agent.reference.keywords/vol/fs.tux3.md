# Driver `fs.tux3`

**Minimal configlet:**

	[fs#1]
	type = tux3
	mnt = /srv/{fqdn}

**Minimal setup command:**

	om test/vol/foo set \
		--kw="type=tux3" \
		--kw="mnt=/srv/{fqdn}"

**Supported keywords:**

- blocking_post_provision
- blocking_post_start
- blocking_post_stop
- blocking_post_unprovision
- blocking_pre_provision
- blocking_pre_start
- blocking_pre_stop
- blocking_pre_unprovision
- check_read
- comment
- configs
- dev
- directories
- dirperm
- disable
- encap
- group
- install
- mkfs_opt
- mnt
- mnt_opt
- monitor
- no_preempt_abort
- optional
- perm
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
- prkey
- promote_rw
- provision
- provision_requires
- restart
- restart_delay
- scsireserv
- secrets
- shared
- signal
- standby
- start_requires
- stat_timeout
- stop_requires
- subset
- tags
- type
- unprovision
- unprovision_requires
- user
- zone

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


## Keyword `check_read`

	required:    false
	scopable:    true
	default:     false
	convert:     bool
	rbac:        A resource of a volume requires the root grant.

**Description:**

Activate file system read check during status evaluation when the
file system is mounted but file system write check is disabled.

This can help detection of nfs stale file systems.
It is ignored when mnt_opt contains 'nointr'.
The file system read check is: 'timeout {stat_timeout} stat -f {mnt}'
The file system write check is disabled when fs_type is a network file system or
when mnt_opt contains 'ro'.


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


## Keyword `configs`

	required:    false
	scopable:    true
	convert:     shlex
	rbac:        A resource of a volume requires the root grant.

**Example:**

	configs=conf/mycnf:/etc/mysql/my.cnf:ro conf/sysctl:/etc/sysctl.d/01-db.conf

**Description:**

The whitespace-separated list of
`<config name>/<key>:<volume relative path>:<options>`.


## Keyword `dev`

	required:    false
	scopable:    true
	default:     none
	rbac:        A resource of a volume requires the root grant.

**Example:**

	dev=/dev/disk/by-id/nvme-eui.002538ba11b75ec8

**Description:**

The block device file or filesystem image file hosting the filesystem to mount.

A different device can be set up on different nodes using the `dev@<nodename>`
scoping syntax.


## Keyword `directories`

	required:    false
	scopable:    true
	convert:     list
	rbac:        A resource of a volume requires the root grant.

**Example:**

	directories=a/b/c d /e

**Description:**

The whitespace-separated list of directories to create in the `vol` head.


## Keyword `dirperm`

	required:    false
	scopable:    true
	convert:     filemode
	rbac:        A resource of a volume requires the root grant.

**Default:**

The value of `perm` with the execute bit added to each class (user,
group, other) that has the read bit set. For example, `perm = 0640`
implies `dirperm = 0750`: user gets `x` because user has `r`, group
gets `x` because group has `r`, other gets neither because other has
no `r`.

If `perm` is also not set,
* the permission of the head directory of the receiver is unchecked
* the permission of other directories defaults to 0755
* the permission of files from sec objects defaults to 0600
* the permission of other files defaults to 0644

**Example:**

	dirperm=750

**Description:**

The permissions to apply to installed directories, in octal notation.


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


## Keyword `group`

	required:    false
	scopable:    true
	rbac:        A resource of a volume requires the root grant.

**Example:**

	group=1001

**Description:**

The group name or id that will own the volume root and installed files and
directories.


## Keyword `install`

	required:    false
	scopable:    true
	convert:     shlex
	rbac:        A resource of a volume requires the root grant.

**Example:**

	install=
		/etc/ mode 0750 user 1000 group 1000
		/etc/ssl/ mode 0700 user 1000 group 1000
		/etc/ from test/cfg/haproxy key haproxy.cfg mode 0640 user 1000 group 1000 signal HUP:container#haproxy
		/etc/ssl/front.pem from ./sec/d key fullpem mode 0640 user 1000 group 1001 required
		/etc/ssl/front.chain from ./sec/d key certificate_chain required
		/etc/profile.d/ from ./sec/d key etc/profile.d/*
		/init/nfs from ./cfg/{name} key init/nfs mode 0755 source https://raw.githubusercontent.com/opensvc/opensvc_templates/refs/heads/main/nfs/script
		/init/backup from ./cfg/{name} key init/backup mode 0755 source /tmp/scripts/backup.sh
		/init/config.sh from ./cfg/{name} key init/config.sh mode 0755 source https://example.com/templates/config.sh template
		/data/

**Description:**

A list of files and directories to install in the volume from cfg and sec keys.

	<path> from <obj_path|obj_relpath> [key <key>] [mode <mode>] [user <user>] [group <group>] [signal <sig>:<rid>] [source <uri>] [template] [required]
	<path> [mode <mode>] [user <user>] [group <group>] [signal <sig>:<rid>]

Where:

* `<path>` (e.g. `/init/installed`, `/init/`)
  * must start with a `/`.
  * is relative to the target resource head.
  * is considered a directory if it ends with a `/` or if `from <obj_path|obj_relpath>` is omitted.
  * content is copied from the value of the key referenced by `from <obj_path|obj_relpath>`.
  * if `key <key>` is not specified, the key name defaults to the `<path>` with the leading `/` stripped.
    e.g. `fs#1.install = /a/b from ./sec/sec1` will install `<fs#1 head>/a/b` from the `./sec/sec1` key named `a/b`.

* `<obj_path>` (e.g. `ns1/sec/d`)
  * is the absolute path of the datastore to install keys from. Note that if the datastore and
    the installing object namespaces are different, the datastore must explicitely share its keys with
    the installing object.

* `<obj_relpath>` (e.g. `./sec/d`)
  * is the path of the datastore to install keys from, relative to the installing object namespace.

* `key <key>`
  * `<key>` is the key name or a globbing pattern from <obj_path|obj_relpath>.
  * if not specified, defaults to the `<path>` with the leading `/` stripped.
    e.g. `fs#1.install = /a/b from ./sec/sec1` will install `<fs#1 head>/a/b` from the `./sec/sec1` key named `a/b`.

* `<mode>`, `<user>`, `<group>` default values are defined by the `mode`, `user` and `group` resource keyword.

* `<sig>:<rid>` (e.g. `HUP:container#haproxy`)
  * `<sig>` is the signal to send to the target resource `<rid>` processes when the file content is modified.

* `<uri>`
  * is the source URI or local file path to seed the datastore key with during provision if the key doesn't already exist.
  * HTTP/HTTPS URIs (http://, https://) are fetched via HTTP GET.
  * Local file paths are read directly from the filesystem.

* `required`
  * stop installing items if this item install failed.

* `source <uri>`
  * seed the datastore key with the content of <uri>.
  * if `template` is also set, treat the <uri> content as a go template, and execute using the [env] section keys as the dataset.
    e.g. {{.foo}} is replaced by the evaluated value of `env.foo`.


## Keyword `mkfs_opt`

	required:    false
	scopable:    true
	convert:     shlex
	rbac:        A resource of a volume requires the root grant.

**Description:**

Options to pass to the `mkfs` command called by the `provision` action.


## Keyword `mnt`

	required:    true
	scopable:    true
	rbac:        A resource of a volume requires the root grant.

**Example:**

	mnt=/srv/{fqdn}

**Description:**

The mount point where to mount the filesystem.


## Keyword `mnt_opt`

	required:    false
	scopable:    true
	rbac:        A resource of a volume requires the root grant.

**Description:**

The mount options, as they would be defined in the fstab.


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


## Keyword `no_preempt_abort`

	required:    false
	scopable:    true
	convert:     bool

**Description:**

If `true`, the agent will preempt the scsi3 persistent reservation with a `preempt`
command instead of a `preempt and and abort`.

Some scsi target implementations do not support `preempt and and abort` (esx).


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


## Keyword `perm`

	required:    false
	scopable:    true
	convert:     filemode
	rbac:        A resource of a volume requires the root grant.

**Default:**

If `perm` is not set,
* the permission of files from sec objects defaults to 0600
* the permission of other files defaults to 0644

**Example:**

	perm=660

**Description:**

The permissions to apply to installed files, in octal notation.

Also used to compute a default value for `dirperm`.


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


## Keyword `prkey`

	required:    false
	scopable:    true
	default:     {node.node.prkey}

**Description:**

A specific scsi3 persistent reservation key for the resource.

It overrides the object-level `prkey` and the node-level `prkey`.


## Keyword `promote_rw`

	required:    false
	scopable:    false
	convert:     bool
	rbac:        A resource of a volume requires the root grant.

**Description:**

If `true`, OpenSVC will try to promote the base devices to read-write on
`start` actions.


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


## Keyword `restart`

	required:    false
	scopable:    true
	default:     0
	convert:     int

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

**Description:**

The minimum delay between two restart tentatives on the resource.


## Keyword `scsireserv`

	required:    false
	scopable:    false
	convert:     bool

**Description:**

If `true`, try to acquire a type-5 (write exclusive, registrant only) scsi3
persistent reservation on every path to every disk used by this resource.

Existing reservations are preempted to not block service failover.

If the `start` was not legitimate the data are still protected from being
written concurrently from all nodes.


## Keyword `secrets`

	required:    false
	scopable:    true
	convert:     shlex
	rbac:        A resource of a volume requires the root grant.

**Example:**

	secrets=cert/pem:server.pem cert/key:server.key

**Description:**

The whitespace-separated list of
`<secret name>/<key>:<volume relative path>:<options>`.


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


## Keyword `signal`

	required:    false
	scopable:    true
	rbac:        A resource of a volume requires the root grant.

**Example:**

	signal=hup:container#1

**Description:**

A `<signal>:<target>` whitespace-separated list, where `<signal>` is a signal
name or number (ex. `1`, `hup` or `sighup`), and target is the comma-separated
list of resource ids to send the signal to (ex: `container#1,container#2`).

If only the signal is specified, all candidate resources will be signaled.

This keyword is typically used to reload daemons on certificate or configuration
files changes.


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


## Keyword `start_requires`

	required:    false
	scopable:    false

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
	default:     5s
	convert:     duration

**Description:**

The fs resources status evaluation includes a stat syscall test.
This keyword defines the maximum wait time for those stat calls to respond.

When expired, the resource status is degraded is to warn, which can trigger
a monitor action (reboot or crash the node) if the resource is monitored.


## Keyword `stop_requires`

	required:    false
	scopable:    false

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


## Keyword `type`

	required:    false
	scopable:    false
	rbac:        A resource of a volume requires the root grant.

**Description:**

The resource driver name.


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
	rbac:        A resource of a volume requires the root grant.

**Example:**

	user=1001

**Description:**

The user name or id that will own the volume root and installed files and
directories.


## Keyword `zone`

	required:    false
	scopable:    true
	rbac:        A resource of a volume requires the root grant.

**Description:**

The zone name the fs refers to.

If set, the fs mount point is reparented into the zonepath rootfs.


