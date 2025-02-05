# Scheduler

The OpenSVC agent includes a scheduler that manages jobs for both the node and each individual service.

## Basic Schedule Definition

The schedule constraints are defined by allowed time ranges and minimum execution interval. An example schedule definition is `00:00-02:00@121m`. In this example:

- **Time Range:** From midnight to 2:00 AM.
- **Interval:** 121 minutes.

Multiple schedule definitions can be specified using the syntax:

```json
["00:00-02:00@121", "12:00-14:00@121"]
```

Execution is permitted if any one of the defined constraints is satisfied.

## Policies

If an allowed time range is longer than the interval, multiple executions happen in the time range.

If not specified, the default interval is the duration of the time range, so there is only one execution of the job during the time range.

If not specified, the default time range is unrestricted. In this case a period must be specified.

If the definition begins with a `~`, the execution is delayed randomly in the allowed time range. The probability of execution increases linearly as time progresses within the allowed time range. For instance:

- At the beginning of the time range (`00:00` in `00:00-02:00`), the probability might be around 10%.
- Near the end of the time range (`01:50`), the probability reaches 100%.

This behavior ensures that the execution of job reporting information to the collector is spread across all nodes throughout the entire time range, leveling the load on the central collector. This approach prevents sudden spikes in load.

## Node Scheduler

    $ om node print schedule -o +KEY:data.key
    NODE  ACTION           LAST_RUN_AT                NEXT_RUN_AT           SCHEDULE      KEY                       
    n1    pushasset        2025-01-27T05:57:06+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  asset.schedule            
    n1    checks           2025-01-27T01:54:15+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  checks.schedule           
    n1    compliance_auto  2025-01-27T02:00:00+01:00  0001-01-01T00:00:00Z  02:00-06:00   compliance.schedule       
    n1    pushdisks        2025-01-27T04:56:30+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  disks.schedule            
    n1    pushpkg          2025-01-27T18:59:54+01:00  0001-01-01T00:00:00Z  @1m           packages.schedule         
    n1    pushpatch        2025-01-27T04:58:22+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  patches.schedule          
    n1    sysreport        0001-01-01T00:00:00Z       0001-01-01T00:00:00Z  ~00:00-06:00  sysreport.schedule        
    n1    dequeue_actions  0001-01-01T00:00:00Z       0001-01-01T00:00:00Z                dequeue_actions.schedule  
    n2    pushasset        2025-01-29T00:35:49+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  asset.schedule            
    n2    checks           2025-01-29T00:10:39+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  checks.schedule           
    n2    compliance_auto  2025-01-29T02:00:00+01:00  0001-01-01T00:00:00Z  02:00-06:00   compliance.schedule       
    n2    pushdisks        2025-01-29T05:14:15+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  disks.schedule            
    n2    pushpkg          2025-01-29T05:33:22+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  packages.schedule         
    n2    pushpatch        2025-01-29T00:42:55+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  patches.schedule          
    n2    sysreport        2025-01-29T03:08:18+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  sysreport.schedule        
    n2    dequeue_actions  0001-01-01T00:00:00Z       0001-01-01T00:00:00Z                dequeue_actions.schedule  
    n3    pushasset        2025-01-29T04:50:18+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  asset.schedule            
    n3    checks           2025-01-29T05:17:24+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  checks.schedule           
    n3    compliance_auto  2025-01-29T02:00:00+01:00  0001-01-01T00:00:00Z  02:00-06:00   compliance.schedule       
    n3    pushdisks        2025-01-29T05:10:43+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  disks.schedule            
    n3    pushpkg          2025-01-29T03:07:57+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  packages.schedule         
    n3    pushpatch        2025-01-29T05:36:14+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  patches.schedule          
    n3    sysreport        2025-01-29T00:34:02+01:00  0001-01-01T00:00:00Z  ~00:00-06:00  sysreport.schedule        
    n3    dequeue_actions  0001-01-01T00:00:00Z       0001-01-01T00:00:00Z                dequeue_actions.schedule  

The scheduled jobs can be configured in `/etc/opensvc/node.conf` with a configlet like:

	[<section>]
	<parameter> = <definition>

The `KEY` column in the above command output is formatted as:

	<section>.<parameter>

And the current definition, explicit or implicit, is visible in the `SCHEDULE` column. Empty means never scheduled.

The `om node` command action executed when the job fires is displayed in the `ACTION` column.

The node supports the following jobs:

* Node inventoring tasks : `pushasset` `pushpatch` `pushpkg` `pushdisks`
* Node performance metrics inventoring : `pushstats`
* Node performance metrics collection : `collect_stats`
* Node file content tracking task : `sysreport`
* Node configuration audit and/or remediation task : `compliance_auto`
* Health checking task : `checks`
* Scheduled node reboot task : `auto_reboot`
* Scheduled root password rotation task : `auto_rotate_root_pw`
* Execution of node actions queued by the collector : `dequeue_actions`
* SAN switches inventoring tasks : `pushbrocade`
* Storage arrays inventoring tasks : `pushcentera` `pushdcs` `pushemcvnx` `pusheva` `pushfreenas` `pushhds` `pushhp3par` `pushibmds` `pushibmsvc` `pushnecism` `pushnetapp` `pushsym` `pushvioserver`
* Backup servers saves index inventoring tasks : `pushnsr`


