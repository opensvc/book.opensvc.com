# Driver `array.pure`

**Minimal configlet:**

	[array#1]
	type = pure
	api = https://array.opensvc.com/api/v1.0
	client_id = bd2c75d0-f0d5-11ee-a362-8b0f2d1b83d7
	issuer = opensvc
	key_id = df80ae3a-f0d5-11ee-94c9-b7c8d2f57c4f
	private_key = from system/sec/array1 key private_key
	username = opensvc

**Minimal setup command:**

	om test/ccfg/foo set \
		--kw="type=pure" \
		--kw="api=https://array.opensvc.com/api/v1.0" \
		--kw="client_id=bd2c75d0-f0d5-11ee-a362-8b0f2d1b83d7" \
		--kw="issuer=opensvc" \
		--kw="key_id=df80ae3a-f0d5-11ee-94c9-b7c8d2f57c4f" \
		--kw="private_key=from system/sec/array1 key private_key" \
		--kw="username=opensvc"

**Supported keywords:**

- api
- client_id
- comment
- insecure
- issuer
- key_id
- private_key
- schedule
- secret
- type
- username

## Keyword `api`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	api=https://array.opensvc.com/api/v1.0

**Description:**

The array rest api url.


## Keyword `client_id`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	client_id=bd2c75d0-f0d5-11ee-a362-8b0f2d1b83d7

**Description:**

The client id to use as the ``aud`` key in the payload of the login jwt.


## Keyword `comment`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

A free form text describing the role of the object, of the node, or of the
section it is set in.

The keyword is accepted in any section, so the DEFAULT section can document a
configuration as a whole, and a resource, pool, heartbeat, array or network
section can document itself.

The agent does not interpret the value.


## Keyword `insecure`

	required:    false
	scopable:    false
	default:     false
	convert:     bool
	rbac:        This driver group requires the root grant.

**Example:**

	insecure=true

**Description:**

Disable secure socket verification.


## Keyword `issuer`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	issuer=opensvc

**Description:**

The issuer to use as the ``iss`` key in the payload of the login jwt token.


## Keyword `key_id`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	key_id=df80ae3a-f0d5-11ee-94c9-b7c8d2f57c4f

**Description:**

The key id to use as the ``kid`` key in the header of the login jwt.


## Keyword `private_key`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	private_key=from system/sec/array1 key private_key

**Description:**

The private key the login jwt is signed with, expressed as a reference to a key
of a secret of the ``system`` namespace.

The long form names the key inside the secret::

    private_key = from system/sec/array1 key private_key

The short form names only the secret, and reads the key named ``private_key``
in it::

    private_key = system/sec/array1


## Keyword `schedule`

	required:    false
	scopable:    false
	rbac:        This driver group requires the root grant.

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `secret`

	required:    false
	scopable:    false
	deprecated:  since 3.0.0, replaced by private_key
	rbac:        This driver group requires the root grant.

**Example:**

	secret=system/sec/array1

**Description:**

The secret to use to store the information required to create the login jwt, expressed as a <path> reference to a secret. The secret must be in the ``system`` namespace and must have the following keys: ``private_key``.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  freenas, hds, eva, nexenta, vioserver, centera, symmetrix, emcvnx, netapp, hp3par, ibmds, ibmsvc, xtremio, dorado, hoc, truenas
	rbac:        This driver group requires the root grant.

**Description:**

The storage array driver name.


## Keyword `username`

	required:    true
	scopable:    false
	rbac:        This driver group requires the root grant.

**Example:**

	username=opensvc

**Description:**

The username to use as the ``sub`` key in the payload of the login jwt.


