<!-- llms: How to create an object: from scratch, from another object, or from a manifest, and what a clone resets. -->
# Create, Deploy

The following actions only modify files in `/etc/opensvc`. No operating system configuration file is modified, so they are safe to experiment with.

The agent support object creation via two commands:

* ``create``
  The object is created but not provisioned nor started.

* ``deploy``
  The object is created, provisioned and started.

Both actions support the same arguments. The following examples use only create commands.

> The **API** tabs assume the `$TOKEN` and the listener endpoint set up in
> [Cluster API](configure.api.md). Creating an object through the api is
> posting its configuration file: `POST …/config/file` creates the object,
> `PUT …/config/file` replaces the configuration of an object that already
> exists, and both answer the `OM-Last-Modified` timestamp the written
> configuration now carries.

## From Scratch, non Interactive

Create a new object with minimal configuration. No resources are described.

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> create
```

</div>
<div class="tab" data-title="API">

```
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" \
  --data-binary '[DEFAULT]' \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config/file"
```

</div>
</div>

Resources and default keywords can be set right from the create command, using ``--kw <keyword>=<value>`` options

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> create \
	--kw container#0.type=oci \
	--kw orchestrate=ha \
	--kw nodes={clusternodes}
```

</div>
<div class="tab" data-title="API">

```
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" \
  --data-binary $'[DEFAULT]\norchestrate = ha\nnodes = {clusternodes}\n\n[container#0]\ntype = oci\n' \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config/file"
```

</div>
</div>

Scripts should describe the object as completely as possible in this single command. The keywords given to ``create`` are part of the first and only commit, so the object is never announced to the cluster in a half-configured state. Creating a bare object then completing it with a series of ``config update`` commands publishes every intermediate state to the peers, and the orchestrator acts on them as soon as ``orchestrate`` is set.

The api has the same property: one `POST …/config/file` carrying the whole
configuration is one commit, where a bare create followed by `PATCH …/config`
calls is several.

## From Another Object

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <dst path> create --config=<src path>
```

</div>
<div class="tab" data-title="API">

```
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<src name>/config/file" |
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" --data-binary @- \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<dst name>/config/file"
```

</div>
</div>

> The api resets the recorded keywords described below, whoever sends the
> configuration: `om`, `ox` and a client of the api alone get the same clone.
> Keyword changes passed as `set` parameters apply after the reset, so a
> recorded keyword they name is kept:
>
> ```
> curl ... -X POST "https://<node>:1215/api/object/path/<ns>/<kind>/<dst name>/config/file?set=ip%231.addr=10.0.0.6"
> ```

## From Manifest

The manifest must be ini formatted, like the output of ``om <path> config show``.

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> create --config=<manifest uri>
```

</div>
<div class="tab" data-title="API">

```
curl -s <manifest uri> |
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" --data-binary @- \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config/file"
```

</div>
</div>

This method can also be used to clone objects

```
om <dst path> create --config=<src path>
```

or

```
om <src path> config show | om <dst path> create --config=-
```

## What a Clone Resets

A clone is another object, so what the source recorded of itself does not come
with it. Those keywords are marked in the keyword reference:

```
recorded:    written when what it names is made, and reset when the object is cloned
```

The object id is one of them, and the clone is given a new one. The uuid of an
md array is another: it is written when the array is created, and is what
assembles that array again afterwards, so a clone keeping it would assemble
the source's array rather than create one of its own. So are the `disk_id` of
a disk a pool created, which a clone keeping would take the source's disk
rather than have one created, and the address an ip drew from a network.

They are written again, for the clone, when the clone makes what they name.

`--restore` keeps them, which is what restoring a saved configuration means:
the object being created is the one the configuration was saved from, not
another like it.

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> create --config=<backup> --restore
```

</div>
<div class="tab" data-title="API">

```
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" --data-binary @<backup> \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config/file?restore=true"
```

</div>
</div>

A restored object takes over what it finds on the nodes when it is
provisioned, as replicated storage: `--restore` implies the `--adopt` of
[Provisioning](apps.deploy.provisioning.md#what-a-provision-checks-first).

## Conflicts with Other Objects

A configuration copied from another object, or restored from another cluster,
can name what an object of this cluster holds already: the mount point of a
filesystem, the device a volume group is made of, an address. Provisioning it
would take it from that object. The configuration is refused when it is
written, before anything is provisioned:

```
$ om ns1/svc/web2 create --config=ns1/svc/web
Error: ns1/svc/web2: fs#1: mount point /srv/web on node1, node2 is held by ns1/svc/web fs#1
```

What a resource holds, its holds, are the values its configuration names, as
evaluated on each node of the object:

* a resource `shared = false` holds each value on the nodes it evaluates to
  it on: `name@node1 = a` and `name@node2 = a` hold `a` on `node1` and `node2`;
* a resource `shared = true` holds every value it evaluates to on every node
  of the cluster.

Two objects conflict when they hold the same value of the same kind, a mount
point, a block device, a volume group, a container name, an ip address, on a
node. A device path meets the volume that exposes it: `dev = /dev/datavg/web`
meets the logical volume `datavg/web` another object holds.

A value referencing what a resource exposes once provisioned, as
`dev = {disk#1.exposed_devs[0]}`, is held by the resource it comes from, whose
own values are checked. Once up, the resources also say the devices they were
found holding, so a device no configuration names is checked too.

The check judges what a write adds: an update giving a resource a value
another object holds is refused too, and a cluster holding conflicting objects
already does not refuse their unrelated changes. Most values made of the
object name, as `{name}`, `{fqdn}`, a container named after the object, an
address drawn from a network, never conflict, which makes them the ones to
use in a configuration meant to be cloned.

### Recreating an object under another name, or taking over from another

A disabled object holds nothing, its resources being never started: the
holds of an object stopped and disabled are free for another to take. That
is the way to restore an object under another name, or in place of an object
receiving its replicated data:

```
om <src path> stop --wait
om <src path> disable
om <dst path> create --config=<saved config of src> --restore
om <dst path> provision --wait
```

The object is disabled on every node a moment after the command: the check of
the create reads what each node published, and refuses until they say the
object is disabled.

A resource up is not disabled, as it would be left running with nothing to
stop it, and what it holds held with no configuration saying so:

```
$ om <src path> disable
Error: <src path>: [403] Forbidden: the resource is up: disable fs#1: up on node1: stop it before
```

And enabling the object again is refused while another holds what it would
hold again: the original does not come back on top of the object made in its
place.

Root writes the configuration all the same with `force`:

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <dst path> create --config=<src path> --force
```

</div>
<div class="tab" data-title="API">

```
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" --data-binary @<config> \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<dst name>/config/file?force=true"
```

</div>
</div>

> ➡️ See Also
> * [Provisioning](apps.deploy.provisioning.md)
> * [Batching configuration changes](apps.deploy.update.md#batching)
