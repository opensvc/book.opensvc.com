<!-- llms: How to change the configuration of an object: adding, modifying and deleting resources, interactively or not, batching, and waiting for propagation. -->
# Update

Configuration files are stored in `/etc/opensvc/`.


* `/etc/opensvc/<name>.conf`

    Root objects configuration file:

* `/etc/opensvc/namespaces/<namespace>/<kind>/<name>.conf`

    Namespaced objects configuration file:

Do not edit these files directly. Use one of the following method instead.

> The **API** tabs assume the `$TOKEN` and the listener endpoint set up in
> [Cluster API](configure.api.md). `PATCH …/config` takes the same `set`,
> `unset` and `delete` operations as `om <path> config update`, and commits
> them as one transaction.

## Interactive

```
om <path> config edit
```

The configuration file syntax is checked upon editor exit. The new configuration is installed if the syntax is found correct, or saved in a temporary location if not. Two options are then possible:

* Discard the erroneous configuration:

    ```
    om <path> config edit --discard
    ```

* Re-edit the erroneous configuration:

    ```
    om <path> config edit --recover
    ```

The api has no interactive counterpart, the editor being the client's. Fetch
the configuration file, edit it, and write it back:

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config/file" > <name>.conf
$EDITOR <name>.conf
curl -s -X PUT -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" --data-binary @<name>.conf \
  "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config/file"
```

The write is refused if the configuration it carries does not validate, so a
typo is caught the same way the editor check catches it.

## Non-Interactive Resource Addition

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> config update --set fs#2.type=ext4 --set fs#2.mnt=/srv/{fqdn}
```

</div>
<div class="tab" data-title="API">

```
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'set=fs#2.type=ext4' \
  --data-urlencode 'set=fs#2.mnt=/srv/{fqdn}' \
  -G "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config"
```

</div>
</div>

The resource identifier (rid) must not be specified. The resource type must be specified (rtype). A free rid will be allocated.

## Non-Interactive Resource Modification

```
om <path> config update --set fs#2.type=ext4 --set fs#2.mnt=/srv/{fqdn}
```

The resource identifier must be specified. A change of what a resource holds
on a node, as this mount point, is refused while the resource is up: see
[Changes Refused While a Resource Is Up](#changes-refused-while-a-resource-is-up).

## Non-Interactive Resource Deletion

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> config update --delete fs#2
```

</div>
<div class="tab" data-title="API">

```
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'delete=fs#2' \
  -G "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config"
```

</div>
</div>

The section of a resource up on a node is not removed: its resource is
stopped first, as nothing would stop it once its section is gone.

```
om <path> stop --rid fs#2
```

## Changes Refused While a Resource Is Up

Some keywords say what a resource holds on a node once started: the `mnt` and
`dev` of a fs, the address, `dev`, `netns` and `network` of an ip, the `name`
of a volume group or a container, ... The stop of a resource acts on the
configuration it reads then, so a change of one of them while the resource is
up would have the stop umount the new mount point, and leave the former one
mounted. Such a change is refused, for every user, root included, while the
resource is up on a node, and so are a change of the `type` of the resource,
and the removal of its section:

```
$ om <path> config update --set fs#1.mnt=/srv/new
Error: <path>: [403] Forbidden: denied: the resource is up: change fs#1.mnt from "/srv/old" to "/srv/new": up on node1: stop it before
```

A keyword concerned says so in its documentation, `om <path> config doc
--kw fs#1.mnt`:

```
stop first:  a change is refused while the resource is up
```

The change is judged on the value evaluated on each node the resource is up
on, so a change of a reference the value holds, as `mnt = /srv/{env.dir}`
with `env.dir` changed, is refused too. A resource is up on a node unless its
status there is `down`, `stdby down` or `n/a`. Stop the resource, change the
keyword, and start it again:

```
om <path> stop --rid fs#1
om <path> config update --set fs#1.mnt=/srv/new
om <path> start --rid fs#1
```

Root writes the change all the same with `force`, as to recover from a
resource that cannot be stopped. What the former value set up stays on the
node, for root to undo:

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> config update --set fs#1.mnt=/srv/new --force
```

</div>
<div class="tab" data-title="API">

```
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'set=fs#1.mnt=/srv/new' \
  --data-urlencode 'force=true' \
  -G "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config"
```

</div>
</div>

`om <path> config edit --force`, and the `force` parameter of
`PUT …/config/file`, do the same for an edited configuration.

## Batching

`om <path> config update` applies all its `--delete`, `--unset` and `--set` arguments as a single transaction: the batch is staged, validated, and committed once.

Scripts should prefer one command carrying many changes:

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> config update \
	--set app#1.type=forking \
	--set app#1.start=/srv/app/bin/start \
	--set app#1.check=/srv/app/bin/check
```

</div>
<div class="tab" data-title="API">

```
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'set=app#1.type=forking' \
  --data-urlencode 'set=app#1.start=/srv/app/bin/start' \
  --data-urlencode 'set=app#1.check=/srv/app/bin/check' \
  -G "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config"
```

</div>
</div>

Splitting this into one command per keyword commits three times. Each commit rewrites the configuration file, and every node in the object scope then fetches the whole file. Worse, each intermediate state is a state the peers and the orchestrator see and act upon, including the states where the resource definition is still incomplete.

Scripts driving the daemon API have the same choice: the `PATCH /api/object/path/{namespace}/{kind}/{name}/config` handler accepts repeated `set`, `unset` and `delete` parameters, and commits them as one transaction.

## Waiting for the Configuration to Propagate

A configuration update is acknowledged by the node that committed it, and
reaches the other nodes of the object a moment later, each fetching the new
file. A script going on to act on the instances, restarting them to apply
a change for example, can wait for that moment instead of racing it:

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> config update --set env.foo=bar --wait [--time 30s]
```

</div>
<div class="tab" data-title="API">

```
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  --data-urlencode 'set=env.foo=bar' \
  --data-urlencode 'wait=30s' \
  -G "https://<node>:1215/api/object/path/<ns>/<kind>/<name>/config"
```

</div>
</div>

The answer is held until every live node of the object holds the new
configuration, which usually takes well under a second:

* The nodes waited for are the ones of the configuration written, so a node
  the update adds to `nodes` is waited for too.
* A node is live while the heartbeats reach it. A node that is down is not
  waited for: it fetches the configuration when it comes back.

A wait that expires, after `--time` (5 minutes by default) or the `wait`
duration, ends with an error, and the api answers `408`, naming the nodes the
configuration has not reached yet. The configuration is committed all the
same. Do not answer a `408` by updating again: a `+=` operation would be
applied twice.

The answer carries the `OM-Last-Modified` timestamp of the configuration
written, which an action asked of an instance can require with its
`config_updated_at` parameter, to refuse running on an older configuration.
