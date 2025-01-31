# Install

## Ubuntu

    # Import opensvc gpg signing keys
    curl -o- https://packages.opensvc.com/gpg.public.key.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/opensvc-package-pub.gpg

    # Add the opensvc repository to apt sources
    cat - <<EOF > /etc/apt/sources.list.d/opensvc.list 
    deb https://packages.opensvc.com/apt/ubuntu dev-opensvc-v3-noble main
    deb-src https://packages.opensvc.com/apt/ubuntu dev-opensvc-v3-noble main

    # Install the opensvc server
    apt update
    apt install opensvc-server



<div class="warning">

See Also:

* [Installed files](agent.items.md)

</div>

