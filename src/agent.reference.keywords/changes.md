# Keyword changes

What each release of the agent added, removed and changed in its keywords. The reference itself documents v3.0.0-rc45.


## v3.0.0-rc45


### Added

- `cluster/collector.action_batch`
- `cluster/collector.action_log_timeout`
- `cluster/collector.feeder`
- `cluster/collector.ping_interval`
- `cluster/collector.server`
- `cluster/collector.status_delay`
- `cluster/collector.timeout`
- `cluster/collector.url`
- `cluster/listener.acme_port`
- `cluster/listener.tls_secs`
- `cluster/node.min_avail_mem`
- `cluster/node.min_avail_swap`
- `cluster/stats.disable`
- `cluster/stats.schedule`
- `node/collector.action_batch`
- `node/collector.action_log_timeout`
- `node/collector.feeder`
- `node/collector.ping_interval`
- `node/collector.server`
- `node/collector.status_delay`
- `node/collector.timeout`
- `node/collector.url`
- `node/listener.acme_port`
- `node/listener.tls_secs`
- `node/node.min_avail_mem`
- `node/node.min_avail_swap`
- `node/stats.disable`
- `node/stats.schedule`
- `sec/acme.directory`
- `sec/acme.renew_before`
- `sec/acme.webroot`
- `svc/task.acme.blocking_post_provision`
- `svc/task.acme.blocking_post_run`
- `svc/task.acme.blocking_post_unprovision`
- `svc/task.acme.blocking_pre_provision`
- `svc/task.acme.blocking_pre_run`
- `svc/task.acme.blocking_pre_unprovision`
- `svc/task.acme.check`
- `svc/task.acme.confirmation`
- `svc/task.acme.disable`
- `svc/task.acme.encap`
- `svc/task.acme.log`
- `svc/task.acme.max_parallel`
- `svc/task.acme.monitor`
- `svc/task.acme.on_error`
- `svc/task.acme.optional`
- `svc/task.acme.post_provision`
- `svc/task.acme.post_run`
- `svc/task.acme.post_unprovision`
- `svc/task.acme.pre_provision`
- `svc/task.acme.pre_run`
- `svc/task.acme.pre_unprovision`
- `svc/task.acme.provision`
- `svc/task.acme.provision_requires`
- `svc/task.acme.retcodes`
- `svc/task.acme.run_requires`
- `svc/task.acme.run_timeout`
- `svc/task.acme.schedule`
- `svc/task.acme.secs`
- `svc/task.acme.shared`
- `svc/task.acme.snooze`
- `svc/task.acme.standby`
- `svc/task.acme.subset`
- `svc/task.acme.tags`
- `svc/task.acme.timeout`
- `svc/task.acme.unprovision`
- `svc/task.acme.unprovision_requires`
- `svc/task.acme.webroot`

### Removed

- `cluster/node.min_avail_mem_pct`
- `cluster/node.min_avail_swap_pct`
- `node/node.min_avail_mem_pct`
- `node/node.min_avail_swap_pct`

### Changed

- `cluster/node.collector`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.url
- `cluster/node.collector_feeder`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.feeder
- `cluster/node.collector_ping_interval`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.ping_interval
- `cluster/node.collector_server`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.server
- `cluster/node.collector_status_delay`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.status_delay
- `cluster/node.collector_timeout`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.timeout
  - description rewritten
- `node/node.collector`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.url
- `node/node.collector_feeder`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.feeder
- `node/node.collector_ping_interval`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.ping_interval
- `node/node.collector_server`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.server
- `node/node.collector_status_delay`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.status_delay
- `node/node.collector_timeout`
  - deprecated: unset -> v3.0.0-rc44
  - replacedBy: unset -> collector.timeout
  - description rewritten
- `svc/app.forking.script`
  - description rewritten
- `svc/app.simple.script`
  - description rewritten
- `svc/container.docker.volume_mounts`
  - description rewritten
- `svc/container.lxc.cf`
  - description rewritten
- `svc/container.lxc.data_dir`
  - description rewritten
- `svc/container.lxc.rootfs`
  - description rewritten
- `svc/container.oci.volume_mounts`
  - description rewritten
- `svc/container.podman.volume_mounts`
  - description rewritten
