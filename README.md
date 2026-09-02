# takuhii.github.io
Personal GitHub Pages site for [takuhii](https://github.com/takuhii), hosted at
**<https://takuhii.github.io/>**.

This repository is a static site (plain HTML and CSS, no build step) deployed
automatically by GitHub Pages from the `main` branch. It hosts the
**Susy-Sass** documentation pages — Susy-Sass is a responsive grid/layout
engine for Sass. Two styled copies of these pages are published: one with the
original light theme and one with an inverted dark theme.

The colour scheme is a property of the HTML pages and their stylesheet only. It
does not affect Susy-Sass itself, which is a layout engine and has nothing to do
with colours.

## Pages
| Site | Page theme | Live URL |
| --- | --- | --- |
| Susy-Sass | Light | <https://takuhii.github.io/susy-sass/> |
| Susy-Sass3 | Dark (inverted) | <https://takuhii.github.io/susy-sass3/> |

Both are the same documentation pages with the same content and layout. The
only difference is how the pages are styled: `susy-sass3` loads a fully inverted
(photographic-negative) version of the `susy-sass` stylesheet, giving the pages
a dark appearance that mirrors the light original. This is a page-styling
choice — it does not change the Susy-Sass layout engine.

## Repository layout
```
.
├── susy-sass/     # Light theme site (original stylesheet)
├── susy-sass3/    # Dark theme site (inverted stylesheet)
├── .nvmrc         # Node version hint (legacy tooling; not used by Pages)
└── README.md
```

Each site folder contains its own `index.html`, a `static/` directory with the
compiled CSS and fonts, and supporting assets (favicon, logo, `robots.txt`).

## Local preview
The site is fully static, so you can preview it with any local web server. For
example, from the repository root:

```sh
python3 -m http.server 8765
```

Then open:
- <http://localhost:8765/susy-sass/index.html>
- <http://localhost:8765/susy-sass3/index.html>

The stylesheet links include a `?v=` query string for cache-busting, so
refreshing the page picks up CSS changes without a hard reload.

## Deployment
GitHub Pages builds and publishes this repository automatically on every push
to `main` (Settings → Pages → "Deploy from a branch"). No manual build or
deploy step is required; changes typically go live within a few minutes.
