# Configs and Secrets

An application needs configuration files, certificates, credentials. Baking
them into the image ties the image to one environment. Leaving them on the
nodes means every node has to be prepared identically, by something that is
not the agent.

OpenSVC stores them in objects of their own, `cfg` for configuration and `sec`
for secrets, and installs them as files into a service's storage when it
starts. `sec` keys are encrypted with the cluster secret at rest.

## Put the data in a datastore

```bash
om myapp/cfg/app create
om myapp/cfg/app key add --name app.conf --from /tmp/app.conf
om myapp/cfg/app key list
```

Secrets work the same way, with `om myapp/sec/creds`.

## Install it where the application will look

The `install` keyword tells a resource to lay keys down inside the storage it
manages, as files:

```ini
[fs#1]
type = directory
path = /var/tmp/myapp
install = /etc/app.conf from ./cfg/app key app.conf

[app#1]
type = simple
start = /opt/myapp/bin/start
```

Starting the instance shows the order this happens in:

    INF myapp: fs#1: create directory /var/tmp/myapp
    INF myapp: fs#1: create directory /var/tmp/myapp/etc to host key app.conf
    INF myapp: fs#1: install key app.conf from myapp/cfg/app to /var/tmp/myapp/etc/app.conf with owner : perm -rw-r--r--
    INF myapp: app#1: run: /opt/myapp/bin/start

The file is in place before the application is launched. That is the point:
the resource holding the storage prepares the dataset, and only then do the
resources that consume it start.

`./cfg/app` is a [relative object path](apps.design.namespaces.md#relative-object-paths),
so the same configuration works in whatever namespace it is cloned to.

## Which resources can install

Any resource that manages a directory the agent can write into, in other words
any driver exposing a head, accepts `install`:

* `volume`
* `fs` (`fs.directory`, the host filesystem drivers, `fs.zfs`)

Resources start in driver group order, and both of those groups start before
`container` and `app`. So a volume or filesystem is always able to stage data
for the containers and applications that follow it, and never the other way
round.

## Beyond plain files

The `install` keyword takes more than a source and a destination:

```ini
install = /etc/app.conf from ./cfg/app key app.conf mode 0600 user app group app signal HUP:container#1
```

* `mode`, `user`, `group` set the installed file's permissions and ownership.
* `signal` sends a signal to another resource's processes when the content
  changes, so a running daemon reloads its configuration instead of being
  restarted.
* `template` treats the key as a Go template, evaluated against the `[env]`
  section, so one key serves several objects that differ only by a value.
* `source` seeds the key from a uri or a local file during provisioning, if it
  does not exist yet.
* `required` stops the install if that item fails, rather than continuing.

A trailing `/` on the destination, or omitting `from`, makes it a directory
rather than a file. A globbing pattern in `key` installs every matching key.

The full syntax is in the `install` keyword reference.

> ➡️ See Also
> * [Namespaces](apps.design.namespaces.md) for the relative path notation.
> * [Provisioning](apps.deploy.provisioning.md) for when `source` seeding runs.
