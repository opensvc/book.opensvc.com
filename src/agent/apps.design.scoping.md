# Scoping

Most keywords in a service configuration support a scoping syntax, allowing each node agent to interpret the value differently.

## Syntax

A scoped keyword is written as:

```
<keyword>@<scope> = <value>
```

### Supported Scopes

- `<nodename>`: The hostname of the node where the keyword value is interpreted as `<value>`.
- `nodes`: The keyword value is interpreted as `<value>` on all service nodes.
- `drpnodes`: The keyword value is interpreted as `<value>` on all service DRP nodes.
- `encapnodes`: The keyword value is interpreted as `<value>` on all service encapsulated nodes.
- `flex_primary`: The keyword value is interpreted as `<value>` on the flex service primary node.
- `drp_flex_primary`: The keyword value is interpreted as `<value>` on the flex service disaster recovery primary node.

## Examples

### Use a Different FS Type on DRP Nodes

```ini
[DEFAULT]
nodes = n1 n2
drpnode = n3

[fs#1]
type = ext4
type@drpnodes = xfs
```

### Use a Different Nodes List at Encapsulated Level

```ini
[DEFAULT]
nodes = n1 n2
encapnodes = vm1
nodes@encapnodes = vm1
```

### Disable a Resource on a Node

```ini
[DEFAULT]
nodes = n1 n2
drpnodes = n3

[ip#backup]
disable@n3 = true
```

## Precedence

When a section has multiple definitions of the same keyword, the most specific takes precedence. If multiple definitions of the same rank are found, the last one takes precedence.

### Examples

```ini
[DEFAULT]
drpnodes = n3

[share#1]
disable = true
disable@drpnodes = false
```

This resource is enabled on `n3` because the generic `disable` is overridden by the more specific `disable@drpnodes` scoped definition.

```ini
[DEFAULT]
drpnodes = n3

[share#1]
disable = true
disable@drpnodes = false
disable@n3 = true
```

This resource is disabled on `n3` because the generic `disable` and `disable@drpnodes` are overridden by the more specific `disable@n3` scoped definition.

```ini
[DEFAULT]
drpnodes = n3

[share#1]
disable@n3 = true
disable@n3 = false
```

This resource is disabled on `n3` because the last of the two same-ranked scoped definitions takes precedence.
