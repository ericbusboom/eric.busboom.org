#!/usr/bin/env python3
"""Fix links left over from the WordPress conversion of eric.busboom.org.

The site merges blog 9 (eric.busboom.org) and blog 12 (ericbusboom.com).

  - links to either old host become site-relative paths
  - /uploads/ links that point at a missing file are matched to the file in
    static/uploads/ (doubled /9/9/, missing blog id, thumbnail size suffix)
  - links to files that exist nowhere: link text kept, marked unavailable;
    images dropped

    python3 tools/fix_links.py [--dry-run]     (run from the site root)
"""
import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"

# Old URLs whose path changed in the Hugo site
MOVED = {
    "/projects/c02-powered-sledge-hammer/pneumatichammer-stripped/": "/projects/c02-powered-sledge-hammer/",
    "/posts/2009/110-life-before-child": "/2009/08/05/life-before-child/",
    "/": "/professional/",  # only for ericbusboom.com, see host_path()
}

HOSTS = re.compile(r"https?://(?:www\.)?(eric\.busboom\.org|ericbusboom\.com)(/[^\s)\"'<>\]]*)?")
ABSOLUTE_UPLOAD = re.compile(r"https?://[^/\s)>]+/wp-content/uploads/(?:sites/)?")
UPLOAD = re.compile(r"/uploads/[^\s)\"'<>#]+")
IMAGE = re.compile(r"!\[[^\]]*\]\(<?(/uploads/[^)>]+)>?\)")
LINK = re.compile(r"(?<!!)\[(?P<text>[^\]]*)\]\(<?(?P<url>/uploads/[^)>]+)>?\)")


def host_path(host, path):
    path = path or "/"
    if host == "ericbusboom.com" and path == "/":
        return MOVED["/"]
    if path != "/" and path in MOVED:
        return MOVED[path]
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    by_rest = defaultdict(set)  # "2009/07/x.png" -> {"/uploads/9/2009/07/x.png"}
    for f in (STATIC / "uploads").rglob("*"):
        if f.is_file():
            url = "/" + str(f.relative_to(STATIC))
            by_rest[re.sub(r"^/uploads/\d+/", "", url)].add(url)

    def fix(url):
        if (STATIC / url.lstrip("/")).is_file():
            return url
        # drop blog-id folders (/uploads/9/, /uploads/9/9/), keep YYYY/MM/
        rest = re.sub(r"^/uploads/((?!\d{4}/)\d+/)*", "", url)
        full = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", rest)  # thumbnail -> original
        for key in (rest, full):
            hits = by_rest.get(key, set())
            # blog 12 copied blog 9's media; prefer blog 9's copy
            hits = {h for h in hits if h.startswith("/uploads/9/")} or hits
            if len(hits) == 1:
                return next(iter(hits))
        return None

    stats = Counter()
    for md in sorted((ROOT / "content").rglob("*.md")):
        old = md.read_text()
        new = ABSOLUTE_UPLOAD.sub("/uploads/", old)

        def host(m):
            stats["old-host links"] += 1
            return host_path(m.group(1), m.group(2))

        new = HOSTS.sub(host, new)
        for bad, good in MOVED.items():
            if bad != "/":
                new = new.replace(f"(<{bad}>)", f"(<{good}>)").replace(f"({bad})", f"({good})")

        def image(m):
            if fix(m.group(1)) is None:
                stats["images removed"] += 1
                return ""
            return m.group(0)

        def link(m):
            if fix(m.group("url").split("#")[0]) is None:
                stats["links marked unavailable"] += 1
                return f"{m.group('text')} (no longer available)"
            return m.group(0)

        def remap(m):
            new_url = fix(m.group(0))
            if new_url and new_url != m.group(0):
                stats["upload links moved"] += 1
                return new_url
            return m.group(0)

        new = IMAGE.sub(image, new)
        new = LINK.sub(link, new)
        new = UPLOAD.sub(remap, new)
        if new != old and not args.dry_run:
            md.write_text(new)

    print(", ".join(f"{k}: {v}" for k, v in sorted(stats.items())) or "nothing to fix")


if __name__ == "__main__":
    main()
