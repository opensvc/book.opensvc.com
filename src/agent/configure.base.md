# Node Configuration

## Set the Node Environment

	sudo om cluster set --kw node.env=PRD

The {{#include ../inc/kw}}`node.env` setting is used to enforce the following policies:

* Only production services are allowed to start on a production node.
* Only production nodes are allowed push data to a production node.

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

The setting is stored in `/etc/opensvc/cluster.conf`.

## Set Node Jobs Schedules

The agent executes periodic tasks.

Display the scheduler configuration and states:

    $ sudo om node print schedule 
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
    eggplant  pushbrocade      0001-01-01T00:00:00Z       0001-01-01T00:00:00Z                

Schedule configuration:

    # Set a job schedule
	om node set --kw "brocade.schedule=02:00-04:00@120 sat,sun"

    # Disable a job schedule
	om node set --kw "brocade.schedule=@0"

<div class="warning">

See Also:
* [Agent Scheduler](internals.daemon.scheduler.md)

</div>

## Register on a Collector

### Set a Collector Url

By default, the agent does not communicate with a collector.

To enable communications with a collector, the {{#include ../inc/kw}}`node.dbopensvc` node configuration parameter must be set. The simplest expression is:

	om cluster set --kw node.dbopensvc=collector.opensvc.com

Here the protocol and path are omitted. In this case, the ``https`` protocol is selected, and the path set to a value matching the standard collector integration.

#### Advanced Url Formats

The following expressions are also supported:

	om cluster set --kw node.dbopensvc=https://collector.opensvc.com
	om cluster set --kw node.dbopensvc=https://collector.opensvc.com/feed/default/call/xmlrpc

The compliance framework uses a separate xmlrpc entrypoint. The {{#include ../inc/kw}}`node.dbcompliance` can be set to override the default, which is deduced from the {{#include ../inc/kw}}`node.dbopensvc` value.

	om cluster set --kw node.dbcompliance=https://collector.opensvc.com/init/compliance/call/xmlrpc

### Register the Node

The collector requires the nodes to provide an authentication token (shared secret) with each request. The token is forged by the collector and stored on the node in `/etc/opensvc/node.conf`. The token initialization is handled by the command:

	om node register --user my.self@my.com [--app MYAPP]

If ``--app`` is not specified the collector automatically chooses one the user is responsible of.

A successful register is followed by a node discovery, so the collector has detailled information about the node and can serve contextualized compliance rulesets up front. The discovery is also scheduled daily, and can be manually replayed with:

	om node pushasset
	om node pushpkg
	om node pushpatch
	om node pushstats
	om node checks


To disable collector communications, use:

	om cluster unset --kw node.dbopensvc
	om cluster unset --kw node.dbcompliance

Or if the settings were added to node.conf

	om node unset --kw node.dbopensvc
	om node unset --kw node.dbcompliance

## Extra System Configurations

### Linux LVM2

OpenSVC controls volume group activation and desactivation. Old Linux distributions activate all visible volume groups at boot, some even re-activate them upon de-activation events. These mechanisms can be disabled using the following setup. It also provides another protection against unwanted volume group activation from a secondary cluster node.

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

	echo activation { volume_list = [\"@local\", \"@$HOSTNAME\"] } >/etc/lvm/lvm_$HOSTNAME.conf

