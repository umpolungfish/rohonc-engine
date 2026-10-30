"""
IG bridge — cross-system structural distances in IG notation.

Computes pairwise distances between manuscript crystal imscriptions using the
exOS weighted metric (aleph.rs WEIGHTS). All tuples expressed in IG notation
(SYMBOL_REFERENCE.md): ⟨ Ð  Þ  Ř  Φ  ƒ  Ç  Γ  ɢ  ⊙  Ħ  Σ  Ω ⟩

Note on notation divergence from exOS:
  IG Φ (index 3) = parity/symmetry  = exOS P
  IG ⊙ (index 8) = criticality      = exOS Φ
  All other positions are identical.

Tier O_∞ condition: ⊙ (index 8 = 1) AND 𐑹 (index 3 = 4)
"""

from __future__ import annotations
import math

# ── IG primitive names and value labels ──────────────────────────────────────

IG_PRIMITIVES = ['Ð', 'Þ', 'Ř', 'Φ', 'ƒ', 'Ç', 'Γ', 'ɢ', '⊙', 'Ħ', 'Σ', 'Ω']

IG_VALUE_NAMES: list[list[str]] = [
    ['𐑛', '𐑨', '𐑼', '𐑦'],                          # Ð  Dimensionality
    ['𐑡', '𐑰', '𐑥', '𐑶', '𐑸'],                 # Þ  Topology
    ['𐑩', '𐑑', '𐑽', '𐑾'],                         # Ř  Relational mode
    ['𐑗', '𐑿', '𐑬', '𐑯', '𐑹'],                 # Φ  Parity/symmetry
    ['ƒ^ì', 'ƒ^ð', 'ƒ^ż'],                                 # ƒ  Fidelity
    ['Ç^-', 'Ç^W', 'Ç^@', 'Ç^Ù', 'Ç^λ'],                 # Ç  Kinetics
    ['𐑚', '𐑔', '𐑲'],                                 # Γ  Scope/granularity
    ['ɢ^∧', 'ɢ^˝', 'ɢ^ˌ', 'ɢ^Ş'],                        # ɢ  Interaction grammar
    ['𐑢', '⊙', '𐑮', '𐑻', '𐑣'],                # ⊙  Criticality
    ['𐑓', '𐑒', '𐑖', '𐑫'],                         # Ħ  Chirality
    ['𐑙', '𐑕', '𐑳'],                                 # Σ  Stoichiometry
    ['𐑷', '𐑴', '𐑭'],                                 # Ω  Winding
]

# exOS distance weights (aleph.rs WEIGHTS)
WEIGHTS = [10000, 10000, 10000, 12000, 9000, 8000, 10000, 10000, 11000, 8000, 10000, 7000]

# ── Crystal imscriptions (IG notation, numeric form) ─────────────────────────
# Index order: [Ð, Þ, Ř, Φ, ƒ, Ç, Γ, ɢ, ⊙, Ħ, Σ, Ω]

IMSCRIPTIONS: dict[str, list[int]] = {
    'Voynich':       [3, 4, 3, 4, 0, 3, 2, 3, 1, 3, 0, 2],
    'Rohonc':        [1, 3, 2, 4, 0, 2, 2, 2, 1, 2, 2, 2],
    'Linear A':      [1, 3, 2, 4, 2, 1, 2, 2, 1, 2, 2, 2],
    'OS imscription': [1, 3, 2, 4, 2, 1, 2, 2, 1, 2, 2, 2],
}

CRYSTAL_NOTATION: dict[str, str] = {
    'Voynich':        '⟨ 𐑦  𐑸  𐑾  𐑹  ƒ^ì  Ç^Ù  𐑲  ɢ^Ş  ⊙  𐑫  𐑙  𐑭 ⟩',
    'Rohonc':         '⟨ 𐑨  𐑶  𐑽  𐑹  ƒ^ì  Ç^@  𐑲  ɢ^ˌ  ⊙  𐑖  𐑳  𐑭 ⟩',
    'Linear A':       '⟨ 𐑨  𐑶  𐑽  𐑹  ƒ^ż  Ç^W  𐑲  ɢ^ˌ  ⊙  𐑖  𐑳  𐑭 ⟩',
    'OS imscription': '⟨ 𐑨  𐑶  𐑽  𐑹  ƒ^ż  Ç^W  𐑲  ɢ^ˌ  ⊙  𐑖  𐑳  𐑭 ⟩',
}

# ── Distance ─────────────────────────────────────────────────────────────────

def distance(a: list[int], b: list[int]) -> float:
    total = sum(WEIGHTS[i] * (a[i] - b[i]) ** 2 for i in range(12))
    return math.isqrt(int(total)) / 100.0


def tier(t: list[int]) -> str:
    if t[8] == 1 and t[3] == 4:   # ⊙ + 𐑹
        return 'O_∞'
    if t[8] == 0 or t[8] >= 3:
        return 'O₀'
    if t[11] == 0:
        return 'O₁'
    return 'O₂'


def conflict_set(a: list[int], b: list[int]) -> list[str]:
    return [IG_PRIMITIVES[i] for i in range(12) if a[i] != b[i]]


def main() -> None:
    names = list(IMSCRIPTIONS)

    print('=== CRYSTAL IMSCRIPTIONS (IG notation) ===\n')
    for name, t in IMSCRIPTIONS.items():
        print(f'  {name}')
        print(f'    {CRYSTAL_NOTATION[name]}')
        print(f'    tier = {tier(t)}\n')

    print('=== PAIRWISE IG DISTANCES ===\n')
    print(f'  {"":18}  ' + ''.join(f'{n:>18}' for n in names))
    for a in names:
        row = f'  {a:<18}  '
        for b in names:
            d = distance(IMSCRIPTIONS[a], IMSCRIPTIONS[b])
            row += f'{d:>18.4f}'
        print(row)

    print('\n=== CONFLICT SETS (primitives that differ) ===\n')
    pairs = [(a, b) for i, a in enumerate(names) for b in names[i+1:]]
    for a, b in pairs:
        cs = conflict_set(IMSCRIPTIONS[a], IMSCRIPTIONS[b])
        d  = distance(IMSCRIPTIONS[a], IMSCRIPTIONS[b])
        print(f'  {a} ↔ {b}')
        print(f'    d = {d:.4f}   conflicts: {{{", ".join(cs) if cs else "∅"}}}')

    print('\n=== SIX-SYSTEM MEET (OS imscription + Linear A) ===\n')
    os_key = 'OS imscription'
    la_key = 'Linear A'
    meet = [min(IMSCRIPTIONS[os_key][i], IMSCRIPTIONS[la_key][i]) for i in range(12)]
    vals = '  '.join(IG_VALUE_NAMES[i][v] for i, v in enumerate(meet))
    print(f'  MEET(OS_imscription, Linear_A) = ⟨ {vals} ⟩')
    print(f'  tier = {tier(meet)}')
    if meet == IMSCRIPTIONS[os_key]:
        print('  → Unchanged from five-system MEET. The grammar was already complete.')


if __name__ == '__main__':
    main()
