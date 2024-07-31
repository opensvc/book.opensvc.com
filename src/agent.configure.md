# Agent Configuration

## Configuration files

The agent configuration is the result of the merge of two `ini` configuration files:

* ``/etc/opensvc/cluster.conf``

  This file is replicated on all cluster nodes.

* ``/etc/opensvc/node.conf``

  This file is not replicated.

## Keywords

With a configuration like:

```ini
[foo]
bar=1
```

* `foo` is a section
* `bar` is a option
* {{#include kw}}`foo.bar` is a keyword.

## Policies

* If a keyword is present in both `node.conf` and `cluster.conf`, the value is evaluated from `node.conf`.
* In this book, all keyword mentions are prefixed with a {{#include kw}} icon.