- `svc/task.docker.volume_mounts`
  - description rewritten
- `svc/task.oci.volume_mounts`
  - description rewritten
- `svc/task.podman.volume_mounts`
  - description rewritten
- `vol/task.docker.volume_mounts`
  - description rewritten
- `vol/task.oci.volume_mounts`
  - description rewritten
- `vol/task.podman.volume_mounts`
  - description rewritten

## v3.0.0-rc43


### Added

- `cluster/console.port`
- `cluster/console.url`
- `node/console.port`
- `node/console.url`
- `svc/container.kvm.migrate_timeout`
- `svc/ip.rule.blocking_post_provision`
- `svc/ip.rule.blocking_post_start`
- `svc/ip.rule.blocking_post_stop`
- `svc/ip.rule.blocking_post_unprovision`
- `svc/ip.rule.blocking_pre_provision`
- `svc/ip.rule.blocking_pre_start`
- `svc/ip.rule.blocking_pre_stop`
- `svc/ip.rule.blocking_pre_unprovision`
- `svc/ip.rule.disable`
- `svc/ip.rule.encap`
- `svc/ip.rule.monitor`
- `svc/ip.rule.netns`
- `svc/ip.rule.optional`
- `svc/ip.rule.post_provision`
- `svc/ip.rule.post_start`
- `svc/ip.rule.post_stop`
- `svc/ip.rule.post_unprovision`
- `svc/ip.rule.pre_provision`
- `svc/ip.rule.pre_start`
- `svc/ip.rule.pre_stop`
- `svc/ip.rule.pre_unprovision`
- `svc/ip.rule.provision`
- `svc/ip.rule.provision_requires`
- `svc/ip.rule.restart`
- `svc/ip.rule.restart_delay`
- `svc/ip.rule.shared`
- `svc/ip.rule.spec`
- `svc/ip.rule.standby`
- `svc/ip.rule.start_requires`
- `svc/ip.rule.stop_requires`
- `svc/ip.rule.subset`
- `svc/ip.rule.tags`
- `svc/ip.rule.unprovision`
- `svc/ip.rule.unprovision_requires`

### Removed

- `cluster/console.insecure`
- `cluster/console.max_greet_timeout`
- `cluster/console.max_seats`
- `cluster/console.server`
- `node/console.insecure`
- `node/console.max_greet_timeout`
- `node/console.max_seats`
- `node/console.server`

### Changed

- `cluster/switch.brocade.method`
  - description rewritten
- `cluster/switch.brocade.name`
  - description rewritten
- `cluster/switch.brocade.password`
  - description rewritten
- `cluster/switch.type`
  - description rewritten
- `node/switch.brocade.method`
  - description rewritten
- `node/switch.brocade.name`
  - description rewritten
- `node/switch.brocade.password`
  - description rewritten
- `node/switch.schedule`
  - description rewritten
- `node/switch.type`
  - description rewritten
- `svc/fs.zfs.quota`
  - description rewritten
- `svc/fs.zfs.refquota`
  - defaultText: unset -> `x1` when `size` is set, none otherwise.

  - description rewritten
- `svc/fs.zfs.refreservation`
  - description rewritten
- `svc/fs.zfs.reservation`
  - description rewritten
- `svc/fs.zfs.size`
  - description rewritten
- `vol/fs.zfs.quota`
  - description rewritten
- `vol/fs.zfs.refquota`
  - defaultText: unset -> `x1` when `size` is set, none otherwise.

  - description rewritten
- `vol/fs.zfs.refreservation`
  - description rewritten
- `vol/fs.zfs.reservation`
  - description rewritten
- `vol/fs.zfs.size`
  - description rewritten

## v3.0.0-rc42


### Added

