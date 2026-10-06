# CLAUDE.md

## Repository purpose

This repository contains Anthony Bale's résumé as a small, static HTML/CSS site that is also intended to print cleanly to PDF.

The project deliberately avoids a JavaScript framework or build system. Prefer simple, direct edits over introducing tooling, dependencies, abstractions or architectural changes.

## Key files

- `resume.html` — the résumé content and semantic structure.
- `style.css` — all layout, typography, screen and print styling.
- `.github/workflows/static.yml` — deploys the repository as static content to GitHub Pages when `main` changes.
- `dep/` — vendored third-party assets retained from the original template. Treat this directory as external/vendor code and do not modify it unless a task specifically requires it.
- `README.md` — brief repository background and attribution.

## How the site works

There is no build step. `resume.html` loads `style.css` directly and can be opened in a browser from the repository root.

The résumé is intentionally split into two A4-style sections using `.page` elements. CSS in `style.css` controls both the browser preview and print-to-PDF output.

GitHub Pages deployment uploads the repository contents directly, so changes to the main HTML/CSS become the deployed site after merging to `main`.

## Editing guidance

When changing résumé content:

- Preserve the existing HTML hierarchy and class names unless a layout change is explicitly requested.
- Keep wording concise enough to preserve the current two-page A4 layout.
- Prefer Australian/British English where applicable (for example, `containerised`).
- Keep terminology and product names correctly capitalised, such as Microsoft, pfSense, WireGuard and Mac.
- Avoid adding decorative or interactive features that do not improve the résumé itself.

When changing styles:

- Preserve the A4 dimensions and print behaviour unless specifically asked to redesign the document.
- Check both normal browser rendering and print preview.
- Be cautious with font sizes, margins and vertical spacing because small changes can cause content to overflow to an additional printed page.
- Reuse the existing CSS variables and visual language rather than adding a second styling system.

## Validation

For content-only changes:

1. Review `resume.html` for spelling, grammar, consistent capitalisation and valid HTML structure.
2. Open `resume.html` in a browser and confirm the content still renders correctly.
3. Use print preview with A4 portrait sizing and confirm the résumé remains two pages without clipped content.

For CSS changes, perform the same checks and pay particular attention to page breaks, footer placement and overflow.

There is currently no automated test, lint or build command.

## Change philosophy

Keep this repository intentionally simple.

Good changes are typically:

- résumé content updates;
- typo and grammar fixes;
- small accessibility or semantic HTML improvements;
- small CSS fixes that preserve the existing design;
- documentation improvements.

Avoid unless explicitly requested:

- framework migrations;
- package managers or build pipelines;
- componentisation for its own sake;
- wholesale redesigns;
- modifying vendored files under `dep/`;
- replacing the existing GitHub Pages deployment without a concrete need.

## Pull requests

Keep PRs focused and describe any impact on print layout. If a change could affect pagination, call that out explicitly and verify print preview before merging.
