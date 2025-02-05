# Node Configuration

## Set the Node Environment

	om cluster set --kw node.env=PRD

The {{#include ../inc/kw}}`node.env` setting is used to enforce the following policies:

*   Only services with {{#include ../inc/kw}}`env=PRD` are allowed to start on a node with {{#include ../inc/kw}}`node.env=PRD`
*   Only nodes with {{#include ../inc/kw}}`node.env=PRD` are allowed push data to a node with {{#include ../inc/kw}}`node.env=PRD`

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

The agent executes periodic tasks. All tasks have a default schedule, which you may want to change.

A schedule configuration can be applied using

    # Set a job schedule
	om node set --kw "brocade.schedule=02:00-04:00@120 sat,sun"

    # Disable a job schedule
	om node set --kw "brocade.schedule=@0"

Node schedules are defined in `/etc/opensvc/node.conf`, where the above command would produce this section:

<pre>
<code class="hljs">
<span style="color: #aa5500">[brocade]</span>
<span style="color: #767676">schedule </span>= 02:00-04:00@120 sat,sun
</code>
</pre>

The live scheduler configuration and states can be extracted with

<pre>
<code class="hljs">
$ om node print schedule
<span style="font-weight: bold">Action                </span>  <span style="font-weight: bold">Last Run           </span>  <span style="font-weight: bold">Config Parameter         </span>  <span style="font-weight: bold">Schedule Definition                               </span>  
|- <span style="color: #767676">auto_reboot        </span>  2017-09-30 16:59:19  reboot.schedule            16:00-17:00@1 sat:last,tue-mon:last * %2+1,feb-apr  
|- <span style="color: #767676">auto_rotate_root_pw</span>  -                    rotate_root_pw.schedule    -                                                   
|- <span style="color: #767676">checks             </span>  2017-10-01 17:43:29  checks.schedule            ["16:00-21:00@30 *:last", "! * wed", "*@1"]         
|- <span style="color: #767676">collect_stats      </span>  2017-10-01 17:42:29  stats_collection.schedule  @10                                                 
|- <span style="color: #767676">compliance_auto    </span>  2017-10-01 00:01:22  compliance.schedule        00:00-01:00@61                                      
|- <span style="color: #767676">dequeue_actions    </span>  2017-01-30 10:02:01  dequeue_actions.schedule   -                                                   
|- <span style="color: #767676">pushasset          </span>  2017-10-01 00:06:22  asset.schedule             00:00-06:00@361 mon-sun                             
|- <span style="color: #767676">pushbrocade        </span>  -                    brocade.schedule           -                                                   
|- <span style="color: #767676">pushcentera        </span>  -                    centera.schedule           -                                                   
|- <span style="color: #767676">pushdcs            </span>  -                    dcs.schedule               -                                                   
|- <span style="color: #767676">pushdisks          </span>  2017-10-01 00:03:22  disks.schedule             00:00-06:00@361 mon-sun                             
|- <span style="color: #767676">pushemcvnx         </span>  -                    emcvnx.schedule            -                                                   
|- <span style="color: #767676">pusheva            </span>  -                    eva.schedule               -                                                   
|- <span style="color: #767676">pushfreenas        </span>  -                    freenas.schedule           -                                                   
|- <span style="color: #767676">pushgcedisks       </span>  -                    gcedisks.schedule          -                                                   
|- <span style="color: #767676">pushhds            </span>  -                    hds.schedule               -                                                   
|- <span style="color: #767676">pushhp3par         </span>  -                    hp3par.schedule            -                                                   
|- <span style="color: #767676">pushibmds          </span>  -                    ibmds.schedule             -                                                   
|- <span style="color: #767676">pushibmsvc         </span>  -                    ibmsvc.schedule            -                                                   
|- <span style="color: #767676">pushnecism         </span>  -                    necism.schedule            -                                                   
|- <span style="color: #767676">pushnetapp         </span>  -                    netapp.schedule            -                                                   
|- <span style="color: #767676">pushnsr            </span>  -                    nsr.schedule               -                                                   
|- <span style="color: #767676">pushpatch          </span>  2017-10-01 00:16:01  patches.schedule           00:00-06:00@361 mon-sun                             
|- <span style="color: #767676">pushpkg            </span>  2017-10-01 00:12:01  packages.schedule          00:00-06:00@361 mon-sun                             
|- <span style="color: #767676">pushstats          </span>  2017-10-01 17:41:29  stats.schedule             ["00:00-23:59@10"]                                  
|- <span style="color: #767676">pushsym            </span>  -                    sym.schedule               -                                                   
|- <span style="color: #767676">pushvioserver      </span>  -                    vioserver.schedule         -                                                   
|- <span style="color: #767676">pushxtremio        </span>  -                    xtremio.schedule           -                                                   
`- <span style="color: #767676">sysreport          </span>  2017-10-01 00:25:02  sysreport.schedule         00:00-06:00@361 mon-sun                             
</code>
</pre>

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

### HP-UX

The python package provided by HP will output garbage on exec because it won't find terminfo at the expected places. To fix that, you have to export ``TERMINFO=/usr/share/lib/terminfo`` from ``/etc/profile``

The HP-UX base system does not provide tools to handle scsi persistent reservations. You have to install the scu tool if you want to activate this feature.

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

