LINE GRAMMAR G1 — test 001: line-internal structural roles

Scope and guardrail:
A physical Voynich transcription line is treated as a neutral line/locus, not assumed to be a linguistic sentence.
Corpus: ZL3b-n exact parser used by the project.

PART A — coarse graphic-family zone prediction
Words were tagged with coarse structural features including pedestal, ordinary gallows, minim-tail, bench-start/end, qo-start and common ending. Positions were reduced to START/MID/END thirds. Five whole-folio held-out folds tested whether these features predict line zone.

Result: negative. Structural-feature logloss was slightly worse than the zone-prior baseline in all five folds (gain approximately -0.0046 to -0.0086 NLL/event). Therefore PED/GAL/MIN-style families alone do not provide a simple beginning/middle/end grammar.

PART B — relations between adjacent words
Restricted to 4,180 lines with at least 3 clean words. For each adjacent pair measured exact repetition, edit-distance<=1 near repetition, same first character, same final character, and word-length direction.

Aggregate rates:
START: exact .00648; near .03811; same-start .16689; same-end .30523; longer .37645; shorter .43493.
MID: exact .01058; near .04810; same-start .19620; same-end .30789; longer .40057; shorter .40651.
END: exact .00848; near .04027; same-start .20008; same-end .27282; longer .40649; shorter .41810.

Qualitative pattern:
- adjacent exact/near variation peaks in the middle;
- shared initial rises from start toward mid/end;
- shared ending is maintained at start/mid but drops at the end;
- early transitions more often shorten than lengthen; the imbalance is smaller later.

The broad tendencies recur across the five folio subsets, although individual rates vary.

Interpretation:
The first G1 result does not support a simple sequence of fixed graphic word classes. It instead suggests that line organization may be relational: an initial establishment region, a more locally repetitive/variant middle, and a terminal region where ending continuity weakens. These labels are descriptive hypotheses, not semantic or linguistic categories.

Next required tests:
1. quantify significance against within-line and folio-local order shuffles while preserving word inventory and line length;
2. use richer word-family similarity rather than first/last character alone;
3. test whether the pattern predicts unseen line order and whether it survives Currier/quire controls.

No claim that lines are sentences, or that meanings have been decoded.