# hb.relay

This driver reads and writes on a remote opensvc agent memory.

## Configuration

    [hb#2]
    type = relay
    relay = relay3.opensvc.com
    timeout = 15
    username = relay
    password = system/sec/relay

Note the v3 relay configuration no longer supports the `secret` keyword. The authentication creadentials are specified using the `username` and `password` keywords. The `password` value is the path of a sec object containing a `password` key.

## Behaviour

The relay listener `<address>:<port>` must be reachable from all cluster nodes in normal operations.

A relay should be located in a site hosting no other node of the cluster, so this heartbeat can prevent a split when the sites hosting cluster nodes are disconnected, but can still reach the relay's site.

The same relay can be used as heartbeat in different clusters.
The relay host can also be used as an arbitrator.

* The rx thread loops over peer nodes and for each requests its heartbeat data from the relay
* The tx thread sends to the relay

OpenSVC v3 clusters must use a OpenSVC v3 relay.

