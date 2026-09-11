# Follow an Action

An action submitted to the daemon returns before it is done. What comes back
is a pair of identifiers, and the daemon remembers what became of them, so a
client that asked for something can ask how it went.

## Three commands, three scales

| command | one row is | ask it when |
| :--- | :--- | :--- |
| `om daemon session list` | one submitted command, whole | "how did what I asked for go?" |
| `om daemon exec list` | one run of one object on one node | "which part of it failed, and why?" |
| `om daemon ps` | one run that is still running | "what is running now, and what is its pid?" |

`om daemon ps` is `om daemon exec list --state running` under a shorter name
and with the pid in front. What is running and what has run are the same
records at different ages, so they are one listing.

## The identifiers you are given

An action addressed to a node returns the **session** id and the **exec** id.
The session is the whole of what you submitted; the exec is the one run:

```bash
$ om 'pod[36]' instance stop --node '*'
OBJECT  NODE    SESSION_ID                            EXEC_ID
pod6    dev2n1  e9440381-9507-42b3-bef3-2c815aceb169  d29abc32-2c0b-45ff-b639-508d5c19fbee
pod3    dev2n1  e9440381-9507-42b3-bef3-2c815aceb169  9178f4f8-cd37-4ab5-874f-6d72b1d825f5
pod6    dev2n2  e9440381-9507-42b3-bef3-2c815aceb169  f40da200-7b6f-41aa-b6aa-dc2568b8cde2
…
```

An action addressed to the object returns an **orchestration** id instead. The
cluster decides which nodes act, and one orchestration runs execs on each of
them:

```bash
$ om pod3 switch
OBJECT  ORCHESTRATION_ID                      STATUS
pod3    934a42f9-b7eb-4d7e-a3ac-18347522f9f9  accepted
```

[Session, Execution and Orchestration Ids](internals.ids.md) says how the
three relate.

## Asking after a session

One row, whatever it took:

```bash
$ om daemon session list e9440381-9507-42b3-bef3-2c815aceb169
SESSION_ID  STATE      EXECS  FAILED  NODES  OBJECTS  ORIGIN  BEGIN_AT  DURATION  COMMAND
e9440381…   succeeded  6      0       3      2        api     …         11s       om pod3 instance stop (+5)
```

`STATE` is the state of the whole: running while any of its execs runs, failed
if any of them failed, and succeeded only when every one of them did. That is
the question you came with, and the reason not to count rows yourself.

`DURATION` is how long you waited, not the sum of the parts: the execs run at
the same time.

Every node is asked. A session spans the nodes it reached, and the count of
part of one is not the session's count, so this command does not default to
the local node the way the others do.

```bash
om daemon session list                       # every session this cluster remembers
om daemon session list --state failed        # sessions with a failed exec in them
om daemon session list --origin scheduler
```

## Asking after one run

When a session failed, the exec listing says which part did:

```bash
$ om daemon exec list --session-id 1ed811b1-088d-4531-bd32-c4be35efe29e --node '*'
NODE    STATE   EXEC_ID    SESSION_ID  PATH  ORIGIN  BEGIN_AT  DURATION  COMMAND
dev2n1  failed  ff0c2d2e…  1ed811b1…   pod3  api     …         35ms      om pod3 instance start --rid nosuch
```

and `-o json` carries the exit code and the error:

```bash
$ om daemon exec list ff0c2d2e-e6a5-47ef-800b-304610179fc6 -o json
[
    {
        "node": "dev2n1",
        "state": "failed",
        "exec_id": "ff0c2d2e-e6a5-47ef-800b-304610179fc6",
        "session_id": "1ed811b1-088d-4531-bd32-c4be35efe29e",
        "path": "pod3",
        "origin": "api",
        "begin_at": "2026-09-11T12:31:23+02:00",
        "duration": "35ms",
        "exit_code": 1,
        "command": "/usr/bin/om pod3 instance start --rid nosuch",
        "error": "/usr/bin/om exit code 1 not in success codes: [0]"
    }
]
```

An exit code of `-1` means the process exited with no status: killed by a
signal, or never started at all. A running exec has no exit code, which is
what tells it apart from one that exited zero.

## What is running now

```bash
$ om daemon ps
PID      NODE    EXEC_ID                               PATH      RID  ORIGIN  DURATION  COMMAND
3871250  dev2n1  1a4a5266-49d8-4983-8613-073b1d40744c  test1          imon    18ms      om test1 instance status -r
3871248  dev2n1  be384858-f3d8-4fab-9fd4-f147427cb6d2  svc111         imon    20ms      om svc111 instance status -r
```

The pid is what `om daemon kill` signals, and only these pids may be signaled.

`ORIGIN` says what submitted the run: `api` for a command a client sent,
`imon` and `nmon` for one the monitors decided on, `scheduler` for one that
came due. `RID` is set on the scheduler's runs, naming the resource whose
schedule fired.

## Asking after an orchestration

```bash
$ om daemon orchestration list 934a42f9-b7eb-4d7e-a3ac-18347522f9f9
STATE      ORCHESTRATION_ID  PATH  GLOBAL_EXPECT  ACCEPTED_BY  BEGIN_AT
succeeded  934a42f9          pod3  placed@        dev2n1       2026-09-10T20:34:27+02:00
```

**Any node answers.** Every node of the object learns of the orchestration
from the instance monitors the daemon replicates, so it does not matter which
one you reach. That is what lets a client behind a floating address follow an
orchestration: the address may move to another node while the orchestration
runs, and a switch is precisely what moves it.

`ACCEPTED_BY` is the node that was asked for the orchestration, and is empty
on a node that only learned of it from the monitors. It is the one detail that
differs between nodes; the state, the object, the target and the start do not.

The execs an orchestration caused are found by its id:

```bash
om daemon exec list --orchestration-id 934a42f9-… --node '*'
```

## When the daemon has forgotten

What the daemon remembers is bounded, by age and by count, so a node that has
been running for months does not carry every command it ever ran. An
identifier it no longer holds says so:

```bash
$ om daemon exec list ff0c2d2e-e6a5-47ef-800b-304610179fc6
Error: exec ff0c2d2e-… is no longer known on dev2n1: it ended long enough ago
to have been dropped, or never ran there
```

That is deliberately not the same answer as an exec that is still running, and
not the same as one that never existed. A client polling for the end of an
action must be able to tell "not finished" from "I no longer know", which is
why forgetting is admitted rather than reported as absence.

What is running is never forgotten for the count. Only what has ended is
dropped.

> ➡️ See Also
> * [Action](apps.operate.action.md)
> * [Session, Execution and Orchestration Ids](internals.ids.md)
> * [Events](internals.daemon.events.md)
