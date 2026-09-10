# Session, Execution and Orchestration Ids

Three identifiers name what the agent is doing, at three different scales.
They appear in the logs, in what an action returns to its submitter, and as
the keys of the two stores the daemon answers questions about past work from.

## sid, the session

An `om` or `ox` command takes a session id when it starts, unless its
environment already names one in `OSVC_SESSION_ID`, in which case it takes
that. The daemon exports its own into the commands it forks, so a whole chain
of causation shares one session id: the command an operator typed, the
commands the daemon forked because of it, and the commands those forked in
turn.

A session id therefore names **what was asked for**, not what was run. One
command can reach several objects, several nodes, or both, and all of it is
one session.

## eid, the execution

Each command the daemon forks takes an execution id of its own, exported as
`OSVC_EXEC_ID`.

An execution is **one run of one object on one node**. It is the scale at
which there is a single outcome, a single duration and a single object, which
is why it, and not the session, is what the daemon records:

```bash
$ om 'pod[36]' instance stop --node '*'
OBJECT  NODE    SID
pod6    dev2n1  a78a69fc-...
pod3    dev2n1  a78a69fc-...
pod6    dev2n2  a78a69fc-...
pod3    dev2n2  a78a69fc-...
pod6    dev2n3  a78a69fc-...
pod3    dev2n3  a78a69fc-...
```

One session, six executions, each with its own outcome. Two of them ran on
`dev2n1`, so a node holds several executions of one session.

## oid, the orchestration

When a command asks for a target state that the daemons must cooperate to
reach, rather than for a command to be run somewhere, the object is assigned
an orchestration id, exported as `OSVC_ORCHESTRATION_ID`.

```bash
$ om pod3 switch
OBJECT  ORCHESTRATION_ID                      STATUS
pod3    934a42f9-b7eb-4d7e-a3ac-18347522f9f9  accepted
```

An orchestration is not a command: the cluster decides which nodes act and
what they run. A switch stops the object on one node and starts it on
another, which is two executions, on two nodes, under the one orchestration
id. Every node of the object knows the orchestration under that id, the
daemons replicating the instance monitors it is carried in.

The executions an orchestration causes carry its id, and the ones it did not
cause carry none. A status evaluation is a step of nothing, and says so.

## Which one to ask with

An accepted action returns the session id **and** the execution id of the run
it accepted, so the submitter can ask after either scale:

```bash
om daemon session list <sid>              # every run of what I submitted
om daemon session list --exec-id <eid>    # the one run I am waiting on
om daemon orchestration list <oid>        # the target state, from any node
```

## Where they are recorded

| id | log key | store | asked through |
| :--- | :--- | :--- | :--- |
| sid | `SID` | — | a filter over the execution store |
| eid | `EID` | executions | `GET /api/node/name/<node>/daemon/session` |
| oid | `ORCHESTRATION_ID` | orchestrations | `GET /api/node/name/<node>/daemon/orchestration` |

The execution store is keyed by execution id and reached by session id,
because the session id is what a submitter is given to poll with. Both stores
are bounded, so an identifier the daemon no longer holds is reported as
forgotten rather than as unknown.

The same three keys are set on the log entries, so what a store no longer
holds can still be found for as long as the logs keep it:

```bash
journalctl SID=a78a69fc-...
journalctl EID=1149992d-...
journalctl ORCHESTRATION_ID=934a42f9-...
```

## A node orchestration

A node has a monitor of its own, carrying an orchestration id the same way an
instance monitor does, so a target state asked of the nodes rather than of an
object is an orchestration too.

> **Note:** these are not currently reported by
> `om daemon orchestration list`. The node orchestration id has not been
> observed reaching the replicated node monitors the listing is built from,
> where the object one does.

> ➡️ See Also
> * [Follow an Action](apps.operate.sessions.md)
> * [Events](internals.daemon.events.md)