## Service Scheduler

    $ om tflex print schedule
    OBJECT  NODE    ACTION           KEY               LAST_RUN_AT                NEXT_RUN_AT                SCHEDULE    
    tflex   dev2n1  status           status_schedule   2025-01-30T11:54:55+01:00  2025-01-30T12:04:55+01:00  @10m        
    tflex   dev2n1  compliance_auto  comp_schedule     2025-01-27T00:09:18+01:00  0001-01-01T00:00:00Z       ~00:00-06:00
    tflex   dev2n1  run              task#1.schedule   2025-01-28T16:27:16+01:00  2025-01-30T16:27:16+01:00  @2d         
    tflex   dev2n1  run              task#2.schedule   2025-01-29T16:27:08+01:00  2025-01-30T16:27:08+01:00  @1d         
    tflex   dev2n1  run              task#3.schedule   2025-01-29T16:27:08+01:00  2025-01-30T16:27:08+01:00  @1d         
    tflex   dev2n1  push_resinfo     resinfo_schedule  2025-01-27T18:56:47+01:00  0001-01-01T00:00:00Z       @60m        

The scheduled jobs can be configured in the service configurations with a configlet like:

	[<section>]
	<parameter> = <definition>

The `KEY` column in the above command output is formatted as:

	<section>.<parameter>

And the current definition, explicit or implicit, is visible in the `SCHEDULE` column. Empty means never scheduled.

The `om <path>` command action executed when the job fires is displayed in the `ACTION` column.

The supported jobs are:

* Service configuration audit and/or remediation : `compliance_auto`
* Service resources kvstores inventoring : `push_env`
* Service status evaluation : `status`
* Service data sync : `sync_all`


## Advanced Schedule Definition

	[!] <timeranges> [<days> [<weeks> [<months>]]]
	
	!
	  desc: exclusion pattern. ommiting the ! implies an inclusion
	
	<timeranges> := <timerange>[,<timerange>]
	  <timerange> := <begin>:<end>@<interval>
	    <begin> <end> := <hour>:<minute>
	    <interval>
	      type: integer
	      unit: minutes
	
	<days> := <day>[-<day>][,<day>[-<day>]]
	  <day> := <day_of_week>[:<day_of_month>]
	    <day_of_week>
	       * iso week day format
	         type: integer between 0 and 6
	       * literal format
	         type: string in ("mon", "tue", "wed", "thu", "fri", "sat",
	               "sun", "monday", "tuesday", "wednesday", "thursday",
	               "friday", "saturday", "sunday")
	    <day_of_month> := <literal> | +<nth> | -<nth> | <nth>
	       <nth>
	         type: integer
	       <literal>
	         type: string in ("first", "1st", "second", "2nd", "third",
	               "3rd", "fourth", "4th", "fifth", "5th", "last")
	
	<weeks> := <week>[-<week>][,<week>[-<week>]]
	  <week>
	    type: integer between 1 and 53
	
	<months> := <monthrange>[,<monthrange>]
	  <monthrange> := <month>[-<month>] | <month_filter>
	    <month>
	      * numeric month format
	        type: integer between 1 and 12
	      * literal format
	        type: string in ("jan", "feb", "mar", "apr", "may", "jun",
	              "jul", "aug", "sep", "oct", "nov", "dec", "january",
	              "february", "march", "april", "may", "june", "july",
	              "august", "september", "october", "november",
	              "december")
	    <month_filter> := %<modulo>[+<shift>]
	      <modulo>
	        type: integer
	      <shift>
	        type: integer

## Examples

* Never schedule

  Either ` `, or `@0`

* Always schedule

  `*`

* Schedule every 60 minutes

  `@60`

* Schedule at first occasion after 9am

  `09:00`

* Schedule every hour between midnight and 6am, every day

  `00:00-06:00@60`

* Schedule once between midnight and 2am, every day

  `00:00-02:00`

* Schedule once between midnight and 2am every last day of month

  `00:00-02:00@121 *:last` or `00:00-02:00@121 *:-1`

* Schedule once between midnight and 2am every last friday of month

  `00:00-02:00@121 fri:last` or `00:00-02:00@121 fri:-1`

* Schedule once between midnight and 2am every week day

  `00:00-02:00@121 mon-fri`

* Schedule once between midnight and 2am every week day from january to february

  `00:00-02:00@121 mon-fri * jan-feb`

* Schedule once between midnight and 2am every odd day (1, 3, 5)

  `00:00-02:00@121 *:%2+1`

* Schedule once between midnight and 2am every monday of even weeks

  `00:00-02:00@121 mon %2`

