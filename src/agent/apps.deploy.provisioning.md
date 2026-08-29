# Provisioning

Creating an object writes a configuration. It does not create anything the
configuration describes. Provisioning is the step that does: allocate the
disks, create the volume group and its logical volumes, format the
filesystems, plumb the ip address, pull the container image.

The reverse, unprovisioning, destroys them again. That distinction matters:
deleting an object removes its configuration, unprovisioning destroys its
data.

## Provisioners

A resource driver may implement a provisioner, and most of the drivers that
represent something allocatable do: the `disk`, `fs`, `ip`, `volume`,
`container`, `share` and `app` families.

A provisioner often needs keywords the resource does not need merely to run,
such as a size or a pool. Those are listed with the driver in the keyword
reference.

A provisioner may also write back into the configuration. Most ip provisioners
set the resource `ipname` once they know the address they obtained.

## Provisioning an object

```bash
om myapp provision
```

This is orchestrated. The daemon provisions the placement leader first and
leaves the instance `up`, so that later provisioners can rely on what the
earlier ones produced: a disk must stay attached for a filesystem provisioner
to format it. Once the leader is provisioned, the other instances are
provisioned in parallel and rolled back, leaving the object in its optimal
state.

`om myapp deploy` does the same in one step, creating the object and
provisioning it.

To act on the local instance only, without involving the daemon:

```bash
om myapp instance provision
```

The provisioners run in the resource start order.

## Shared resources

A SAN disk visible from several nodes, or the filesystem on it, must be
provisioned once, not once per node. Flag those resources:

```ini
[disk#1]
type = vg
name = datavg
shared = true
```

The provisioned state of a shared resource is synchronized across the object's
nodes. The state of a non-shared resource is node-affine, and each node
provisions its own.

The leader is the node that provisions shared resources. When driving this by
hand, that is what `--leader` selects:

```bash
om myapp instance provision --leader
```

## Resources you provisioned yourself

Resources that already existed when the object was created are reported as not
provisioned, which `om mon` marks with a `P`.

Starting such a resource successfully marks it provisioned: if it starts, it
is sane to consider it provisioned. When starting it is not possible or not
wanted, flag it without touching the system:

```bash
om myapp instance provision --state-only --rid disk#1
```

This only sets the flag. Nothing is formatted, allocated or created. The flag
matters because unprovision skips resources that were never provisioned, so an
unflagged resource would survive an unprovision it should not have.

## Unprovisioning

```bash
om myapp unprovision
```

This destroys the resources, and it is the dangerous half of the pair. Shared
resources are unprovisioned once, by the leader, in the reverse order.

> ➡️ See Also
> * [Create, Deploy](apps.deploy.create.md)
> * [Purge, Delete](apps.deploy.delete.md)
