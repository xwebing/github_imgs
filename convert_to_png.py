#!/usr/bin/env python3
import os
from PIL import Image

dir_path = os.path.dirname(os.path.abspath(__file__))
avatars_dir = os.path.join(dir_path, "avatars")

converted = 0
skipped = 0
errors = []

for filename in os.listdir(avatars_dir):
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".png":
        skipped += 1
        continue
    if ext not in (".jpeg", ".jpg", ".gif", ".bmp", ".tiff", ".webp"):
        continue

    src = os.path.join(avatars_dir, filename)
    base = os.path.splitext(filename)[0]
    dst = os.path.join(avatars_dir, base + ".png")

    try:
        with Image.open(src) as img:
            if img.mode == "CMYK":
                img = img.convert("RGB")
            elif img.mode == "P":
                img = img.convert("RGBA")
            elif img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGBA")
            img.save(dst, "PNG")
        converted += 1
        print(f"Converted: {filename} -> {base}.png")
    except Exception as e:
        errors.append(f"{filename}: {e}")

print(f"\nDone. Converted: {converted}, Skipped (already PNG): {skipped}")
if errors:
    print(f"Errors ({len(errors)}):")
    for err in errors:
        print(f"  {err}")
