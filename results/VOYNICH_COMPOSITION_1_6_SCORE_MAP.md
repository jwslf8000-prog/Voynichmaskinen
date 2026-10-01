# Voynich-komposition 1.6 — partiturkartan

Orden behandlas här endast som identiteter. Varje upprepning av samma ord inom en locus bildar en båge mellan två positioner.

## Kontroll
100 deterministiska folio-lokala nuller:
- samma folios tokenmängd
- samma ordens foliofrekvenser
- exakt samma radlängder
- ordordningen förstörd genom omblandning inom folio

## Grundarkitektur
Verkligt / nullmedel:
- rader med minst en båge: 860 / 693,72
- alla bågar: 1310 / 996,84
- korta gap 2–4: 614 / 411,20
- rader med flera bågar: 171 / 115,83
- återanvända geometriska bågmönster: 683 / 556,92

0/100 nuller nådde verkligt resultat på dessa mått.

## Interaktion mellan bågar
Alla bågpar:
- nästlade: 1723 / null 528,25
- korsande: 2594 / null 529,94
- delad ändpunkt: 744 / null 399,36

Eftersom ett ord som förekommer 3+ gånger automatiskt skapar flera bågar gjordes en separat kontroll där endast bågpar från OLIKA temaord räknades.

### Olika temaord
- nästlade: real 1562; nullmedel 469,70; null max 856; 0/100 >= real
- korsande: real 2433; nullmedel 464,56; null max 826; 0/100
- separata/disjunkta: real 1163; nullmedel 471,03; null max 890; 0/100
- rader med minst två olika återkommande temaord: real 129; nullmedel 77,42; null max 92; 0/100

Den starka arkitektursignalen kan alltså inte förklaras enbart av att ett enda ord upprepas tre eller fler gånger.

## Tolkning
Voynichrader innehåller en ovanligt rik intern återkomstarkitektur. Flera olika ordteman återkommer inom samma rad och deras bågar korsar, nästlas eller bildar separata återkomstsegment mycket oftare än väntat när foliospecifik vokabulär/frekvens och radlängd bevaras.

Detta stödjer en strukturell "partitur"-beskrivning men etablerar inte bokstavlig musik, dikt, recept eller semantik.

En arbetsrepresentation kan nu vara:
rad = ordpositioner + bågar mellan återkommande identiteter.

Nästa test bör klassificera rader efter bågarkitektur och fråga om ett litet antal återkommande arketyper beskriver en oproportionerligt stor del av de 860 bågraderna. Därefter kan arketyperna jämföras blindt mot manuskriptets externa metadata.
