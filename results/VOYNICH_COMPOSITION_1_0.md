# Voynich-komposition 1.0

Hypotesen testas utan antagande att manuskriptet bokstavligen är musik. Varje locus/rad behandlas som en fras. Fokus är återkomst, variation och positionsmönster.

## Material
4 180 loci med minst tre rena EVA-ord.

Vanligaste radlängder:
8 ord: 564
9 ord: 620
10 ord: 569
7 ord: 395
11 ord: 395
6 ord: 386.

Ingen hel rad upprepades exakt:
- exakta ordsekvenser: 4 180 / 4 180 unika
- exakta PKT-fingeravtryckssekvenser: 4 180 / 4 180 unika

Det finns alltså inga enkla identiska refränger i detta material.

## Abstrakta återkomstformer
När varje nytt ord i en rad betecknas A,B,C... och återkommande ord återanvänder samma bokstav finns 480 olika former; 184 former förekommer mer än en gång.

Exempel på återkommande former:
- ABCDEBFG
- ABCDEDFG
- ABCBDEFGHI
- ABBCDE

## Test av lokal ordåterkomst
Verkligt:
- 860 rader har minst en intern exakt ordåterkomst
- 1 310 återkomstpar totalt

100 deterministiska nuller skapades genom global tokenomblandning samtidigt som varje rads längd bevarades.

Null:
- rader med återkomst: medel 367,28; 95-percentil 398
- återkomstpar: medel 443,66; 95-percentil 479
- 0/100 nuller nådde verkligt resultat på båda måtten

Återkomst efter positionsavstånd:
gap 1: real 267, nullmedel 82,91
gap 2: real 261, nullmedel 71,14
gap 3: real 193, nullmedel 61,62
gap 4: real 160, nullmedel 50,23
gap 5: real 88, nullmedel 41,58
gap 6: real 68, nullmedel 30,65
gap 7: real 39, nullmedel 23,33
gap 8: real 29, nullmedel 16,15
gap 9: real 17, nullmedel 11,07
gap 10: real 7, nullmedel 7,46

## Tolkning
Voynichtexten har mycket starkare kortdistans-återkomst inom rader än en global frekvensbevarande tokenomblandning. Överskottet avtar med avstånd och är borta omkring gap 10.

Detta är förenligt med lokal fras-/kompositionsstruktur, men bevisar inte dikt, sång, recept eller tabell. En starkare null måste bevara varje ords lokala repetitionsbenägenhet och folio/sektion innan strukturen kan tillskrivas en kompositionsregel.

Nästa test:
lokalt block-/folio-bevarande null samt analys av A-B-A, A-B-C-A och andra återkomstmotiv.
