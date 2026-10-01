# Voynich-PKT 0.1 – 000013 aktiv-händelseprediktion

Fem blinda folio-holdouts. Rå 00000-dominans togs bort genom två separata mål.

## A. Kommer nästa ord vara PKT-aktivt?
Prediktor: de två föregående ordens binära PKT-aktivitet.
Mått: balanced accuracy på blind test.

Foldar:
- 51,35 %
- 52,04 %
- 52,89 %
- 51,72 %
- 52,11 %

Medel: 52,02 %.

Det är endast svagt över 50 % och ger inte stöd för stark sekventiell prediktion.

## B. Om nästa ord är aktivt, vilken exakt aktiv PKT-profil?
Viktat över 944 aktiva blindmål:
- global vanligaste aktiva profil: 22,56 %
- två föregående exakta PKT-profiler: 22,03 %

PKT-kontext förbättrar alltså inte profilgissningen.

## Slutsats
Den generaliserande låg-PKT-egenskapen är inte i denna representation en enkel Markovkedja mellan PKT-profiler. Exakt textgissning är ännu inte etablerad.

Nästa test bör skilja strukturell/grammatisk position från PKT-sekvens: använd ordformskontext som prediktor och PKT-aktivitet/profil som mål på blinda folios.
