# Keyword changes

What each release of the agent added, removed and changed in its keywords. The reference itself documents v3.0.0-rc41.


## v3.0.0-rc41


### Changed

- `svc/container.oci.userns`
  - description rewritten
- `svc/task.oci.userns`
  - description rewritten
- `vol/task.oci.userns`
  - description rewritten

## v3.0.0-rc40


### Changed

- `svc/DEFAULT.orchestrate`
  - description rewritten

## v3.0.0-rc39


### Added

- `cluster/pool.directory.quota`
- `node/pool.directory.quota`
- `svc/fs.directory.project_id`
- `svc/fs.directory.size`
- `vol/fs.directory.project_id`
- `vol/fs.directory.size`

### Changed

- `cfg/DEFAULT.id`
  - recorded: unset -> true
- `sec/DEFAULT.id`
  - recorded: unset -> true
- `svc/DEFAULT.id`
  - recorded: unset -> true
- `svc/disk.disk.size`
  - inherit: leaf2head -> leaf
- `svc/disk.loop.size`
  - converter: unset -> size
  - inherit: leaf2head -> leaf
- `svc/disk.lv.size`
  - arithmetic: unset -> true
  - inherit: leaf2head -> leaf
  - description rewritten
- `svc/disk.md.uuid`
  - recorded: unset -> true
- `svc/disk.rados.size`
  - converter: unset -> size
  - inherit: leaf2head -> leaf
- `svc/disk.zvol.size`
  - inherit: leaf2head -> leaf
- `svc/fs.zfs.size`
  - inherit: leaf2head -> leaf
- `svc/volume..size`
  - inherit: leaf2head -> leaf
- `usr/DEFAULT.id`
  - recorded: unset -> true
- `vol/DEFAULT.id`
  - recorded: unset -> true
- `vol/disk.disk.size`
  - inherit: leaf2head -> leaf
- `vol/disk.loop.size`
  - converter: unset -> size
  - inherit: leaf2head -> leaf
- `vol/disk.lv.size`
  - arithmetic: unset -> true
  - inherit: leaf2head -> leaf
  - description rewritten
- `vol/disk.md.uuid`
  - recorded: unset -> true
- `vol/disk.rados.size`
  - converter: unset -> size
  - inherit: leaf2head -> leaf
- `vol/disk.zvol.size`
  - inherit: leaf2head -> leaf
- `vol/fs.zfs.size`
  - inherit: leaf2head -> leaf
- `vol/volume..size`
  - inherit: leaf2head -> leaf

## v3.0.0-rc38


### Changed

- `svc/disk.sgcp_nfs_cg.endpoint`
  - description rewritten
- `svc/fs.sgcp_nfs.endpoint`
  - description rewritten
- `svc/ip.sgcp_dnsalias.endpoint`
  - description rewritten
- `vol/disk.sgcp_nfs_cg.endpoint`
  - description rewritten
- `vol/fs.sgcp_nfs.endpoint`
  - description rewritten
- `vol/ip.sgcp_dnsalias.endpoint`
  - description rewritten

## v3.0.0-rc37


### Added

- `cluster/array.pure.private_key`
- `node/array.pure.private_key`

### Changed

- `cluster/array.pure.secret`
  - deprecated: unset -> 3.0.0
  - replacedBy: unset -> private_key
  - required: true -> unset
- `node/array.pure.secret`
  - deprecated: unset -> 3.0.0
  - replacedBy: unset -> private_key
  - required: true -> unset
- `svc/DEFAULT.pg_blkio_weight`
  - description rewritten
- `svc/DEFAULT.pg_cpu_quota`
  - description rewritten
- `svc/DEFAULT.pg_cpu_shares`
  - description rewritten
- `svc/DEFAULT.pg_cpus`
  - description rewritten
- `svc/DEFAULT.pg_mem_limit`
  - description rewritten
- `svc/DEFAULT.pg_mem_oom_control`
  - description rewritten
- `svc/DEFAULT.pg_mem_swappiness`
  - description rewritten
- `svc/DEFAULT.pg_mems`
  - description rewritten
- `svc/DEFAULT.pg_vmem_limit`
  - description rewritten
- `vol/DEFAULT.pg_blkio_weight`
  - description rewritten
- `vol/DEFAULT.pg_cpu_quota`
  - description rewritten
- `vol/DEFAULT.pg_cpu_shares`
  - description rewritten
- `vol/DEFAULT.pg_cpus`
  - description rewritten
- `vol/DEFAULT.pg_mem_limit`
  - description rewritten
- `vol/DEFAULT.pg_mem_oom_control`
  - description rewritten
- `vol/DEFAULT.pg_mem_swappiness`
  - description rewritten
- `vol/DEFAULT.pg_mems`
  - description rewritten
- `vol/DEFAULT.pg_vmem_limit`
  - description rewritten

## v3.0.0-rc36

Where this timeline starts: 8948 keywords, none of them new.
