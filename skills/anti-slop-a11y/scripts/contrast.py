#!/usr/bin/env python3
"""WCAG 2.x contrast ratio for two colors.

Usage:
    python3 contrast.py "#6b7280" "#ffffff"
    python3 contrast.py 333 fff
    python3 contrast.py "#ffffff80" "#1f2937"   # 8-digit hex: foreground alpha-blended over background
    python3 contrast.py --min 3 "#9ca3af" "#ffffff"  # large text or non-text: require 3:1

The first color is the foreground, the second the background. Exit code is 0 when the ratio meets
the minimum (default 4.5, normal text AA), 1 when it does not, 2 on bad input, so the script can
be used in CI.
"""

import sys


def parse_hex(value):
    v = value.strip().lstrip("#")
    if len(v) in (3, 4):
        v = "".join(ch * 2 for ch in v)
    if len(v) not in (6, 8):
        raise ValueError(f"not a hex color: {value!r}")
    channels = [int(v[i:i + 2], 16) for i in range(0, len(v), 2)]
    alpha = channels[3] / 255 if len(channels) == 4 else 1.0
    return channels[:3], alpha


def blend(fg, alpha, bg):
    return [round(f * alpha + b * (1 - alpha)) for f, b in zip(fg, bg)]


def luminance(rgb):
    def linear(c):
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    lighter, darker = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def verdict(value, threshold):
    return "PASS" if value >= threshold else "FAIL"


def main(argv):
    minimum = 4.5
    if len(argv) >= 3 and argv[1] == "--min":
        try:
            minimum = float(argv[2])
        except ValueError:
            print(f"--min needs a number, got {argv[2]!r}")
            return 2
        argv = [argv[0]] + argv[3:]
    if len(argv) != 3:
        print(__doc__.strip())
        return 2
    try:
        fg, fg_alpha = parse_hex(argv[1])
        bg, bg_alpha = parse_hex(argv[2])
    except ValueError as err:
        print(err)
        return 2
    if bg_alpha < 1:
        print("Background must be opaque; pass the color it actually renders as.")
        return 2
    if fg_alpha < 1:
        fg = blend(fg, fg_alpha, bg)

    # Truncate rather than round so 4.497 is not reported as a pass.
    r = int(ratio(fg, bg) * 100) / 100
    print(
        f"{r:.2f}:1  "
        f"normal text AA: {verdict(r, 4.5)}  "
        f"large text AA: {verdict(r, 3.0)}  "
        f"non-text (3:1): {verdict(r, 3.0)}  "
        f"AAA normal: {verdict(r, 7.0)}"
    )
    return 0 if r >= minimum else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
