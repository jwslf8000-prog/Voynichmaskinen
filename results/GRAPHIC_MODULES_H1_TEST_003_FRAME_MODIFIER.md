# Graphic Modules H1 — test 003: FRAME + MODIFIER

Frozen construction from tests 001–002:
FRAME = c_h
MODIFIER = t / k / p / f

Corpus: ZL3b-n clean EVA words.
2,120 pedestal events:
t 928
k 906
p 212
f 74

Five deterministic whole-folio held-out folds.

## Test A: can local word architecture predict modifier identity?
Baseline uses training-fold modifier frequencies only.

Baseline:
logloss 1.07512
accuracy 41.23%

Position in word only:
logloss 1.02157
gain 0.05355/event
accuracy 56.60%
Improvement occurs in all five held-out folds.

Immediately preceding character only:
logloss 1.01791
gain 0.05722/event
accuracy 56.56%
Improvement occurs in all five folds.

Immediately following character only:
logloss 1.05357
gain 0.02155/event
accuracy 49.95%.

Word length only:
logloss 1.05060
gain 0.02452/event
accuracy 52.22%.

More detailed feature combinations do not outperform the simple position/pre-character models, consistent with a relatively simple local rule rather than whole-word memorization.

## Test B: does modifier identity predict the character after the frame?
Baseline ignores modifier:
logloss 1.53359
accuracy 41.89%

Given modifier t/k/p/f:
logloss 1.51293
gain 0.02067/event
accuracy 43.16%.

Logloss improves in four of five folds; fold 4 is essentially flat/slightly worse. This is weaker than Test A but points in the reciprocal direction.

## Interpretation
The internal gallows identity is not an interchangeable graphic variant. Its identity carries held-out information about where the shared c_h frame occurs and about its immediate context.

Together with tests 001 and 002, the most parsimonious current structural hypothesis is:
- c_h behaves as a shared construction/frame;
- t/k/p/f behaves as a modifier with distributional consequences;
- especially k has a different positional role from the other family members.

This is structural evidence only. It does not assign semantic meaning, identify a historical abbreviation, or establish language/cipher mechanism.

Next:
test whether the same FRAME + MODIFIER principle exists outside pedestal forms, especially gallows without c_h and ch/sh families. A repeated factorization principle would support a general Voynich construction grammar rather than one exceptional symbol family.
