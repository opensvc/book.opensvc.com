# Cluster Configuration

Upon agent installation, the node is considered part of its own 1-node cluster.

In ``<OSVCETC>/cluster.conf``:

* {{#include kw}}`cluster.secret` is auto-generated, if not already defined.
* {{#include kw}}`cluster.name` is set to ``default``, if not already defined.

## Bootstrap a new cluster

If the node joins an existing cluster, skip this section.

### Add Heartbeats

On a new cluster, the heartbeats configuration need to be applied only on the first node. The joining nodes will fetch this configuration from this joined node.

For example, the simplest heartbeat configuration would be

```
        om cluster set --kw hb#1.type=unicast
```

Display the result

```
        om mon
```

<div class="warning">

See Also:

* [Heartbeats](agent.daemon.heartbeats)

</div>

### Add Stonith methods

Stonith is optional. Skip to the next section if not concerned.

On a new cluster, the stonith configuration can be applied on the first node. The joining nodes will fetch this configuration from this joined node.

For example, a dummy stonith configuration would be

```
om cluster set --kw stonith#node2.cmd=/bin/true
```

This configuration will execute :cmd:`/bin/true` on the node taking over a service which was previously running on the now stalled {{#include node}}`node2`.

Good, isolated fencing packages are freely available. For one, https://github.com/ClusterLabs/fence-agents

### Add Arbitrators

Arbitrators are optional. Skip to the next section if not concerned.

The arbitrator configuration can be applied on any node of the cluster.

```
om cluster set --kw arbitrator#1.name=relay1 \
               --kw arbitrator#1.secret=10231023102310231023102310231023
```

This configuration will ask for the agent on node {{#include node}}`relay1` for its vote in a quorum race, if needed to get a majority.

The {{#include kw}}`arbitrator#1.secret` value comes from the {{#include kw}}`cluster.secret` value on the arbitrator `relay1`.

<div class="warning">

See Also:

* [Quorum](agent.daemon.quorum.md)

</div>

## Join a Cluster

The joining node can choose to join any of the cluster node already joined.

On the joined node {{#include node}}`node1`

```
om cluster get --kw cluster.secret
```

On the joining node {{#include node}}`node2`

```
om daemon join --secret <secret> --node node1
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
