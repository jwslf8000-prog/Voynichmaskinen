# H1 – frekvensbevarande permutationstest 001

## Syfte
Testa om sambandet (P,K) -> S kan förklaras enbart av suffixens globala frekvenser.

## Fryst struktur
- samma Korpus 2.0
- samma produktivitetströsklar som H1 pass 1
- 18 produktiva tvåteckens-prefix
- 15 produktiva tvåteckens-suffix
- 18 608 användbara token
- fem deterministiska folio-blockerade folds

## Reproducerbarhetsregel
Vid lika träningsfrekvens mellan suffix väljs suffix deterministiskt i alfabetisk ordning.
Denna tie-break-regel låses från och med detta test.

Detta ger verklig held-out accuracy **60,9994 %**. Föregående pass rapporterade 60,76 % med en icke-explicit tie-break. Skillnaden dokumenteras och får inte döljas eller blandas.

## Nollmodell
Suffixetiketterna permuteras globalt mellan token.
Därmed bevaras exakt den globala suffixfrekvensen, medan kopplingen mellan (P,K) och S bryts.

200 deterministiskt seedade permutationer.

## Resultat
- verklig accuracy: **60,999 %**
- nollmodell medel: **23,868 %**
- nollmodell SD: **0,347 procentenheter**
- minimum: **22,902 %**
- 2,5-percentil: **23,234 %**
- median: **23,874 %**
- 97,5-percentil: **24,513 %**
- maximum: **24,617 %**
- empiriskt p med +1-korrektion: **0,00498**
- standardiserad separation: cirka **107 SD**

Ingen av 200 permutationer nådde den verkliga modellen.

## Slutsats
Den observerade (P,K)->S-strukturen kan inte i detta test förklaras av suffixens marginalfrekvenser ensamma.

Detta är stöd för verkligt kombinatoriskt beroende i textstrukturen, men är inte i sig bevis för att Voynichtexten är en tabell, taxonomi eller ett specifikt språk-/kodsystem.

## Nästa kontroller
1. K -> S utan P
2. P -> S utan K
3. held-out nya (P,K)-kombinationer
4. degree-/folio-bevarande nollmodell
5. fysisk radgräns kontra sekvensfortsättning
6. stabilitet mellan P/L/C/R
