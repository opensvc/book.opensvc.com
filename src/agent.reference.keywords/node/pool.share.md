# Driver `pool.share`

**Minimal configlet:**

	[pool#1]
	type = share

**Minimal setup command:**

	om node set --kw="type=share"

**Supported keywords:**

- path

## Keyword `path`

	required:    false
	scopable:    false
	default:     {var}/pool/share

**Description:**

The fullpath of the shared directory hosting the pool volumes directories or loop files.


