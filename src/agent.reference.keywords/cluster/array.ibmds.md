# Driver `array.ibmds`

**Minimal configlet:**

	[array#1]
	type = ibmds
	hmc1 = hmc1.mycorp
	hmc2 = hmc2.mycorp
	username = root

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=ibmds" \
		--kw="hmc1=hmc1.mycorp" \
		--kw="hmc2=hmc2.mycorp" \
		--kw="username=root"

**Supported keywords:**

- comment
- hmc1
- hmc2
- schedule
- type
- username

## Keyword `comment`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

A free form text describing the role of the object, of the node, or of the
section it is set in.

The keyword is accepted in any section, so the DEFAULT section can document a
configuration as a whole, and a resource, pool, heartbeat, array or network
section can document itself.

The agent does not interpret the value.


## Keyword `hmc1`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	hmc1=hmc1.mycorp

**Description:**

The host name of the primary HMC.


## Keyword `hmc2`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	hmc2=hmc2.mycorp

**Description:**

The host name of the secondary HMC.


## Keyword `schedule`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  freenas, hds, eva, nexenta, vioserver, centera, symmetrix, emcvnx, netapp, hp3par, ibmds, ibmsvc, xtremio, dorado, hoc, truenas
	rbac:        This driver group requires the root grant.

**Description:**

The storage array driver name.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in.


