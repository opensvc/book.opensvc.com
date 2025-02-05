# Quorum

When a peer is flagged as stale by all heartbeats, the daemon assumes the cluster is in a split-brain situation, as it cannot determine whether the stale peer has failed or is isolated.

OpenSVC minimizes the likelihood of a split-brain scenario by leveraging multiple independent heartbeats.

## Enabling Quorum Enforcement

Users who prefer to have a cluster segment shut down in such situations can enable quorum by setting `cluster.quorum` to `true`:

    om cluster set --kw cluster.quorum=true

By default, the system allows split nodes to take over services, which may result in services running on multiple isolated segments. To revert to the default behavior, use:

    om cluster unset --kw cluster.quorum

To check the current quorum configuration:

    om cluster get --kw cluster.quorum

## Quorum Behavior

If the cluster is configured for quorum and a split-brain situation occurs, a node will shut down if the number of reachable nodes (including itself) plus arbitrators is less than half of the total cluster and arbitrator nodes.

Frozen nodes do no evaluate quorum. They will not shut down on split-brain.

Frozen nodes still vote for peer nodes quorum evaluation.

### Example Arbitrator Requirements

To survive a interconnect outage:

- In a 2-node cluster, a single node requires 1 arbitrator vote to survive the split.
- In a 3-node cluster, a single node requires 2 arbitrator votes.
- In a 4-node cluster, a single node requires 3 arbitrator votes.
- In a 5-node cluster, a single node requires 3 arbitrator votes.

To survive a interconnect outage, plus all peers outage in the same availability zone:

- In a 2-node cluster, a single node requires 1 arbitrator vote to survive the split.
- In a 3-node cluster, a single node requires 2 arbitrator votes.
- In a 4-node cluster, a single node requires 3 arbitrator votes.
- In a 5-node cluster, a single node requires 4 arbitrator votes.

## Configuring Arbitrators

Any OpenSVC agent can act as an arbitrator, and multiple arbitrators can be configured. For example, to configure an arbitrator:

### Use a https server as an arbitrator

    [arbitrator#a1]
    uri = https://dev2n1:1215/metrics
    #insecure = true

### Use a tcp server as an arbitrator

    [arbitrator#a2]
    uri = dev2n2:22

## Testing Arbitrators

Alive test of an arbitrator:

        $ om node ping --node a1
 
The `om mon` output show all arbitrator alive state from the point of view of every node.

        $ om mon
        ...
        Arbitrators                       n1   n2
         a1                warn         | X    X          
         a2                warn         | X    X          
         a3                             | O    O          
        ...

## Best Practices

* Configure <number of nodes> minus 1 arbitrators
* Host all arbitrators on the same 3rd site
* Use one of the arbitrators as a relay for the relay heartbeat driver
* Disable quorum or freeze all nodes when doing a relayout of the cluster

