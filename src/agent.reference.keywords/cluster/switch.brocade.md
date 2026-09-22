# Driver `switch.brocade`

**Minimal configlet:**

	[switch#1]
	type = brocade
	username = admin

**Minimal setup command:**

	om test/ccfg/foo set \
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
	rbac:        This driver group requires the root grant.

**Example:**

	key=/path/to/key

**Description:**

The path to the private key to use to log in the switch.


## Keyword `method`

	required:    false
	scopable:    false
	candidates:  telnet, ssh
	default:     ssh
	rbac:        This driver group requires the root grant.

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
	rbac:        This driver group requires the root grant.

**Example:**

	name=sansw1.my.corp

**Description:**

The name connect to the switch (dns name or ip address).

If not set, fallback to the section name suffix.


## Keyword `password`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	password=mysec/password

**Description:**

The password to use to log in, expressed as a `sec` name (not path).

The secret must be in the `system` namespace and must have a `password` key.

Either `username` or `key` must be specified.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=admin

**Description:**

The username to use to log in the switch.


