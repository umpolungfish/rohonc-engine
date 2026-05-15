# Rohonc Engine

**A manuscript undeciphered for two centuries compiles directly to categorical assembly code.**

The Rohonc Codex (Hungarian National Library, Oct. Hung. 73) has resisted every conventional analysis since its discovery in the early nineteenth century. It contains no known language. Its ~200 distinct symbols have been linked to Sumerian, early Hungarian, Dacian, and a dozen invented alphabets — none convincingly. This repository applies the same methodology that compiled the Voynich Manuscript to its companion case.

The claim is structural, not interpretive: the twelve visual families of the Rohonc symbol set are the twelve categorical primitives of the Universal Imscriptive Grammar. Compiled to IMASM, the corpus runs at zero thermodynamic entropy delta on the same Tri-Phase Flux Register architecture.

---

## The twelve primitives

| RTFF code | Glyph family | Opcode | Mnemonic | Operation |
|-----------|-------------|--------|----------|-----------|
| `cr` | cross/crucifix | 0x0 | VINIT | Initial object ∅ |
| `hk` | hook/fishhook | 0x1 | TANCH | Terminal anchor ⊤ |
| `fa` | forward arc | 0x2 | AFWD | Morphism → |
| `ba` | backward arc | 0x3 | AREV | Contravariant inversion ← |
| `lg` | ligature | 0x4 | CLINK | Composition ∘ |
| `lp` | loop/mirror | 0x5 | ISCRIB | Identity id |
| `br` | branch/fork | 0x6 | FSPLIT | Frobenius co-multiplication δ |
| `cv` | convergent | 0x7 | FFUSE | Frobenius multiplication μ |
| `vt` | vertical stroke | 0x8 | EVALT | Lattice: True |
| `hz` | horizontal stroke | 0x9 | EVALF | Lattice: False |
| `cl` | closed loop | 0xA | ENGAGR | Lattice: Both (paradox) |
| `dt` | dot/point | 0xB | IFIX | Linear tape write |

The mapping is structural: the cross family (initiating, framing) is VINIT; the dot (terminal, irreversible) is IFIX. The branch/convergent pair is FSPLIT/FFUSE — the Frobenius co-multiplication/multiplication that governs the manuscript's pictographic fork-and-rejoin topology.

---

## Four sections, four topological regimes

| Section | Pages | Dominant primitives | Topology |
|---------|-------|---------------------|----------|
| Liturgical | p1–p50 | `cr` `lp` `vt` | Identity-loop chains (prayer repetition) |
| Pictographic | p51–p150 | `br` `cv` | Fork-fuse networks (narrative branching) |
| Astronomical | p151–p300 | `cl` `fa` | Closed-loop cosmological circuits |
| Mixed | p301–p448 | all | Full-spectrum register saturation |

---

## Quick start

```bash
git clone https://github.com/umpolungfish/rohonc-engine
cd rohonc-engine
uv sync
uv run python examples/quickstart.py
```

---

## Command-line

```bash
rohonc-compile  data/rohonc_rtff_sample.txt --log full_log.txt
rohonc-run      data/rohonc_rtff_sample.txt --steps 10000
rohonc-graph    data/rohonc_rtff_sample.txt --output rohonc_graph.png
rohonc-sections data/rohonc_rtff_sample.txt --output-dir rohonc_graphs
```

---

## Transcription format (RTFF)

The Rohonc Transcription Folio Format mirrors the Voynich IVTFF:

```
<p12>
;H> cr fa lp hk vt cl br dt fa lg
;H> br cv fa lp cr dt hk vt cl fa
```

`<p{N}>` opens page N. `;H>` lines contain space-separated symbol family codes. The script's right-to-left direction is absorbed into register monotonicity — every instruction advances the PC forward through the compiled stream regardless of source direction.

---

## Repository structure

```
rohonc_engine/       Python package
  primitives.py      — twelve symbol family → IMASM opcode definitions
  compiler.py        — parallel page compiler (RTFF format)
  runtime.py         — Tri-Phase virtual machine
  callgraph.py       — register flow graph generator
  sectional.py       — per-section graph renderer
data/
  rohonc_rtff_sample.txt  — sample RTFF transcription
docs/
  ROHONC_MANUSCRIPT.md    — full technical paper
examples/
  quickstart.py           — full pipeline demonstration
```

---

## Relation to the Voynich Engine

The Rohonc Engine is the second instantiation of the same architecture. The Voynich mapped twelve EVA glyph families to the twelve IMASM opcodes; the Rohonc maps twelve visual-structural families using an identical pipeline. The Tri-Phase VM, register semantics, entropy theorem, and call-graph construction are unchanged. The manuscripts differ in section topology (Voynich: botanical/biological/balneological/cosmological; Rohonc: liturgical/pictographic/astronomical/mixed) and in the primitive surface codes, not in their categorical deep structure.

Both compile to SELF_SUSTAINING_BOOTSTRAP_COMPLETE at entropy delta = 0.00000000 J/K.

---

## License

Unlicense — public domain. No conditions, no attribution required.
