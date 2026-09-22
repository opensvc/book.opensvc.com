# Driver `pool.share`

**Minimal configlet:**

	[pool#1]
	type = share

**Minimal setup command:**

	om test/ccfg/foo set --kw="type=share"

**Supported keywords:**

- path

## Keyword `path`

	required:    false
	scopable:    false
	default:     {var}/pool/share
	rbac:        This driver group requires the root grant.

**Description:**

The fullpath of the shared directory hosting the pool volumes directories or loop files.


