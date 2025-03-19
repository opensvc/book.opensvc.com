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

