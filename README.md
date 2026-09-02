# takuhii.github.io
Personal GitHub Pages site for [takuhii](https://github.com/takuhii), hosted at
**<https://takuhii.github.io/>**.

This repository is a static site (plain HTML and CSS, no build step) deployed
automatically by GitHub Pages from the `main` branch. It currently hosts two
versions of the **Susy-Sass** documentation site, a responsive layout engine
for Sass.

## Pages
| Site | Live URL |
| --- | --- |
| Susy-Sass | <https://takuhii.github.io/susy-sass/> |
| Susy-Sass3 | <https://takuhii.github.io/susy-sass3/> |

Both sites share the same content and layout.

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
