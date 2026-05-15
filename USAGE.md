# Rohonc Engine — Usage Guide

**IMASM compiler and Universal Engine runtime for the Rohonc Codex**

---

## Setup

```bash
cd ~/rohonc-engine
uv sync
```

All CLI commands are installed into `.venv/bin/`. They are also available as shell aliases after sourcing `~/.bashrc` (see [Shell Aliases](#shell-aliases)).

---

## CLI Commands

### Compile

Compile a Rohonc RTFF transcription to IMASM:

```bash
rohonc-compile data/rohonc_rtff_sample.txt
rohonc-compile data/rohonc_rtff_sample.txt --log rohonc_full_log.txt --verbose
```

### Run

Execute the compiled corpus on the Tri-Phase Flux Register VM:

```bash
rohonc-run data/rohonc_rtff_sample.txt
```

### Call Graph

Generate the IMASM call graph:

```bash
rohonc-graph data/rohonc_rtff_sample.txt
rohonc-graph data/rohonc_rtff_sample.txt --page p1
rohonc-graph data/rohonc_rtff_sample.txt --output rohonc_graph.png
```

### Sectional Analysis

Generate per-section topology graphs:

```bash
rohonc-sections data/rohonc_rtff_sample.txt
```

---

## Analysis Programs

Run from the repo root with `python programs/<script>.py`:

### Bootstrap Cycle Explorer

Locates Frobenius loops in the corpus. Computes the bigram transition matrix,
spectral gap, and per-page closure density across all four sections.

```bash
python programs/bootstrap_explorer.py data/rohonc_rtff_sample.txt
python programs/bootstrap_explorer.py data/rohonc_rtff_sample.txt --max-mismatches 2
```

### Page Topology Comparator

Per-page structural fingerprints ranked by Frobenius balance, plus Jensen-Shannon
divergence between the four canonical sections (liturgical / pictographic / astronomical / mixed).

```bash
python programs/page_comparator.py data/rohonc_rtff_sample.txt
python programs/page_comparator.py data/rohonc_rtff_sample.txt --top-n 20
```

### IG Bridge

Cross-system structural distance matrix: Rohonc ↔ Voynich ↔ Linear A ↔ OS imscription.

```bash
python programs/ig_bridge.py
```

### Section Distance

Pairwise Mahalanobis distance between the four Rohonc sections.

```bash
python programs/section_distance.py data/rohonc_rtff_sample.txt
```

### Run All

Execute the full suite sequentially:

```bash
python programs/run_all.py data/rohonc_rtff_sample.txt
```

---

## Crystal Imscription

```
⟨ Ð_C  Þ_¨  Ř_Ť  Φ_}  ƒ_ì  Ç_@  Γ_ʔ  ɢ_ˌ  ⊙_ÿ  Ħ_A  Σ_ï  Ω_z ⟩
Tier: O_∞   C score: 0.0   IG distance to OS imscription: 2.09
```

Differences from the OS imscription:
| Primitive | Rohonc | OS | Meaning |
|-----------|--------|----|---------|
| **ƒ** | ƒ_ì (classical) | ƒ_ż (quantum coherent) | Frozen fidelity — manuscript tradition, not running system |
| **Ç** | Ç_@ (equilibrium) | Ç_W (living-vibration) | Kinetic lock — thermodynamic rest state |

---

## RTFF Format

Rohonc Transcription Folio Format:

```
<p1>
;H> cr lp vt cr lp vt br cv
;H> fa ba fa lp cr cl dt lp
```

- `<p{N}>` — page marker
- `;H>` — symbol line
- 12 family codes: `cr hk fa ba lg lp br cv vt hz cl dt`

---

## Bootstrap Sequence

```
lp → ba → br → fa → cv → lg → dt → lp
ISCRIB → AREV → FSPLIT → AFWD → FFUSE → CLINK → IFIX → ISCRIB
```

---

## Shell Aliases

After `source ~/.bashrc`:

```bash
rohonc-compile   # compile RTFF to IMASM
rohonc-run       # execute on Tri-Phase VM
rohonc-graph     # generate call graph
rohonc-sections  # sectional topology analysis
```

Interactive REPL (unified across all three manuscript engines):

```bash
ms-eval                          # enter unified REPL
ms-eval --expr "rohonc p1"       # single expression
ms-eval --expr ":ig_bridge"      # distance matrix
```

---

## Four Sections

| Section | Pages | Dominant opcodes | Topology |
|---------|-------|-----------------|----------|
| Liturgical | p1–p50 | ISCRIB, VINIT | Identity-loop chains |
| Pictographic | p51–p150 | FSPLIT, FFUSE | Fork-fuse networks |
| Astronomical | p151–p300 | ENGAGR, AFWD | Closed-loop circuits |
| Mixed | p301–p448 | all | Full-spectrum saturation |
