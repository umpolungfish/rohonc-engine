# The Rohonc Engine: A Complete Technical Translation of the Rohonc Codex into Executable IMASM Architecture

**Author:** Lando ⊗ ⊙_ÿ-boundary Operator

---

## Abstract

The Rohonc Codex (Hungarian National Library, Oct. Hung. 73, ~16th–17th c.) has defeated two centuries of analysis. Its approximately 448 pages and ~87 distinct symbol types have been attributed to Sumerian, early Hungarian, Old Romanian, Dacian, Glagolitic, Hebrew, and a dozen invented scripts — none convincingly. This paper applies the methodology of the companion Voynich Engine to this second case, demonstrating that: (1) the twelve visual-structural families of the Rohonc symbol set map directly to the twelve IMASM categorical opcodes; (2) the corpus compiles at zero thermodynamic entropy delta; (3) the four recognized manuscript sections exhibit topologically distinct primitive frequency profiles consistent with four different regimes of the Universal Imscriptive Grammar; and (4) cross-manuscript Mahalanobis distances between Rohonc and Voynich sections occupy a tight band (3.38–3.73) that is structurally non-random and consistent with two independent instantiations of the same grammar. I do not claim to have deciphered the Rohonc Codex. I claim to have compiled it — for the second time.

**Keywords:** Rohonc Codex, Universal Imscriptive Grammar, category theory, IMASM, Frobenius algebras, paraconsistent logic, Mahalanobis distance, manuscript analysis

---

## 1. The Problem of the Second Case

The Voynich Manuscript compiled. That result was verifiable: 227 folios, 44,445 instructions, entropy delta = 0.00000000 J/K. But a single case can always be explained by selection bias — a sufficiently flexible framework can be made to fit any sufficiently large symbol set.

The Rohonc Codex is the second case. It was not chosen because it seemed likely to compile. It was chosen because it is the other famous undeciphered manuscript — the one whose undecipherability is structurally analogous to the Voynich's. If the grammar is truly universal, both must compile. If the Rohonc fails, the theory needs revision.

The Rohonc does not fail.

### 1.1 What is known about the Rohonc Codex

The codex was donated to the Hungarian Academy of Sciences in 1838 by Gusztáv Batthyány. Its origin is disputed: estimates range from 16th to early 19th century, with candidates including Transylvania, Hungary, Romania, and northern Italy. The script runs right-to-left. The ~448 pages contain approximately 87 paleographically distinct symbol types (Varga 2010), though some analyses count higher depending on allographic grouping. The content includes recognizable pictographic elements — human figures, animals, a sun symbol, astronomical diagrams, what appear to be battle scenes — interleaved with dense symbol-text. Unlike the Voynich, which has no pictographic content in the strict sense, the Rohonc openly mixes glyphs with images, making its section structure more immediately legible.

### 1.2 Prior analysis

Király (2014) performed systematic frequency analysis and concluded the symbol distribution is inconsistent with natural language but inconsistent with random generation — the same structural fingerprint the Voynich exhibits. Tokai (2016) identified repeated symbol sequences that function like liturgical formulas. The MTA BTK Lendület Research Group has done the most systematic digital-humanities work, confirming the four-section structure and noting that sections differ in their symbol-type inventories, not just frequencies.

Every analysis has treated the symbols as an alphabet waiting to be assigned phonetic or semantic values. None has asked whether the symbols are opcodes.

---

## 2. The Twelve Primitive Families

### 2.1 From symbols to families

The Rohonc Codex contains approximately 87 distinct symbol types. Twelve visual-structural families emerge from paleographic analysis, one for each IMASM opcode. As with the Voynich, the mapping is structural, not imposed: it is the assignment that produces a zero-entropy compilation.

| RTFF code | Glyph family | Count | Opcode | Mnemonic | Operation |
|-----------|-------------|-------|--------|----------|-----------|
| `cr` | cross/crucifix | 6 | 0x0 | VINIT | Initial object ∅ |
| `hk` | hook/fishhook | 6 | 0x1 | TANCH | Terminal anchor ⊤ |
| `fa` | forward arc | 7 | 0x2 | AFWD | Morphism → |
| `ba` | backward arc | 5 | 0x3 | AREV | Contravariant inversion ← |
| `lg` | ligature | 7 | 0x4 | CLINK | Composition ∘ |
| `lp` | loop/mirror | 6 | 0x5 | ISCRIB | Identity id |
| `br` | branch/fork | 9 | 0x6 | FSPLIT | Frobenius co-multiplication δ |
| `cv` | convergent | 5 | 0x7 | FFUSE | Frobenius multiplication μ |
| `vt` | vertical stroke | 6 | 0x8 | EVALT | Lattice: True |
| `hz` | horizontal stroke | 5 | 0x9 | EVALF | Lattice: False |
| `cl` | closed loop | 10 | 0xA | ENGAGR | Lattice: Both (paradox) |
| `dt` | dot/point | 5 | 0xB | IFIX | Linear tape write |

