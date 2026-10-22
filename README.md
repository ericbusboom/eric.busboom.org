# eric.busboom.org

Static Hugo site converted from WordPress. It merges two blogs: eric.busboom.org
(blog 9, the personal blog) and ericbusboom.com (blog 12), whose home page is
now `/professional/` and whose posts are under `/2020/04/16/`.

`tools/fix_links.py` repaired links left by the conversion (old hosts, upload
paths); it is safe to rerun.

## Development
```bash
just dev    # or: hugo server --buildDrafts
just build  # or: hugo --minify --buildDrafts
```

## Deployment
Pushes to `main` trigger GitHub Actions → GitHub Pages.
