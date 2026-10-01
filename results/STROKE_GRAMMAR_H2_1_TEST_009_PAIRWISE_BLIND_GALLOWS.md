Stroke Grammar H2.1 — test 009: grid-free blind gallows pair relations

Goal: test whether visually predicted gallows relations emerge from distributional behavior without imposing any 2x2 grid or component labels.

Dataset: 18,211 ordinary EVA t/k/p/f events; pedestal occurrences excluded.
For each glyph, empirical profiles were built for:
- preceding EVA character
- following EVA character
- within-word position
- word length

Pairwise distance = sum of Jensen-Shannon divergences across the four profiles, with 0.5 smoothing.
The aaa relations were not used in computing distances.

Whole-corpus pair distances, nearest first:
p-f 0.051497
t-k 0.056120
t-p 0.267083
t-f 0.267450
k-f 0.331957
k-p 0.387856

Thus p-f and t-k are dramatically closer than the other four pairs; the third-nearest distance is about 4.76 times the t-k distance and 5.19 times the p-f distance.

Five whole-folio test subsets:
In every one of the five folds, t-k and p-f are the two nearest pairs. Their internal ordering can switch, but the pair-of-pairs is stable.

This matches one independently documented aaa component relation:
- t and k share the p-family component;
- p and f share the x-family component.

The other aaa axis does not emerge as simple nearest-neighbor similarity, so this test should not be described as full blind recovery of the entire 2x2 geometry.

Interpretation:
Without giving the analysis a grid, component assignment, or visual pairing, distributional profiles recover a stable t-k / p-f division corresponding to one graphical component dimension. This is strong evidence that at least one visible gallows component relation tracks statistical behavior rather than being merely decorative resemblance.

No semantic, phonetic, language, cipher, or historical-origin inference follows.