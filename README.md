[![Deploy static content to Pages](https://github.com/Ajsensai/aj-resume/actions/workflows/static.yml/badge.svg)](https://github.com/Ajsensai/aj-resume/actions/workflows/static.yml)

# aj-resume

A lightweight résumé built with plain HTML and CSS, designed for browser viewing and A4 print-to-PDF output.

The project is based on the HTML résumé template by [mnjul](https://github.com/mnjul/html-resume). The original project's background is documented in [this blog post](https://blogs.purincess.tw/matrixblog/2016/04/typesetting-resume-with-html-and-css/).

## Structure

- `templates/index.html` — page shell and component composition
- `components/` — résumé content partials
- `scripts/build.py` — zero-dependency renderer for `{{> ... }}` partials
- `index.html` — generated static résumé; do not edit directly
- `style.css` — screen and print styling
- `CLAUDE.md` — guidance for AI coding agents working in this repository
- `.github/workflows/static.yml` — GitHub Pages deployment

## Editing

Edit the template or a component, then regenerate the static page:

```bash
python3 scripts/build.py
```

To verify that the committed `index.html` matches the template without changing files:

```bash
python3 scripts/build.py --check
```

There are no third-party runtime or build dependencies. GitHub Pages regenerates `index.html` during deployment before publishing the repository.
