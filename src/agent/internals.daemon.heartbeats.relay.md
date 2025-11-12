# hb.relay

This driver implements a heartbeat mechanism by reading and writing on the memory of a dedicated OpenSVC agent relay host.

## Purpose

The `hb.relay` heartbeat is designed to prevent split-brain scenarios in a cluster by establishing a neutral, off-site communication check.

  * A relay should ideally be located in a **third site** that hosts **no other node** of the cluster.
  * This setup allows the cluster to make a correct quorum decision when the sites hosting the cluster nodes become disconnected from each other, but can still independently reach the relay's site.
  * The same relay host can be shared and used as a heartbeat mechanism by multiple different clusters.

## Configuration

The heartbeat is defined in the cluster configuration file (`cluster.conf`) within a `[hb#N]` section.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **`type`** | String | Must be set to `relay`. |
| **`relay`** | String | The hostname or IP address of the remote OpenSVC relay agent. |
| **`timeout`** | Duration | The connection and I/O timeout (e.g., `15s`). |
| **`username`** | String | The username for authentication with the relay host. |
| **`password`** | String | The path to a `sec` object containing the authentication password key (e.g., `system/sec/relay`). |

### Example

```ini
[hb#2]
type = relay
relay = relay3.opensvc.com
timeout = 15
username = relay
password = system/sec/relay
```

### Authentication Note

The OpenSVC v3 relay configuration **no longer supports** the `secret` keyword. Authentication credentials must be specified exclusively using the `username` and `password` keywords.

## Requirements

  * **Reachability:** The relay listener (typically at `<address>:<port>`) must be **reachable** from all cluster nodes during normal operations.
  * **Version Compatibility:** OpenSVC v3 clusters **must** use an OpenSVC v3 relay agent.
  * **Arbitration:** The relay host **can** also be configured and used as a cluster arbitrator.

## Key Operations

The driver utilizes two primary threads for communication:

  * **The Transmission Thread (TX):**
      * This thread is responsible for **sending** the local cluster node's heartbeat data to the remote relay agent, updating its status in the relay's memory.
  * **The Reception Thread (RX):**
      * This thread constantly **loops** over all peer nodes in the cluster and for each one, **requests** its current heartbeat data from the relay agent. This data retrieval determines the peer's reachability.

