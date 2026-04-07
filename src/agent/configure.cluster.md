# Cluster Configuration

Upon agent installation, the node is considered part of its own 1-node cluster.

In `/etc/opensvc/cluster.conf`:

* {{#include ../inc/kw}}`cluster.secret` is initialized to a random value.
* {{#include ../inc/kw}}`cluster.name` is initialized to a random value.

## Bootstrap a new cluster

If the node joins an existing cluster, skip this section.

### Add Heartbeats

If the cluster seed node has no heartbeat setup, a `unicast` heartbeat with default settings will be automatically added on first join.

This default heartbeat requires every nodename to be resolved to an ip address reachable on 1215/tcp.

If these requirements are not met, you can setup one or more custom heartbeats on the seed node before joins.

For example, a custom heartbeat configuration would be:

        om cluster config update --set hb#2.type=unicast --set hb#2.port=10002

The heartbeats status is summarized in the top section of the monitoring command output:

        om mon

And the detailed status is shown by:

        om daemon hb status

> ➡️ See Also
> * [Heartbeats](internals.daemon.heartbeats.md)

### Add Stonith methods

Stonith is optional. Skip to the next section if not concerned.

On a new cluster, the stonith configuration can be applied on the first node. The joining nodes will fetch this configuration from this joined node.

For example, a dummy stonith configuration would be

```
om cluster config update --set stonith#node2.command=/bin/true
```

This configuration will execute {{#include ../inc/cmd}}`/bin/true` on the node taking over a service which was previously running on the now stalled {{#include ../inc/node}}`node2`.

Good, isolated fencing packages are freely available. For one, https://github.com/ClusterLabs/fence-agents

## Join a Cluster

The joining node can choose to join any of the cluster node already joined.

On the joined node {{#include ../inc/node}}`node1`, generate a join token:

```
$ sudo om daemon auth --role join
```

On the joining node {{#include ../inc/node}}`node2`:

```
sudo om cluster join --token <token> --node node1
```

<div class="warning">
Note:

* If the node was frozen before the join, it is left frozen after the join.
* If the node was not frozen before the join, the join process freezes it. If the join is successful, the node is thawed. If not, the node is left frozen.

</div>

## Leave a Cluster

```
sudo om cluster leave
```


> ➡️ See Also
> * [Scheduler](internals.daemon.scheduler.md)
> * [Heartbeats](internals.daemon.heartbeats.md)
