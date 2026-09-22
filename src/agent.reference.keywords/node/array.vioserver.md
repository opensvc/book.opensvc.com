# Driver `array.vioserver`

**Minimal configlet:**

	[array#1]
	type = vioserver
	key = /path/to/key
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=vioserver" \
		--kw="key=/path/to/key" \
		--kw="username=root"

**Supported keywords:**

- key
- username

## Keyword `key`

	required:    true
	scopable:    false

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in.


