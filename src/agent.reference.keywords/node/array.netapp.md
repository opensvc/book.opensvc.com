# Driver `array.netapp`

**Minimal configlet:**

	[array#1]
	type = netapp
	key = /path/to/key
	server = centera1
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=netapp" \
		--kw="key=/path/to/key" \
		--kw="server=centera1" \
		--kw="username=root"

**Supported keywords:**

- key
- server
- username

## Keyword `key`

	required:    true
	scopable:    false

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in.


## Keyword `server`

	required:    true
	scopable:    false

**Example:**

	server=centera1

**Description:**

The storage server to connect.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in.


