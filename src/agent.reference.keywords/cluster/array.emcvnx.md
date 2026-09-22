# Driver `array.emcvnx`

**Minimal configlet:**

	[array#1]
	type = emcvnx
	spa = array1-a
	spb = array1-b

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=emcvnx" \
		--kw="spa=array1-a" \
		--kw="spb=array1-b"

**Supported keywords:**

- method
- password
- scope
- spa
- spb
- username

## Keyword `method`

	required:    false
	scopable:    false
	candidates:  secfile, credentials
	default:     secfile
	rbac:        This driver group requires the root grant.

**Example:**

	method=secfile

**Description:**

The authentication method to use.


## Keyword `password`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	password=system/sec/array1

**Description:**

The password to use to log in, expressed as a datastore reference.

Value format:
- New format: `from <namespace>/<kind>/<name> key <key name>`
- Legacy format: `<namespace>/<kind>/<name>` (uses default key "password")

Array passwords are usually stored in sec datastores like `system/sec/<array name>`.


## Keyword `scope`

	required:    false
	scopable:    false
	default:     0
	rbac:        This driver group requires the root grant.

**Example:**

	scope=1

**Description:**

The VNC scope to work in.


## Keyword `spa`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	spa=array1-a

**Description:**

The name of the Service Processor A.


## Keyword `spb`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	spb=array1-b

**Description:**

The name of the Service Processor B.


## Keyword `username`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in, if configured.


