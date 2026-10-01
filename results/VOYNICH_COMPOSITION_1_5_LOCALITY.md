# Voynich-komposition 1.5 — lokal temautveckling

## Fråga
Är variationerna mellan samma tema A och samma båglängd mer lika när A...A-bågarna ligger nära varandra i manuskriptet?

## Rå jämförelse
614 bågar gav 1 615 par inom samma A+båglängd.

Prefix2-likhet:
- avstånd <=10 loci: 18,63 %
- avstånd >=500 loci: 13,07 %
- rå skillnad +5,56 procentenheter

Suffix2:
- <=10: 20,59 %
- >=500: 16,30 %
- rå skillnad +4,29 pp

## Hård permutation
500 deterministiska permutationer. Inom varje exakt A+båglängd-grupp behölls variationsmaterialet men dess manuskriptpositioner permuterades. Därmed kontrolleras temaordets egen form- och variationsbenägenhet.

Prefix2 nära-minus-långt:
- real +0,05560
- nullmedel +0,02042
- 103/500 nuller >= real
- empiriskt p ≈ 0,208

Suffix2:
- real +0,04288
- nullmedel +0,04618
- 254/500 >= real
- empiriskt p ≈ 0,509

## Slutsats
Den råa närhetseffekten överlever inte den tema-matchade permutationstesten. Vi har därför inte evidens för att variationernas prefix/suffix bildar lokala verser eller stycken på detta mått.

Det robusta fyndet från 1.1 kvarstår:
korta A...A-bågar med återkomst efter 2–4 positioner är kraftigt överrepresenterade mot folio-lokal null.

Arbetshypotesen ändras:
informationsbäraren kan ligga i själva återkomstarkitekturen — var och när ett tema återkommer — snarare än i en fast klass av mellanord.

Nästa spår bör modellera bågarnas geometri:
- vilket ord återkommer
- gap 2/3/4
- var i raden bågen börjar/slutar
- överlappande/nästlade bågar
- kedjor av återkomster
och jämföra denna arkitektur mot starka folio-lokala nuller.
