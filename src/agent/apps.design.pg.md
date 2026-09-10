# Resource Capping

A misbehaving application should not be able to take a node down with it. The
agent puts every object it starts in its own cgroup, and the `pg_*` keywords
turn that into a limit.

## The slice an object runs in

Starting an instance builds a hierarchy under `opensvc.slice`, one level per
scope:

    opensvc.slice
    └ opensvc-ns.<namespace>.slice
      └ opensvc-ns.<namespace>-svc.<name>.slice
        └ opensvc-ns.<namespace>-svc.<name>-app.1.slice

A resource's processes live in its own leaf, inside its object, inside its
namespace. That nesting is what makes a limit set at any level apply to
everything below it.

## Capping an object

```ini
[DEFAULT]
pg_cpus = 0
pg_mem_limit = 256m
```

Starting the instance logs what it applied:

    INF myapp: applied pg /opensvc.slice/...-svc.myapp.slice: cpus=0 mem_limit=256m
    INF myapp: app#1: run: om exec --pg /opensvc.slice/...-svc.myapp-app.1.slice -- ...

And the kernel agrees:

```bash
$ cat /sys/fs/cgroup/opensvc.slice/.../opensvc-svc.myapp.slice/memory.max
268435456
$ cat /sys/fs/cgroup/opensvc.slice/.../opensvc-svc.myapp.slice/cpuset.cpus
0
```

The keywords are the usual cgroup controls:

| Keyword | Caps |
| :--- | :--- |
| `pg_cpus` | the cpus the object may run on, as a list or range: `0,1,2` or `0-2` |
| `pg_mems` | the memory nodes it may allocate from, same syntax |
| `pg_cpu_shares` | its share of cpu **when the node is cpu-bound**, relative to other objects |
| `pg_cpu_quota` | its cpu time whether or not the node is busy: `50%` is half of one cpu, `50%@all` half of every cpu the node has, `10%@2` a tenth of two |
| `pg_mem_limit` | resident memory, in bytes. Exceeding it wakes the OOM killer |
| `pg_vmem_limit` | memory plus swap |
| `pg_mem_oom_control` | `0` lets the OOM killer run, `1` freezes the group instead. v1 hierarchy only |
| `pg_mem_swappiness` | how readily its pages are swapped. v1 hierarchy only |
| `pg_blkio_weight` | its share of block io, between `10` and `1000` |

`pg_cpu_shares` and `pg_cpu_quota` are the pair worth telling apart: shares only
arbitrate a contended cpu, whereas a quota caps the group on an idle node too.

The two marked *v1 hierarchy only* cap nothing on a node running the unified
hierarchy, which has neither `memory.swappiness` nor `memory.oom_control`.
Setting one there is warned about, and ignored.

## Capping a resource

The same keywords set on a resource cap that resource alone, which is how a
sidecar is kept from starving the process it assists:

```ini
[app#1]
type = simple
start = /opt/myapp/bin/server

[app#2]
type = simple
start = /opt/myapp/bin/indexer
pg_cpu_shares = 128
```

## Capping a namespace

An `nscfg` object holds the defaults of its namespace, the `pg_*` keywords among
them:

```bash
om test/nscfg/namespace create --kw pg_mem_limit=4g
```

Every object in `test` is then capped by it, no matter who created it, which is
how a namespace is handed to a team without handing them the node.

## Lifting a capping

Removing a `pg_*` keyword does not lift what it capped. What was written stays
written, because the agent has no way of telling a capping it wrote from one
systemd or an operator wrote, and silently undoing the second would be worse
than leaving the first.

So lifting a capping is asked for, and there are two ways of asking.

The keyword set to `default` puts that one capping back where a node that never
capped anything leaves it:

```ini
[DEFAULT]
pg_cpu_quota = default
```

This is the one to reach for. It is the configuration, so every node converges
to it: a peer taking the object over, or a node provisioned tomorrow, lifts the
capping too.

The command lifts every capping of an instance at once, whatever the keywords
say:

```bash
om test/svc/myapp instance pg reset
```

That one is for a capping the configuration knows nothing about — left by an
older agent, by systemd, or by hand. It is not a lasting decision: a capping
the keywords do name comes back at the next `pg update`, and at the next start.

## Turning it off

```ini
[DEFAULT]
create_pg = false
```

Grouping is on by default. Turning it off leaves the processes ungrouped and
uncapped, and is worth doing only where the cgroup itself causes the problem.

> ➡️ See Also
> * [Namespaces](apps.design.namespaces.md)
