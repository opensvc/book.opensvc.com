# Driver `array.ibmds`

**Minimal configlet:**

	[array#1]
	type = ibmds
	hmc1 = hmc1.mycorp
	hmc2 = hmc2.mycorp
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=ibmds" \
		--kw="hmc1=hmc1.mycorp" \
		--kw="hmc2=hmc2.mycorp" \
		--kw="username=root"

**Supported keywords:**

- hmc1
- hmc2
- username

## Keyword `hmc1`

	required:    true
	scopable:    false

**Example:**

	hmc1=hmc1.mycorp

**Description:**

The host name of the primary HMC.


## Keyword `hmc2`

	required:    true
	scopable:    false

**Example:**

	hmc2=hmc2.mycorp

**Description:**

The host name of the secondary HMC.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in.


