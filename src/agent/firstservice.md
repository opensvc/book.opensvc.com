# Your First Service

This page takes about five minutes and needs nothing but the agent
[installed](install.md) on one machine. No shared storage, no second node, no
cluster. At the end you will have created a service, started it, proven it is
serving, and stopped it.

We will wrap a plain HTTP server, because it is the shortest thing whose
running you can prove rather than take on trust.

## Create it

An object is created from the command line, resource by resource. Here is a
single `app` resource, told how to start:

```bash
om hello create \
  --kw app#1.type=simple \
  --kw 'app#1.start=/usr/bin/python3 -m http.server 8099'
```

Nothing was started, and nothing outside `/etc/opensvc` was touched. The
command only wrote a configuration, which you can read back:

```bash
om hello config show
```

    [DEFAULT]
    id = 0e745444-6724-48f9-8167-e865b4f9ec94

    [app#1]
    type = simple
    start = /usr/bin/python3 -m http.server 8099

`[app#1]` is a resource. `app` is its driver group, `1` its index, and
`type = simple` picks the driver that supervises a long-running process.

## Start it

```bash
om hello instance start
```

    INF hello: >>> do start [om hello instance start] (origin user, sid 7b9772c8)
    INF hello: app#1: run: om exec --pg /opensvc.slice/... -- /usr/bin/python3 -m http.server 8099
    INF hello: <<< done start in 98.079925ms, instance status is now up

The agent tells you what it ran and what the instance status became.

## Prove it

```bash
curl -o /dev/null -w "%{http_code}\n" http://localhost:8099/
```

    200

## Look at it

```bash
om hello instance status
```

    hello
    └ instances
      └ node1                    up  no-monitor
        └ resources
          └ app#1      ...../..  up  simple

The instance is `up` because its only resource is `up`. Had the resource
failed, both lines would say so. This is the command you will reach for most
often.

## Stop it

```bash
om hello instance stop
```

    INF hello: app#1: send termination signal to process 2615892
    INF hello: app#1: process 2615892 is now terminated
    INF hello: <<< done stop in 86.862589ms, instance status is now down

The port is closed and the status agrees:

```bash
curl --max-time 3 http://localhost:8099/
om hello instance status
```

    curl: (7) Failed to connect to localhost port 8099: Connection refused

    hello
    └ instances
      └ node1                    down  no-monitor
        └ resources
          └ app#1      ...../..  down  simple

## Clean up

```bash
om hello delete
```

    OBJECT  ORCHESTRATION_ID                      STATUS
    hello   068b4fb0-ba3f-4d62-81e7-92ed88039239  accepted

The configuration is gone, and with it the object.

## Two ways to start

You used `om hello instance start`, which starts the instance **on this node,
now**, and prints each step as it happens.

Its cluster counterpart is `om hello start`, which does not act directly. It
asks the cluster to reach the started state, and answers with an
orchestration id:

    OBJECT  ORCHESTRATION_ID                      STATUS
    hello   45c9de82-ed12-48df-bdb2-21a251fb039d  accepted

The daemon then picks a node and starts the instance there, which is what you
want once the object runs on more than one node. Watch it happen with `om mon`.
Note that the matching `om hello stop` also freezes the instance, so the daemon
does not immediately start it again.

## What you just did

You described a process in a configuration file, and the agent started it,
tracked its state, and stopped it. Everything else the agent does is this same
loop with more interesting resources: an ip that moves between nodes, a
filesystem mounted from a shared disk, a container, a database volume.

Where to go next:

* [Naming](apps.deploy.naming.md) to place objects in namespaces before you
  have many of them.
* [Create, Deploy](apps.deploy.create.md) for the other ways to create an
  object, including from a manifest.
* [Cluster Configuration](configure.cluster.md) to add a second node, which is
  where failover starts to matter.
