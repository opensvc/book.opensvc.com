KVM Live Migration on ZFS
---

# Introduction

The [DRBD howto](kvm.live.migration.md) migrates a virtual machine whose disk both nodes can reach at once. A ZFS pool is imported on one node at a time, so a virtual machine whose disks live in it can not be migrated that way: its disks have to be copied to the destination while it runs.

OpenSVC does this copy when the disks of the virtual machine are held by these resources:

- `fs.zfs`: disk images, as qcow2 or raw files, in the filesystem of a dataset
- `disk.zvol`: zvols, used as block devices

A `switch --live` then moves the virtual machine with no downtime, the disks included.

# How a move works

On a `om <path> switch --live --node <dest>`, the node the virtual machine runs on:

1. Snapshots each `fs.zfs` and `disk.zvol` dataset, named `<dataset>@osvc_move_<UTC date>`.
2. Sends the snapshot to the destination node over ssh, incrementally from the newest snapshot both nodes hold, and in full when there is none. The first move to a node is a full copy, the next ones send what changed since the last move. The snapshots a `sync.zfs` replication leaves are a base too.
3. Mounts the `fs.zfs` copy on the destination, and waits for the device of the `disk.zvol` copy to appear there.
4. Runs `virsh migrate --live --persistent --copy-storage-all --migrate-disks <disks>`, which copies the memory of the virtual machine and mirrors its disks onto the copies while it runs. Only the disks held by `fs.zfs` and `disk.zvol` resources are mirrored: the disks of a shared storage, as a drbd, are not.
5. Once the virtual machine runs on the destination, destroys the older move snapshots on both nodes. The last one is kept, as the base of the next move.

The node the object is placed on then runs its start, which finds the filesystem mounted and the virtual machine up.

A migration that fails unmounts the copy on the destination, and the virtual machine keeps running where it was.

## How long a move may take

The migration mirrors the whole disks of the virtual machine, so it takes the time to copy them over the link between the nodes, which grows with their size. It is not bounded by the `stop_timeout` of the `container.kvm` resource, which is the time a guest has to shut down, two minutes by default: a migration copying disks has no timeout of its own, and the stop action of the object bounds it, by `DEFAULT.stop_timeout`, else `DEFAULT.timeout`, one hour by default.

Raise `DEFAULT.stop_timeout` when the disks take longer than that to copy, or bound the migration alone with the `migrate_timeout` keyword of the `container.kvm` resource:

<div class="tabs">
<div class="tab" data-title="CLI">

```
om kvm/svc/vm7 config update --set container#1.migrate_timeout=2h
```

</div>
<div class="tab" data-title="API">

```
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/object/path/kvm/svc/vm7/config?set=container%231.migrate_timeout%3D2h"
```

</div>
</div>

A migration that runs past its timeout is cancelled and rolled back, as a failed one is. A migration of shared storage, as a drbd in dual primary, copies the memory of the virtual machine only, and keeps the `stop_timeout` of the resource unless `migrate_timeout` is set.

# Prerequisites

- A ZFS pool of the same name on every node the object can run on, imported, with room for a copy of the datasets.
- The OpenSVC ssh trust between nodes, which the move uses to send the datasets and libvirt to migrate:

  ```
  om cluster ssh trust
  ```

- The libvirt disk mirroring flows open between nodes: libvirt serves the disks of an incoming migration on a port of the `49152-49215/tcp` range of the destination.

# Configure the service

## Disk images in a dataset

The virtual machine `vm6` has its disk image in the dataset `tank/vm6`, mounted on `/srv/kvm/vm6`:

```
[DEFAULT]
nodes = {clusternodes}
orchestrate = ha

[fs#1]
type = zfs
dev = tank/{name}
mnt = /srv/kvm/{name}

[container#1]
type = kvm
name = {name}
```

The domain refers to the image by its path in the dataset:

```
<disk type='file' device='disk'>
  <driver name='qemu' type='qcow2' cache='none'/>
  <source file='/srv/kvm/vm6/vm6.qcow2'/>
  <target dev='vda' bus='virtio'/>
</disk>
```

A read-only disk, as a cdrom image, is not mirrored by the migration: if it is in the dataset, it reaches the destination as a file of the copy. The same goes for the other files of the dataset, as an nvram, which are copied as they were when the snapshot was taken.

## Zvols

The virtual machine `vm7` has its disk on the zvol `tank/vm7`:

```
[DEFAULT]
nodes = {clusternodes}
orchestrate = ha

[disk#1]
type = zvol
name = tank/{name}
size = 10g

[container#1]
type = kvm
name = {name}
```

The domain refers to the device of the zvol:

```
<disk type='block' device='disk'>
  <driver name='qemu' type='raw' cache='none'/>
  <source dev='/dev/zvol/tank/vm7'/>
  <target dev='vda' bus='virtio'/>
</disk>
```

# Move the virtual machine

<div class="tabs">
<div class="tab" data-title="CLI">

```
om kvm/svc/vm6 switch --live --node n2 --wait
```

</div>
<div class="tab" data-title="API">

```
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"destination": ["n2"], "live": true}' \
  "https://<node>:1215/api/object/path/kvm/svc/vm6/action/switch"
```

</div>
</div>

The orchestration log shows the steps:

```
fs#1: zfs snapshot tank/vm6@osvc_move_20261001T075256.633159686Z
fs#1: /usr/sbin/zfs send -p -i tank/vm6@osvc_move_20261001T073633.292969041Z tank/vm6@osvc_move_20261001T075256.633159686Z | ssh n2 /usr/sbin/zfs receive -u -F tank/vm6
fs#1: ssh n2 /usr/sbin/zfs mount 'tank/vm6'
container#1: migrating container vm6 to n2
container#1: run /usr/bin/virsh migrate --live --persistent --copy-storage-all --migrate-disks vda vm6 qemu+ssh://n2/system?keyfile=/root/.ssh/opensvc
fs#1: zfs destroy tank/vm6@osvc_move_20261001T073633.292969041Z
fs#1: ssh n2 zfs destroy tank/vm6@osvc_move_20261001T073633.292969041Z
fs#1: tank/vm6: run /usr/sbin/zfs unmount tank/vm6
```

Each node keeps a copy of the datasets the virtual machine ran on, and the last move snapshot:

```
root@n1:~# zfs list -t snapshot tank/vm6
NAME                                            USED  AVAIL  REFER  MOUNTPOINT
tank/vm6@osvc_move_20261001T075256.633159686Z     0B      -  21.5M  -
```

> ⚠️ **Warning**: A destination that holds the dataset with no snapshot in common with the source is refused, as receiving a full copy over it would destroy what it holds. Destroy the dataset there, or replicate it with a `sync.zfs` resource, for the move to send it.

> 🛈 **Info**: The disks are mirrored in full by the migration, whatever the snapshot sent: the snapshot only makes the files and the devices the virtual machine opens exist on the destination. A move takes the time to copy the disks and the memory of the virtual machine, and the virtual machine runs all along.
