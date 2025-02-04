# Install

## Ubuntu

    #
    # Import opensvc gpg signing keys
    # -------------------------------
    curl -s -o- https://packages.opensvc.com/gpg.public.key.asc | \
        sudo gpg --dearmor --output /etc/apt/trusted.gpg.d/opensvc-package-pub.gpg --yes

    #
    # Add the opensvc repository to apt sources
    # -----------------------------------------
    cat - <<EOF | sudo tee /etc/apt/sources.list.d/opensvc.list 
    deb https://packages.opensvc.com/apt/ubuntu dev-opensvc-v3-noble main
    deb-src https://packages.opensvc.com/apt/ubuntu dev-opensvc-v3-noble main
    EOF

    #
    # Install the opensvc server
    # --------------------------
    sudo apt update
    sudo apt install opensvc-server
