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

The processes of a resource live in its own leaf, inside its object, inside its
namespace. That nesting is what makes a limit set at any level apply to
everything below it.

## Capping an object

```ini
[DEFAULT]
pg_cpus = 0
pg_mem_limit = 256m
```

Starting it says what it applied:

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
| `pg_cpu_quota` | its cpu time whether or not the node is busy: `50%`, `50%@all`, `10%@2` |
| `pg_cpu_cores` | a guaranteed cpu time reservation, in ms per period |
| `pg_mem_limit` | resident memory, in bytes. Trespassing wakes the OOM killer |
| `pg_vmem_limit` | memory plus swap |
| `pg_mem_oom_control` | `0` lets the OOM killer run, `1` freezes the group instead |
| `pg_mem_swappiness` | how readily its pages are swapped |
| `pg_blkio_weight` | its share of block io, between `10` and `1000` |

`pg_cpu_shares` and `pg_cpu_quota` are the pair worth telling apart: shares only
arbitrate a contended cpu, a quota caps the group on an idle node too.

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

A `nscfg` object holds the defaults of its namespace, the `pg_*` keywords among
them:

```bash
om test/nscfg/namespace create --kw pg_mem_limit=4g
```

Every object in `test` is then capped by that, whoever created it, which is the
knob for handing a namespace to a team without handing them the node.

## Turning it off

```ini
[DEFAULT]
create_pg = false
```

Grouping is on by default. Turning it off leaves the processes ungrouped and
uncapped, and is worth doing only where the cgroup itself is the problem.

> ➡️ See Also
> * [Namespaces](apps.design.namespaces.md)
