# Adaptiv betydelsekedja – test 000009–000011

## 000009 – rå lokal kontextinformation
För 9 338 angränsande reducerbara token:
- information mellan aktuell K och föregående grannes K: 2,339 bit
- aktuell K och nästa grannes K: 2,339 bit
Motsvarande P/S-information var mycket lägre.

Varning: rå MI med högkardinala kärnor kan vara starkt biaserad.

## 000010 – permutation
9 338 K→nästa-K-par.
- observerad MI: 2,339 bit
- 300 globala frekvensbevarande permutationer: null ca 0,000638 bit
- empiriskt p med +1-korrigering: 0,00332

Naiv permutation visar mycket stark lokal ordning, men detta är inte tillräckligt för semantik.

## 000011 – held-out folio-prediktion
Fem folio-blockerade folds.

Viktad:
- global nästa-K-baslinje: 15,22 %
- föregående K -> nästa K: 13,92 %

### Kritisk slutsats
Den lokala K-K-associationen generaliserar inte till nya folios och kan därför inte ännu tolkas som en stabil semantisk relation.

Det starka in-sample-resultatet kan komma från:
- folio-specifika ämnen,
- lokala återkommande formulär,
- kopierings/genereringsregler,
- kärnor som är begränsade till vissa sidor.

## Ny fråga
Är kärnorna organiserade i återkommande foliofamiljer, och sammanfaller sådana textfamiljer med manuskriptets sektioner/bildtyper?

Detta blir nästa bro mellan intern struktur och möjlig betydelse.