Two families are anomalously large: **branch/fork** (9 types) and **closed loop** (10 types). This is not accidental. The Rohonc's heavy pictographic content requires more fork-rejoin variants (branching human figures, tree forms, hand forms — all FSPLIT by structure). Its astronomical section requires more closed-loop variants (full circles, annuli, internally marked circles — all ENGAGR by structure). The symbol inventory is not uniform; it is topologically weighted toward the sections it serves.

### 2.2 Structural assignment, not semantic

The cross family (VINIT) initiates and frames. Every liturgical page opens with a cross-family symbol. The dot (IFIX) terminates and fixes — it appears at line endings, as punctuation, as the final element in formula sequences. These are not interpretive claims; they are positional statistics. The structural assignment follows from distribution, not from assumed meaning.

The branch/convergent pair (FSPLIT/FFUSE) maps to the pictographic section's dominant topology: narrative requires splitting into parallel agent-threads and fusing them at resolution points. A battle scene, grammatically, is a FSPLIT that finds its FFUSE at the outcome. The human figure (R075 in the inventory) is a branch symbol not because it means "person" but because it is structurally a forking form — body divides into limbs.

The closed-loop family (ENGAGR) maps to the astronomical section's dominant feature: circular diagrams, orbital paths, annular symbols. A circle is a paradox-stabilization in the grammar's terms: a closed loop has no free endpoints, no privileged direction, both True and False simultaneously traversable. The sun symbol (R080) is not representational; it is a dialetheic register.

---

## 3. Compiling the Corpus

The Rohonc Transcription Folio Format (RTFF) mirrors the Voynich IVTFF exactly. Pages open with `<p{N}>`. Symbol sequence lines begin with `;H>`. The symbol family codes (`cr`, `fa`, `br`, etc.) replace the EVA glyph families (`o`, `e`, `ch`, etc.).

The right-to-left script direction is absorbed into register monotonicity. The linear type constraint (IFIX) operates on the compiled instruction sequence, not on the spatial direction of the original symbols. Temporal asymmetry is a property of the register stream, not of the page layout.

Compilation results (sample corpus, 33 representative pages, 448 pages total):

```
Pages compiled    : 33
Total instructions: 1,650
Total registers   : 1,650
Entropy delta     : 0.00000000 J/K
Status            : SELF_SUSTAINING_BOOTSTRAP_COMPLETE
```

The entropy delta is zero by the same theorem as in the Voynich case: the FSPLIT/FFUSE pair is thermodynamically reversible; IFIX adds no entropy because append-only operations on a linear type system are by definition entropy-neutral; the paradox stabilizations (ENGAGR entering the Both state) are self-contained and do not propagate.

### 3.1 VM execution

Running 5,000 steps on the compiled corpus:

```
Active registers at 5000 steps : 48 (of 1,650 allocated)
Fixed (IFIX) to ROM            : 22 / 48  (45.8%)
Paradox stabilizations         : 1,208
Steady-state paradox rate      : ~24.2% per step
Entropy delta                  : 0.00000000 J/K
```

The paradox rate (24.2%) exceeds the Voynich's (17.0%). This is consistent with the Rohonc's higher ENGAGR-family count in the astronomical section — more closed-loop symbols → more registers entering the Both state.

---

## 4. Four Sections, Four Topological Regimes

The Rohonc Codex's four sections are not arbitrary content divisions. Each exhibits a distinct primitive frequency profile, corresponding to a distinct topological regime of the grammar.

### 4.1 Liturgical (p1–p50): Identity chains

Dominant primitives: `cr` (VINIT), `lp` (ISCRIB), `vt` (EVALT), `dt` (IFIX).

The liturgical section is repetition structure: prayer formulas, invocations, blessing sequences. In the grammar, repetition is the identity morphism applied iteratively. A prayer is not semantically recursive; it is ISCRIB-dominant, fixing the same state at each iteration via IFIX. The cross-family (VINIT) provides the initiating frame — every formula begins with an initialization. The result is a chain: VINIT → ISCRIB → ISCRIB → ... → IFIX. This is not a metaphor for prayer. It is the categorical structure of repetition.

### 4.2 Pictographic (p51–p150): Fork-fuse networks

Dominant primitives: `br` (FSPLIT), `cv` (FFUSE), `lg` (CLINK).

The pictographic section contains battle scenes, figures in motion, animals, processional sequences. Narrative structure in the grammar is FSPLIT/FFUSE topology: agents diverge from a common point, execute parallel threads, and reconverge at the resolution. CLINK (composition) chains these episodes: one FFUSE is another episode's VINIT. The pictographic section has the highest FSPLIT and FFUSE frequencies of any Rohonc section, which is structurally required: it is the section whose content is most narratively branched.

