## Resource Info

Each resource of an instance publishes a set of key-values describing what it
is made of: the device a disk resource activates, the mount point a fs
resource uses, the command an app resource runs. Together they form a
per-resource inventory, refreshed on a schedule and centralized on the
collector.

This is deliberately not the resource *status*. Status answers "is it up
right now", changes constantly, and is evaluated every 10 minutes by default.
Resource info answers "what is it made of", changes rarely, and is refreshed
hourly. Keeping the two apart lets each have the schedule it deserves.

### Read

```bash
om myapp instance info
```

    OBJECT  NODE    RID     KEY            VALUE
    myapp   dev2n1  disk#1  driver         disk.vg
    myapp   dev2n1  disk#1  name           datavg
    myapp   dev2n1  app#1   driver         app.simple
    myapp   dev2n1  app#1   start          /opt/myapp/bin/start

This reports a cache. It does not run anything on the resources, so it is
cheap and safe to call as often as needed.

Every resource contributes a common set of keys, `driver`, `standby`,
`optional`, `disable`, `monitor`, `shared`, `encap`, and the restart policy
when it has one. Each driver adds its own on top.

The command is also mounted on every resource group, so a group name narrows
the report, and a trailing pattern narrows it further:

```bash
om myapp disk info          # only the disk resources
om myapp disk info 1        # only disk#1
om myapp resource info      # same as instance info
```

### Refresh

```bash
om myapp instance info --refresh
```

This walks the resources, asks each one for its key-values, and rewrites the
cache. It is what the scheduler runs hourly, driven by the `info_schedule`
keyword:

```ini
[DEFAULT]
info_schedule = @60m
```

Refreshing a subset merges into the cache rather than replacing it, so
`om myapp disk info --refresh 1` leaves the key-values of the other resources
alone. A full refresh rewrites everything, and drops the resources the
configuration no longer declares.

### Centralization

The refresh does not talk to the collector. It only writes the local cache and
signals the cluster.

One node, the collector speaker, subscribes to that signal, fetches the
key-values from whichever node refreshed them, and reports them to the
collector on its own throttled schedule. A cluster therefore feeds the
collector through a single node, and a burst of refreshes across many
instances is coalesced instead of turning into a burst of collector requests.

The practical consequences:

* The reporting is deferred. A refresh shows up on the collector within
  minutes, not instantly.
* An instance whose node is unreachable when the speaker tries to fetch it is
  retried later, not lost.
* Nothing is reported for an instance that never refreshed successfully.

### Plug your own key-values

An `app` resource can feed arbitrary key-values into this subsystem with the
`info` keyword, which makes the inventory extensible with data the agent has
no way to know about: an application version, a schema revision, a licence
expiry, a tenant name.

Point it at a command printing one `key:value` per line:

```ini
[app#1]
type = simple
start = /opt/myapp/bin/start
info = /opt/myapp/bin/inventory
```

With `/opt/myapp/bin/inventory` printing:

    version:4.2.1
    schema:19
    tenant:acme

Those three keys are then reported next to the standard ones, and land on the
collector like the rest.

Set `info = true` instead to call the resource `script` with the `info`
argument, which keeps a single executable for the start, stop, check and info
entry points:

```ini
[app#1]
type = simple
script = /opt/myapp/bin/app.sh
start = true
info = true
```

> **Writing an info command**
>
> * Lines that are not exactly `key:value` are silently dropped. A value
>   containing a `:`, like a url or a timestamp, has more than one separator
>   and is dropped with them. Encode it, or split it across keys.
> * The command must exit 0. A failure aborts the refresh of the whole
>   instance, which then reports no key-value at all, not even for the other
>   resources.
> * Keep it fast and side-effect free. It runs on a schedule, and is bounded
>   by `info_timeout`.
