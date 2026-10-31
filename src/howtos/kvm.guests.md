# KVM Guests

A `container.kvm` resource can describe a guest with a few keywords, instead of a `virtinst` command. `virt-install` and libvirt pick the qemu options for the node.

The node needs `virt-install`, `qemu-img` and systemd. A guest on an om network also needs `dnsmasq` and `nft`.

A user holding the `admin` role of a namespace can run a guest. See [What a Namespace Administrator May Set](#what-a-namespace-administrator-may-set).

## A Guest From a Cloud Image

```
[DEFAULT]
nodes = n1 n2

[volume#1]
size = 10g
format = false

[volume#2]
name = images
exclusive = false

[container#1]
type = kvm
vcpus = 2
memory = 2g
disk = volume#1
network = backend3 backend5
image = volume#2:/noble.qcow2
cloud_init = from ./cfg/vm1 key user-data
```

`volume#1` is the disk of the guest, and `volume#2` a volume holding images. The keywords are read at the provision only, the definition of the domain being the reference from then on, except `network`.

`image` is a file of a volume of the object, or an http(s) url, or a path of the node for root. A qcow2 or raw image with no backing file. It is written to the first disk.

`name` defaults to `<namespace>..<name>.container.1`.

The placement leader makes the guest. The other nodes receive its definition, and do not touch its disks, so a guest failing over needs replicated or shared storage.

## Upload a File to a Volume

A namespace administrator gives a guest an operating system through a volume. The webapp has a **Files** tab on the volumes.

The api issues a ticket, and the file is sent to the console port of the node, served by a process of its own, which survives a restart of the daemon:

<div class="tabs">
<div class="tab" data-title="API">

```
TICKET=$(curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/node/name/<node>/instance/path/<ns>/vol/images/file?name=noble.qcow2" | jq -r .ticket)

curl -X PUT --data-binary @noble.qcow2 "https://<node>:1216/?ticket=$TICKET"
```

</div>
</div>

The file appears complete or not at all. The transfer is answered `204`, `409` when the volume is not available on the node, and `507` when the file does not fit in the size of the volume.

A volume shared by several objects needs `exclusive = false` on all their `volume` resources.

## Download Images

The node policy on urls refuses every image url by default. Root says the sources the cluster trusts, for all the nodes:

<div class="tabs">
<div class="tab" data-title="CLI">

```
om cluster config update --set "node.image_urls=https://cloud-images.ubuntu.com/*"
```

</div>
</div>

`node.image_cidrs` allows the private range of a mirror of the site. Redirects stay refused, so a url must be the final one.

## Install From a CDROM

```
[container#1]
type = kvm
vcpus = 2
memory = 2g
disk = volume#1
network = backend3
cdrom = volume#2:/debian.iso
osinfo = debian12
```

The installer runs at the provision. Answer it on the [display](#display).

The guest stops at the first reboot of the installer, for it to boot its disk from then on. The object is then in `warn`, its volumes being up, which an orchestrated start refuses. Start the instance:

<div class="tabs">
<div class="tab" data-title="CLI">

```
om <path> instance start
```

</div>
<div class="tab" data-title="API">

```
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/node/name/<node>/instance/path/<ns>/svc/<name>/action/start"
```

</div>
</div>

An installer stopped before its end is not resumed: the definition no longer has the media, and the guest is to be provisioned again.

A lan network is refused with `cdrom`, an installed system having no cloud-init to tell it its address.

## Networks

`network` gives the guest an interface per om network. A network being of one family, a guest of both is on two.

* On a `routed_bridge` or a `bridge` network, a dnsmasq of the bridge hands the address out by mac at each boot. A start on another node gets an address of that node.
* On a `lan` network, the address follows the guest, which cloud-init tells it at its first boot, so a lan needs `image`.

The addresses are in the dns of the cluster, in the `ipaddr` and `ipaddrs` resource status info.

A filter keeps the guest to its mac and its addresses: it can not take the address of another, nor answer as a router or a dhcp server. The start is refused on a node with no `nft`, and the status warns of a running guest having lost its filter or its dnsmasq. The filter expects an eui-64 link-local address on an ipv6 network, which a cloud image is told to use. A guest installed by hand has to use one.

A guest on an om network can not be moved live. A lan on an interface that is neither a linux nor an openvswitch bridge is refused, and so is a lan for a flex object, whose instances would hold one mac and one address.

## Display

A guest the keywords describe has a vnc display on a unix socket, so the node opens no port for it. The webapp has a **Display** action on the `container.kvm` resources, to see the screen, use the keyboard and send Ctrl+Alt+Del.

The action opens a console session with a one-time ticket, for the `admin` of the namespace:

<div class="tabs">
<div class="tab" data-title="API">

```
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  "https://<node>:1215/api/node/name/<node>/instance/path/<ns>/svc/<name>/console?rid=container%231&graphics=true"
```

</div>
</div>

The binary messages of the websocket opened with the ticket are the bytes of the RFB protocol. A guest with a spice display says so: the browser speaks vnc.

## Caps and Claims

A guest runs in the process group of its resource, under the ones of its object and its namespace, so the `pg_*` keywords bound it. A cap changes live with `om <path> instance pg update`.

`vcpus` and `memory` are what the guest sees, whatever the caps:

* `pg_cpus` says the host cpus its threads run on.
* `pg_cpu_quota` caps all its threads together: `100%@2` for 2 vcpus at full speed.
* `pg_mem_limit` counts the memory it touched and what qemu takes, which is about 300m more for a guest of 1g. Over it, the guest is killed.

So a cap below the `memory` of a guest plus 384m is refused, and so are guests of an object not fitting its cap together.

In a namespace claiming the cpu or the memory, a guest with no cap is capped to what it is given, and counted for it: `100%@<vcpus>`, and `memory` plus 384m. A node with no systemd can not cap a guest, which is refused there.

## What a Namespace Administrator May Set

| Keyword | |
|---|---|
| `vcpus`, `memory`, `cloud_init`, `start_timeout`, `stop_timeout` | yes |
| `disk` | `volume#N` only |
| `image`, `cdrom` | a url, or `volume#N:/path` |
| `network` | network names, within the claims of the namespace |
| `osinfo` | an osinfo name |
| anything else, as `virtinst`, `virtinst_args`, `bridge`, `network_filter`, `name`, `rcmd` | root |

`encapnodes` with a kvm guest needs root too: the node reaches an encapsulated node by name, as root.
