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

If this requirements are not met, you can setup one or more custom heartbeats on the seed node before joins.

For example, a custom heartbeat configuration would be:

        om cluster config set --kw hb#1.type=unicast --kw hb#1.port=1216

The new heartbeats are visible in the top section of the monitoring command output:

        om mon

<div class="warning">

See Also:

* [Heartbeats](internals.daemon.heartbeats.md)

</div>

### Add Stonith methods

Stonith is optional. Skip to the next section if not concerned.

On a new cluster, the stonith configuration can be applied on the first node. The joining nodes will fetch this configuration from this joined node.

For example, a dummy stonith configuration would be

```
om cluster config set --kw stonith#node2.cmd=/bin/true
```

This configuration will execute :cmd:`/bin/true` on the node taking over a service which was previously running on the now stalled {{#include ../inc/node}}`node2`.

Good, isolated fencing packages are freely available. For one, https://github.com/ClusterLabs/fence-agents

### Add Arbitrators

Arbitrators are optional. Skip to the next section if not concerned.

The arbitrator configuration can be applied on any node of the cluster.

```
om cluster config set --kw arbitrator#1.name=relay1 \
                      --kw arbitrator#1.secret=10231023102310231023102310231023
```

This configuration will ask for the agent on node {{#include ../inc/node}}`relay1` for its vote in a quorum race, if needed to get a majority.

The {{#include ../inc/kw}}`arbitrator#1.secret` value comes from the {{#include ../inc/kw}}`cluster.secret` value on the arbitrator `relay1`.

<div class="warning">

See Also:

* [Quorum](internals.daemon.quorum.md)

</div>

## Join a Cluster

The joining node can choose to join any of the cluster node already joined.

On the joined node {{#include ../inc/node}}`node1`, generate a join token:

```
$ om daemon auth --role join
```

On the joining node {{#include ../inc/node}}`node2`:

```
om daemon join --token <token> --node node1
```

<div class="warning">
Note:

* If the node was frozen before the join, it is left frozen after the join.
* If the node was not frozen before the join, the join process freezes it. If the join is successful, the node is thawed. If not, the node is left frozen.

</div>

## Leave a Cluster

```
om daemon leave
```



<div class="warning">

See Also:

* [Listener](agent.daemon.listener.md)
* [Monitor](agent.daemon.monitor.md)
* [Scheduler](agent.daemon.scheduler.md)
* [Quorum](agent.daemon.quorum.md)
* [Heartbeats](agent.daemon.heartbeats.md)
* [Orchestration](agent.service.orchestration.md)
* [DNS](agent.dns.md)

</div>
