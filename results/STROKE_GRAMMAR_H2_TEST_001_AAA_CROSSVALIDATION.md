# Stroke Grammar H2 — test 001: independent aaa cross-validation

External representation source: the analytical alignment alphabet (aaa), defined independently for Voynich transliteration/alignment.

Documented aaa mappings:
- cth = c2:q3:p3:c1
- ckh = c2:l3:p3:c1
- cph = c2:q3:x1:c1
- cfh = c0:l3:x1:c1

Thus the four EVA pedestal types factor approximately as a 2x2 combination:
LEFT gallows stroke = q vs l
RIGHT gallows stroke = p vs x
inside an outer c...c frame. Note: cfh uses c0 rather than c2 at the left edge, so the outer frame is not literally identical in aaa.

Corpus: ZL3b-n clean EVA.
Pedestal events: 2,120.
Whole-folio deterministic 5-fold holdout.

Question:
Do the independently defined aaa stroke dimensions preserve the distributional signal previously found for EVA modifier identity?

Predictors:
- coarse within-word position
- immediately preceding EVA character
No target information enters predictors.

LEFT aaa dimension q/l:
baseline logloss 0.692107
stroke model logloss 0.646187
gain 0.045920/event
baseline accuracy 53.77%
stroke accuracy 63.82%
logloss improved in all five folds. Accuracy improved strongly in four folds and was slightly lower in fold 2.

RIGHT aaa dimension p/x:
baseline logloss 0.396101
stroke model logloss 0.385570
gain 0.010531/event
baseline accuracy 86.51%
stroke accuracy 86.42%
The class is highly imbalanced, so accuracy is uninformative. Logloss improved in four of five folds and was slightly worse in fold 4.

Interpretation:
An independently designed graphical stroke decomposition recovers part of the held-out distributional structure previously observed for the t/k/p/f modifier labels. The strongest recovered dimension is the aaa left-stroke distinction q vs l.

This is cross-representation structural evidence for a component grammar: visual subcomponents are associated with reproducible positional/contextual roles.

It is not semantic evidence and does not establish phonetic values, historical derivation, cipher mechanism, or meaning.

Important caveat:
The aaa system was designed for alignment and stroke representation, not as a linguistic grammar. Also cfh differs in its left outer c component (c0 vs c2), so the simple shared-frame description is approximate.

Next test:
compare the 2x2 aaa factor model against an unfactored four-category modifier model on held-out prediction of multiple context targets. If the factored model retains most of the predictive information with fewer degrees of freedom, that would support compositional construction rather than four unrelated glyph classes.
