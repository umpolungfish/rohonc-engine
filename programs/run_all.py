#!/usr/bin/env python3
"""
Master Analysis Runner — runs all Rohonc Engine analysis programs.

Usage:
    python programs/run_all.py data/rohonc_rtff_sample.txt
"""

from __future__ import annotations
import argparse
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DEFAULT = REPO_ROOT / 'data' / 'rohonc_rtff_sample.txt'

PROGRAMS = [
    {
        'name': 'Bootstrap Cycle Explorer',
        'script': 'programs/bootstrap_explorer.py',
        'args': ['--max-mismatches', '1'],
        'description': 'Frobenius cycles, spectral gap, closure density per section',
    },
    {
        'name': 'Page Topology Comparator',
        'script': 'programs/page_comparator.py',
        'args': ['--top-n', '10'],
        'description': 'Per-page structural fingerprints, JS divergence between sections',
    },
    {
        'name': 'IG Bridge',
        'script': 'programs/ig_bridge.py',
        'args': [],
        'description': 'Cross-system IG distance matrix (Rohonc ↔ Voynich ↔ Linear A)',
    },
    {
        'name': 'Section Distance',
        'script': 'programs/section_distance.py',
        'args': [],
        'description': 'Pairwise Mahalanobis distance between the four canonical sections',
    },
]


def run_program(script: str, transcription: str, extra_args: list[str]) -> int:
    cmd = [sys.executable, script, transcription] + extra_args
    t0 = time.time()
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    elapsed = time.time() - t0
    return result.returncode


def main():
    ap = argparse.ArgumentParser(description='Rohonc Engine — master analysis runner')
    ap.add_argument('transcription', nargs='?', default=str(DATA_DEFAULT))
    args = ap.parse_args()

    print(f"\n{'═' * 65}")
    print(f"  Rohonc Engine — Full Analysis Suite")
    print(f"  Transcription: {args.transcription}")
    print(f"{'═' * 65}")

    passed = failed = 0
    for prog in PROGRAMS:
        print(f"\n{'─' * 65}")
        print(f"  ▶  {prog['name']}")
        print(f"     {prog['description']}")
        print(f"{'─' * 65}")
        rc = run_program(prog['script'], args.transcription, prog['args'])
        if rc == 0:
            passed += 1
        else:
            failed += 1
            print(f"  [FAILED with exit code {rc}]")

    print(f"\n{'═' * 65}")
    print(f"  Complete: {passed} passed, {failed} failed")
    print(f"{'═' * 65}\n")
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
