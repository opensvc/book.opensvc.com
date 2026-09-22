# Driver `array.centera`

**Minimal configlet:**

	[array#1]
	type = centera
	java_bin = /opt/java/bin/java
	jcass_dir = /opt/centera/LIB
	password = from system/sec/array1 key password
	server = centera1
	username = root

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=centera" \
		--kw="java_bin=/opt/java/bin/java" \
		--kw="jcass_dir=/opt/centera/LIB" \
		--kw="password=from system/sec/array1 key password" \
		--kw="server=centera1" \
		--kw="username=root"

**Supported keywords:**

- java_bin
- jcass_dir
- password
- server
- username

## Keyword `java_bin`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	java_bin=/opt/java/bin/java

**Description:**

The path to the java executable to use to run the Centera management program.


## Keyword `jcass_dir`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	jcass_dir=/opt/centera/LIB

**Description:**

The path of the directory hosting the `JCASScript.jar`.


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


## Keyword `server`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	server=centera1

**Description:**

The storage server to connect.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=root

**Description:**

The username to use to log in.