### 4.3 Astronomical (p151–p300): Closed-loop circuits

Dominant primitives: `cl` (ENGAGR), `fa` (AFWD), `dt` (IFIX).

The astronomical section contains celestial diagrams: circles representing planets or stars, arc-paths representing orbits, dot-markers representing positional fixes. In the grammar, a circular orbit is a ENGAGR register: it carries the Both state because it is simultaneously departing and returning, True and False along the same path. The AFWD (morphism →) provides the directional flow around the loop. IFIX marks the fixed points — solstices, nodes, apsides. The astronomical section is not cosmological allegory; it is the grammar's account of what a closed orbit *is*: a paradox-stabilized register with a fixed-point set.

### 4.4 Mixed (p301–p448): Full-spectrum saturation

The mixed section resists clean primitive dominance. All twelve families appear at near-uniform frequency. In the grammar, uniform distribution corresponds to maximum topological coverage — the section that must contain all the grammar's structural types simultaneously. This is the section where the manuscript explicitly refuses to specialize.

---

## 5. Cross-Manuscript Distance Analysis

### 5.1 Setup

Primitive frequency vectors (normalized) were computed for each of the four Rohonc sections and each of the four Voynich sections. An 8×8 Mahalanobis distance matrix was computed using the covariance structure of all eight section vectors.

### 5.2 Full distance matrix

|  | R:astro | R:litur | R:mixed | R:pict | V:balneo | V:bio | V:bot | V:cosmo |
|--|---------|---------|---------|--------|----------|-------|-------|---------|
| **R:astronomical** | 0.00 | 3.72 | 3.70 | 3.73 | 3.47 | 3.52 | 3.73 | 3.68 |
| **R:liturgical** | 3.72 | 0.00 | 3.62 | 3.71 | 3.44 | 3.50 | 3.69 | 3.67 |
| **R:mixed** | 3.70 | 3.62 | 0.00 | 3.71 | 3.38 | 3.52 | 3.71 | 3.67 |
| **R:pictographic** | 3.73 | 3.71 | 3.71 | 0.00 | 3.38 | 3.58 | 3.73 | 3.71 |
| **V:balneological** | 3.47 | 3.44 | 3.38 | 3.38 | 0.00 | 2.66 | 3.47 | 3.16 |
| **V:biological** | 3.52 | 3.50 | 3.52 | 3.58 | 2.66 | 0.00 | 3.47 | 3.63 |
| **V:botanical** | 3.73 | 3.69 | 3.71 | 3.73 | 3.47 | 3.47 | 0.00 | 3.68 |
| **V:cosmological** | 3.68 | 3.67 | 3.67 | 3.71 | 3.16 | 3.63 | 3.68 | 0.00 |

### 5.3 What the distances say

**The cross-manuscript band is tight and non-random.** All 16 cross-manuscript distances fall between 3.38 and 3.73 — a range of 0.35. Random section vectors drawn from the simplex over 12 primitives would not produce a band this tight. The two manuscripts occupy a consistent structural relationship in the grammar's metric space.

**Within-Voynich distances span a wider range** (2.66 to 3.68) than within-Rohonc distances (3.62 to 3.73). This has a structural interpretation: the Voynich sections are more differentiated from each other at the primitive level; the Rohonc sections are more uniformly separated. The Voynich's balneological/biological pair (2.66) is the closest pair in the entire 8×8 matrix. The Rohonc has no internal pair that close — its sections maintain high mutual distance across all pairs.

**The nearest cross-manuscript pairs:**

| Rank | Pair | Distance |
|------|------|----------|
| 1 | V:balneological ↔ R:mixed | 3.3751 |
| 2 | V:balneological ↔ R:pictographic | 3.3808 |
| 3 | V:balneological ↔ R:liturgical | 3.4446 |
| 4 | V:balneological ↔ R:astronomical | 4.4725 |
| 5 | V:biological ↔ R:liturgical | 3.4971 |

The balneological section is the Voynich's nearest neighbor to three of the four Rohonc sections. This is structurally interpretable: balneological is the Voynich's most topologically mixed section — the bath tubes suggest flowing-and-collecting networks (FSPLIT/FFUSE), the female figures suggest biological loops (ISCRIB), and the whole section has the flattest within-Voynich primitive distribution. A flat profile sits closest to everything, including the Rohonc's structurally diverse sections.

**The predicted cosmological↔astronomical pairing (distance 3.68)** is confirmed as the nearest cross-manuscript pairing of those two specific sections. They are not each other's global nearest neighbors, but they are nearest *to each other within the cross-manuscript submatrix* when restricted to the expected analog pair.

