Stroke Grammar H2 test 005 — global flat model

Frozen families before test:
1. pedestalled gallows: bench/frame plus aaa gallows components
2. minim-tail: minim count plus n/r/l/m tail
3. ordinary gallows: aaa q/l x p/x components
ch/sh was not counted as an independent factorization family.

Corpus: 36,241 clean ZL3b-n word positions.
Evaluation: deterministic five-fold whole-folio holdout.
Model: same first-order previous-token + four-bin relative-position model and add-0.5 smoothing for both representations. Score normalized per original EVA character.

Atomic EVA:
NLL/EVA char 1.432594822
perplexity 4.189556252

Flat H2 stroke expansion:
NLL/EVA char 1.433258553
perplexity 4.192337915

delta NLL +0.000663731 (H2 worse)
perplexity ratio 1.000663952 (~0.0664% worse)

Fold direction:
H2 better in folds 0 and 2; worse in folds 1, 3, 4.

Conclusion:
The preregistered flat whole-corpus stroke expansion does NOT improve held-out description length over atomic EVA. This is a negative result and must remain part of H2 evidence.

This does not erase the three family-level factorization results. It falsifies the stronger/simple model that all component strokes should be emitted as one flat first-order token stream. A plausible next model, if tested, must be preregistered as hierarchical: choose construction/family, then component values, rather than flattening strokes into ordinary sequential tokens.

No semantic, phonetic, language, cipher, or historical-origin conclusion follows.