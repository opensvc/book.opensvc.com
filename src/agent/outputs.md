# Outputs

The `om` query commands display the data using a human-readable renderer by default. The `-o` command flag can be used to select another renderer.

```
$ om svc resource list
OBJECT      NODE    RID     TYPE       STATUS  IS_MONITORED  IS_DISABLED  IS_STANDBY  RESTART  RESTART_REMAINING  
stonith8    dev2n2  fs#1    fs.flag    down    false         false        false       0        0                  
testsched   dev2n2  fs#1    fs.flag    down    true          false        false       0        0                  
testsched   dev2n2  task#1  task.host  n/a     false         false        false       0        0                  
...
```

## Custom tables

**Custom column selection, with header**

```
$ om svc resource ls -o tab=OBJ:.meta.object,NODE:.meta.node,RID:.meta.rid,STATUS:.data.status.status
OBJ         NODE    RID     STATUS       
cva1        dev2n2  fs#1    down        
cva1        dev2n2  sync#1  n/a         
testflex    dev2n2  fs#1    down        
stonith236  dev2n2  fs#1    down        
...
```

**Single column selection, without header**

```
$ om svc resource ls -o tab=.meta.rid
fs#1
sync#1
fs#1
fs#1
...
```

## Machine-readable

```
$ om svc resource ls -o json
{
    "items": [
        {
            "data": {
                "config": {
                    "is_disabled": false,
                    "is_monitored": false,
                    "is_standby": false,
                    "restart": 0,
                    "restart_delay": 500000000
...
```

```
$ om svc resource ls -o yaml
items:
- data:
    config:
      is_disabled: false
      is_monitored: false
      is_standby: false
      restart: 0
      restart_delay: 500000000
    monitor:
      restart:

```

## Key-Value

```
$ om svc resource ls -o yaml
items[0].data.config.is_disabled = false
items[0].data.config.is_monitored = false
items[0].data.config.is_standby = false
items[0].data.config.restart = 0
items[0].data.monitor.restart.last_at = "0001-01-01T00:00:00Z"
items[0].data.monitor.restart.remaining = 0
items[0].data.status.label = "zfssnap 1d of foo"
items[0].data.status.provisioned.mtime = "2025-10-03T19:04:15.963080783+02:00"
items[0].data.status.provisioned.state = "n/a"
items[0].data.status.status = "n/a"
...
```

## Template

This output uses the golang template syntax, with the following extra functions:

| Function                  | Result        |
| :---                      | :---          |
| `drvName "ip.host"`       | `"host"`      |
| `drvGroup "ip.host"`      | `"ip"`        |
| `resName "container#db"`  | `"db"`        |
| `resGroup "container#db"` | `"container"` |
| `objKind "svc1"`          | `"svc"`       |
| `objName "svc1"`          | `"svc1"`      |
| `objNamespace "svc1"`     | `"root"`      |
| `hasPrefix "foo" "f"`     | `true`        |
| `hasSuffix "foo" "o"`     | `true`        |
| `contains [a b] a`        | `true`        |
| `reMatch "f.*" "foo"`     | `true`        |
| `fnMatch "f*"` "foo"`     | `true`        |

Example:
```
$ om svc resource ls -o template='{{range .}}{{if eq (resName .meta.rid) "hdoc"}}{{printf "%s@%s\n" .meta.object .meta.node}}{{end}}{{end}}'
test/svc/hdoc@dev2n2
test/svc/hdoc@dev2n3
test/svc/hdoc@dev2n1
```
