#!/usr/bin/env python3
"""Write the compact keyword corpus two releases are compared through.

The rendered reference says what a release has. This says the same thing in
the shape a diff can read: one entry per keyword, holding what a change is
worth reporting about, and a fingerprint of the prose rather than the prose
itself, which keeps the file small enough to carry one per release.

Usage:
    kwindex.py --version 3.1.0 --out index.json node.json svc.json ...

Each input is the output of "om <kind> config doc -o json". The kind is taken
from the file name.
"""

import argparse
import hashlib
import json
import os
import sys

# FIELDS are what a reader of the "what changed" page is told about. The text
# is not one of them: it is fingerprinted, so a reworded description shows as
# a change without the index carrying the prose twice. Neither is the set of
# kinds a keyword applies to: an entry is named by its kind, so a keyword of
# both svc and vol is two entries, and the set would say a second time what
# their names already say.
FIELDS = (
    "default",
    "defaultOption",
    "defaultText",
    "candidates",
    "converter",
    "scopable",
    "required",
    "provisioning",
    "inherit",
    "aliases",
    "depends",
    "types",
    "since",
    "deprecated",
    "replacedBy",
    "redactSecret",
    "recorded",
    "arithmetic",
    "minimal",
)


def keyword_id(kind, item):
    section = item.get("section") or ""
    types = item.get("types") or []
    # A driver keyword is named by its driver rather than by a section, the
    # section being whichever rid of the group carries it.
    if types:
        section = "%s.%s" % (section, types[0]) if section else types[0]
    return "%s/%s.%s" % (kind, section or "DEFAULT", item.get("option") or "")


# SETS are the properties whose order carries nothing: what they hold is a
# set, and an agent that came out of a map in a different order every run
# would otherwise show as a change in every release it was compared with.
SETS = ("candidates", "aliases", "types", "depends")


def entry(item):
    e = {}
    for field in FIELDS:
        value = item.get(field)
        if field in SETS and isinstance(value, list):
            # "<nil>" is what an agent that could not name a kind printed. It
            # describes a bug of the documentation rather than the keyword,
            # and a timeline is about the keywords.
            value = sorted(v for v in value if v != "<nil>")
        if value in (None, "", [], False):
            continue
        e[field] = value
    text = item.get("text") or ""
    if text:
        e["textSum"] = hashlib.sha256(text.encode()).hexdigest()[:16]
    return e


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("corpus", nargs="+")
    args = parser.parse_args()

    keywords = {}
    for path in args.corpus:
        kind = os.path.basename(path).rsplit(".", 1)[0]
        with open(path) as f:
            items = json.load(f)
        for item in items:
            keywords[keyword_id(kind, item)] = entry(item)

    index = {"version": args.version, "keywords": keywords}
    with open(args.out, "w") as f:
        # Sorted and indented: this file is committed, and what a release
        # changed has to read as a diff.
        json.dump(index, f, indent=1, sort_keys=True)
        f.write("\n")
    print("%s: %d keywords of %s" % (args.out, len(keywords), args.version), file=sys.stderr)


if __name__ == "__main__":
    main()
