#!/usr/bin/env python3
"""
Page Topology Comparator — structural fingerprints across Rohonc pages.

Computes per-page primitive distributions and Jensen-Shannon divergence
between the four canonical sections.

Usage:
    python programs/page_comparator.py data/rohonc_rtff_sample.txt [--top-n 10]
"""

from __future__ import annotations
import argparse
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rohonc_engine import compile_corpus, PRIMITIVES

ALL_CODES = list(PRIMITIVES.keys())
ALL_MNEMONICS = [PRIMITIVES[c]['mnemonic'] for c in ALL_CODES]


def page_dist(page_data: dict) -> dict[str, float]:
    counts: Counter = Counter()
    for instr in page_data['instructions']:
        m = re.search(r'\|\s*(\w+)', instr)
        if m:
            mnem = m.group(1)
            counts[mnem] += 1
    total = sum(counts.values()) or 1
    return {mnem: counts.get(mnem, 0) / total for mnem in ALL_MNEMONICS}


def js_divergence(p: dict[str, float], q: dict[str, float]) -> float:
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    def kl(a, b):
        return sum(a[k] * math.log(a[k] / b[k]) for k in keys
                   if a.get(k, 0) > 1e-12 and b.get(k, 0) > 1e-12)
    return (kl(p, m) + kl(q, m)) / 2


def section_of_page(page_name: str) -> str:
    n = int(re.sub(r'\D', '', page_name) or 0)
    if n <= 50:
        return 'liturgical'
    elif n <= 150:
        return 'pictographic'
    elif n <= 300:
        return 'astronomical'
    else:
        return 'mixed'


def section_aggregate(pages: dict, section: str) -> dict[str, float]:
    combined: Counter = Counter()
    total = 0
    for page_name, page_data in pages.items():
        if section_of_page(page_name) != section:
            continue
        for instr in page_data['instructions']:
            m = re.search(r'\|\s*(\w+)', instr)
            if m:
                combined[m.group(1)] += 1
                total += 1
    if total == 0:
        return {mn: 0.0 for mn in ALL_MNEMONICS}
    return {mn: combined.get(mn, 0) / total for mn in ALL_MNEMONICS}


def top_pages(pages: dict, n: int) -> list[tuple[str, dict]]:
    scored = []
    for name, data in pages.items():
        dist = page_dist(data)
        # score = Frobenius balance (|FSPLIT - FFUSE|)
        fsplit = dist.get('FSPLIT', 0)
        ffuse  = dist.get('FFUSE', 0)
        balance = 1 - abs(fsplit - ffuse)
        scored.append((name, dist, balance))
    scored.sort(key=lambda x: -x[2])
    return [(name, dist) for name, dist, _ in scored[:n]]


def main():
    ap = argparse.ArgumentParser(description='Page Topology Comparator — Rohonc')
    ap.add_argument('transcription')
    ap.add_argument('--top-n', type=int, default=10)
    args = ap.parse_args()

    result = compile_corpus(args.transcription)
    pages = result['pages']

    print(f"\nRohonc Page Topology Comparator")
    print(f"{'─' * 60}")
    print(f"Pages: {len(pages)}  ·  Total instructions: {result['total_instructions']}")

    # per-page fingerprints
    print(f"\nTop {args.top_n} pages by Frobenius balance (|FSPLIT−FFUSE| minimised):")
    print(f"  {'Page':8s}  {'Section':14s}  {'FSPLIT':7s}  {'FFUSE':7s}  {'ISCRIB':7s}  {'ENGAGR':7s}")
    print(f"  {'─' * 60}")
    for page_name, dist in top_pages(pages, args.top_n):
        sec = section_of_page(page_name)
        print(f"  {page_name:8s}  {sec:14s}  "
              f"{dist.get('FSPLIT', 0):.3f}    {dist.get('FFUSE', 0):.3f}    "
              f"{dist.get('ISCRIB', 0):.3f}    {dist.get('ENGAGR', 0):.3f}")

    # section aggregates
    SECTIONS = ['liturgical', 'pictographic', 'astronomical', 'mixed']
    section_dists = {s: section_aggregate(pages, s) for s in SECTIONS}

    print(f"\nSection-level primitive distributions (top 6 opcodes):")
    for sec in SECTIONS:
        d = section_dists[sec]
        top = sorted(d.items(), key=lambda x: -x[1])[:6]
        print(f"  {sec:16s}  " + "  ".join(f"{mn}:{pct:.3f}" for mn, pct in top))

    # JS divergence matrix
    print(f"\nJensen-Shannon divergence between sections:")
    header = f"  {'':16s}" + "".join(f"  {s[:12]:12s}" for s in SECTIONS)
    print(header)
    for a in SECTIONS:
        row = f"  {a:16s}"
        for b in SECTIONS:
            if a == b:
                row += f"  {'0.000':12s}"
            else:
                js = js_divergence(section_dists[a], section_dists[b])
                row += f"  {js:.4f}      "
        print(row)


if __name__ == '__main__':
    main()