- `cluster/array.dorado.timeout`
- `cluster/array.freenas.insecure`
- `cluster/array.ibmsvc.key`
- `cluster/pool.dorado.array`
- `cluster/pool.dorado.diskgroup`
- `cluster/pool.dorado.fs_type`
- `cluster/pool.drbd.max_peers`
- `cluster/pool.shm.mode`
- `node/array.dorado.timeout`
- `node/array.freenas.insecure`
- `node/array.ibmsvc.key`
- `node/pool.dorado.array`
- `node/pool.dorado.diskgroup`
- `node/pool.dorado.fs_type`
- `node/pool.drbd.max_peers`
- `node/pool.shm.mode`
- `svc/DEFAULT.pg_cpu_burst`
- `svc/DEFAULT.pg_mem_high`
- `svc/DEFAULT.pg_pids_max`
- `svc/DEFAULT.wait_syncs_timeout`
- `svc/container.oci.rootless_group`
- `svc/container.oci.rootless_user`
- `svc/container.podman.rootless_group`
- `svc/container.podman.rootless_user`
- `svc/disk.hp3par.update_requires`
- `svc/fs.tmpfs.mode`
- `svc/fs.tmpfs.size`
- `svc/sync.rsync.update_requires`
- `svc/sync.symsnapvx.update_requires`
- `svc/sync.symsrdfs.update_requires`
- `svc/sync.zfs.max_lag_age`
- `svc/sync.zfs.max_lag_size`
- `svc/sync.zfs.update_requires`
- `svc/sync.zfssnap.update_requires`
- `svc/task.docker.read_only`
- `svc/task.docker.stop_timeout`
- `svc/task.docker.sysctl`
- `svc/task.oci.read_only`
- `svc/task.oci.rootless_group`
- `svc/task.oci.rootless_user`
- `svc/task.oci.stop_timeout`
- `svc/task.oci.sysctl`
- `svc/task.podman.read_only`
- `svc/task.podman.rootless_group`
- `svc/task.podman.rootless_user`
- `svc/task.podman.stop_timeout`
- `svc/task.podman.sysctl`
- `vol/DEFAULT.pg_cpu_burst`
- `vol/DEFAULT.pg_mem_high`
- `vol/DEFAULT.pg_pids_max`
- `vol/DEFAULT.wait_syncs_timeout`
- `vol/disk.hp3par.update_requires`
- `vol/fs.tmpfs.mode`
- `vol/fs.tmpfs.size`
- `vol/sync.rsync.update_requires`
- `vol/sync.symsnapvx.update_requires`
- `vol/sync.symsrdfs.update_requires`
- `vol/sync.zfs.max_lag_age`
- `vol/sync.zfs.max_lag_size`
- `vol/sync.zfs.update_requires`
- `vol/sync.zfssnap.update_requires`
- `vol/task.docker.read_only`
- `vol/task.docker.stop_timeout`
- `vol/task.docker.sysctl`
- `vol/task.oci.read_only`
- `vol/task.oci.rootless_group`
- `vol/task.oci.rootless_user`
- `vol/task.oci.stop_timeout`
- `vol/task.oci.sysctl`
- `vol/task.podman.read_only`
- `vol/task.podman.rootless_group`
- `vol/task.podman.rootless_user`
- `vol/task.podman.stop_timeout`
- `vol/task.podman.sysctl`

### Removed

- `cluster/array.freenas.timeout`
- `cluster/array.netapp.key`
- `cluster/array.pure.insecure`
- `cluster/drbd.max_peers`
- `cluster/pool.freenas.array`
- `cluster/pool.freenas.diskgroup`
- `cluster/pool.freenas.fs_type`
- `node/array.freenas.timeout`
- `node/array.netapp.key`
- `node/array.pure.insecure`
- `node/drbd.max_peers`
- `node/pool.freenas.array`
- `node/pool.freenas.diskgroup`
- `node/pool.freenas.fs_type`
- `svc/disk.hp3par.sync_requires`
- `svc/sync.rsync.sync_requires`
- `svc/sync.symsnapvx.sync_requires`
- `svc/sync.symsrdfs.sync_requires`
- `svc/sync.zfs.sync_requires`
- `svc/sync.zfssnap.sync_requires`
- `vol/disk.hp3par.sync_requires`
- `vol/sync.rsync.sync_requires`
- `vol/sync.symsnapvx.sync_requires`
- `vol/sync.symsrdfs.sync_requires`
- `vol/sync.zfs.sync_requires`
- `vol/sync.zfssnap.sync_requires`

### Changed

- `cluster/arbitrator.weight`
  - description rewritten
- `cluster/array.pure.secret`
  - description rewritten
- `node/arbitrator.weight`
  - description rewritten
- `node/array.pure.secret`
  - description rewritten
