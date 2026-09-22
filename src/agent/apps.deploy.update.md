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

The resource identifier must be specified.

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

This command does not stop the resource before removing its definition. If desired, this can be done with

```
om <path> stop --rid fs#2
```

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
