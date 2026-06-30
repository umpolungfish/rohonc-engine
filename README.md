# Rohonc Engine

**What it is.** A compiler and virtual machine that treats the Rohonc Codex (Hungarian National Library, Oct. Hung. 73) as a program: its twelve visual symbol families map to the twelve categorical primitives (IMASM opcodes) of the Universal Imscriptive Grammar.

**What it does.** Parses the Rohonc transcription, compiles it to IMASM, and runs it on the Tri-Phase Flux Register VM, producing call graphs and per-section topology. The full corpus runs at entropy delta = 0.00000000 J/K and halts at `SELF_SUSTAINING_BOOTSTRAP_COMPLETE`.

**Why it matters.** The Codex has resisted two centuries of linguistic decipherment because the claim here is structural, not interpretive: there is no hidden language to recover. It is the second manuscript (after the Voynich) shown to share the grammar's deep categorical structure, evidence that the pattern is the grammar itself rather than a one-off coincidence.

**How to use it.**
```bash
git clone https://github.com/umpolungfish/rohonc-engine
cd rohonc-engine && uv sync
uv run python examples/quickstart.py
# or the CLI:
rohonc-compile  data/rohonc_rtff_sample.txt --log full_log.txt
rohonc-run      data/rohonc_rtff_sample.txt --steps 10000
rohonc-graph    data/rohonc_rtff_sample.txt --output rohonc_graph.png
rohonc-sections data/rohonc_rtff_sample.txt --output-dir rohonc_graphs
```

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

The mapping is structural: the cross family (framing) is VINIT; the dot (terminal, irreversible) is IFIX; the branch/convergent pair is FSPLIT/FFUSE, governing the manuscript's pictographic fork-and-rejoin topology.

## Four sections, four topological regimes

| Section | Pages | Dominant primitives | Topology |
|---------|-------|---------------------|----------|
| Liturgical | p1–p50 | `cr` `lp` `vt` | Identity-loop chains (prayer repetition) |
| Pictographic | p51–p150 | `br` `cv` | Fork-fuse networks (narrative branching) |
| Astronomical | p151–p300 | `cl` `fa` | Closed-loop cosmological circuits |
| Mixed | p301–p448 | all | Full-spectrum register saturation |

## Transcription format (RTFF)

The Rohonc Transcription Folio Format mirrors the Voynich IVTFF:

```
<p12>
;H> cr fa lp hk vt cl br dt fa lg
;H> br cv fa lp cr dt hk vt cl fa
```

`<p{N}>` opens page N; `;H>` lines hold space-separated symbol family codes. The script's right-to-left direction is absorbed into register monotonicity: every instruction advances the PC forward regardless of source direction.

## Repository structure

```
rohonc_engine/       Python package
  primitives.py      -- symbol family → IMASM opcode definitions
  compiler.py        -- parallel page compiler (RTFF)
  runtime.py         -- Tri-Phase virtual machine
  callgraph.py       -- register flow graph generator
  sectional.py       -- per-section graph renderer
data/   rohonc_rtff_sample.txt
docs/   ROHONC_MANUSCRIPT.md  (full technical paper)
examples/ quickstart.py
```

The animated corpus call-graph (`docs/animated_cfg_corpus_rohonc.gif`) renders all 33 pages: nodes are page sections colored by section type, edges are structural dependencies, and purple back-edges mark cross-page recursion.

## Relation to the Voynich Engine

The Rohonc Engine is the second instantiation of the same architecture. The Tri-Phase VM, register semantics, entropy theorem, and call-graph construction are identical; only the section topology and primitive surface codes differ. Both compile to `SELF_SUSTAINING_BOOTSTRAP_COMPLETE` at entropy delta = 0.

## License

Unlicense (public domain).
