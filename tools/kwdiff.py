#!/usr/bin/env python3
"""Write the page saying what the keywords of a release gained, lost and
changed, from the indexes of two releases.

A binary can only document itself: a keyword removed in a release is simply
absent from it, and no field of it could say it ever existed. Two indexes say
it between them, which is why the answer is computed from the corpus of each
release rather than carried in the agent.

Usage:
    kwdiff.py --from index-3.0.json --to index-3.1.json --out changes.md
"""

import argparse
import json


def load(path):
    with open(path) as f:
        index = json.load(f)
    return index.get("version") or "?", index.get("keywords") or {}


def render_value(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) or "none"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def changed_fields(before, after):
    fields = sorted(set(before) | set(after))
    lines = []
    for field in fields:
        if field == "textSum":
            if before.get(field) != after.get(field):
                lines.append("description rewritten")
            continue
        if before.get(field) == after.get(field):
            continue
        lines.append("%s: %s -> %s" % (
            field,
            render_value(before.get(field, "")),
            render_value(after.get(field, "")),
        ))
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--from", dest="src", required=True)
    parser.add_argument("--to", dest="dst", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    from_version, before = load(args.src)
    to_version, after = load(args.dst)

    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = []
    for kid in sorted(set(before) & set(after)):
        lines = changed_fields(before[kid], after[kid])
        if lines:
            changed.append((kid, lines))

    out = []
    out.append("# Keyword changes in %s\n" % to_version)
    out.append("What the keywords of %s gained, lost and changed since %s.\n"
               % (to_version, from_version))
    out.append("A keyword is named by the kind it belongs to, then by its "
               "driver or section, then by its option.\n")

    out.append("\n## Added\n")
    if added:
        for kid in added:
            out.append("- `%s`" % kid)
    else:
        out.append("None.")

    out.append("\n## Removed\n")
    if removed:
        out.append("A configuration still naming one of these is reported by "
                   "`om <path> config validate`.\n")
        for kid in removed:
            out.append("- `%s`" % kid)
    else:
        out.append("None.")

    out.append("\n## Changed\n")
    if changed:
        for kid, lines in changed:
            out.append("- `%s`" % kid)
            for line in lines:
                out.append("  - %s" % line)
    else:
        out.append("None.")

    with open(args.out, "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
