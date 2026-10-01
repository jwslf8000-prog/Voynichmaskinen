Stroke Grammar H2.1 — hierarchical whole-corpus test

Frozen families before test:
1. pedestal construction
2. ordinary gallows
3. minim-tail construction
Other EVA characters remain atomic. ch/sh is not counted as an independent factorization family.

Goal: test a hierarchical construction model rather than the flat stroke stream falsified in H2 test 005.

Coding structure:
- ordinary atomic characters are coded directly as atomic heads;
- pedestal events are coded as construction P plus separate aaa left/right component choices;
- ordinary gallows are coded as construction G plus separate aaa left/right choices;
- minim-tail events are coded as construction M plus minim-count and tail choices.
Components are not emitted as extra sequential word positions.

Evaluation: 36,241 clean ZL3b-n words; deterministic five-fold whole-folio holdout; same previous-head + four-bin relative-position context; add-0.5 smoothing; NLL normalized per original EVA character.

Implementation note:
An initial implementation redundantly coded family A and then atomic identity, heavily double-charging ordinary characters. It produced perplexity 11.08 and is invalid for the intended compact hierarchy. No family/component definitions were changed. The corrected implementation codes ordinary atoms directly and only opens the three frozen factorable constructions.

Corrected result:
Atomic EVA NLL/char 1.432368561; perplexity 4.188608426.
Hierarchical H2.1 NLL/char 1.415312498; perplexity 4.117773061.
Delta NLL -0.017056063.
Perplexity ratio 0.983088568: about 1.69% lower perplexity.

Fold deltas H2.1 - EVA NLL/char:
fold0 -0.0178574
fold1 -0.0140936
fold2 -0.0223195
fold3 -0.0171117
fold4 -0.0154690
H2.1 improves in all five held-out folio folds.

Interpretation:
The flat-stroke model remains falsified. A compact hierarchy that keeps ordinary symbols atomic while factorizing only independently replicated graphical constructions improves whole-corpus held-out description length. This is consistent with a construction grammar rather than a flat stroke alphabet.

This is not yet sufficient to establish a general Voynich construction grammar. Required next control: compare the same hierarchical model capacity against matched arbitrary alternative factorings/permutations of the internal component assignments. The external aaa/minim factorization must outperform those controls.

No semantic, phonetic, language, cipher, or historical-origin claim follows.