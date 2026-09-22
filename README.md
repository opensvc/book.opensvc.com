This documentation is built with

	mdbook build

Or tested in a local browser, with live updates with

	mdbook serve --open

The mdbook binary can be downloaded from https://github.com/rust-lang/mdBook/releases

## Keyword reference and versions

One book is built per agent release, deployed under its own path, and picked
from the version selector in the menu bar.

The keyword reference under `src/agent.reference.keywords` is tracked. It is
generated once, at release time, with the binary of that release, and read
from the repository by every later build: the book then builds anywhere with
no agent installed, and a keyword change arrives in a pull request as a diff a
reviewer can read.

Cutting the book of a release:

	# with the binary of the release being cut
	make kw OM=/path/to/om

	# what this release gained, lost and changed, from the index of the
	# previous one
	make changes PREVIOUS_INDEX=/path/to/previous/index.json

	# the path this book is deployed under, in book.toml
	site-url = "/v3.1/"

	make

`make kw` also writes `src/agent.reference.keywords/index.json`, the compact
corpus the next release computes its changes page from. Keep it: a binary can
only document itself, so what a release removed is only answerable by the
corpus of the release before it.

The version selector reads `/versions.json` at the site root, which lives
outside any book because a book cannot know about the releases that come after
it. The file in this repository is the template to deploy there:

	[
	  {"name": "v3.1", "path": "/v3.1/"},
	  {"name": "v3.0", "path": "/v3.0/"}
	]
