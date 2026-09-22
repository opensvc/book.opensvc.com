# Driver `switch.brocade`

**Minimal configlet:**

	[switch#1]
	type = brocade
	username = admin

**Minimal setup command:**

	om node set \
		--kw="type=brocade" \
		--kw="username=admin"

**Supported keywords:**

- key
- method
- name
- password
- username

## Keyword `key`

	required:    false
	scopable:    false

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in the switch.


## Keyword `method`

	required:    false
	scopable:    false
	candidates:  telnet, ssh
	default:     ssh

**Example:**

	method=ssh

**Description:**

The method to use to connect to the switch. 

* `ssh`
  Use `key` to provide a ssh key, or use the `sshpass` program.

* `telnet`
  Set `username` and `password` with this method.


## Keyword `name`

	required:    false
	scopable:    false

**Example:**

	name=sansw1.my.corp

**Description:**

The name connect to the switch (dns name or ip address).

If not set, fallback to the section name suffix.


## Keyword `password`

	required:    false
	scopable:    false

**Example:**

	password=mysec/password

**Description:**

The password to use to log in, expressed as a `sec` name (not path).

The secret must be in the `system` namespace and must have a `password` key.

Either `username` or `key` must be specified.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=admin

**Description:**

The username to use to log in the switch.


