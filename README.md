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

## Home page and blog

The home page is the Projects page: `layouts/index.html` renders
`content/projects/_index.md` and the project cards
(`layouts/partials/project-list.html`, also used by `/projects/`). The blog
post list is at `/blogs/` (`content/blogs/_index.md`, layout
`layouts/_default/blog.html`, 10 per page); `/archives/`, `/posts/` and the
old home pagination `/page/N/` redirect there (2026-11-05). When the post
count passes 60, add `/page/7/` etc. only if old links need it.

## Pages are bundles

Each standalone page is a directory holding its Markdown (`index.md`) and
every image or file it uses, referenced by bare filename
(`![](relief.jpg)`):

- `content/about/`, `content/professional/`
- `content/projects/_index.md`: the Projects page itself
- `content/projects/<slug>/`: one directory per project, served at
  `/projects/<slug>/`

Blog posts are still single files in `content/<yyyy>/<mm>/<dd>/` with images
in `static/uploads/` (from the WordPress conversion). Reorganized 2026-11-05;
`/shop-redesign/` and `/summer-robot-program/` redirect to their new
`/projects/` addresses.

## Adding a project

The Projects page (layout `layouts/_default/projects.html`) lists every page
whose front matter has `project: true`, newest first, as a card with `image`
(thumbnail, cropped to 4:3) and `summary`. To add one:

1. `content/projects/<slug>/index.md` with `project: true`, `summary`,
   `image` (a filename in the same directory, e.g. `thumb.jpg`) and a `date`
   (sets the card's order).
2. Put the images in that directory (JPEG ≤ 1200 px wide; a cropped
   `thumb.jpg` for the card). Placeholders are fine to start
   (example: `content/projects/carvera-bed-scan/rig-placeholder.svg`).
3. A live demo goes in an iframe with the shortcode
   `{{< app-embed src="https://<name>.busboom.org/" title="…" height="640" >}}`
   (`layouts/shortcodes/app-embed.html`; adds an "open full screen" link).
   The demo itself runs as a container on docker1: see
   `../_infra/docker-do/AGENTS.md`, "Adding a project demo".
4. Preview with the local stack (`../localhost`, `just up`):
   http://eric.localhost:8000/projects/. After adding a new `layouts/`
   directory or changing `hugo.toml`, restart the container
   (`docker restart localhost-eric-1`); hugo server doesn't pick those up.

Example: `content/projects/carvera-bed-scan/` (2026-11-05).
