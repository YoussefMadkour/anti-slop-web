#!/usr/bin/env python3
"""Build a role-based palette from seed colors, in OKLCH, with a WCAG contrast report.

Usage:
    python3 palette.py --primary "#1f6f5c"
    python3 palette.py --primary "#1f6f5c" --accent "#d9822b" --neutral-tint primary
    python3 palette.py --primary "#c2410c" --neutral-tint 0.012 --format json

Each seed becomes an 11-step scale (50 to 950) that keeps the seed's hue and character, with
lightness spread evenly and chroma reduced where the color would leave the sRGB gamut. Neutrals
are generated from the primary hue with a small chroma (--neutral-tint: "none" for pure gray,
"primary" for a faint tint of the primary hue, or a number such as 0.01 for the chroma).

Output: CSS custom properties (primitive tokens) plus semantic suggestions for light and dark
themes, and the contrast ratio of each key text and control pairing. Exit code 0 when every
reported pairing meets its minimum, 1 otherwise, 2 on bad input.

This proposes a starting point. Adjust by eye against real screens, then re-run contrast.py
on the final values.
"""

import argparse
import json
import math
import sys

STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
# Target OKLCH lightness per step: light end near white, dark end near black.
LIGHTNESS = [0.975, 0.945, 0.885, 0.805, 0.71, 0.62, 0.53, 0.45, 0.375, 0.305, 0.235]
# Chroma multiplier per step relative to the seed: lower at the extremes, where gamut is tight.
CHROMA_SHAPE = [0.12, 0.22, 0.42, 0.66, 0.88, 1.0, 1.0, 0.92, 0.8, 0.66, 0.52]


# --- conversions (sRGB <-> OKLab <-> OKLCH) ---------------------------------------------

def parse_hex(value):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(ch * 2 for ch in v)
    if len(v) != 6:
        raise ValueError(f"not a 3- or 6-digit hex color: {value!r}")
    return [int(v[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02x}" for c in rgb)


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def rgb_to_oklch(rgb):
    r, g, b = (srgb_to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    a = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    bb = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    C = math.hypot(a, bb)
    H = math.degrees(math.atan2(bb, a)) % 360
    return L, C, H


def oklch_to_linear(L, C, H):
    a = C * math.cos(math.radians(H))
    b = C * math.sin(math.radians(H))
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return [
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    ]


def oklch_to_rgb(L, C, H):
    """Convert to sRGB, reducing chroma until the color is in gamut."""
    lo, hi = 0.0, C
    lin = oklch_to_linear(L, C, H)
    if all(-1e-4 <= c <= 1 + 1e-4 for c in lin):
        return [linear_to_srgb(max(0, min(1, c))) for c in lin]
    for _ in range(30):
        mid = (lo + hi) / 2
        lin = oklch_to_linear(L, mid, H)
        if all(-1e-4 <= c <= 1 + 1e-4 for c in lin):
            lo = mid
        else:
            hi = mid
    return [linear_to_srgb(max(0, min(1, c))) for c in oklch_to_linear(L, lo, H)]


# --- contrast ---------------------------------------------------------------------------

def luminance(rgb):
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(hex_a, hex_b):
    la, lb = sorted((luminance(parse_hex(hex_a)), luminance(parse_hex(hex_b))), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# --- palette ----------------------------------------------------------------------------

def scale(seed_hex, chroma=None):
    _, C, H = rgb_to_oklch(parse_hex(seed_hex))
    base = C if chroma is None else chroma
    return {
        step: to_hex(oklch_to_rgb(L, base * (shape if chroma is None else 1), H))
        for step, L, shape in zip(STEPS, LIGHTNESS, CHROMA_SHAPE)
    }


def neutral_scale(primary_hex, tint):
    _, _, H = rgb_to_oklch(parse_hex(primary_hex))
    if tint == "none":
        chroma = 0.0
    elif tint == "primary":
        chroma = 0.008
    else:
        chroma = float(tint)
    return {
        step: to_hex(oklch_to_rgb(L, chroma, H))
        for step, L in zip(STEPS, [0.985, 0.965, 0.925, 0.87, 0.71, 0.555, 0.445, 0.37, 0.28, 0.21, 0.16])
    }


def pick_action_step(primary, surface, minimum=4.5):
    """Lightest step whose white label and surface contrast both meet the minimum."""
    for step in STEPS[4:]:
        if contrast(primary[step], "#ffffff") >= minimum and contrast(primary[step], surface) >= 3:
            return step
    return 700


def build(args):
    scales = {"primary": scale(args.primary), "neutral": neutral_scale(args.primary, args.neutral_tint)}
    if args.accent:
        scales["accent"] = scale(args.accent)
    n, p = scales["neutral"], scales["primary"]

    action = pick_action_step(p, n[50])
    light = {
        "surface-page": n[50], "surface-raised": "#ffffff", "border": n[200],
        "text-primary": n[900], "text-secondary": n[600], "text-disabled": n[400],
        "action-primary": p[action], "action-primary-hover": p[STEPS[min(STEPS.index(action) + 1, 10)]],
        "on-action-primary": "#ffffff", "focus-ring": p[action],
    }
    dark = {
        "surface-page": n[950], "surface-raised": n[900], "border": n[800],
        "text-primary": n[100], "text-secondary": n[400], "text-disabled": n[600],
        "action-primary": p[300], "action-primary-hover": p[200],
        "on-action-primary": n[950], "focus-ring": p[300],
    }
    checks = []
    for theme, t in (("light", light), ("dark", dark)):
        for fg, bg, minimum, what in (
            ("text-primary", "surface-page", 4.5, "body text"),
            ("text-secondary", "surface-page", 4.5, "secondary text"),
            ("text-secondary", "surface-raised", 4.5, "secondary text on cards"),
            ("on-action-primary", "action-primary", 4.5, "button label"),
            ("action-primary", "surface-page", 3.0, "button or link against page"),
            ("focus-ring", "surface-page", 3.0, "focus indicator"),
            ("border", "surface-page", 1.0, "decorative border (no minimum)"),
        ):
            ratio = contrast(t[fg], t[bg])
            checks.append({"theme": theme, "pair": f"{fg} on {bg}", "use": what,
                           "ratio": round(ratio, 2), "min": minimum, "pass": ratio >= minimum})
    return scales, light, dark, checks


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--primary", required=True, help="seed hex for the primary role")
    ap.add_argument("--accent", help="optional seed hex for a second voice")
    ap.add_argument("--neutral-tint", default="primary", help='"none", "primary", or a chroma number')
    ap.add_argument("--format", choices=["css", "json"], default="css")
    args = ap.parse_args()
    try:
        scales, light, dark, checks = build(args)
    except ValueError as err:
        print(err, file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps({"scales": scales, "light": light, "dark": dark, "contrast": checks}, indent=2))
    else:
        print(":root {\n  /* primitives */")
        for name, sc in scales.items():
            print("  " + "  ".join(f"--{name}-{s}: {v};" for s, v in list(sc.items())[:6]))
            print("  " + "  ".join(f"--{name}-{s}: {v};" for s, v in list(sc.items())[6:]))
        print("  /* semantic, light */")
        for k, v in light.items():
            print(f"  --color-{k}: {v};")
        print("}\n[data-theme=\"dark\"] {")
        for k, v in dark.items():
            print(f"  --color-{k}: {v};")
        print("}\n")
        print("Contrast (WCAG 2.x):")
        for c in checks:
            mark = "PASS" if c["pass"] else "FAIL"
            print(f"  {mark}  {c['theme']:5}  {c['ratio']:>5}:1  (min {c['min']})  {c['pair']}  [{c['use']}]")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
