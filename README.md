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

## Adding a project

The Projects page (`content/projects.md`, layout
`layouts/_default/projects.html`) lists every page whose front matter has
`project: true`, newest first, as a card with `image` (thumbnail, cropped to
4:3) and `summary`. To add one:

1. `content/<slug>.md` with `project: true`, `summary`, `image`,
   `url: "/projects/<slug>/"`, and a `date` (sets the card's order).
2. Images in `static/projects/<slug>/` (JPEG ≤ 1200 px wide; a cropped
   `thumb.jpg` for the card). Placeholders are fine to start
   (example: `static/projects/carvera-bed-scan/rig-placeholder.svg`).
3. A live demo goes in an iframe with the shortcode
   `{{< app-embed src="https://<name>.busboom.org/" title="…" height="640" >}}`
   (`layouts/shortcodes/app-embed.html`; adds an "open full screen" link).
   The demo itself runs as a container on docker1: see
   `../_infra/docker-do/AGENTS.md`, "Adding a project demo".
4. Preview with the local stack (`../localhost`, `just up`):
   http://eric.localhost:8000/projects/. After adding a new `layouts/`
   directory, restart the container (`docker restart localhost-eric-1`);
   hugo server doesn't pick up new layout directories.

Example: `content/carvera-bed-scan.md` (2026-11-05).
