Stroke Grammar H2.1 — test 007: blind gallows geometry discrimination

Question: among all possible 2x2 factorizations of ordinary EVA t/k/p/f, is the independently motivated aaa q/l x p/x geometry unusually good at predicting local held-out properties?

Dataset: 18,211 ordinary gallows events. Pedestalled c[t/k/p/f]h occurrences excluded.
Evaluation: five deterministic whole-folio held-out folds.
No global H2.1 likelihood target was used.

For every one of the 24 labelled assignments of t/k/p/f to a 2x2 grid, an additive component model predicted four external/local properties:
- previous EVA character
- following EVA character
- within-word position
- word length

AAA assignment corresponds to:
t=(q,p), k=(l,p), p=(q,x), f=(l,x).

AAA held-out NLL:
PRE 1.316302728
POST 1.605006340
POSITION 0.983216333
LENGTH 1.917743908
sum 5.822269309

Result:
AAA is in the best class by summed held-out NLL.
No labelled assignment has strictly lower summed NLL.
Eight labelled assignments tie exactly with AAA.

Important symmetry correction:
Those eight ties are not eight distinct structural hypotheses. A 2x2 factorization is invariant to swapping binary labels on either axis and swapping the two axes. The 24 labelled assignments therefore collapse into three unique unlabeled 2x2 partitions, with eight label/axis symmetries per partition.

Thus the aaa partition ranks 1st of the 3 genuinely distinct 2x2 gallows partitions on the combined local held-out criterion.

Interpretation:
This resolves part of the ambiguity seen in test 006. Global hierarchical corpus likelihood did not uniquely favor aaa and could favor another partition. But on the preregistered local properties that originally motivated component behavior, the aaa partition is the best unique partition. This supports, but does not prove, the specific visual/statistical gallows geometry.

The evidence now separates two questions:
1. hierarchical factorization is useful globally;
2. the aaa gallows partition is specifically favored by independent local/contextual prediction.

No semantic, phonetic, language, cipher, or historical-origin inference follows.