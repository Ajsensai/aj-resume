#!/usr/bin/env python3
"""Render the résumé HTML template using zero-dependency partial includes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "index.html"
OUTPUT = ROOT / "index.html"
INCLUDE_RE = re.compile(r"{{>\s*([^}]+?)\s*}}")


def render_file(path: Path, stack: tuple[Path, ...] = ()) -> str:
    path = path.resolve()

    if ROOT not in path.parents and path != ROOT:
        raise ValueError(f"Include escapes repository root: {path}")

    if path in stack:
        chain = " -> ".join(str(item.relative_to(ROOT)) for item in (*stack, path))
        raise ValueError(f"Circular include detected: {chain}")

    text = path.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        include_name = match.group(1).strip()
        include_path = (ROOT / include_name).resolve()
        return render_file(include_path, (*stack, path))

    return INCLUDE_RE.sub(replace, text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render index.html from résumé partials.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if index.html does not match the rendered template.",
    )
    args = parser.parse_args()

    rendered = render_file(TEMPLATE)

    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print("index.html is out of date. Run: python3 scripts/build.py", file=sys.stderr)
            return 1
        print("index.html is up to date.")
        return 0

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
