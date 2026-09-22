# Driver `array.dorado`

**Minimal configlet:**

	[array#1]
	type = dorado
	api = https://array.opensvc.com/api/v1.0
	password = from system/sec/array1 key password
	username = root

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=dorado" \
		--kw="api=https://array.opensvc.com/api/v1.0" \
		--kw="password=from system/sec/array1 key password" \
		--kw="username=root"

**Supported keywords:**

- api
- name
- password
- timeout
- username

## Keyword `api`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	api=https://array.opensvc.com/api/v1.0

**Description:**

The array rest api url.


## Keyword `name`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	name=a09

**Description:**

The name of the array. If not provided, fallback to the section name suffix.


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


## Keyword `timeout`

	required:    false
	scopable:    false
	default:     120s
	convert:     duration
	rbac:        This driver group requires the root grant.

**Example:**

	timeout=10s

**Description:**

The api request timeout.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in.


