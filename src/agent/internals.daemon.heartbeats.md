# Heartbeats

Heartbeats serve the following purposes:

- Exchange data between cluster nodes.
- Detect stale nodes.
- Execute the quorum race when a peer becomes stale.

OpenSVC supports multiple parallel running heartbeats. Exercising different code paths and infrastructure data paths (network and storage switches and site interconnects) helps limit split-brain situations.

## Configuration

Heartbeats are declared in `/etc/opensvc/cluster.conf`, each in a dedicated section named `[hb#<n>]`. A heartbeat definition should work on all nodes, using scoped keywords if necessary, as the definitions are served by the joined node to the joining nodes.

### Reconfiguration

Any command that changes the timestamp of the following configuration files triggers a reconfiguration of heartbeats:

- `/etc/opensvc/node.conf`
- `/etc/opensvc/cluster.conf`

### Actions Taken During Reconfiguration:

- Any updated parameters are applied to the heartbeats.
- Heartbeats removed from the configuration are stopped.
- Heartbeats newly defined in the configuration are started.

### Set a Heartbeat Timeout

To set a timeout for the `hb#1` heartbeat, use this command:

```
om cluster config update --set hb#1.timeout=20
```

### Drop a Heartbeat

To delete the `hb#1` heartbeat from the configuration:

```
om cluster config update --delete hb#1
```

## Monitoring

Each heartbeat runs two threads: `tx` and `rx`.

The `om mon` command display the heartbeats status, statistics, and each peer state.

<head>
<style type="text/css">
.ansi2html-content { display: inline; white-space: pre-wrap; word-wrap: break-word; }
.body_foreground { color: #AAAAAA; }
.body_background { background-color: #000000; }
.inv_foreground { color: #000000; }
.inv_background { background-color: #AAAAAA; }
.ansi1 { font-weight: bold; }
.ansi32 { color: #00aa00; }
.ansi33 { color: #aa5500; }
.ansi90 { color: #7f7f7f; }
.ansi91 { color: #ff0000; }
.ansi92 { color: #00ff00; }
.ansi93 { color: #ffff00; }
.ansi94 { color: #5c5cff; }
</style>
</head>
<pre class="ansi2html-content">
<code class="hljs">
Threads                                <span class="ansi1">n1</span>        <span class="ansi1">n2</span>        <span class="ansi1">n3</span>        
 <span class="ansi1">...</span>
 <span class="ansi1">hb</span>                                  |                                           <span class="ansi1">
  hb#1.rx</span>          <span class="ansi32">running</span> unicast   | <span class="ansi90">/</span>         <span class="ansi32">O</span>         <span class="ansi32">O</span>             <span class="ansi1">
  hb#1.tx</span>          <span class="ansi32">running</span> unicast   | <span class="ansi90">/</span>         <span class="ansi32">O</span>         <span class="ansi32">O</span>             <span class="ansi1">
  hb#2.rx</span>          <span class="ansi32">running</span> relay     | <span class="ansi90">/</span>         <span class="ansi32">O</span>         <span class="ansi32">O</span>             <span class="ansi1">
  hb#2.tx</span>          <span class="ansi32">running</span> relay     | <span class="ansi90">/</span>         <span class="ansi32">O</span>         <span class="ansi32">O</span>             
<span class="ansi1"> ...</span>
                                                                                 
</code>
</pre>                                                                                 

The agent daemon automatically restarts heartbeat threads if they exit unexpectedly.

## Heartbeat Thread Pair

### Tx (Transmit)

The Tx thread handles the transmission of the node data:

- Regularly transmit data or send it as soon as changes occur.
- Data is encrypted.

### Rx (Receive)

The Rx thread manages data reception and integration into cluster data:

- Regularly read data from disk or receive it in response to transmissions (unicast/multicast).
- Update peer data in the cluster.
- Timeout if no heartbeat is received within the configured {{#include ../inc/kw}}`<hb#n>.timeout`. The default timeout is 15 seconds.

Actions Performed by Rx:

- On receive data:
  - Merge updated peer data to maintain accurate cluster data.
  - Publish the received events on the local event bus.
- On receive timeout:
  - Publish a `HbStale` event 
  - Purge stale peer data if:
    - **No Maintenance Advertised:** Immediately purge stale peer data.
    - **Maintenance Advertised:** Wait for the `node.maintenance grace_period` before purging.

<div class="warning">

See Also:
* [Cluster Data](internals.cluster_data.md)

</div>

