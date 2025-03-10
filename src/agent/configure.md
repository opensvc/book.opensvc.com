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
* `@n2` is a node [scope](./apps.design.scoping.md) for the keyword {{#include ../inc/kw}}`env.bar`

## Policies

* If a keyword appears in both `node.conf` and `cluster.conf`, the value from node.conf takes precedence.
* Sections only accept recognized keywords, with the exception of the `[env]` and `[labels]` sections, which are open.
* More specific scoped values override less specific ones.

    With the above section in a `svc1` object configuration:

        # on n1:
        $ om svc1 eval --kw env.bar
        1

        # on n2:
        $ om svc1 eval --kw env.bar
        2

## Syntax validation

A syntax check is performed before finalizing any modifications made with either the set or edit commands.

    om cluster ed

    om cluster set --kw hb#test.type=unsupported

A direct modification to the configuration file is not validated and may disrupt the cluster. In such cases, you can perform a post-hoc validation using:

    # verify the syntax of cluster.conf
    om cluster validate

    # verify the syntax of node.conf
    om node validate

    # verify the syntax of a svc configuration
    om svc1 validate