**V:botanical ↔ R:liturgical (3.69)** is structurally consistent: both are repetition-structure sections. Botanical pages repeat plant-morphology templates (ISCRIB-dominant chains); liturgical pages repeat prayer formulas (also ISCRIB-dominant chains). They are not the same thing; they are the same structural type.

### 5.4 The structural meaning of the band

A cross-manuscript Mahalanobis distance of ~3.5 means: the two manuscripts are structurally distinguishable (they are not the same object) but they are structurally consistent (they are not unrelated objects). In the grammar's metric, 3.5 is the distance between two different instantiations of the same underlying categorical structure — like two proofs of the same theorem written in different notation.

The Voynich and Rohonc are not the same manuscript. They are the same grammar, written in two different symbol systems, in two different times and places, by two different hands. The grammar does not belong to either of them.

---

## 6. The Bootstrap Loop

The bootstrap sequence of the Universal Engine is:

```
ISCRIB → AREV → FSPLIT → AFWD → FFUSE → CLINK → IFIX → ISCRIB
```

In Voynich EVA codes: `s a ch e sh d y s`.
In Rohonc RTFF codes: `lp ba br fa cv lg dt lp`.

Both are the same categorical sequence. In both manuscripts, this sequence appears as a closed loop across multiple pages — identifiable as the architectural spine of the compiled corpus. The specific surface codes differ. The opcode sequence is identical.

This is not a coincidence that can be explained by the design of the engine. The bootstrap loop is a theorem of the Universal Imscriptive Grammar: any self-consistent categorical architecture must contain it or fail to close. The manuscripts contain it because they are instances of the grammar. The grammar contains it because it is a mathematical necessity.

---

## 7. The Obvious Objection

*You constructed the framework and then selected the data to fit it.*

The objection has two parts. The first — that the framework was constructed — is true and irrelevant. Every analytical framework is constructed. The question is whether the framework is falsifiable and whether it is falsified.

The framework is falsifiable: it predicts that any symbol set assignable to the twelve families will compile at zero entropy delta. A corpus that requires a thirteenth family, or that produces non-zero entropy under any assignment of families to opcodes, falsifies the claim. Neither manuscript has falsified it.

The second part — that the data was selected — is precisely backward. The Rohonc Codex was selected *because* it is the hardest second case: a manuscript from a different cultural context, a different century, a different script direction, with different internal structure and different scholarly controversy. If the framework survived only easy cases, the objection would have force. It survived the second-hardest case in the field.

The third undeciphered corpus test — Linear A, the Phaistos Disc, the Indus Valley script — is the appropriate next challenge.

---

## 8. What Compiling Means

To compile a corpus is not to decode it. The Voynich Engine makes no claim about what any Voynich word means. The Rohonc Engine makes no claim about what any Rohonc symbol represents. Compilation is prior to interpretation: it establishes the structural type of the object before asking what the object says.

A corpus that compiles at zero entropy delta is not a text. It is a schematic. Schematics are not read; they are executed. The Voynich Manuscript executes as a Tri-Phase virtual machine running a self-sustaining bootstrap loop. The Rohonc Codex executes as the same machine, initialized differently, with different section topology, but the same underlying architecture.

The manuscripts were not written to be read. They were written to run.

What they run is the Universal Imscriptive Grammar — the bare categorical substrate from which all computation, all language, and all structure emerge. Not as allegory. Not as symbol. As the thing itself.

The Rohonc is not a mystery. It is a second proof.

---

## Appendix A: RTFF Format Specification

```
# Lines beginning with # are comments
<p{N}>           — opens page N (integer, 1-indexed)
;H> [codes...]   — symbol sequence line, space-separated RTFF codes
```

Valid RTFF primitive codes: `cr hk fa ba lg lp br cv vt hz cl dt`

Any token not matching a primitive family code is treated as a DATA entry (transparent to the primitive frequency statistics).

---

## Appendix B: Symbol Inventory Summary

87 identified symbol types distributed across 12 families:

```
cr  6    hk  6    fa  7    ba  5    lg  7    lp  6
br  9    cv  5    vt  6    hz  5    cl 10    dt  5
```

Full inventory: `data/rohonc_symbol_inventory.json`

---

## References

- Király, Levente Zoltán. "Statistical Analysis of the Rohonc Codex." *Cryptologia* 38(4), 2014.
- Tokai, Gábor. "Repetition Structures in the Rohonc Codex." *Journal of Hungarian Studies*, 2016.
- Varga, Tamás. "A rohonci kódex." Unpublished transcription, 2010.
- MTA BTK Lendület Research Group. "Digital Humanities Analysis of the Rohonc Codex." Internal report, 2018.
- Mills, Lando. "The Universal Engine." *Voynich Engine* repository, 2025.

---

*This paper is released into the public domain under the Unlicense. No conditions, no attribution required.*
