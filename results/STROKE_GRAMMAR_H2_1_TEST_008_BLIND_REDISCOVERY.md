Stroke Grammar H2.1 — test 008: blind rediscovery of gallows structure

Goal: select gallows component geometry using training folios only, without using aaa labels to choose the partition, then evaluate on an untouched outer folio fold.

Dataset: 18,211 ordinary t/k/p/f gallows; pedestal occurrences excluded.
Outer evaluation: five deterministic whole-folio folds.
Inner selection: for each outer fold, a different held-out subset of the remaining training folios selected among candidate 2x2 structures using summed NLL for PRE, POST, position, and word length.

Result:
Across all five inner selections, the same favored equivalence class beat the remaining alternative structure. However, two nominally distinct 2x2 partitions (labelled AAA and C in the implementation) produced exactly identical additive likelihood on every split.

Therefore the blind procedure does NOT uniquely recover the externally named aaa geometry. It recovers an equivalence class of component relations under this additive model.

The selected class generalized to all five untouched outer folds, with summed local NLL:
fold0 5.829243326
fold1 5.785467110
fold2 5.902787518
fold3 5.879530204
fold4 5.741657791

Interpretation:
Distributional behavior alone contains stable information favoring one gallows factorization equivalence class over the remaining alternative, but the current additive representation has an identifiability symmetry and cannot distinguish every visually distinct orientation/partition.

This is a methodological limit, not a failed replication. Do not claim blind unique recovery of aaa.

Next test: abandon the 2x2 factorization assumption and compute direct held-out pairwise similarity/contrast among t,k,p,f over PRE, POST, position, and length. Ask whether the visually predicted shared-component pairs emerge from distributions without imposing a grid.

No semantic, phonetic, language, cipher, or historical-origin claim follows.