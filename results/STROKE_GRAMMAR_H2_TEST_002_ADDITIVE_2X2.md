# Stroke Grammar H2 — test 002: additive 2x2 factorization

External aaa mapping is frozen:
cth = c2:q3:p3:c1
ckh = c2:l3:p3:c1
cph = c2:q3:x1:c1
cfh = c0:l3:x1:c1

Internal modifier factorization:
LEFT = q/l
RIGHT = p/x

Important methodological correction:
Using the pair (LEFT,RIGHT) as a categorical key is exactly one-to-one with t/k/p/f and therefore is only a relabeling, not evidence of compositionality.

The valid test forces an additive/factored model:
P(context | LEFT,RIGHT) is reconstructed from separate LEFT and RIGHT effects relative to the context baseline. The model cannot memorize the four modifier combinations as four categories.

Corpus: 2,120 pedestal events in clean ZL3b-n.
Evaluation: deterministic 5-fold whole-folio holdout.
Comparison:
- baseline ignores modifier
- FOUR treats t/k/p/f as unrelated categories
- ADDITIVE uses separate aaa LEFT and RIGHT stroke effects

Held-out results:

PREVIOUS CHARACTER
baseline NLL 1.466697
FOUR 1.412324
ADDITIVE 1.412791
FOUR gain 0.054374
ADDITIVE gain 0.053906
fraction of FOUR gain retained: 99.14%

FOLLOWING CHARACTER
baseline 1.523924
FOUR 1.504242
ADDITIVE 1.504571
FOUR gain 0.019682
ADDITIVE gain 0.019354
retained: 98.33%

WITHIN-WORD POSITION
baseline 1.102658
FOUR 1.049111
ADDITIVE 1.051490
FOUR gain 0.053547
ADDITIVE gain 0.051169
retained: 95.56%

WORD LENGTH
baseline 1.767755
FOUR 1.741256
ADDITIVE 1.744902
FOUR gain 0.026500
ADDITIVE gain 0.022853
retained: 86.24%

Interpretation:
The independently defined aaa 2x2 stroke factorization retains nearly all held-out contextual information carried by the four unfactored EVA pedestal categories, despite being constrained to separate component effects.

This is stronger evidence for compositional graphical construction than the previous categorical tests. The data are compatible with the behavioral role of a pedestal modifier being largely decomposable into effects associated with its visual left and right stroke components.

Caveats:
- cfh has c0 rather than c2 at the outer left frame.
- aaa was designed for graphical alignment, not semantics.
- This does not establish meaning, phonetic values, historical derivation, or a cipher mechanism.
- The next important replication is outside the pedestal family: test whether independent aaa component factorization also compresses contextual behavior of other Voynich glyph families (especially minim/tail families and ch/sh-related constructions).
