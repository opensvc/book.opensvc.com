# Driver `acme`

**Supported keywords:**

- comment
- directory
- renew_before
- webroot

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


## Keyword `directory`

	required:    false
	scopable:    false

**Example:**

	directory=letsencrypt

**Description:**

The ACME directory the certificate of the sec is issued by, renewed by
`om <path> certificate renew` or a `task.acme` resource. `letsencrypt` and
`letsencrypt-staging` name the directories of Let's Encrypt, and any other
value is the url of a directory.

The domains are the `cn` and the `alt_names` of the sec, and the account is
registered there, with its `email` as the contact when it has one.

A sec naming no directory has its certificate generated as `certificate
create` does, self-signed or signed by its `ca`, and renewed the same way when
due.

Use the staging directory of Let's Encrypt to try a setup out: its
certificates are not trusted, and its rate limits are far higher.


## Keyword `renew_before`

	required:    false
	scopable:    false
	default:     30d
	convert:     duration

**Example:**

	renew_before=20d

**Description:**

How long before its expiry the certificate is renewed: a renewal earlier
than that does nothing. A certificate naming other domains than the sec asks,
or self-signed, is renewed whatever its expiry.


## Keyword `webroot`

	required:    false
	scopable:    true
	rbac:        A host path the challenge token is written in requires the root grant.

**Example:**

	webroot=/srv/web-cfg.ns1.vol.cluster1/acme-challenges

**Description:**

The directory, on the node renewing the certificate, the http server of the
domains serves `/.well-known/acme-challenge/` from: the renewal writes the
http-01 challenge token there, under `.well-known/acme-challenge/`, and the
ACME directory reads it back through the domains.

It is usually a directory of a volume of the service publishing the domains,
the renewal running as a task of that service, where it runs.