- `svc/DEFAULT.pg_cpu_shares`
  - description rewritten
- `svc/DEFAULT.pg_cpus`
  - description rewritten
- `svc/DEFAULT.pg_mem_limit`
  - description rewritten
- `svc/DEFAULT.pg_mem_oom_control`
  - description rewritten
- `svc/DEFAULT.pg_mems`
  - description rewritten
- `svc/DEFAULT.pg_vmem_limit`
  - description rewritten
- `svc/disk.drbd.template`
  - description rewritten
- `svc/disk.hp3par.array`
  - description rewritten
- `svc/disk.rados.config`
  - description rewritten
- `svc/disk.rados.keyring`
  - description rewritten
- `svc/disk.sgcp_nfs_cg.secret`
  - description rewritten
- `svc/fs.9pfs.install`
  - description rewritten
- `svc/fs.afs.install`
  - description rewritten
- `svc/fs.bfs.install`
  - description rewritten
- `svc/fs.bind.install`
  - description rewritten
- `svc/fs.btrfs.install`
  - description rewritten
- `svc/fs.cephfs.install`
  - description rewritten
- `svc/fs.cifs.install`
  - description rewritten
- `svc/fs.directory.install`
  - description rewritten
- `svc/fs.ext2.install`
  - description rewritten
- `svc/fs.ext3.install`
  - description rewritten
- `svc/fs.ext4.install`
  - description rewritten
- `svc/fs.f2fs.install`
  - description rewritten
- `svc/fs.gfs.install`
  - description rewritten
- `svc/fs.gfs2.install`
  - description rewritten
- `svc/fs.glusterfs.install`
  - description rewritten
- `svc/fs.gpfs.install`
  - description rewritten
- `svc/fs.hfs.install`
  - description rewritten
- `svc/fs.hfsplus.install`
  - description rewritten
- `svc/fs.hpfs.install`
  - description rewritten
- `svc/fs.jffs.install`
  - description rewritten
- `svc/fs.jffs2.install`
  - description rewritten
- `svc/fs.jfs.install`
  - description rewritten
- `svc/fs.jfs2.install`
  - description rewritten
- `svc/fs.lofs.install`
  - description rewritten
- `svc/fs.logfs.install`
  - description rewritten
- `svc/fs.minix.install`
  - description rewritten
- `svc/fs.msdos.install`
  - description rewritten
- `svc/fs.ncpfs.install`
  - description rewritten
- `svc/fs.nfs.install`
  - description rewritten
- `svc/fs.nfs4.install`
  - description rewritten
- `svc/fs.nilfs.install`
  - description rewritten
- `svc/fs.none.install`
  - description rewritten
- `svc/fs.ntfs.install`
  - description rewritten
- `svc/fs.ocfs.install`
  - description rewritten
- `svc/fs.ocfs2.install`
  - description rewritten
- `svc/fs.qnx4.install`
  - description rewritten
- `svc/fs.reiserfs.install`
  - description rewritten
- `svc/fs.reiserfs4.install`
  - description rewritten
- `svc/fs.rpc_pipefs.install`
  - description rewritten
- `svc/fs.sgcp_nfs.install`
  - description rewritten
- `svc/fs.sgcp_nfs.secret`
  - description rewritten
- `svc/fs.smbfs.install`
  - description rewritten
- `svc/fs.tmpfs.install`
  - description rewritten
- `svc/fs.tux3.install`
  - description rewritten
- `svc/fs.ufs.install`
  - description rewritten
- `svc/fs.ufs2.install`
  - description rewritten
- `svc/fs.umsdos.install`
  - description rewritten
- `svc/fs.vfat.install`
  - description rewritten
- `svc/fs.vxfs.install`
  - description rewritten
- `svc/fs.xfs.install`
  - description rewritten
- `svc/fs.xia.install`
  - description rewritten
- `svc/fs.zfs.install`
  - description rewritten
- `svc/ip.sgcp_dnsalias.secret`
  - description rewritten
- `svc/task.docker.max_parallel`
  - description rewritten
- `svc/task.host.max_parallel`
  - description rewritten
- `svc/task.oci.max_parallel`
  - description rewritten
- `svc/task.podman.max_parallel`
  - description rewritten
- `svc/volume..install`
  - description rewritten
