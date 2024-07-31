# Upgrade

OpenSVC provides packages for all supported operating systems at https://repo.opensvc.com. Agents can be upgraded using one of the following methods, ordered by scalability:

* Download the required opensvc package to your hosts and use operating system specific local package management commands.
* Feed the opensvc packages into your existing per operating system package depots and use operating system specific network-aware package management commands.
* Mirror https://repo.opensvc.com on a corporate server and set up the opensvc agent to use this mirror as a package source.

This chapter describes the last method.

## Initialize a Mirror

A mirror can be set up using:

	wget -m -A '*.deb' -A '*.rpm' -A '*.exe' \
	     -A '*.pkg' -A '*.tbz' -A '*.depot' \
	     -A 'bundle' -A 'current' -A '*.txz' \
	     -A '*.p5p' \
	     https://repo.opensvc.com

The resulting file tree must organized as:

	repo.opensvc.com/
	|- cluster-manager/
	|- deb/
	|- depot/
	|- exe/
	|- sunos-pkg/
	|- rpms/
	|  |- current -> 2.0/current
	|  `- 2.0
	|     |- current -> opensvc-2.0-50.rpm
	|     |- opensvc-2.0-48.rpm
	|     |- opensvc-2.0-49.rpm
	|     `- opensvc-2.0-50.rpm
	`- tbz/

## Set Up Published Versions

The OpenSVC agent downloads the file pointed by the link named ``current`` under the package category supported by the operating system running the agent. For example a Solaris host executing ``om node updatepkg`` would try to download ``sunos-pkg/current``.

After the mirror initialization, you have to update the current links according to your own policies. Beware, the mirroring step may have installed current links pointing to the lastest available agent packages.

## Set Up Agents

The repository must be known to the agent. This set up is done with either the node.repo or the node.repopkg ``node.conf`` parameters.

{{#include kw}}`node.repo`

	This parameter allows to set up a URI pointing to a repository hosting both compliance gzipped tarballs in the compliance/ subdirectory and OpenSVC agent packages in the packages/ subdirectory.

{{#include kw}}`node.repopkg`

	This parameter allows to set up a URI pointing to a pure OpenSVC agent packages repository. If specified node.repopkg overrides node.repo.

Example:

	om node set --kw node.repopkg=https://repo.opensvc.com

## Upgrade Agents

The upgrade command is:

	om node updatepkg

This command is operating system agnostic.


