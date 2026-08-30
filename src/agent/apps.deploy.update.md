# Update

Configuration files are stored in `/etc/opensvc/`.


* `/etc/opensvc/<name>.conf`

    Root objects configuration file:

* `/etc/opensvc/namespaces/<namespace>/<kind>/<name>.conf`

    Namespaced objects configuration file:

Do not edit these files directly. Use one of the following method instead.

## Interactive

	om <path> config edit

The configuration file syntax is checked upon editor exit. The new configuration is installed if the syntax is found correct, or saved in a temporary location if not. Two options are then possible:

* Discard the erroneous configuration:

		om <path> config edit --discard

* Re-edit the erroneous configuration:

		om <path> config edit --recover


## Non-Interactive Resource Addition

	om <path> config update --set fs#2.type=ext4 --set fs#2.mnt=/srv/{fqdn}

The resource identifier (rid) must not be specified. The resource type must be specified (rtype). A free rid will be allocated.

## Non-Interactive Resource Modification

	om <path> config update --set fs#2.type=ext4 --set fs#2.mnt=/srv/{fqdn}

The resource identifier must be specified.

## Non-Interactive Resource Deletion

	om <path> config update --delete fs#2

This command does not stop the resource before removing its definition. If desired, this can be done with

	om <path> stop --rid fs#2

## Batching

`om <path> config update` applies all its `--delete`, `--unset` and `--set` arguments as a single transaction: the batch is staged, validated, and committed once.

Scripts should prefer one command carrying many changes:

	om <path> config update \
		--set app#1.type=forking \
		--set app#1.start=/srv/app/bin/start \
		--set app#1.check=/srv/app/bin/check

Splitting this into one command per keyword commits three times. Each commit rewrites the configuration file, and every node in the object scope then fetches the whole file. Worse, each intermediate state is a state the peers and the orchestrator see and act upon, including the states where the resource definition is still incomplete.

Scripts driving the daemon API have the same choice: the `PATCH /api/object/path/{namespace}/{kind}/{name}/config` handler accepts repeated `set`, `unset` and `delete` parameters, and commits them as one transaction.

