#!/usr/bin/env python3
"""Publish new photos from photos/ into the gallery.

Resizes any original in photos/ that isn't in the gallery yet, writing a
web copy to static/img/photos/, then adds an <img> tag for it to
content/photos/_index.md. Safe to re-run: already-published photos are
skipped and existing markup is left alone.

    scripts/add-photos.py [--dry-run] [--force]
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

WIDTH = 1600          # px; matches the width="1600" in the gallery markup
QUALITY = 80          # JPEG quality
SUFFIXES = {".jpg", ".jpeg"}

ROOT = Path(__file__).resolve().parent.parent
ORIGINALS = ROOT / "photos"
PUBLISHED = ROOT / "static" / "img" / "photos"
PAGE = ROOT / "content" / "photos" / "_index.md"

IMG_TAG = '<img src="/img/photos/{name}.jpg" alt="Photograph" loading="lazy" width="1600">'
GRID_END = "</div>"


def magick():
    """ImageMagick's CLI, whichever name it goes by here."""
    for exe in ("magick", "convert"):
        found = shutil.which(exe)
        if found:
            return found
    sys.exit("error: ImageMagick not found (install it, or `apt install imagemagick`)")


def originals():
    """Source photos, keyed by their published stem (lowercased)."""
    found = {}
    for path in sorted(ORIGINALS.iterdir()):
        if path.is_file() and path.suffix.lower() in SUFFIXES:
            found[path.stem.lower()] = path
    return found


def resize(exe, src, dest, dry_run):
    """Write a web-sized, EXIF-stripped copy of src to dest.

    -strip drops EXIF, which keeps camera GPS coordinates out of the
    published files. Don't remove it.
    """
    if dry_run:
        return
    subprocess.run(
        [exe, str(src), "-auto-orient", "-resize", f"{WIDTH}x",
         "-strip", "-quality", str(QUALITY), str(dest)],
        check=True,
    )


def add_to_page(names, dry_run):
    """Insert <img> tags for names, in sorted position, into the grid.

    Only adds what's missing, so any hand-editing of the page survives.
    """
    text = PAGE.read_text(encoding="utf-8")
    referenced = set(re.findall(r"/img/photos/([a-z0-9_]+)\.jpg", text))
    missing = sorted(set(names) - referenced)
    if not missing:
        return []

    lines = text.split("\n")
    end = next(i for i, line in enumerate(lines) if line.strip() == GRID_END)

    for name in missing:
        tag = IMG_TAG.format(name=name)
        # Keep the grid in filename order: sit before the first later tag.
        at = end
        for i, line in enumerate(lines[:end]):
            found = re.search(r"/img/photos/([a-z0-9_]+)\.jpg", line)
            if found and found.group(1) > name:
                at = i
                break
        lines.insert(at, tag)
        end += 1

    if not dry_run:
        PAGE.write_text("\n".join(lines), encoding="utf-8")
    return missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="report what would change, write nothing")
    parser.add_argument("--force", action="store_true",
                        help="re-encode photos already in the gallery")
    args = parser.parse_args()

    if not ORIGINALS.is_dir():
        sys.exit(f"error: no originals directory at {ORIGINALS}")
    PUBLISHED.mkdir(parents=True, exist_ok=True)

    exe = magick()
    published = []
    for name, src in originals().items():
        dest = PUBLISHED / f"{name}.jpg"
        if dest.exists() and not args.force:
            continue
        print(f"  {src.name} -> static/img/photos/{dest.name}")
        resize(exe, src, dest, args.dry_run)
        published.append(name)

    # Pick up any web copy that never made it into the page. Include what we
    # just resized, which on a dry run isn't on disk to be found.
    all_names = sorted({p.stem for p in PUBLISHED.glob("*.jpg")} | set(published))
    added = add_to_page(all_names, args.dry_run)

    what = "would publish" if args.dry_run else "published"
    print(f"\n{what} {len(published)} photo(s), added {len(added)} to the gallery page")
    if published or added:
        print("next: review the page, then commit static/img/photos/ and content/photos/_index.md")


if __name__ == "__main__":
    main()
