# Install

## Debian

    # Select a os version and opensvc branch
    # --------------------------------------
    DISTRIB=bookworm
    DISTRIB=bullseye
    DISTRIB=buster
    BRANCH=dev
    BRANCH=prod
    
    # Import opensvc gpg signing keys
    # -------------------------------
    curl -s -o- https://packages.opensvc.com/gpg.public.key.asc | \
        sudo gpg --dearmor --output /etc/apt/trusted.gpg.d/opensvc-package-pub.gpg --yes

    #
    # Add the opensvc repository to apt sources
    # -----------------------------------------
    cat - <<EOF | sudo tee /etc/apt/sources.list.d/opensvc.list 
    deb https://packages.opensvc.com/apt/debian $BRANCH-opensvc-v3-$DISTRIB main
    deb-src https://packages.opensvc.com/apt/debian $BRANCH-opensvc-v3-$DISTRIB main
    EOF

    #
    # Install the opensvc server
    # --------------------------
    sudo apt update
    sudo apt install opensvc-server

    #
    # Enable the systemd unit and start the server
    # --------------------------------------------
    sudo systemctl enable --now opensvc-server

## Ubuntu

    # Select a os version and opensvc branch
    # --------------------------------------
    DISTRIB=focal
    DISTRIB=jammy
    DISTRIB=noble
    BRANCH=dev
    BRANCH=prod

    #
    # Import opensvc gpg signing keys
    # -------------------------------
    curl -s -o- https://packages.opensvc.com/gpg.public.key.asc | \
        sudo gpg --dearmor --output /etc/apt/trusted.gpg.d/opensvc-package-pub.gpg --yes

    #
    # Add the opensvc repository to apt sources
    # -----------------------------------------
    cat - <<EOF | sudo tee /etc/apt/sources.list.d/opensvc.list 
    deb https://packages.opensvc.com/apt/ubuntu $BRANCH-opensvc-v3-$DISTRIB main
    deb-src https://packages.opensvc.com/apt/ubuntu $BRANCH-opensvc-v3-$DISTRIB main
    EOF

    #
    # Install the opensvc server
    # --------------------------
    sudo apt update
    sudo apt install opensvc-server

    #
    # Enable the systemd unit and start the server
    # --------------------------------------------
    sudo systemctl enable --now opensvc-server

## Red Hat Enterprise Linux 7

    # Select a os version and opensvc branch
    # --------------------------------------
    DISTRIB=rhel7
    BRANCH=dev
    BRANCH=prod

    #
    # Add the opensvc repository to apt sources
    # -----------------------------------------
    cat << EOF >/etc/yum.repos.d/opensvc.repo
    [opensvc]
    name=OpenSVC Packages RHEL \$releasever - \$basearch
    baseurl=https://packages.opensvc.com/rpm/$BRANCH-opensvc-v3-$DISTRIB/\$basearch/
    enabled=1
    gpgcheck=0
    EOF

    #
    # Install the opensvc server
    # --------------------------
    sudo yum update
    sudo yum install opensvc-server

    #
    # Enable the systemd unit and start the server
    # --------------------------------------------
    sudo systemctl enable --now opensvc-server

## Red Hat Enterprise Linux 8+

    # Select a os version and opensvc branch
    # --------------------------------------
    DISTRIB=rhel8
    DISTRIB=rhel9
    BRANCH=dev
    BRANCH=prod

    #
    # Add the opensvc repository to apt sources
    # -----------------------------------------
    cat << EOF >/etc/yum.repos.d/opensvc.repo
    [opensvc]
    name=OpenSVC Packages RHEL \$releasever - \$basearch
    baseurl=https://packages.opensvc.com/rpm/$BRANCH-opensvc-v3-$DISTRIB/\$basearch/
    enabled=1
    gpgcheck=1
    gpgkey=https://packages.opensvc.com/gpg.public.key.asc
    EOF

    #
    # Install the opensvc server
    # --------------------------
    sudo dnf update
    sudo dnf install opensvc-server

    #
    # Enable the systemd unit and start the server
    # --------------------------------------------
    sudo systemctl enable --now opensvc-server

## SuSE Linux Enterprise Server

    # Select a os version and opensvc branch
    # --------------------------------------
    DISTRIB=sles15
    BRANCH=dev
    BRANCH=prod

    #
    # Add the opensvc repository to apt sources
    # -----------------------------------------
    cat << EOF >/etc/zypp/repos.d/opensvc.repo
    [opensvc]
    name=OpenSVC Packages SLES \$releasever - \$basearch
    baseurl=https://packages.opensvc.com/rpm/$BRANCH-opensvc-v3-$DISTRIB/\$basearch/
    enabled=1
    autorefresh=1
    gpgcheck=1
    gpgkey=https://packages.opensvc.com/gpg.public.key.asc
    EOF

    #
    # Install the opensvc server
    # --------------------------
    sudo zypper --gpg-auto-import-keys --non-interactive refresh
    sudo zypper install opensvc-server

    #
    # Enable the systemd unit and start the server
    # --------------------------------------------
    sudo systemctl enable --now opensvc-server

<div class="warning">

See Also:
* [Installed Files](internals.installed_files.md)

</div>

