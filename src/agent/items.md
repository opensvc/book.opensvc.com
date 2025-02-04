# Installed Items

## Executables

The `/usr/bin/om` executable, installed by the `opensvc-server` package, contains:

* The Cluster Resource Manager
* The Cluster Monitor and API daemon
* The local management commandline interface

The `/usr/bin/ox` executable, installed by the `opensvc-client` package, contains:

* The remote management commandline interface

## Directories

The agent file organization follows the Filesystem Hierarchy Standard guidelines on Unix.

The package installs the following directory tree:

| Git Workspace                    | Unix Packages                   | Reference in docs |
|----------------------------------|---------------------------------|-------------------|
| `<OSVCROOT>/`                    |                                 | `<OSVCROOT>`      |
| `<OSVCROOT>/etc`                 | `/etc/opensvc`                  | `<OSVCETC>`       |
| `<OSVCROOT>/usr/share/doc`       | `/usr/share/doc/opensvc`        | `<OSVCDOC>`       |
| `<OSVCROOT>/tmp`                 | `/var/tmp/opensvc`              | `<OSVCTMP>`       |
| `<OSVCROOT>/var`                 | `/var/lib/opensvc`              | `<OSVCVAR>`       |
| `<OSVCROOT>/log`                 | `/var/log/opensvc`              | `<OSVCLOG>`       |

