# Voynich-komposition 1.24 — komponentreliabilitet

## Syfte
Reducera 1.16/1.23-axeln till enklaste reproducerbara mekanism utan att optimera nya vikter.

Samma 63 folios med minst 20 analyserbara rader som i 1.23.
Tre redan frysta dominerande komponenter testades separat:
1. total exakt återkomstbågtäthet per rad
2. korta återkomstbågar med gap 2–4 per rad
3. andel rader med minst två återkomstbågar

5000 permutationer per komponent och split.

## A. Alternerande rader
### Alla bågar
r = 0,66686
R² = 0,44471
0/5000 null >= real
p < 0,0002

### Korta gap 2–4
r = 0,55234
R² = 0,30508
0/5000
p < 0,0002

### Rader med flera bågar
r = 0,50260
R² = 0,25261
0/5000
p < 0,0002

## B. Första sammanhängande halvan mot andra
### Alla bågar
r = 0,34316
R² = 0,11776
41/5000 >= real
p = 0,00840

### Korta gap 2–4
r = 0,28418
R² = 0,08076
107/5000
p = 0,02160

### Rader med flera bågar
r = 0,16487
R² = 0,02718
509/5000
p = 0,10198

## Slutsats
Den mest stabila och enklaste reproducerbara folioprofilen är total exakt återkomsttäthet: hur ofta samma exakta ord återkommer inom en locus.

Korta gap 2–4 är också reproducerbara och verkar vara en andra egenskap hos samma återkomstsystem.

Måttet "rader med flera bågar" är stabilt vid interfolierad split men klarar inte den hårdare sammanhängande halvkontrollen på 5 %-nivå. Det bör därför inte betraktas som nödvändigt för kärnmekanismen.

Förenklad modell:
1. FOLIO-ÅTERKOMSTNIVÅ = total antal exakta inom-locus återkomstbågar per analyserbar rad.
2. KORT-RYTM = andel/täthet av dessa återkomster på gap 2–4.

Den tidigare femdimensionella axeln är fortfarande användbar som explorativ sammanfattning, men framtida bekräftande test bör i första hand använda dessa enklare, fördefinierade mått.

Detta minskar modellens frihetsgrader och risken för överanpassning.

## Nästa test
Använd endast FOLIO-ÅTERKOMSTNIVÅ som primärt mått och KORT-RYTM som sekundärt mått. Testa om samma folioprofil består när ordidentiteter kontrolleras för lokal ordfrekvens/vokabulär, så att hög återkomst inte bara betyder att foliot använder färre eller mer ojämnt fördelade ord.
