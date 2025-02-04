# Client UI

The `ox` program uses only the agent API and mirrors the `om` commandset, which makes it suitable for managing one or more clusters from a tiers linux box.

## Configure remotes

The remotes configuration is described in YAML format in the `~/.config/opensvc/contexts.yaml` file.

Example:

	users:
	  john:
	    password: xxx
	  mary:
	    password: xxx
	clusters:
	  dreamy-leopard:
	    server: https://dreamy-leopard.example.com:1215
	    insecure: true
	  bold-rat:
	    server: https://bold-rat:1215
	contexts:
	  john@dreamy-leopard:
	    user: john
	    cluster: dreamy-leopard
	  mary@bold-rat:
	    user: mary
	    cluster: bold-rat

## Terminal UI

At this point, executing `ox` with no argument launches the Terminal User Interface, and offers a context selector dialog.

## Commandline UI

    # Set a context
    # -------------
	$ export OSVC_CONTEXT=john@dreamy-leopard


    # Manage like om
    # --------------
	$ ox cluster get --kw cluster.name -o tab=data.value
	dreamy-leopard 

	$ ox node ls
	NAME                  AGENT STATE
	dreamy-leopard-node-1 3.0.0 idle
	dreamy-leopard-node-2 3.0.0 idle
	dreamy-leopard-node-3 3.0.0 idle

	$ ox svc ls
	OBJECT AVAIL OVERALL 
	svc2   down  down    
	svc1   down  down   


