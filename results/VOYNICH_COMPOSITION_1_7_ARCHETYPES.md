# Voynich-komposition 1.7 — arketyper

## Exakta normaliserade former
Varje rad normaliserades efter första förekomst:
första nya ordet=A, nästa nya=B osv; återkommande ord återanvänder bokstaven.

860 rader har minst en återkomstbåge.
- 455 olika exakta normaliserade former
- 166 former förekommer minst två gånger
- 571/860 rader tillhör en återanvänd form
- topp 10 former täcker 75 rader
- topp 20 täcker 135

100 folio-lokala nuller:
- återanvända former: nullmedel 150,33; real 166; 3/100 >= real
- rader i återanvänd form: nullmedel 459,44; real 571; 0/100
- topp10-täckning: nullmedel 61,03; real 75; 0/100
- topp20: nullmedel 108,91; real 135; 0/100

Det finns alltså återanvändning, men inget litet alfabet av ett fåtal exakta mallar.

Vanligaste exakta former:
ABCDEBFG (9)
ABCDEDFG (9)
ABCBDEFGHI (8)
ABBCDE (8)
ABCBDE (7)
ABCDEFGDHI (7)
ABCDEFGBH (7)
ABCBDEFGH (7)
ABCDEFGHEIJ (7)

## Geometriska familjer
Bågrader grupperades grövre efter relationerna mellan bågar.

- enkel båge: 689; nullmedel 578,94; 0/100 >= real
- korsande: 29; null 18,56; 1/100
- separata/disjunkta: 29; null 17,93; 1/100
- nästlade: 28; null 18,24; 0/100
- shared endpoint: 39; null 33,03; 15/100

En mer komplex familj med nested+cross+shared:
- real 9
- nullmedel 2,50
- null q95 5
- 0/100 >= real

Små komplexa familjer har låga antal och ska tolkas försiktigt.

## Slutsats
Voynichs återkomstarkitektur verkar inte bestå av ett litet antal identiska mallar. Bättre beskrivning:
många konkreta variationer byggs ur ett mindre antal geometriska operationer — enkel återkomst, nästling, korsning, separation och delade ändpunkter.

Det passar en generativ kompositionsmodell bättre än en katalog av fasta rader:
en rad konstrueras genom att lägga återkomstoperationer ovanpå en ordsekvens.

Nästa steg:
bygg en minimal "kompositionsgrammatik" av dessa operationer och testa hur väl den kan generera/klassificera osedda Voynichrader jämfört med folio-lokala nuller.
