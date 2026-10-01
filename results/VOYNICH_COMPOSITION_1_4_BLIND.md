# Voynich-komposition 1.4 — blind generalisering

## Hypotes
Kan variationsordets form på ett helt osedd folio förutsägas från:
tema A + båglängd (gap 2–4) + roll (only/first/middle/last)?

## Design
- 1 127 variationspositioner från A...A-bågar.
- Folios delades deterministiskt i fem folds.
- Fyra folds tränar, femte hålls helt blind.
- Mål testades separat: prefix2 och suffix2.
- Kontext används vid minst 3 träningsexempel; annars backoff till båglängd+roll.
- Baslinje: global vanligaste prefix2/suffix2 i respektive träningsmängd.
- Ingen information från testfolio används för träning.

## Resultat

Prefix2, viktat:
- global baseline: 17,5688 %
- tema+gap+roll: 15,9716 %
- delta: -1,5972 procentenheter

Suffix2, viktat:
- global baseline: 21,8279 %
- tema+gap+roll: 21,3842 %
- delta: -0,4437 procentenheter

Prefixmodellen slog inte baseline totalt och var sämre i de flesta folds.
Suffixmodellen gav blandade foldresultat men var också sämre totalt.

## Slutsats
Den starka lokala formkoncentrationen i Komposition 1.3 generaliserar inte som en universell regel av typen:
"samma tema A + samma båglängd + samma roll -> samma prefix/suffixklass"
över osedda folios.

Detta försvagar den globala kompositionsgrammatiken men inte fyndet från 1.1 att korta A...A-återkomstbågar är överrepresenterade även mot folio-lokal null.

Ny arbetshypotes:
kompositionsregeln kan vara lokal till folio, stycke, närliggande rader eller en latent radfamilj. Formen kan alltså skapas genom lokal variation snarare än en manuskriptomfattande fast A->B-regel.

Nästa test bör därför mäta närhetsberoende:
är två A...A-bågar med samma A mer lika i variationsform när de ligger nära varandra i manuskriptet än när de ligger långt ifrån varandra?
