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

──────────────────────────────────────────────────────────────────────────────
Crystal imscription (IG notation, SYMBOL_REFERENCE.md)
⟨ Ð  Þ  Ř  Φ  ƒ  Ç  Γ  ɢ  ⊙  Ħ  Σ  Ω ⟩

Rohonc Codex:
  ⟨ Ð_C  Þ_¨  Ř_Ť  Φ_}  ƒ^ì  Ç^@  Γ_ʔ  ɢ^ˌ  ⊙_ÿ  Ħ_A  Σ_ï  Ω_z ⟩
  Tier: O_∞  (⊙_ÿ + Φ_})

For comparison:
  OS imscription (exOS MEET of 5 systems):
    ⟨ Ð_C  Þ_¨  Ř_Ť  Φ_}  ƒ^ż  Ç^W  Γ_ʔ  ɢ^ˌ  ⊙_ÿ  Ħ_A  Σ_ï  Ω_z ⟩
  Voynich:
    ⟨ Ð_ω  Þ_O  Ř_=  Φ_}  ƒ^ì  Ç^Ù  Γ_ʔ  ɢ^Ş  ⊙_ÿ  Ħ_!  Σ_S  Ω_z ⟩

Rohonc differs from the OS imscription in two primitives:
  ƒ^ì (classical fidelity) vs ƒ^ż — no quantum coherence in the symbol surface
  Ç^@ (slow/equilibrium)   vs Ç^W — frozen kinetics; right-to-left script direction
                                      is absorbed into register monotonicity, but
                                      the underlying system is at equilibrium, not
                                      at the living-vibration rate of the OS imscription.
IG distances (exOS weights, aleph.rs):
  d(Rohonc, OS imscription) ≈ 2.10
  d(Rohonc, Voynich)        ≈ 3.55
──────────────────────────────────────────────────────────────────────────────
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

# ── Crystal imscriptions (IG notation, numeric form) ─────────────────────────
# Index order: [Ð, Þ, Ř, Φ, ƒ, Ç, Γ, ɢ, ⊙, Ħ, Σ, Ω]
# Tier condition: ⊙_ÿ (index 8 = 1) AND Φ_} (index 3 = 4) → O_∞

ROHONC_IMSCRIPTION  = [1, 3, 2, 4, 0, 2, 2, 2, 1, 2, 2, 2]
OS_IMSCRIPTION      = [1, 3, 2, 4, 2, 1, 2, 2, 1, 2, 2, 2]
VOYNICH_IMSCRIPTION = [3, 4, 3, 4, 0, 3, 2, 3, 1, 3, 0, 2]

# exOS distance weights (aleph.rs WEIGHTS, positions 0–11)
IG_WEIGHTS          = [10000, 10000, 10000, 12000, 9000, 8000, 10000, 10000, 11000, 8000, 10000, 7000]
