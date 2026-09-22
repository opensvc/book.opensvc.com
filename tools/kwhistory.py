#!/usr/bin/env python3
"""Keep, and render, the timeline of the agent keywords.

The book documents the newest release. What a reader also needs is when a
keyword appeared, when it went away, and what moved between the release they
run and this one. Snapshotting the whole reference per release answers that
by duplicating a corpus which changes by a fraction of a percent each time.

The timeline answers it from the index of each release instead: one entry per
keyword, saying which release first had it, which release last had it, and
what changed in between. It is the only place a removed keyword can be
recorded at all, a release having nothing to say about what it does not have.

    kwhistory.py update --history history.json --index index.json
    kwhistory.py render --history history.json --dir <keyword reference dir>
"""

import argparse
import json
import os
import sys

# RENDERED are the properties a change is worth reporting. The others are
# carried in the index for completeness and compared all the same, but these
# are the ones named in the page.
LABELS = {
    "textSum": "description rewritten",
}


def load(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path) as f:
        return json.load(f)


def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=1, sort_keys=True)
        f.write("\n")


def render_value(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) or "none"
    if isinstance(value, bool):
        return "true" if value else "false"
    if value in (None, ""):
        return "unset"
    return str(value)


def diff(before, after):
    lines = []
    for field in sorted(set(before) | set(after)):
        if before.get(field) == after.get(field):
            continue
        if field in LABELS:
            lines.append(LABELS[field])
            continue
        lines.append("%s: %s -> %s" % (
            field, render_value(before.get(field)), render_value(after.get(field))))
    return lines


def update(args):
    history = load(args.history, {"releases": [], "keywords": {}})
    index = load(args.index)
    if index is None:
        print("no index at %s" % args.index, file=sys.stderr)
        return 1
    release = index["version"]
    keywords = index["keywords"]

    if release in history["releases"]:
        # A release is recorded once. Regenerating the same one is not a
        # change of anything.
        print("%s is already in the timeline" % release, file=sys.stderr)
        return 0

    previous = history["releases"][-1] if history["releases"] else None
    history["releases"].append(release)

    for kid, entry in keywords.items():
        known = history["keywords"].get(kid)
        if known is None:
            history["keywords"][kid] = {
                "since": release,
                "until": None,
                "properties": entry,
                "changes": {},
            }
            continue
        if known["until"] is not None:
            # It is back. A keyword that returns is worth seeing as it is:
            # gone after one release, and here again since another.
            known["changes"].setdefault(release, []).append(
                "back, gone after %s" % known["until"])
            known["until"] = None
        lines = diff(known["properties"], entry)
        if lines:
            known["changes"][release] = lines
        known["properties"] = entry

    for kid, known in history["keywords"].items():
        if kid in keywords or known["until"] is not None:
            continue
        # Absent from this release, and present in the one before: this is
        # where it went away, and the timeline is the only record of it.
        known["until"] = previous

    save(args.history, history)
    print("%s: %d keywords of %s, %d releases" % (
        args.history, len(keywords), release, len(history["releases"])), file=sys.stderr)
    return 0


def render(args):
    history = load(args.history)
    if history is None:
        print("no timeline at %s" % args.history, file=sys.stderr)
        return 1
    releases = history["releases"]
    keywords = history["keywords"]
    current = releases[-1] if releases else "?"

    # what each release added, removed and changed
    added, removed, changed = {}, {}, {}
    for kid, known in keywords.items():
        added.setdefault(known["since"], []).append(kid)
        if known["until"]:
            # It went away in the release that follows the last one that had
            # it, which is the next one in the timeline.
            i = releases.index(known["until"])
            gone = releases[i + 1] if i + 1 < len(releases) else None
            if gone:
                removed.setdefault(gone, []).append(kid)
        for release, lines in known["changes"].items():
            changed.setdefault(release, []).append((kid, lines))

    out = ["# Keyword changes\n"]
    out.append("What each release of the agent added, removed and changed in "
               "its keywords. The reference itself documents %s.\n" % current)
    shown = releases[-args.max_releases:] if args.max_releases else releases
    if len(shown) < len(releases):
        out.append("The %d most recent releases are listed. The whole "
                   "timeline is in `history.json`, beside this page.\n"
                   % len(shown))
    for release in reversed(shown):
        if release == releases[0]:
            # The release the timeline starts at has every keyword there is
            # as "added", which says nothing about that release.
            out.append("\n## %s\n" % release)
            out.append("Where this timeline starts: %d keywords, none of them "
                       "new." % len(added.get(release, [])))
            continue
        out.append("\n## %s\n" % release)
        a, r, c = sorted(added.get(release, [])), sorted(removed.get(release, [])), sorted(changed.get(release, []))
        if not (a or r or c):
            out.append("No keyword changed.")
            continue
        if a:
            out.append("\n### Added\n")
            for kid in a:
                out.append("- `%s`" % kid)
        if r:
            out.append("\n### Removed\n")
            for kid in r:
                out.append("- `%s`" % kid)
        if c:
            out.append("\n### Changed\n")
            for kid, lines in c:
                out.append("- `%s`" % kid)
                for line in lines:
                    out.append("  - %s" % line)
    with open(os.path.join(args.dir, "changes.md"), "w") as f:
        f.write("\n".join(out) + "\n")

    # the keywords no release can describe any more
    gone = sorted((known["until"], kid) for kid, known in keywords.items() if known["until"])
    out = ["# Removed keywords\n"]
    out.append("Keywords the agent no longer has. A release cannot document "
               "what it does not carry, so this is written from the timeline "
               "of the releases that had them.\n")
    if gone:
        out.append("A configuration still naming one of these is reported by "
                   "`om <path> config validate`.\n")
        out.append("| keyword | last release that had it |")
        out.append("|---|---|")
        for until, kid in gone:
            out.append("| `%s` | %s |" % (kid, until))
    else:
        out.append("None, since %s." % (releases[0] if releases else "?"))
    with open(os.path.join(args.dir, "removed.md"), "w") as f:
        f.write("\n".join(out) + "\n")

    print("%s/changes.md, %s/removed.md: %d releases, %d keywords ever seen, %d gone" % (
        args.dir, args.dir, len(releases), len(keywords), len(gone)), file=sys.stderr)
    return 0


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("update")
    p.add_argument("--history", required=True)
    p.add_argument("--index", required=True)
    p.set_defaults(func=update)

    p = sub.add_parser("render")
    p.add_argument("--history", required=True)
    p.add_argument("--dir", required=True)
    p.add_argument("--max-releases", type=int, default=20,
                   help="how many of the most recent releases the page lists")
    p.set_defaults(func=render)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
