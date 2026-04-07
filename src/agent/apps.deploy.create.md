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

	om <path> create
		--kw container#0.type=oci \
		--kw orchestrate=ha \
		--kw nodes={clusternodes}

## From Another Object


	om <dst path> create --config=<src path>

## From Manifest

The manifest must be ini formatted, structured like ``om <path> print config --format=json``.

	om <path> create --config=<manifest uri>

This method can also be used to clone objects

	om <dst path> create --config=<src path>

or

	om <src path> config show | om <dst path> create --config=-


> ➡️ See Also
> * [Provisioning](agent-service-provisioning)