- `vol/DEFAULT.pg_cpu_shares`
  - description rewritten
- `vol/DEFAULT.pg_cpus`
  - description rewritten
- `vol/DEFAULT.pg_mem_limit`
  - description rewritten
- `vol/DEFAULT.pg_mem_oom_control`
  - description rewritten
- `vol/DEFAULT.pg_mems`
  - description rewritten
- `vol/DEFAULT.pg_vmem_limit`
  - description rewritten
- `vol/disk.drbd.template`
  - description rewritten
- `vol/disk.hp3par.array`
  - description rewritten
- `vol/disk.rados.config`
  - description rewritten
- `vol/disk.rados.keyring`
  - description rewritten
- `vol/disk.sgcp_nfs_cg.secret`
  - description rewritten
- `vol/fs.9pfs.install`
  - description rewritten
- `vol/fs.afs.install`
  - description rewritten
- `vol/fs.bfs.install`
  - description rewritten
- `vol/fs.bind.install`
  - description rewritten
- `vol/fs.btrfs.install`
  - description rewritten
- `vol/fs.cephfs.install`
  - description rewritten
- `vol/fs.cifs.install`
  - description rewritten
- `vol/fs.directory.install`
  - description rewritten
- `vol/fs.ext2.install`
  - description rewritten
- `vol/fs.ext3.install`
  - description rewritten
- `vol/fs.ext4.install`
  - description rewritten
- `vol/fs.f2fs.install`
  - description rewritten
- `vol/fs.gfs.install`
  - description rewritten
- `vol/fs.gfs2.install`
  - description rewritten
- `vol/fs.glusterfs.install`
  - description rewritten
- `vol/fs.gpfs.install`
  - description rewritten
- `vol/fs.hfs.install`
  - description rewritten
- `vol/fs.hfsplus.install`
  - description rewritten
- `vol/fs.hpfs.install`
  - description rewritten
- `vol/fs.jffs.install`
  - description rewritten
- `vol/fs.jffs2.install`
  - description rewritten
- `vol/fs.jfs.install`
  - description rewritten
- `vol/fs.jfs2.install`
  - description rewritten
- `vol/fs.lofs.install`
  - description rewritten
- `vol/fs.logfs.install`
  - description rewritten
- `vol/fs.minix.install`
  - description rewritten
- `vol/fs.msdos.install`
  - description rewritten
- `vol/fs.ncpfs.install`
  - description rewritten
- `vol/fs.nfs.install`
  - description rewritten
- `vol/fs.nfs4.install`
  - description rewritten
- `vol/fs.nilfs.install`
  - description rewritten
- `vol/fs.none.install`
  - description rewritten
- `vol/fs.ntfs.install`
  - description rewritten
- `vol/fs.ocfs.install`
  - description rewritten
- `vol/fs.ocfs2.install`
  - description rewritten
- `vol/fs.qnx4.install`
  - description rewritten
- `vol/fs.reiserfs.install`
  - description rewritten
- `vol/fs.reiserfs4.install`
  - description rewritten
- `vol/fs.rpc_pipefs.install`
  - description rewritten
- `vol/fs.sgcp_nfs.install`
  - description rewritten
- `vol/fs.sgcp_nfs.secret`
  - description rewritten
- `vol/fs.smbfs.install`
  - description rewritten
- `vol/fs.tmpfs.install`
  - description rewritten
- `vol/fs.tux3.install`
  - description rewritten
- `vol/fs.ufs.install`
  - description rewritten
- `vol/fs.ufs2.install`
  - description rewritten
- `vol/fs.umsdos.install`
  - description rewritten
- `vol/fs.vfat.install`
  - description rewritten
- `vol/fs.vxfs.install`
  - description rewritten
- `vol/fs.xfs.install`
  - description rewritten
- `vol/fs.xia.install`
  - description rewritten
- `vol/fs.zfs.install`
  - description rewritten
- `vol/ip.sgcp_dnsalias.secret`
  - description rewritten
- `vol/task.docker.max_parallel`
  - description rewritten
- `vol/task.host.max_parallel`
  - description rewritten
- `vol/task.oci.max_parallel`
  - description rewritten
- `vol/task.podman.max_parallel`
  - description rewritten
- `vol/volume..install`
  - description rewritten

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
