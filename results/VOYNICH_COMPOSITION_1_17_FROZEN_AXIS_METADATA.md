# Voynich-komposition 1.17 — fryst latent axel mot metadata

## Förregistrerad/frozen analys
Huvudaxeln från 1.16 ändrades inte.
Urval: 93 folios med minst 15 analyserbara rader.
Fem bågmått, robust standardisering och 1.16-loadings:
(0.530951, 0.428837, 0.730545, 0.013584, 0.017578).

Metadata öppnades först efter att axeln var fryst.

## IVTFF sidtyp $I
Gruppskillnad mätt med eta².
Real eta² = 0.21036.
5000 folio-permutationer:
- null mean 0.06476
- q95 0.13856
- 78/5000 >= real
- empiriskt p = 0.01580

Gruppmedel på axeln:
- H n28: -0.635
- S n25: +0.168
- T n6: +0.857
- B n19: +1.453
- P n8: +1.631
- C n6: +2.470
- A n1: -1.456 (för liten för tolkning)

## Currier $L
89 av de 93 hade A/B-label.
- A n33 mean -0.218
- B n56 mean +0.936
eta² = 0.06333.

5000 permutationer:
- null mean 0.01154
- q95 0.04284
- 82/5000 >= real
- p = 0.01660

Currier är alltså associerat med axeln, men förklarad variation är mycket mindre än för sidtyp I.

## Kontroll: sidtyp efter Currier
För de 89 folios med både I och L:
1. axelvärdet residualiserades genom att respektive Currier A/B-medel drogs bort.
2. I-labels permuterades endast inom samma Currier-stratum.
3. 5000 permutationer.

Resultat:
- residual sidtyp eta² = 0.22189
- null mean 0.05113
- q95 0.12086
- 12/5000 >= real
- empiriskt p = 0.00260

## Slutsats
Den frysta återkomstaxeln har ett statistiskt samband med etablerad sid-/innehållstyp.
Sambandet med sidtyp I kvarstår och blir tydligt även när Currier A/B kontrolleras genom residualisering och stratifierad permutation.

Detta stärker tolkningen att återkomstarkitekturen inte bara återupptäcker Currier-språken. Den bär information som sammanfaller med manuskriptets sid-/innehållsorganisation.

Detta är fortfarande strukturell evidens, inte semantisk översättning och inte bevis för en avsiktlig matematisk kod.

Nästa steg bör frysa H vs de högre axelgrupperna och testa om skillnaden kan reproduceras på radnivå/held-out folios, eller koppla axeln till konkret etablerad manuskriptsektion efter att IVTFF-kodernas betydelse dokumenterats.
