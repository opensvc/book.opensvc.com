# Driver `pool.dorado`

**Minimal configlet:**

	[pool#1]
	type = dorado
	array = 
	diskgroup = 

**Minimal setup command:**

	om node set \
		--kw="type=dorado" \
		--kw="array=" \
		--kw="diskgroup="

**Supported keywords:**

- array
- compression
- dedup
- diskgroup
- fs_type
- hypermetrodomain

## Keyword `array`

	required:    true
	scopable:    true

**Description:**

The name of the array, known as `array#<name>` in the node or cluster
configuration.


## Keyword `compression`

	required:    false
	scopable:    false
	default:     false
	convert:     bool

**Description:**

Activate compression on created luns.


## Keyword `dedup`

	required:    false
	scopable:    false
	default:     false
	convert:     bool

**Description:**

Activate data deduplcation on created luns.


## Keyword `diskgroup`

	required:    true
	scopable:    false

**Description:**

The name of the array disk group to allocate volumes from.


## Keyword `fs_type`

	required:    false
	scopable:    false
	default:     xfs

**Description:**

The filesystem to format the pool devices with.


## Keyword `hypermetrodomain`

	required:    false
	scopable:    false

**Example:**

	hypermetrodomain=HyperMetroDomain_000

**Description:**

Create LUN as HyperMetro replicated pairs, using this domain.


