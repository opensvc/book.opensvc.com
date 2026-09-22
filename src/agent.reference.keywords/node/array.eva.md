# Driver `array.eva`

**Minimal configlet:**

	[array#1]
	type = eva
	manager = evamanager.mycorp
	password = from system/sec/array1 key password
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=eva" \
		--kw="manager=evamanager.mycorp" \
		--kw="password=from system/sec/array1 key password" \
		--kw="username=root"

**Supported keywords:**

- bin
- manager
- password
- username

## Keyword `bin`

	required:    false
	scopable:    false

**Example:**

	bin=/opt/sssu/bin/sssu

**Description:**

The EVA manager executable to use.


## Keyword `manager`

	required:    true
	scopable:    false

**Example:**

	manager=evamanager.mycorp

**Description:**

The EVA manager to connect.


## Keyword `password`

	required:    true
	scopable:    false

**Example:**

	password=from system/sec/array1 key password

**Description:**

The password to use to log in, expressed as a datastore reference.

Value format:
- New format: `from <namespace>/<kind>/<name> key <key name>`
- Legacy format: `<namespace>/<kind>/<name>` (uses default key "password")

Array passwords are usually stored in sec datastores like `system/sec/<array name>`.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in.


