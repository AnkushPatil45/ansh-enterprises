#!/usr/bin/env python3
"""
optimize_images.py — resize + convert product photos to web-optimized WebP.

Why: product photos from the camera/supplier are multi-MB JP/PNG. The site needs
small WebP files (max ~1200px, quality 82) so it stays fast on mobile.

Setup (one time):
    python3 -m venv .venv
    .venv/bin/pip install Pillow
    # (numpy only needed for the background-whitening helper below)
    .venv/bin/pip install numpy

Usage:
    .venv/bin/python scripts/optimize_images.py SOURCE.jpg  assets/img/products/groundnut-oil.webp
    # background-whiten a studio shot that has an off-white/grey backdrop:
    .venv/bin/python scripts/optimize_images.py SOURCE.jpg  OUT.webp --whiten

Notes:
- Originals are never modified; output is written to the given path.
- File names must match the "image" field in products.json (e.g. honey.webp).
- --whiten uses a luminance-gated border flood fill: good for a single light
  backdrop behind a clearly darker/coloured product. Not for decorative
  backgrounds (rings/leaves/pedestals) — those need manual editing.
"""
import argparse
from collections import deque
from PIL import Image

MAX_SIDE = 1200
QUALITY = 82


def resize(im):
    w, h = im.size
    s = min(1.0, MAX_SIDE / max(w, h))
    return im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s < 1 else im


def whiten_bg(im, thresh=16, lum_min=160):
    import numpy as np
    arr = __import__("numpy").asarray(im, dtype=np.int16)
    H, W, _ = arr.shape
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    light = lum >= lum_min
    bg = np.zeros((H, W), dtype=bool)
    dq = deque()

    def seed(y, x):
        if light[y, x] and not bg[y, x]:
            bg[y, x] = True
            dq.append((y, x))

    for x in range(W):
        seed(0, x); seed(H - 1, x)
    for y in range(H):
        seed(y, 0); seed(y, W - 1)
    while dq:
        y, x = dq.popleft()
        c = arr[y, x]
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and not bg[ny, nx] and light[ny, nx]:
                if abs(int(arr[ny, nx][0]) - int(c[0])) <= thresh and \
                   abs(int(arr[ny, nx][1]) - int(c[1])) <= thresh and \
                   abs(int(arr[ny, nx][2]) - int(c[2])) <= thresh:
                    bg[ny, nx] = True
                    dq.append((ny, nx))
    out = arr.copy()
    out[bg] = [255, 255, 255]
    return Image.fromarray(out.astype("uint8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("output")
    ap.add_argument("--whiten", action="store_true", help="flood the light backdrop to white")
    args = ap.parse_args()

    im = resize(Image.open(args.source).convert("RGB"))
    if args.whiten:
        im = whiten_bg(im)
    im.save(args.output, "WEBP", quality=QUALITY, method=6)
    print(f"wrote {args.output} {im.size}")


if __name__ == "__main__":
    main()
