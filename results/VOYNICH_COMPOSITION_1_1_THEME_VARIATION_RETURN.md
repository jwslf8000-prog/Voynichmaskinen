# Voynich-komposition 1.1 — tema → variation → återkomst

## Fråga
Finns ett lokalt motiv där ett ord/tema introduceras, en kort variation följer och samma ord sedan återkommer?

Motivnotation:
- ABA = tema, ett annat ord, tema
- ABCA = tema, två andra ord, tema
- ABCDA = tema, tre andra ord, tema

## Starkare null
100 deterministiska nullkorpusar.
Ordtoken blandades endast inom samma folio och varje locus behöll exakt sin ursprungliga längd.

Därmed bevaras:
- foliospecifik vokabulär och frekvens
- varje folios tokenmängd
- radlängder
men lokal ordordning förstörs.

## Alla återkomstbågar, gap 2–8
Verkligt: 838
Nullmedel: 647,04
Null 95-percentil: 685
0/100 nuller >= verkligt.

### Efter avstånd
gap 2: 261 vs null 162,44; 0/100 >= real
gap 3: 193 vs 136,49; 0/100
gap 4: 160 vs 112,27; 0/100
gap 5: 88 vs 87,22; 46/100
gap 6: 68 vs 65,90; 43/100
gap 7: 39 vs 49,10; 92/100
gap 8: 29 vs 33,62; 83/100

Överskottet är alltså koncentrerat till kort återkomst efter 2–4 positioner.

## Motiv
ABA:
- real 251
- nullmedel 157,96
- null q95 182
- 0/100 null >= real

ABCA:
- real 168
- nullmedel 128,94
- null q95 148
- 0/100

ABCDA:
- real 142
- nullmedel 101,85
- null q95 120
- 0/100

Ett mer komplext symmetriskt motiv ABCBA förekommer 4 gånger mot nullmedel 0,76 (0/100 >= real), men antalet är för litet för stark slutsats.

## Tolkning
Det finns en robust lokal ordningssignal av formen:
tema → kort variation → återkomst av samma tema.

Den överlever en folio-lokal frekvenskontroll och är främst begränsad till 2–4 ords avstånd.

Detta etablerar inte att texten är musik, dikt eller recept. Det visar däremot att lokal återkomst är organiserad av ordordningen och inte enbart av global eller foliospecifik ordfrekvens.

## Nästa steg
Studera vad som händer i variationsplatserna B/C/D:
1. Är variationsorden från samma PKT-klassfamiljer?
2. Är variationen systematisk mellan olika förekomster av samma temaord?
3. Finns återkommande övergångar tema→variation och variation→tema?
4. Kan en variation förutsägas blindt från temaordet och båglängden?

Detta är den första konkreta modellen för "komposition" som kan testas prediktivt.
