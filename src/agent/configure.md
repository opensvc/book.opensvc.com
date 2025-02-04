# Agent Configuration

## Concepts

The agent uses `ini` configuration files.

Considering a configuration like:

```ini
[env]
bar = 1
bar@n2 = 2
```

* `env` is a section
* `bar` is a option
* {{#include ../inc/kw}}`env.bar` is a keyword.
* {{#include ../inc/kw}}`env.bar=1` is a keyword operation.
* `1` is the {{#include ../inc/kw}}`env.bar` keyword value.
* `@n2` is a node scope for the keyword {{#include ../inc/kw}}`env.bar

## Policies

* If a keyword is present in both `node.conf` and `cluster.conf`, the value is evaluated from `node.conf`.
* A section only accepts known keywords, except the `[env]` and `[labels]` open sections.
* The most specific scoped value overrides the least specific values.

    With the above section in a `svc1` object configuration:

        # on n1:
        $ om svc1 eval --kw env.bar
        1

        # on n2:
        $ om svc1 eval --kw env.bar
        2

## Syntax validation

A syntax validation is executed before committing a change done using either a `set` or `edit` command.

    om cluster ed

    om cluster set --kw hb#test.type=unsupported

A direct configuration file change is not validated and can break the cluster.
In this case, you can validate post portem using:

    # verify the syntax of cluster.conf
    om cluster validate

    # verify the syntax of node.conf
    om node validate

    # verify the syntax of a svc configuration
    om svc1 validate



