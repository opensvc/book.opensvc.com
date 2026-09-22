# Driver `array.vioserver`

**Minimal configlet:**

	[array#1]
	type = vioserver
	key = /path/to/key
	username = root

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=vioserver" \
		--kw="key=/path/to/key" \
		--kw="username=root"

**Supported keywords:**

- key
- username

## Keyword `key`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in.


