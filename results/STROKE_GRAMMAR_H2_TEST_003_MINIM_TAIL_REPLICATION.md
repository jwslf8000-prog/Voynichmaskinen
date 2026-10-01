# Stroke Grammar H2 — test 003: minim + tail replication

Goal: replicate graphical compositionality outside the pedestal family.

Frozen family:
i{1,3} followed by tail n/r/l/m.
The model does not select forms by outcome.

Clean ZL3b-n:
6,966 minim+tail events.

Main observed forms:
iin 4,157
in 1,737
ir 618
iir 168
iiin 168
im 48
il 36
iil 14
iim 13
iiil 4
iiir 3

Component counts:
minim run 1: 2,439
run 2: 4,352
run 3: 175
tail n: 6,062
r: 789
l: 54
m: 61

Evaluation:
five deterministic whole-folio holdout folds.
Targets are external context/architecture: previous char, following char, within-word position, word length.

WHOLE model may memorize each complete form (in, iin, ir, iir, ...).
ADDITIVE model is forbidden to memorize combinations and reconstructs behavior from separate effects of:
- minim count (1/2/3)
- tail identity (n/r/l/m)

Held-out signal retained by additive factorization relative to WHOLE gain:

previous character: 87.81%
following character: 86.38%
within-word position: 81.89%
word length: 84.14%

Detailed NLL:

PRE
baseline 0.234532
whole 0.223869
additive 0.225169

POST
baseline 0.381779
whole 0.339553
additive 0.345306

POSITION
baseline 0.834680
whole 0.792425
additive 0.800078

LENGTH
baseline 1.893795
whole 1.850456
additive 1.857331

The component model improves over baseline across the held-out folds and retains most of the complete-form information.

Interpretation:
The component-factorization principle replicates outside pedestal glyphs in a larger independent family. Minim-run count and tail identity behave as separable contributors to contextual distribution.

This also resolves an apparent tension with Graphic Modules H1 test 001: naively collapsing minim strings into single modules worsened prediction. H2 predicts the opposite representation — do not collapse them; preserve their internal minim-count + tail composition.

Current evidence therefore supports at least two compositional families:
1. pedestal: left aaa stroke + right aaa stroke inside a bench/frame;
2. minim-tail: minim count + tail type.

No semantic, phonetic, cipher, or historical meaning is assigned.

Next test:
seek a third independent family, preferably ch/sh/bench-related or other aaa stroke families, before proposing a general Voynich construction grammar.
