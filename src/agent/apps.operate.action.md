## Action

### Base Actions

#### Start

**Local Start (Bypasses Orchestrator)**

Start the service instance on the local node directly.

```
om <path> instance start
```

> **Resource Start Order:** `ip`, `disk`, `fs`, `share`, `container`, `app`.

**Orchestrated Start**

Instruct the orchestrator to start the service on the node(s) selected by the placement policy.

```
om <path> start [--wait] [--time <duration expr>] [--watch]
```

  * By default, the command returns upon daemon acknowledgment.
  * `--wait` holds the command until the action completes.
  * `--time` sets a maximum wait duration.

#### Stop

**Local Stop (Bypasses Orchestrator)**

Stop the service instance on the local node directly.

```
om <path> instance stop
```

> **Resource Stop Order:** `app`, `container`, `share`, `fs`, `disk`, `ip`.

**Orchestrated Stop and Freeze**

Instruct the orchestrator to stop the service wherever it runs and **freeze** it to prevent automatic restarts.

```
om <path> stop [--wait] [--time <duration expr>] [--watch]
```

#### Relocation

**Switch**

Stop the service on its current node(s) and start it on the specified target node. All instances are thawed afterward.

```
om <path> switch --node <nodename> [--wait] [--time <duration expr>] [--watch] [--live]
```

> The `container.kvm` supports live migration. Live migration requires the VM storage to be read-write from all nodes during the switch. SAN disks and drbd pass-through, NFS, Ceph, ClusterFS can satisfy this requirement.

**Takeover**

Stop the service instances on peer nodes and start it on the local node. All instances are thawed afterward.

```
om <path> takeover [--wait] [--time <duration expr>] [--watch]
```

**Giveback**

Thaw all nodes/instances, stop the service on non-leader nodes, and let the orchestrator start instances on the designated leaders. All instances are thawed afterward.

```
om <path> giveback [--wait] [--time <duration expr>] [--watch]
```

#### Handling Failures

If an action fails, the orchestrator is blocked, and the failure is reported in `om mon` and `om <path> print status`.

  * **Clear Failure:** Allows the daemon to **retry** the execution plan.
    ```
    om <path> clear
    ```
  * **Abort Action:** Aborts the currently blocked orchestrated action.
    ```
    om <path> abort
    ```

#### Sync

**Sync All**

Run resource replication to all configured targets (e.g., production (`prd`) or disaster recovery (`drp`)).

```
om <path> update
```

**Sync Nodes**

Trigger file synchronization to secondary cluster nodes. No-op if run from a node not running the service.

```
om <path> sync update --target nodes
```

**Sync DRP**

Trigger file synchronization to disaster recovery nodes. No-op if run from a node not running the service.

```
om <path> sync update --target drp
```

#### Run

Execute tasks defined within the service configuration.

```
om <path> instance run [--rid ...]
```

### Resource Filtering

Filter actions to be executed only on specific resources using `--rid`, `--tags`, or `--subsets`.

| Option | Syntax | Description |
| :--- | :--- | :--- |
| **`--rid` (ID List)** | `om <path> --rid <rid>[,<rid>,...] <action>` | Execute action on resources specified by resource IDs. |
| **`--rid` (Group List)** | `om <path> --rid <drvgrp>[,<drvgrp>,...] <action>` | Execute action on resources belonging to specified driver groups (`ip`, `disk`, `fs`, `share`, `container`, `app`, `sync`, `task`). |
| **`--tag` (OR)** | `om <path> --tag tag1,tag2 <action>` | Execute action on resources tagged with **either** `tag1` **or** `tag2`. |
| **`--tag` (AND/OR)** | `om <path> --tag tag1+tag2,tag3 <action>` | Execute action on resources tagged with **both** `tag1` **and** `tag2`, **OR** with `tag3`. |
| **`--subset`** | `om <path> --subset s1,s2 <action>` | Execute action on resources belonging to subset `s1` **or** `s2`. |


## Logging

All action logs are multiplexed to multiple destinations:

  * **Stdout/Stderr**
  * **Journald** or **Syslog**
  * **Collector Database** (Optional, via asynchronous XML-RPC calls)


## Examples

### Starting a Service (Local)

Shows the ordered execution of resource start-up.

```
# om svc0 instance start
10:51:50.590 INF svc0: >>> do start [om svc0 instance start] (origin user, sid ae60fdd4-6629-40eb-a993-4f1380d66516)
10:51:52.061 INF svc0: fs#1: install flag file /dev/shm/opensvc/svc/svc0/fs#1.flag
10:51:52.062 INF svc0: app#0: applied pg /opensvc.slice/opensvc-svc.svc0.slice
10:51:52.063 INF svc0: app#0: applied pg /opensvc.slice/opensvc-svc.svc0.slice/opensvc-svc.svc0-app.0.slice
10:51:52.090 INF svc0: app#0: run: /usr/bin/om exec --pg /opensvc.slice/opensvc-svc.svc0.slice/opensvc-svc.svc0-app.0.slice -- touch test -f /tmp/svc0.root.svc.reliable-leopard
10:51:52.194 INF svc0: <<< done start [om svc0 instance start] in 1.603582081s, instance status is now up
```

### Stopping a Service (Local)

Shows the ordered execution of resource shut-down.

```
# om svc0 instance stop
10:51:55.282 INF svc0: >>> do stop [om svc0 instance stop] (origin user, sid 807b55a5-8a5e-4a38-920c-94b6956da6a7)
10:51:55.380 INF svc0: app#0: run: /usr/bin/om exec --pg /opensvc.slice/opensvc-svc.svc0.slice/opensvc-svc.svc0-app.0.slice -- rm -f /tmp/svc0.root.svc.reliable-leopard
10:51:55.461 INF svc0: fs#1: uninstall flag file /dev/shm/opensvc/svc/svc0/fs#1.flag
10:51:55.494 INF svc0: <<< done stop [om svc0 instance stop] in 211.596639ms, instance status is now down
```
