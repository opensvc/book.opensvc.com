# Role-Based Access Control

A cluster reached over its API requires authentication, and every request is
checked against the privileges of the authenticated user.

Privileges live in the `grant` keyword of a `usr` object, as a
whitespace-separated list of grant expressions. A grant is a role, optionally
scoped to namespaces:

```ini
[DEFAULT]
grant = guest:prod* admin:test*
```

That user is a guest in every namespace whose name starts with `prod`, and an
admin in those starting with `test`.

A role given without a scope applies cluster-wide:

```ini
[DEFAULT]
grant = operator
```

## Namespace roles

These roles are the ones you scope to namespaces. Each inherits the previous.

### guest

Read-only. List objects, read their configuration, status, schedule, resource
info and logs.

### operator

Inherits `guest`, and may change the state of what already exists: start,
stop, restart, freeze, unfreeze, shutdown, switch, giveback, abort, run,
clear, refresh status and resource info.

An operator runs services. An operator does not create, delete or provision
them.

### admin

Inherits `operator`, and may change what exists: create and delete objects,
edit their configuration, provision and unprovision their resources, purge
them, and manage the keys of `cfg` and `sec` objects.

## Cluster roles

These roles are not namespace-scoped.

### root

All privileges. A user granted `root` can read and change the system's files
and run commands as the root system user, so it is the grant to give last and
audit first.

### squatter

May create namespaces. The creator is automatically granted `admin` on the
namespace it creates.

### prioritizer

May set object priority. Priority arbitrates between objects across namespace
boundaries, which is why it is a cluster role rather than something an admin
holds in its own namespace.

### blacklistadmin

Reserved for clearing the client blacklist. The role is accepted in a grant,
but no v3 endpoint requires it yet, so granting it currently confers nothing.

### heartbeat

May use the relay handlers. A relay heartbeat authenticates on a foreign
OpenSVC daemon with a user holding this role.

    om daemon relay status

### join, leave

May add a node to the cluster, or remove one from it, plus the reads a node
performs while joining. These back the token minted for a joining node:

    om daemon auth --role join

> ➡️ See Also
> * [Cluster API](configure.api.md)
> * [Cluster Configuration](configure.cluster.md) for the join procedure.
