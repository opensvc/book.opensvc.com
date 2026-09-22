# Driver `array.hoc`

**Minimal configlet:**

	[array#1]
	type = hoc
	api = https://array.opensvc.com/api/v1.0
	model = VSP G350
	password = from system/sec/array1 key password
	username = root

**Minimal setup command:**

	om node set \
		--kw="type=hoc" \
		--kw="api=https://array.opensvc.com/api/v1.0" \
		--kw="model=VSP G350" \
		--kw="password=from system/sec/array1 key password" \
		--kw="username=root"

**Supported keywords:**

- api
- comment
- delay
- http_proxy
- https_proxy
- insecure
- model
- name
- password
- retry
- schedule
- timeout
- type
- username
- wwid_prefix

## Keyword `api`

	required:    true
	scopable:    false

**Example:**

	api=https://array.opensvc.com/api/v1.0

**Description:**

The array rest api url.


## Keyword `comment`

	required:    false
	scopable:    false

**Description:**

A free form text describing the role of the object, of the node, or of the
section it is set in.

The keyword is accepted in any section, so the DEFAULT section can document a
configuration as a whole, and a resource, pool, heartbeat, array or network
section can document itself.

The agent does not interpret the value.


## Keyword `delay`

	required:    false
	scopable:    false
	default:     10s
	convert:     duration

**Description:**

The delay between request attempts on retryable errors.


## Keyword `http_proxy`

	required:    false
	scopable:    false

**Example:**

	http_proxy=http://proxy.mycorp:3158

**Description:**

The proxy server to use for http requests to the api.


## Keyword `https_proxy`

	required:    false
	scopable:    false

**Example:**

	https_proxy=https://proxy.mycorp:3158

**Description:**

The proxy server to use for https requests to the api.


## Keyword `insecure`

	required:    false
	scopable:    false
	default:     false
	convert:     bool

**Example:**

	insecure=true

**Description:**

Disable secure socket verification.


## Keyword `model`

	required:    true
	scopable:    false
	candidates:  VSP G370, VSP G700, VSP G900, VSP F370, VSP F700, VSP F900, VSP G350, VSP F350, VSP G800, VSP F800, VSP G400, VSP G600, VSP F400, VSP F600, VSP G200, VSP G1000, VSP G1500, VSP F1500, Virtual Storage Platform, HUS VM

**Example:**

	model=VSP G350

**Description:**

The array model.


## Keyword `name`

	required:    false
	scopable:    false

**Example:**

	name=a09

**Description:**

The name of the array. If not provided, fallback to the section name suffix.


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


## Keyword `retry`

	required:    false
	scopable:    false
	default:     30
	convert:     int

**Description:**

The number of request attempts on retryable errors.


## Keyword `schedule`

	required:    false
	scopable:    false

**Description:**

Schedule parameter for the `pusharray` node action.

See `usr/share/doc/schedule` for the schedule syntax.


## Keyword `timeout`

	required:    false
	scopable:    false
	default:     120s
	convert:     duration

**Example:**

	timeout=10s

**Description:**

The api request timeout.


## Keyword `type`

	required:    true
	scopable:    false
	candidates:  freenas, hds, eva, nexenta, vioserver, centera, symmetrix, emcvnx, netapp, hp3par, ibmds, ibmsvc, xtremio, dorado, hoc, truenas

**Description:**

The storage array driver name.


## Keyword `username`

	required:    true
	scopable:    false

**Example:**

	username=root

**Description:**

The username to use to log in.


## Keyword `wwid_prefix`

	required:    false
	scopable:    false

**Description:**

Hitachi APIs do not report the disks NAA wwids, but it can be forged from a array-specifix prefix concatenated with the LDev id. This keyword allow the cluster admin to define this prefix.
Do not include the NAA Type digit prefix (define 62400000ec12ac73541d instead of 362400000ec12ac73541d).


