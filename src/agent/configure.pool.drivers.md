# Pool Drivers

Reference of the pool drivers, their capabilities and their keywords. To
choose between them, see [Cluster Storage Pools](configure.pool.md).

## directory

### Capabilities

rox, rwx, roo, rwo

### Layout

A volume object from this type of pool contains:

* a fs.directory resource, with {{#include ../inc/kw}}`path=<pool head>/<volume fqdn>`.

### Keywords

- [Reference](/agent.reference.keywords/node/pool.directory.md)

## drbd

### Capabilities

rox, rwx, shared, blk, roo, rwo

### Layout

A volume object from this type of pool contains:

If a vg is defined in the pool configuration,

* a fs resource, with {{#include ../inc/kw}}`dev=<drbd devpath>`
* a drbd resource, layered over a logical volume of the pool vg
* a lv resource

If a zpool is defined in the pool configuration,

* a fs resource, with {{#include ../inc/kw}}`dev=<drbd devpath>`
* a drbd resource, layered over a zvol of the pool zpool
* a zvol resource

If the pool configuration has neither vg nor zpool set,

* a fs resource, with {{#include ../inc/kw}}`dev=<drbd devpath>`
* a drbd resource, layered over a logical volume
* a lv resource
* a vg resource
* a loop resource, with image file hosted in the pool defined {{#include ../inc/kw}}`path` or in `<PATHVAR>/pool/<poolname>/`

### Keywords

- [Reference](/agent.reference.keywords/node/pool.drbd.md)

## freenas

### Capabilities

roo, rwo, shared, blk, iscsi

### Layout

A volume object from this type of pool contains:

* a disk.disk resource named, with {{#include ../inc/kw}}`name=<volume fqdn>`

If the consumer has {{#include ../inc/kw}}`format=true` (default), the volume object also contains:

* a `fs.<pool fs_type>` resource, with {{#include ../inc/kw}}`mnt=/srv/<volume fqdn>`

### Keywords

- [Reference](/agent.reference.keywords/node/pool.freenas.md)

## loop

### Capabilities

rox, rwx, roo, rwo, blk

### Layout

A volume object from this type of pool contains:

* a disk.loop resource, with {{#include ../inc/kw}}`file=<pool head>/<volume fqdn>.img`

If the consumer has {{#include ../inc/kw}}`format=true` (default), the volume object also contains:

* a `fs.<pool fs_type>` resource, with {{#include ../inc/kw}}`mnt=/srv/<volume fqdn>`

### Keywords

- [Reference](/agent.reference.keywords/node/pool.loop.md)

## symmetrix

### Capabilities

roo, rwo, shared, blk, fc

### Layout

A volume object from this type of pool contains:

* a disk.disk resource named, with {{#include ../inc/kw}}`name=<volume fqdn>`

If the consumer has {{#include ../inc/kw}}`format=true` (default), the volume object also contains:

* a `fs.<pool fs_type>` resource, with {{#include ../inc/kw}}`mnt=/srv/<volume fqdn>`

### Keywords

- [Reference](/agent.reference.keywords/node/pool.symmetrix.md)

## vg

### Capabilities

rox, rwx, roo, rwo, blk, snap

### Layout

A volume object from this type of pool contains:

* a disk.lv resource, with {{#include ../inc/kw}}`name=<volume fqdn>`

If the consumer has {{#include ../inc/kw}}`format=true` (default), the volume object also contains:

* a `fs.<pool fs_type>` resource, with {{#include ../inc/kw}}`mnt=/srv/<volume fqdn>`

### Keywords

- [Reference](/agent.reference.keywords/node/pool.vg.md)

## share

### Capabilities

rox, rwx, roo, rwo, shared

### Layout

A volume object from this type of pool contains:

* a fs.directory resource, with {{#include ../inc/kw}}`path=<pool head>/<volume fqdn>`.

### Keywords

- [Reference](/agent.reference.keywords/node/pool.share.md)

## zpool

### Capabilities

rox, rwx, roo, rwo, blk, snap

### Layout

A volume object from this type of pool contains:

* a fs.zfs resource, with {{#include ../inc/kw}}`name=<pool>/<volume fqdn>` and {{#include ../inc/kw}}`mnt=/srv/<volume fqdn>`.

### Keywords

- [Reference](/agent.reference.keywords/node/pool.zpool.md)

## Virtual Pool Driver

A virtual pool allow administrators to create complex layouts based on volumes from other pools.

A typical use-case in a virtual pool allocating volumes mirrored over two other volumes allocated from arrays on two different sites.

A virtual pool volume is created from a template volume object the administrator can design at wish to meet its specific needs.

### Capabilities

Capabilities are user defined.

### Keywords

- [Reference](/agent.reference.keywords/node/pool.virtual.md)
