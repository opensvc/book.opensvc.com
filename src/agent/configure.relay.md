# Cluster Relay

A relay is typically installed on a third site to provide two services to clusters:

* Act as a key-value store for relay-type heartbeats to exchange their encrypted datasets using different network paths.
* Act as a voter in quorum votations.

## Compatibility

A relay is a simple standalone OpenSVC server.

* A v2 server can serve as a relay for v2 clusters
* A v3 server can serve as a relay for v3 clusters.
* A v2 server can not serve as relay for v3 clusters
* A v3 server can not serve as relay for v2 clusters

Changes:

* The v2 server relay API handlers require the cluster nodes communicate with the relay node secret, granting `root` privilege.
* The v3 server relay API handlers require the cluster nodes communicate with a user account with the `heartbeat` privilege.
* The v3 server relay API handlers store the cluster nodes datasets in per-user namespaces, so a single relay can serve multiple client populations.

## Configure a v3 relay server

Install the opensvc-server package, then create the user account the clusters will use:

    om system/usr/relay create --kw grant=heartbeat

> ➡️ See Also
> * [How to install the agent](install.md)
> * [How to add a relay heartbeat to a cluster](internals.daemon.heartbeats.relay.md)
> * [How to add a arbitrator to a cluster](configure.quorum.md)

