# Voynich-komposition 1.23 — intern folio-replikation av återkomstaxeln

## Fråga
Är 1.16:s återkomstaxel en reproducerbar egenskap hos ett folio, eller främst mätbrus från enstaka repetitiva rader?

Axeln och dess fem vikter frystes oförändrade.
För att båda delarna skulle ha rimligt antal rader krävdes minst 20 analyserbara rader per folio.
63 folios uppfyllde kravet.

## Test A: alternerande rader
Udda och jämna analyserbara rader bildade två oberoende halvor.
Samma fem bågmått och samma frysta axel beräknades separat.

Korrelation mellan halvor:
- Pearson r = 0,64736
- R² = 0,4191

5000 permutationer där andra-halvans foliokoppling slumpades:
- null mean r = 0,00153
- q95 = 0,22507
- 0/5000 >= real
- p < 0,0002 (empiriskt +1: 0,00019996)

## Test B: första sammanhängande halvan mot andra
Varje folios analyserbara rader delades i två sammanhängande halvor.

Korrelation:
- r = 0,27479
- R² = 0,07551

5000 permutationer:
- q95 = 0,25804
- 197/5000 >= real
- p = 0,03959

## Tolkning
Återkomstaxeln reproduceras starkt när två utspridda, oberoende radprov tas från samma folio. Den reproduceras också svagare men fortfarande positivt mellan folions första och andra sammanhängande halva.

Skillnaden mellan testen tyder på två skalor samtidigt:
1. en stabil folioövergripande profil;
2. lokal drift/heterogenitet inom ett folio som gör sammanhängande halvor mindre lika än interfolierade prov.

Detta är stark evidens för att axeln inte bara är brus från enstaka rader eller metadata. Den mäter en faktisk statistisk egenskap hos hur ord återkommer inom loci på samma folio.

Det säger fortfarande inte vad egenskapen betyder semantiskt.

## Nästa steg
Frys split-half-resultatet och testa vilken av de tre dominerande axelkomponenterna som bär reliabiliteten:
- total bågtäthet
- korta gap 2–4
- rader med flera bågar

Gör komponentvis split-half utan att optimera vikter. Då kan vi reducera axeln till den enklaste reproducerbara mekanismen.
