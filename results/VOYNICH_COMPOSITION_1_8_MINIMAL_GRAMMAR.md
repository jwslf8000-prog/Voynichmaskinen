# Voynich-komposition 1.8 — minimal kompositionsgrammatik

## Grammatik
Varje locus klassas enbart efter återkomstgeometri:
- none
- single
- nested
- cross
- disjoint
- complex

Klassantal i verkliga korpus:
none 3320
single 689
nested 30
cross 29
disjoint 33
complex 79

## Blind femfaldig folio-holdout
Modellen lär endast P(arkitektur | radlängdsbin) på träningsfolios.
Baseline lär global P(arkitektur).
Hela folios hålls blinda.

Log-loss per fold, baseline -> grammatik:
0: 0,65277 -> 0,60547
1: 0,66675 -> 0,61321
2: 0,62371 -> 0,59296
3: 0,63818 -> 0,58206
4: 0,73685 -> 0,68011

Viktat:
- baseline 0,66495
- grammatik 0,61558
- förbättring 0,04937

Vanlig accuracy är oförändrad 79,43 %, eftersom none är majoritetsklassen. Log-loss är därför det relevanta måttet: grammatiken ger bättre kalibrerade sannolikheter för alla arkitekturklasser.

## Avgörande folio-lokal null
100 korpusar skapades genom att ordtoken blandades inom varje folio medan exakt radlängd och foliospecifik tokenmängd bevarades. Samma femfoldsmodell kördes på varje null.

Förbättring baseline -> längdgrammatik:
- verkligt: 0,049372
- nullmedel: 0,030765
- null q95: 0,037117
- null max: 0,039819
- 0/100 nuller >= verkligt

## Slutsats
Radlängd bär blindt generaliserande information om återkomstarkitekturen, och sambandet är starkare i verkliga Voynich än i folio-lokala frekvensbevarande omblandningar.

Detta är den första mycket enkla generativa kompositionsgrammatiken som:
1. definieras utan semantik,
2. generaliserar till helt osedda folios,
3. slår samma mekanism i matchade nullkorpusar.

Den förklarar ännu inte vilka ord som återkommer eller varför. Den visar att radens storlek och dess återkomstgeometri är kopplade på ett manuskriptomfattande sätt.

Nästa test:
utöka grammatiken med endast preregistrerade geometriska variabler:
- normaliserad startposition för första bågen
- gapklass 1 / 2–4 / 5+
- antal olika återkommande teman
och testa om varje tillägg ger separat blind förbättring över längdmodellen.
