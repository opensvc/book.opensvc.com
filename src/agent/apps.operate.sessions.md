# Follow an Action

An action submitted to the daemon returns before it is done. What comes back
is an identifier, and the daemon remembers what became of it, so a client that
asked for something can ask how it went.

## The identifier you are given

Which one depends on who decides where the action runs.

An action addressed to a node is a **session**. You chose the node, so the
answer is on that node:

```bash
$ om pod3 stop --node dev2n1
OBJECT  NODE    SID
pod3    dev2n1  efa38cf0-55f1-405d-b727-ac9791ef9938
```

An action addressed to the object is an **orchestration**. The cluster decides
which nodes act, and one orchestration runs sessions on each of them:

```bash
$ om pod3 switch
OBJECT  ORCHESTRATION_ID                      STATUS
pod3    934a42f9-b7eb-4d7e-a3ac-18347522f9f9  accepted
```

## Asking after a session

```bash
$ om daemon session list efa38cf0-55f1-405d-b727-ac9791ef9938
NODE    STATE      ID        PATH  ORIGIN  BEGIN_AT                   DURATION  COMMAND
dev2n1  succeeded  efa38cf0  pod3  api     2026-09-10T18:49:15+02:00  168ms     om pod3 instance stop
```

Naming no session lists them all, and `--state` narrows:

```bash
om daemon session list                      # every state, this node
om daemon session list --state running
om daemon session list --state failed       # the second thing anyone asks
om daemon session list --node dev2n2
```

A failed session carries what failed, in the `error` field the `-o json`
output shows.

## Asking after an orchestration

```bash
$ om daemon orchestration list 934a42f9-b7eb-4d7e-a3ac-18347522f9f9
STATE      ID        PATH  GLOBAL_EXPECT  ACCEPTED_BY  BEGIN_AT
succeeded  934a42f9  pod3  placed@        dev2n1       2026-09-10T20:34:27+02:00
```

**Any node answers.** Every node of the object learns of the orchestration
from the instance monitors the daemon replicates, so it does not matter which
one you reach. That is what lets a client behind a floating address follow an
orchestration: the address may move to another node while the orchestration
runs, and a switch is precisely what moves it.

`ACCEPTED_BY` is the node that was asked for the orchestration, and is empty
on a node that only learned of it from the monitors. It is the one detail that
differs between nodes; the state, the object, the target and the start do not.

## An orchestration is several sessions

A switch stops the object on one node and starts it on another, under one
orchestration id. Each node holds the session it ran itself, so the whole of
an orchestration is the union over the nodes:

```bash
$ om daemon session list --orchestration-id 934a42f9-... --node dev2n1
dev2n1  succeeded  ...  pod3  imon  ...  532ms   om pod3 instance stop

$ om daemon session list --orchestration-id 934a42f9-... --node dev2n2
dev2n2  succeeded  ...  pod3  imon  ...  1614ms  om pod3 instance start
```

## When the daemon has forgotten

What the daemon remembers is bounded, by age and by count, so a node that has
been running for months does not carry every action it ever ran. An identifier
it no longer holds says so:

```bash
$ om daemon session list efa38cf0-55f1-405d-b727-ac9791ef9938
Error: dev2n1: session efa38cf0-... is no longer known: it ended long enough
ago to have been dropped, or never ran there
```

That is deliberately not the same answer as a session that is still running,
and not the same as one that never existed. A client polling for the end of
an action must be able to tell "not finished" from "I no longer know", which
is why forgetting is admitted rather than reported as absence.

What is running is never forgotten for the count. Only what has ended is
dropped.

> ➡️ See Also
> * [Action](apps.operate.action.md)
> * [Events](internals.daemon.events.md)
