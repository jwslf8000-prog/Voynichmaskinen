# Graphic Modules H1 — test 002: pedestal family

Frozen family: cth, ckh, cph, cfh.

Question: do the four forms behave as members of one structural family rather than unrelated trigrams?

Corpus: ZL3b-n, clean EVA words.

Observed counts:
cth 928
ckh 906
cph 212
cfh 74

Context dimensions:
- four-bin relative within-word position
- immediately preceding EVA character, including word boundary
- immediately following EVA character, including word boundary
Similarity measured with Jensen-Shannon divergence.

Qualitative profile:
All four strongly share a small following-character repertoire dominated by y/e/o/a.
cth, cph and cfh have relatively similar positional profiles.
ckh is systematically shifted further into words and is the clearest within-family positional specialization.

Combined mean pairwise family distance (position + preceding + following):
0.1242522

Frequency-matched control:
300 deterministic four-trigram control groups, with each member frequency-matched to one pedestal member.
Control mean distance 0.9892334
Control median 0.9971366
Control 5th percentile approximately 0.6960
Best control 0.3669507
0/300 controls were as similar or more similar than pedestal family.
Empirical p = 0.0033223.

Interpretation:
The four pedestal forms are an unusually coherent contextual family. Together with test 001, where treating cth/cph/ckh/cfh as compound units improved held-out prediction beyond frequency-matched arbitrary trigram sets, two independent structural observations point in the same direction.

The family is not homogeneous: especially ckh has a distinct positional role. A parsimonious structural model is therefore a shared construction/frame with a variable internal gallows element whose identity modifies distributional function.

This does not establish meaning, historical abbreviation identity, language, or cipher mechanism.

Next test:
factor the pedestal forms into FRAME(c_h) + MODIFIER(t/k/p/f) and test whether modifier identity predicts surrounding context/word architecture on held-out folios better than treating the four forms as unrelated categorical units.
