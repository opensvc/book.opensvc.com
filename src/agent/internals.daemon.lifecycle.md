# Agent Daemon Lifecycle

## Enable

    sudo systemctl enable --now opensvc-server

🛈 Newly installed daemons are not enabled by default.

## Boot

    om daemon start

* Executed on server boot.
* After reaching the multi-user target.

Side Effects:

* HA services in down state start a local instance.
* Standby resources of all services are started.

🛈 Administrators can prevent these side effects on boot setting the `osvc.freeze` option in the kernel boot command line.

## Shutdown

    om daemon shutdown

* Executed on server shutdown.
* The daemon drains all service instances running on the node.
* The peer nodes are free to takeover a HA service as soon as its local instance is drained.

## Stop

    om daemon stop

* Announces a maintenance period.
* The service instances running on the node are not stopped.
* Peer nodes wait for `node.maintenance_grace_period` before taking over, expecting the daemon to restart.

🛈 The mainteance period ends as soon as the daemon restarts.

## Restart

    om daemon restart

A restart is a simple stop-start sequence:

* Maintenance period is announced
* Peer nodes wait for the daemon to restart without taking over.

## Run

    om daemon run

* Runs a daemon in foreground
* Logs are printed on the console
* Stacks are printed on the console

🛈 Useful for debugging.

## Watchdog

* The daemon sends a periodic probe to systemd.
* If the daemon hangs, the probe flow stops, and systemd kill-restart the daemon.

🛈 The daemon event bus hangs are detected internally and cause the watchdog probe flow to stop.


