#!/usr/bin/env python3
"""Verify susy-sass3 CSS is a true per-channel inverse of susy-sass CSS.

For each stylesheet pair, extract literal colors position-by-position and assert
each susy-sass3 literal equals (255 - original) per RGB channel, alpha preserved.
Ignores var()-based colors and the hsl(Ndeg,...) demo wheel (those aren't literal
light/dark colors and are handled by the CCS mode flip instead).
"""
import re
import sys

PAIRS = [
    "static/css/screen.css",
    "static/css/demos/demos.css",
    "static/css/demos/grid-types.css",
]
BASE_A = "susy-sass"
BASE_B = "susy-sass3"

NAMED = {"white": (255, 255, 255), "black": (0, 0, 0)}

# Token regex: hex, rgb/rgba(...), or named white/black
TOKEN = re.compile(
    r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)|\b(?:white|black)\b',
    re.IGNORECASE,
)

def parse(tok):
    """Return (r,g,b,alpha_or_None) for a literal token, or None to skip."""
    t = tok.strip()
    low = t.lower()
    if low in NAMED:
        r, g, b = NAMED[low]
        return (r, g, b, None)
    if t.startswith('#'):
        h = t[1:]
        if len(h) == 3:
            h = ''.join(c * 2 for c in h)
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), None)
    if low.startswith('rgb'):
        inner = t[t.index('(') + 1:t.index(')')]
        if 'var(' in inner:
            return None  # skip var-based
        parts = [p.strip() for p in inner.split(',')]
        try:
            r, g, b = (int(round(float(parts[i]))) for i in range(3))
        except ValueError:
            return None
        a = parts[3] if len(parts) > 3 else None
        return (r, g, b, a)
    return None

def norm_alpha(a):
    return None if a is None else a.strip()

fails = 0
checked = 0
for rel in PAIRS:
    a_txt = open(f"{BASE_A}/{rel}").read()
    b_txt = open(f"{BASE_B}/{rel}").read()
    a_toks = TOKEN.findall(a_txt)
    b_toks = TOKEN.findall(b_txt)
    # findall with alternation returns full match strings here
    a_toks = TOKEN.findall(a_txt)
    b_toks = [m.group(0) for m in TOKEN.finditer(b_txt)]
    a_toks = [m.group(0) for m in TOKEN.finditer(a_txt)]

    if len(a_toks) != len(b_toks):
        print(f"[WARN] {rel}: token count differs a={len(a_toks)} b={len(b_toks)}")

    for i, (ta, tb) in enumerate(zip(a_toks, b_toks)):
        pa = parse(ta)
        pb = parse(tb)
        if pa is None or pb is None:
            continue
        checked += 1
        exp = (255 - pa[0], 255 - pa[1], 255 - pa[2])
        got = (pb[0], pb[1], pb[2])
        if exp != got:
            fails += 1
            print(f"[FAIL] {rel} #{i}: {ta} -> {tb} (expected rgb {exp}, got {got})")
        elif norm_alpha(pa[3]) != norm_alpha(pb[3]):
            fails += 1
            print(f"[FAIL] {rel} #{i}: alpha changed {ta} -> {tb}")

print(f"\nChecked {checked} literal colors. {'ALL PASS' if fails == 0 else str(fails) + ' FAILURES'}")
sys.exit(1 if fails else 0)
