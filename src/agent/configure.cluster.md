# Cluster Configuration

Upon agent installation, the node is considered part of its own 1-node cluster.

In `/etc/opensvc/cluster.conf`:

* {{#include ../inc/kw}}`cluster.secret` is initialized to a random value.
* {{#include ../inc/kw}}`cluster.name` is initialized to a random value.

## Bootstrap a new cluster

If the node is to be enrolled in an existing cluster, skip this section.

### Add Heartbeats

If the cluster seed node has no heartbeat setup, a `unicast` heartbeat with default settings is automatically added on daemon start.

This default heartbeat requires every nodename to be resolved to an ip address reachable on 1215/tcp.

If these requirements are not met, you can setup one or more custom heartbeats on the seed node before enrolling nodes.

For example, a custom heartbeat configuration would be:

        om cluster config update --set hb#2.type=unicast --set hb#2.port=10002

The heartbeats status is summarized in the top section of the monitoring command output:

        om mon

And the detailed status is shown by:

        om daemon hb status

> ➡️ See Also
> * [Heartbeats](internals.daemon.heartbeats.md)
> * [Roles](configure.rbac.md)

### Add Stonith methods

Stonith is optional. Skip to the next section if not concerned.

On a new cluster, the stonith configuration can be applied on the first node. The enrolled nodes fetch this configuration from the cluster.

For example, a dummy stonith configuration would be

```
om cluster config update --set stonith#node2.command=/bin/true
```

This configuration will execute {{#include ../inc/cmd}}`/bin/true` on the node taking over a service which was previously running on the now stalled {{#include ../inc/node}}`node2`.

Good, isolated fencing packages are freely available. For one, https://github.com/ClusterLabs/fence-agents

## Enroll a Node

A node is added to the cluster from the cluster side: a cluster node enrolls the new node, which leaves its own 1-node cluster and joins.

The node to enroll must be a 1-node cluster. A node that is still a member of a cluster with peers is refused, because its peers would keep it in their `cluster.nodes`.

On the node to enroll {{#include ../inc/node}}`node2`, create a token with the `join` role, and store it in a file:

```
sudo om daemon auth --role join --duration 10m >/root/node2.token
```

The token is valid for 60 seconds by default, so `--duration` gives time to copy the file to a cluster node.

On any cluster node, for example {{#include ../inc/node}}`node1`, enroll {{#include ../inc/node}}`node2` using the copied token file:

```
$ sudo om cluster enroll --node node2 --token /root/node2.token --wait
Node node2 accepted the join order
Cluster nodes updated
Waiting for node2 to beat
Node node2 is alive
```

* `--node` is the location of the node to enroll, in the `[<scheme>://]<addr>[:<port>]` format.
* `--token` is the path of the token file. The `OSVC_JOIN_TOKEN` environment variable is used when the flag is not set.
* `--join-addr` is the location {{#include ../inc/node}}`node2` must use to reach {{#include ../inc/node}}`node1`, in the same format. By default, a name the cluster certificate is valid for is used. Set it when this name does not resolve to an address reachable from {{#include ../inc/node}}`node2`.
* `--wait` waits for the {{#include ../inc/node}}`node2` heartbeat to beat in the cluster. Without it, follow the join with `om daemon events --filter 'NodeAlive,.node=node2'`.
* `--timeout` is the maximum duration of the join, `1h` by default.

The enroll requires the `root` grant.

<div class="warning">

The enrolled node is drained before it leaves its cluster. As a 1-node cluster has nowhere to relocate its instances, they are stopped, stay down, and their configurations are removed.

Its configuration directory is moved to the backup directory, then the cluster, heartbeat and certificate configurations are fetched from the cluster.

</div>

## Evict a Node

A node is removed from the cluster by another cluster node. The evicted node leaves the cluster, then restarts its daemon alone, in a new 1-node cluster.

The node to evict must be drained: frozen, with no running instance. Else its instances would stay up on a node the cluster no longer knows about, free to start a second time elsewhere.

On any other cluster node, for example {{#include ../inc/node}}`node1`, drain then evict {{#include ../inc/node}}`node2`:

```
$ sudo om node drain --node node2 --wait
$ sudo om cluster evict --node node2 --credential /root/node2.cred --wait
Node node2 accepted the leave order
Cluster nodes updated
Node node2 is restarting alone, its instances stay down
```

* `--node` is the name of the cluster node to evict. It can not be the local node: run the command on one of its peers.
* `--credential` is the path of a file holding the `<username>:<password>` of a user to create on the evicted node, in the `system` namespace with the `root` grant. The `OSVC_CREDENTIAL` environment variable is used when the flag is not set.
* `--wait` waits for the cluster nodes to be updated. Without it, follow the eviction with `om daemon events --filter 'LeaveSuccess,removed_node=node2'`.
* `--timeout` is the maximum duration of the leave, `1h` by default.

The evict requires the `root` grant.

<div class="warning">

The evicted node ends up with a cluster secret of its own, so no user, token or certificate of the cluster can reach its api anymore. Without `--credential`, its api is only reachable locally, as root.

Its configuration directory is moved to the backup directory.

</div>

> ➡️ See Also
> * [Scheduler](internals.daemon.scheduler.md)
> * [Heartbeats](internals.daemon.heartbeats.md)
> * [Roles](configure.rbac.md)
