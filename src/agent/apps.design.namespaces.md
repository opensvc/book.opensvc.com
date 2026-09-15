# Namespaces

Namespaces allow users to create objects with the same name in different naming spaces.

The `<namespace>/<kind>/<name>` notation is called a path.

The object selector (`--service` option for `svcmgr` and `svcmon`, first argument for `om`) accepts the path notation.

Namespaced objects have their config stored in `/etc/opensvc/namespaces/<namespace>/<kind>/`.

This feature is available since version 1.9-2748.

## Operations with namespaces

### The object path

The namespace is part of the path, so naming the object names its namespace.
This is the way to create an object in a namespace, and it works for every
command:

```sh
om test/svc/svc1 create
om test/svc/svc1 start
om 'test/**' ls
```

### OSVC_NAMESPACE environment variable

`OSVC_NAMESPACE` narrows which objects a command sees, so a selector that would
match the whole cluster is confined to one namespace:

```sh
$ export OSVC_NAMESPACE=test
$ om '**' ls
test/svc/svc1
test/svc/svc2
```

```sh
$ unset OSVC_NAMESPACE
$ om '**' ls
svc0
test/svc/svc1
test/svc/svc2
```

It selects among the objects that exist. It does not decide where a new one is
created: with `OSVC_NAMESPACE=test` exported, `om svc1 create` still creates
`svc1` in the root namespace, because the path it was given says root. Name the
namespace in the path instead.

### Cloning into a namespace

When creating an object from another one, `--namespace` overrides the
destination namespace, which saves rewriting the path:

```sh
om svc2 create --config=svc1 --namespace=test
```

This creates `test/svc/svc2` from the configuration of `svc1`.

A configuration that refers to other objects survives the clone only if those
references are relative. See [Relative object paths](#relative-object-paths).

## Claims on cluster resources

The objects of a namespace consume things the cluster owns and its peers share:
the space of a pool, the addresses of a network. A namespace can be capped on
what it takes of one, so that it cannot drain a resource the others are meant
to share. A cap is declared in the namespace configuration, as a `claim`
section naming the kind of resource, the resource, and the limit:

```ini
[claim#1]
type = pool
name = tank
limit = 250m

[claim#2]
type = network
name = backend2
limit = 10
```

Edit it like any other object configuration, naming the namespace with a
trailing `/`:

```sh
om test/ config update --set claim#1.type=pool --set claim#1.name=tank --set claim#1.limit=250m
om / config show
```

A namespace declaring no claim on a resource is not capped on it. A claim
naming no limit says the namespace uses the resource, not that it is capped on
it.

### Pool claims

A pool claim counts the size each volume of the namespace was created or
resized with, cluster-wide. An allocation or a resize taking the namespace over
its limit is refused, and the pool is reported as one that does not match, with
the reason:

```
$ om test/svc/app provision
... no pool matching criteria: [tank] the test namespace may claim 250mi of it
and already claims 200mi, so it cannot claim 100mi more
```

It counts what was asked for, not what is written: a pool hands out what it
promised, and that promise is what is being rationed. So a namespace can be at
its limit on a pool that is nearly empty, and a pool can be full while every
namespace is under its limit.

### Network claims

A network claim counts the addresses the namespace holds in the network,
cluster-wide. An allocation taking the namespace over its limit is refused:

```
$ om test/svc/app start
... ip#1: start: network backend2: the test namespace may hold 10 address(es)
of it and already holds 10
```

Addresses are counted, not reservations: a failover object holds the same
address on every node it is configured on, and that is one address taken from
the network, while the instances of a flex each hold one of their own.

The limit is checked when an address is allocated, not when one already held is
asked for again, so a namespace that reached its limit still restarts what it
already runs. Lowering a limit below what a namespace already holds is
therefore allowed, and takes effect on the next allocation rather than by
taking addresses back.

### Where the limit is read

The limit is read from the namespace configuration on the node doing the
allocation, never over the api. A namespace configuration is present on every
cluster node, and most namespaces claim nothing, so the common case asks
nothing of the daemon. Only a namespace that is actually capped needs the
cluster-wide count of what it already holds, and failing to reach the daemon
for that count leaves the claim unchecked rather than refused: a cap is
something the cluster brokers, and where no daemon answers there is nothing
brokering.

## References

A `{namespace}` reference is available in service configuration.

## Cgroups

Services in an explicit namespace have the namespace name inserted in their cgroup path:
```
opensvc.slice/<namespace>.slice/<name>.slice
```

## The "root" pseudo namespace

Services created before namespace support, and services created without an explicit namespace, are assigned to a pseudo namespace named `root`. Their configs are stored in `/etc/opensvc/`.

The root pseudo namespace name is used in cluster DNS names (`<name>.root.svc.<clustername>`) and DNS search paths, but is not embedded in Docker container names or cgroup paths.

The `{namespace}` reference evaluates to `root`.

### Select objects in the root namespace
```sh
$ om 'root/**' ls
$ OSVC_NAMESPACE=root om '**' ls
```

### Create objects in the root namespace
```sh
$ unset OSVC_NAMESPACE
$ om svc1 create
```

## Relative object paths

An object referring to another one can name it with a path relative to its own
namespace, by replacing the namespace with a `.`:

```ini
[DEFAULT]
parents = ./svc/db

[fs#1]
install = /etc/app.conf from ./cfg/app key app.conf
```

`./svc/db` reads as "the `db` service, in whatever namespace I am in". For
`test/svc/app` it resolves to `test/svc/db`, and for `prod/svc/app` to
`prod/svc/db`, with no change to the configuration.

That is the point of the notation: a set of objects designed together can be
cloned from a development namespace to a production one, and keeps referring to
its own members rather than reaching back into the namespace it came from. A
fully qualified `test/svc/db` would follow the clone and still point at `test`.

Node configuration is not namespaced, so the same notation in `node.conf`
resolves in the `system` namespace: `./sec/relays` is `system/sec/relays`.

## Relations

Children and parents relations use object paths or object names.

- If a name is declared in the parents, slaves, or children lists, the related objects are searched in the same namespace. `svc2` and `./svc/svc2` are the same relation, the second stating it explicitly.
- A relation to an object in another namespace must be declared using its path instead of its name.
- Relations to objects in the root pseudo namespace must be defined as `root/<kind>/<name>` to avoid ambiguity.
