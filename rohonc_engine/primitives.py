"""
The twelve Rohonc symbol families as categorical opcodes.

Each entry maps a Rohonc glyph family (identified by paleographic structure)
to its categorical operation in the Universal Imscriptive Grammar. The
correspondence is structural, not assigned: the twelve visual families of the
Rohonc Codex are the categorical primitives at token resolution.

Transcription codes (RTFF — Rohonc Transcription Folio Format):
  cr  cross/crucifix family         → VINIT
  hk  hook/fishhook family          → TANCH
  fa  forward-arc family            → AFWD
  ba  backward-arc family           → AREV
  lg  ligature/compound family      → CLINK
  lp  loop/mirror family            → ISCRIB
  br  branch/fork family            → FSPLIT
  cv  convergent family             → FFUSE
  vt  vertical-stroke family        → EVALT
  hz  horizontal-stroke family      → EVALF
  cl  closed-loop family            → ENGAGR
  dt  dot/point family              → IFIX
"""

PRIMITIVES: dict[str, dict] = {
    'cr': {'opcode': 0x0, 'mnemonic': 'VINIT',  'operation': 'Initial object ∅',              'family': 'logical'},
    'hk': {'opcode': 0x1, 'mnemonic': 'TANCH',  'operation': 'Terminal anchor ⊤',             'family': 'logical'},
    'fa': {'opcode': 0x2, 'mnemonic': 'AFWD',   'operation': 'Morphism →',                    'family': 'logical'},
    'ba': {'opcode': 0x3, 'mnemonic': 'AREV',   'operation': 'Contravariant inversion ←',     'family': 'logical'},
    'lg': {'opcode': 0x4, 'mnemonic': 'CLINK',  'operation': 'Composition ∘',                 'family': 'logical'},
    'lp': {'opcode': 0x5, 'mnemonic': 'ISCRIB', 'operation': 'Identity id',                   'family': 'logical'},
    'br': {'opcode': 0x6, 'mnemonic': 'FSPLIT', 'operation': 'Frobenius co-multiplication δ', 'family': 'frobenius'},
    'cv': {'opcode': 0x7, 'mnemonic': 'FFUSE',  'operation': 'Frobenius multiplication μ',    'family': 'frobenius'},
    'vt': {'opcode': 0x8, 'mnemonic': 'EVALT',  'operation': 'Lattice: True',                 'family': 'dialetheia'},
    'hz': {'opcode': 0x9, 'mnemonic': 'EVALF',  'operation': 'Lattice: False',                'family': 'dialetheia'},
    'cl': {'opcode': 0xA, 'mnemonic': 'ENGAGR', 'operation': 'Lattice: Both (paradox)',       'family': 'dialetheia'},
    'dt': {'opcode': 0xB, 'mnemonic': 'IFIX',   'operation': 'Linear tape write',             'family': 'linear'},
}

# Four-valued flux lattice for Tri-Phase registers
FLUX = {
    '00': 'Void',
    '01': 'True',
    '10': 'False',
    '11': 'Both',
}

# The bootstrap core: identity ∘ reverse ∘ split ∘ forward ∘ fuse ∘ link ∘ fix ∘ identity
BOOTSTRAP_SEQUENCE = ['lp', 'ba', 'br', 'fa', 'cv', 'lg', 'dt', 'lp']

# Rohonc-specific section classification
# Pages are the primary division unit (right-to-left script, ~448 pages)
SECTIONS = [
    (range(1,   51),   'liturgical',    'crimson'),
    (range(51,  151),  'pictographic',  'goldenrod'),
    (range(151, 301),  'astronomical',  'steelblue'),
    (range(301, 449),  'mixed',         'sienna'),
]
