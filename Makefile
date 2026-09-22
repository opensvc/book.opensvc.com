-include Makefile.inc

OM ?= om
SHELL := /bin/bash

# AGENT_VERSION is the agent the keyword reference documents.
#
# It is read from the binary that generates the reference, and written into
# the book, because a keyword reference that does not name its agent is a
# reference to whatever the person building the book happened to have
# installed. One book is built per agent release, and this is what that book
# says it documents.
AGENT_VERSION ?= $(shell $(OM) --version | awk '{print $$NF}')

KWDIR = src/agent.reference.keywords
KINDS = node cluster svc vol sec cfg usr

.ONESHELL: kw summary changes
.SILENT: kw summary changes

all: kw summary build

# kw generates the keyword reference of $(OM) into the tracked tree.
#
# It is generated at release time, with the binary of that release, and
# committed: the book then builds anywhere, with no agent installed, and a
# keyword change arrives in a pull request as a diff a reviewer can read.
kw:
	set -e
	rm -rf $(KWDIR)
	mkdir -p $(KWDIR)
	summary="SUMMARY.md.in"
	echo -e "# Agent Keywords Reference ($(AGENT_VERSION))\n" >$(KWDIR)/$${summary}
	head=$$(pwd)
	for kind in $(KINDS); do
		echo "- [$${kind}](agent.reference.keywords/$${kind}/SUMMARY.md)" >>$(KWDIR)/$${summary}
		mkdir -p $(KWDIR)/$${kind}
		printf "# $${kind}\n\n" >$(KWDIR)/$${kind}/SUMMARY.md
		cd $(KWDIR)/$${kind}
		${OM} $${kind} config doc | csplit -q -z - "/^# /" {*}
		for f in $$(echo xx*); do
			title=$$(head -n1 $$f|cut -d'`' -f2)
			mv $${f} $${title}.md
			echo "  - [$${title}](agent.reference.keywords/$${kind}/$${title}.md)" >>../$${summary}
			echo "- [$${title}]($${title}.md)" >>../$${kind}/SUMMARY.md
		done
		cd $$head
	done
	$(MAKE) index

# index writes the compact corpus the "what changed" page is computed from.
#
# The rendered reference says what a release has; the index is what two
# releases are compared through, which markdown is a poor carrier for. It
# holds what a diff has to talk about, and not the prose, which it fingerprints
# instead.
index:
	set -e
	tmp=$$(mktemp -d)
	for kind in $(KINDS); do
		${OM} $${kind} config doc -o json >$${tmp}/$${kind}.json
	done
	tools/kwindex.py --version "$(AGENT_VERSION)" --out $(KWDIR)/index.json $${tmp}/*.json
	rm -rf $${tmp}

# changes writes the page saying what the keywords of this release gained,
# lost and changed, from the index of the release before it.
#
# A binary can only document itself: a keyword removed in this release is
# simply absent from it, and no field of it could say it ever existed. The
# indexes of two releases say it between them.
changes:
	set -e
	if [ -z "$(PREVIOUS_INDEX)" ]; then
		echo "PREVIOUS_INDEX=<path to the index.json of the previous release> is required" >&2
		exit 1
	fi
	tools/kwdiff.py --from "$(PREVIOUS_INDEX)" --to $(KWDIR)/index.json --out $(KWDIR)/changes.md
	summary="$(KWDIR)/SUMMARY.md.in"
	grep -q "changes.md" $${summary} || sed -i "2a - [Changes in $(AGENT_VERSION)](agent.reference.keywords/changes.md)" $${summary}

summary:
	cat src/preamble/SUMMARY.md.in src/agent/SUMMARY.md.in src/howtos/SUMMARY.md.in src/appendix/SUMMARY.md.in src/agent.reference.keywords/SUMMARY.md.in > src/SUMMARY.md

build:
	mdbook build
