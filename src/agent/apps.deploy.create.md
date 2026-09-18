# Create, Deploy

The following actions only modify files in `/etc/opensvc`. No operating system configuration file is modified, so they are safe to experiment with.

The agent support object creation via two commands:

* ``create``
  The object is created but not provisioned nor started.

* ``deploy``
  The object is created, provisioned and started.

Both actions support the same arguments. The following examples use only create commands.

## From Scratch, non Interactive

Create a new object with minimal configuration. No resources are described.


	om <path> create

Resources and default keywords can be set right from the create command, using ``--kw <keyword>=<value>`` options

	om <path> create \
		--kw container#0.type=oci \
		--kw orchestrate=ha \
		--kw nodes={clusternodes}

Scripts should describe the object as completely as possible in this single command. The keywords given to ``create`` are part of the first and only commit, so the object is never announced to the cluster in a half-configured state. Creating a bare object then completing it with a series of ``config update`` commands publishes every intermediate state to the peers, and the orchestrator acts on them as soon as ``orchestrate`` is set.

## From Another Object


	om <dst path> create --config=<src path>

## From Manifest

The manifest must be ini formatted, like the output of ``om <path> config show``.

	om <path> create --config=<manifest uri>

This method can also be used to clone objects

	om <dst path> create --config=<src path>

or

	om <src path> config show | om <dst path> create --config=-

## What a Clone Resets

A clone is another object, so what the source recorded of itself does not come
with it. Those keywords are marked in the keyword reference:

	recorded:    written when what it names is made, and reset when the object is cloned

The object id is one of them, and the clone is given a new one. The uuid of an
md array is another: it is written when the array is created, and is what
assembles that array again afterwards, so a clone keeping it would assemble
the source's array rather than create one of its own.

They are written again, for the clone, when the clone makes what they name.

`--restore` keeps them, which is what restoring a saved configuration means:
the object being created is the one the configuration was saved from, not
another like it.

	om <path> create --config=<backup> --restore

> ➡️ See Also
> * [Provisioning](apps.deploy.provisioning.md)
> * [Batching configuration changes](apps.deploy.update.md#batching)
