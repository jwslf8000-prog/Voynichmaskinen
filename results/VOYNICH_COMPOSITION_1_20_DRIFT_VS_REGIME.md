# Voynich-komposition 1.20 — gradvis drift kontra abrupt regimskifte

Samma frysta 1.16-axel, samma 93 folios och samma manuskriptordning som 1.19.

## Linjär trend
Konstantmodell SSE = 447,5666.
Linjär trend SSE = 423,5410.
SSE-vinst = 24,0256.
R² = 0,05368.
Lutning över normaliserad manuskriptposition = +1,7419.

Axeln tenderar alltså att öka genom manuskriptordningen, men position ensam förklarar endast ca 5,4 % av variationen.

## Låst 1.19-brytpunkt efter trend
Brytpunkten ändrades inte:
f69r | f70r2, index 32.

Efter att den globala linjära trenden dragits bort:
- extra SSE-vinst från steget = 10,9372
- vänster residualmedel = -0,4735
- höger residualmedel = +0,2484

5000 permutationer av trendresidualerna vid den redan låsta punkten:
- null mean gain 4,5225
- q95 16,8338
- 589/5000 >= real
- p = 0,1180

Det abrupta steget är alltså inte tydligt efter att global drift räknats bort.

## Blockbevarande kontroll av linjär drift
För att inte förstöra all lokal autokorrelation delades serien i sammanhängande block om fem folios. Blockens ordning permuterades, medan ordningen inom varje block bevarades.

5000 blockpermutationer:
- real linjär R² = 0,05368
- null mean = 0,01719
- q95 = 0,06604
- 390/5000 >= real
- p = 0,07818

Den globala driften är starkare än genomsnittlig blockordning men når inte 5 %-nivå mot denna hårdare lokalt bevarande null.

## Slutsats
1.19:s blinda brytpunkt är verkligt ovanlig mot helt slumpad folioordning, men 1.20 visar att den inte kan separeras robust från en bredare gradvis/sektionell drift.

Bästa nuvarande beskrivning:
- återkomstarkitekturen har ordnings-/sektionsstruktur genom manuskriptet;
- det finns en övergripande tendens mot högre återkomsttäthet senare i serien;
- evidensen räcker inte för att låsa ett abrupt regimskifte vid f69r/f70r2;
- den linjära driften är själv bara måttlig mot blockbevarande null (p≈0,078).

Nästa steg bör inte optimera fler brytpunkter. Ett starkare test är att använda sammanhängande manuskriptblock som held-out data: uppskatta riktning/axel på en del och testa om ordningsgradienten reproduceras i andra oberoende block.
