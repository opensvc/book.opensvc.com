# Node Configuration

## Set the Node Environment

Set a default environment for all cluster nodes:

	sudo om cluster config update --set node.env=PRD

Optionally set an override in the node configuration:

	sudo om node config update --set node.env=DEV

{{#include ../inc/kw}}`node.env` marks a node production or not, which the
agent then enforces two ways:

* Only production services may start on a production node.
* Only production nodes may push data to a production node.

Supported {{#include ../inc/kw}}`node.env` values:

Env      | Behaves As | Description
---------|------------|---------------------
PRD      | PRD        | Production
PPRD     | PRD        | Pre Production
REC      | not PRD    | Prod-like testing
INT      | not PRD    | Integration
DEV      | not PRD    | Development
TST      | not PRD    | Testing (Default)
TMP      | not PRD    | Temporary
DRP      | not PRD    | Disaster recovery
FOR      | not PRD    | Training
PRA      | not PRD    | Disaster recovery
PRJ      | not PRD    | Project
STG      | not PRD    | Staging


## Set Node Jobs Schedules

The agent executes periodic tasks.

Display the scheduler configuration and states:

    $ sudo om node schedule list
    NODE      ACTION           LAST_RUN_AT                NEXT_RUN_AT           SCHEDULE      
    eggplant  pushasset        2025-01-20T01:31:17+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  
    eggplant  checks           2025-01-20T16:40:20+01:00  0001-01-01T00:00:00Z  @10m          
    eggplant  compliance_auto  2025-01-20T05:34:49+01:00  0001-01-01T00:00:00Z  02:00-06:00   
    eggplant  pushdisks        2025-01-20T02:42:29+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  
    eggplant  pushpkg          2025-01-20T00:16:38+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  
    eggplant  pushpatch        2025-01-20T01:50:37+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  
    eggplant  sysreport        2025-01-20T00:58:22+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  
    eggplant  dequeue_actions  2023-08-03T14:05:50+02:00  0001-01-01T00:00:00Z                
    eggplant  pushhcs          2025-01-15T18:00:59+01:00  0001-01-01T00:00:00Z  @1d           
    eggplant  pushswitch       0001-01-01T00:00:00Z       0001-01-01T00:00:00Z                

Schedule configuration:

<div class="tabs">
<div class="tab" data-title="CLI">

```bash
# Set a job schedule
om node config update --set "switch#sansw1.schedule=02:00-04:00@120 sat,sun"

# Disable a job schedule
om node config update --set "switch#sansw1.schedule=@0"
```

</div>
<div class="tab" data-title="API">

```bash
# Set a job schedule
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" -G \
  --data-urlencode 'set=switch#sansw1.schedule=02:00-04:00@120 sat,sun' \
  "https://<node>:1215/api/node/name/<node>/config"

# Disable a job schedule
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" -G \
  --data-urlencode 'set=switch#sansw1.schedule=@0' \
  "https://<node>:1215/api/node/name/<node>/config"
```

</div>
</div>

> The **API** tabs assume the `$TOKEN` and the listener endpoint set up in
> [Cluster API](configure.api.md). A node keyword is patched on the node that
> holds it, `PATCH …/node/name/<node>/config`, and a cluster keyword on any
> node, `PATCH /api/cluster/config`. Both take the same `set`, `unset` and
> `delete` operations as the matching `config update` command.

> ➡️ See Also
> * [Agent Scheduler](internals.daemon.scheduler.md)

## Register on a Collector

### Set a Collector Url

By default, the agent does not communicate with a collector.

To enable communications with a collector, the {{#include ../inc/kw}}`node.dbopensvc` node configuration parameter must be set. The simplest expression is:

<div class="tabs">
<div class="tab" data-title="CLI">

```bash
om cluster config update --set node.dbopensvc=collector.opensvc.com
```

</div>
<div class="tab" data-title="API">

```bash
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" -G \
  --data-urlencode 'set=node.dbopensvc=collector.opensvc.com' \
  "https://<node>:1215/api/cluster/config"
```

</div>
</div>

Here the protocol and path are omitted. In this case, the ``https`` protocol is selected, and the path set to a value matching the standard collector integration.

#### Advanced Url Formats

The following expressions are also supported:

	om cluster config update --set node.dbopensvc=https://collector.opensvc.com
	om cluster config update --set node.dbopensvc=https://collector.opensvc.com/feed/default/call/xmlrpc

The compliance framework uses a separate xmlrpc entrypoint. The {{#include ../inc/kw}}`node.dbcompliance` can be set to override the default, which is deduced from the {{#include ../inc/kw}}`node.dbopensvc` value.

	om cluster config update --set node.dbcompliance=https://collector.opensvc.com/init/compliance/call/xmlrpc

### Register the Node

The collector requires the nodes to provide an authentication token (shared secret) with each request. The token is forged by the collector and stored on the node in `/etc/opensvc/node.conf`. The token initialization is handled by the command:

	om node register --user my.self@my.com [--app MYAPP]

If ``--app`` is not specified the collector automatically chooses one the user is responsible of.

A successful register is followed by a node discovery, so the collector has detailed information about the node and can serve contextualized compliance rulesets up front. The discovery is also scheduled daily, and can be manually replayed with:

	om node push asset
	om node push pkg
	om node push patch
	om node checks


To disable collector communications, use:

	om cluster config update --unset node.dbopensvc
	om cluster config update --unset node.dbcompliance

Or if the settings were added to node.conf

	om node config update --unset node.dbopensvc
	om node config update --unset node.dbcompliance

### Inventory the SAN Switches

A couple of nodes of the infrastructure usually inventory the SAN switches, and
report their configuration to the collector, which indexes their ports, zones
and aliases. A switch is a `switch#<name>` section of the node or cluster
configuration:

```ini
[switch#sansw1]
type = brocade
name = sansw1.my.corp
username = admin
password = from system/sec/sansw1 key password
schedule = 02:00-04:00
```

The node logs in over ssh, with the private key `key` points to or with the
password of the secret, and runs `switchshow`, `nsshow` and `zoneshow`. The
telnet method v2 offered is refused. The key of the switch is trusted on the
first connection and recorded in the known hosts of root: a switch presenting
another key later is refused, until its old key is removed from
`/root/.ssh/known_hosts`.

```bash
# Push every switch, or the one named
om node push switch
om node push switch sansw1
```

The report goes to the switch feed of the collector. A collector that does not
serve it yet is sent the report the way v2 sent it.

### Track the System Configuration

The node reports its configuration files, and the output of a few commands,
to the collector, which keeps their history: what changed on a node, and when,
is at hand when a service misbehaves there. The first report sends every
tracked file, and the following ones what changed and what was deleted.

The agent configuration files are always tracked, the cluster secret masked.
The other files and commands are listed in files of the
`/etc/opensvc/sysreport.conf.d` directory, one item per line:

| Item | Tracks |
| :--- | :--- |
| `FILE <path>` | a file |
| `DIR <path>` | a directory, recursively |
| `GLOB <glob>` | the files and directories matching the pattern |
| `EXC <glob>` | none of the files matching the pattern, among the ones above |
| `CMD <argv>` | the output of a command, run without a shell |

```
# /etc/opensvc/sysreport.conf.d/system
FILE /etc/hosts
FILE /etc/fstab
DIR /etc/netplan
FILE /etc/multipath.conf
FILE /etc/lvm/lvm.conf
DIR /etc/sysctl.d
CMD ip -br addr
CMD lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINT
CMD multipath -ll
CMD systemctl list-unit-files --state=enabled --no-pager --no-legend
```

The files of the directory must belong to root and not be writable by others,
or they are ignored. Track no file holding a credential, as an `iscsid.conf`
with CHAP passwords can. Prefer the commands whose output only changes when
the configuration does: a counter or a timestamp in an output makes every
report a change.

The report runs on the `sysreport.schedule`, once a day by default. Every hour:

```bash
om cluster config update --set sysreport.schedule=@60m
```

Run a report, or a full one, which sends every tracked file for the collector
to replace what it holds of the node with:

<div class="tabs">
<div class="tab" data-title="CLI">

```bash
om node sysreport
om node sysreport --force
```

</div>
<div class="tab" data-title="API">

```bash
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/node/name/<node>/action/sysreport"

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/node/name/<node>/action/sysreport?force=true"
```

</div>
</div>

A report the collector refused is followed by a full one, so no change is
lost to a collector out of reach.

## Extra System Configurations

### Linux LVM2

OpenSVC controls volume group activation and deactivation. Old Linux distributions activate all visible volume groups at boot, some even re-activate them upon de-activation events. These mechanisms can be disabled using the following setup. It also provides another protection against unwanted volume group activation from a secondary cluster node.

This setup tells LVM2 commands to activate only the objects tagged with the hostname. Opensvc makes sure the tags are set on start and unset on stop. Opensvc also purges all tags before adding the one it needs to activate a volume group, so opensvc can satisfy a start request on a service uncleanly shut down.

#### /etc/lvm/lvm.conf

Add the following root-level configuration node:

	tags {
	    hosttags = 1
	    local {}
	}

And add the ``local`` tag to all local volume groups. For example:

	sudo vgchange --addtag local rootvg

Finally you need to rebuild the initrd/initramfs to prevent shared vg activation at boot.

#### /etc/lvm/lvm_$HOSTNAME.conf

	cat >/etc/lvm/lvm_$HOSTNAME.conf <<EOF
	activation {
	    volume_list = [ "@local", "@$HOSTNAME" ]
	    auto_activation_volume_list = [ "@local" ]
	}
	EOF

``volume_list`` says what may be activated at all: the local volume groups, and
the shared ones tagged with this node. ``auto_activation_volume_list`` says
what LVM activates on its own, at boot or when a device appears: the local
volume groups only. OpenSVC activates the shared volume groups itself, with a
direct activation this second list does not apply to.

Without it, a shared volume group still tagged with the node, as an unclean
stop leaves it, is activated at the next boot. The ``boot`` action of the
instance deactivates it once the agent starts, but until then it can be active
on this node and on the node the service failed over to. And the ``boot``
action runs only for the instances configured on the node: a node reinstalled
under the same name activates the volume groups left tagged by its previous
installation, and nothing deactivates them.

Both lists are supported by the LVM2 of RHEL 7 and later.

