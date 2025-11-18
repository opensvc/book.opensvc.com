## Services Status

### Cluster Overview (`om mon`)

The `om mon` command provides a real-time, human-readable overview of the cluster and service states.

#### Human Readable

```bash
om monitor
```

> **Requirements:**
>
>   * The agent daemon must be **up and running**.
>   * The displayed information is **near synchronous**.

#### Status and Alert Markers

Markers are used to optimize information density.

| Heartbeat Markers | On `hb.tx` Target | On `hb.rx` Source |
| :--- | :--- | :--- |
| **`O`** | Data has been sent in time | Data has been received in time |
| **`X`** | Data has not been sent in time | Data has not been received in time |
| **`/`** | Not applicable | Not applicable |

| General Markers | On Service Instance | On Service | On Node Status |
| :--- | :--- | :--- | :--- |
| **`O`** | `up` | | |
| **`o`** | `standby up` instance | | |
| **`X`** | `down` instance or heartbeat failure | | |
| **`x`** | `standby down` instance | | |
| **`/`** | Not applicable, undefined | | |
| **`^`** | Placement leader | Placement alert | |
| **`!`** | Warning | Warning raised by any instance | |
| **`!!`** | Not fully available instance | | |
| **`*`** | Frozen instance | | Frozen node |
| **`P`** | Not fully provisioned instance | | |

#### Machine Readable

Use the `--format` option for structured data output.

```bash
om daemon status --format json
```

#### Watch

Continuously refresh the status display.

```bash
om monitor --watch
```

