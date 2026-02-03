-include Makefile.inc

OM ?= om
SHELL := /bin/bash

.ONESHELL: kw summary
.SILENT: kw summary

all: kw summary build

kw:
	d="agent.reference.keywords"
	sd="src/agent.reference.keywords"
	rm -rf $$d
	mkdir $$d
	summary="SUMMARY.md.in"
	echo -e "# Agent Keywords Reference\n" >$${sd}/$${summary}
	head=$$(pwd)
	for kind in node cluster svc vol sec cfg usr; do
		echo "- [$${kind}]($${d}/$${kind}/SUMMARY.md)" >>$${sd}/$${summary}
		mkdir -p $${sd}/$${kind}
		printf "# $${kind}\n\n" >$${sd}/$${kind}/SUMMARY.md
		cd $${sd}/$${kind}
		sudo ${OM} $${kind} config doc | csplit -q -z - "/^# /" {*}
		for f in $$(echo xx*); do
	       		title=$$(head -n1 $$f|cut -c3-)
			mv $${f} $${title}.md
			echo "  - [$${title}](agent.reference.keywords/$${kind}/$${title}.md)" >>../$${summary}
			echo "- [$${title}]($${title}.md)" >>../$${kind}/SUMMARY.md
		done
		cd $$head
	done

summary:
	cat src/preamble/SUMMARY.md.in src/agent/SUMMARY.md.in src/howtos/SUMMARY.md.in src/agent.reference.keywords/SUMMARY.md.in > src/SUMMARY.md

build:
	mdbook build
