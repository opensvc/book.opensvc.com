# Driver `array.nexenta`

**Minimal configlet:**

	[array#1]
	type = nexenta
	password = from system/sec/array1 key password
	username = root

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=nexenta" \
		--kw="password=from system/sec/array1 key password" \
		--kw="username=root"

**Supported keywords:**

- password
- port
- username

## Keyword `password`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	password=from system/sec/array1 key password

**Description:**

The password to use to log in, expressed as a datastore reference.

Value format:
- New format: `from <namespace>/<kind>/<name> key <key name>`
- Legacy format: `<namespace>/<kind>/<name>` (uses default key "password")

Array passwords are usually stored in sec datastores like `system/sec/<array name>`.


## Keyword `port`

	required:    false
	scopable:    false
	default:     2000
	convert:     int
	rbac:        This driver group requires the root grant.

**Example:**

	port=2000

**Description:**

The nexenta administration listener port.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in.


