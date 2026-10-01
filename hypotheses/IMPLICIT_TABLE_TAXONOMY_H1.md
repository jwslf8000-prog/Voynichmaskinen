# H1 – Implicit tabell / taxonomisk tillhörighet

Status: förregistrerad hypotes. Ingen semantik antas.

## Hypotes
Voynichtextens återkommande interna delar kan fungera som tillhörighetsfält i en implicit tabell eller klassifikation snarare än enbart som ordmorfologi.

Arbetstermer:
- P = vänster/prefixstruktur
- K = kärnstruktur
- S = höger/suffixstruktur
- R = övrig/reststruktur

Dessa namn anger position/struktur, inte betydelse.

## Linné-analogin
Linné används endast som abstrakt jämförelse för hierarkisk klassifikation:
klass -> underklass -> medlem -> egenskap.
Testet får inte anta att Voynich beskriver botanisk taxonomi eller att någon komponent motsvarar en bestämd Linné-nivå.

## H1-förutsägelser
Om texten beter sig tabell-/klassifikationslikt bör minst flera av följande observeras:
1. vissa P/K/S-komponenter bildar stabila samförekomstgrupper,
2. grupperna återkommer över flera loci/folios och är inte bara sidlayout,
3. villkorliga kombinationer är starkare än frekvensen hos delarna var för sig,
4. nätverket uppvisar reproducerbar block-/hierarkistruktur,
5. dolda kombinationer kan förutsägas bättre än frekvensbaslinje,
6. struktur kan fortsätta över fysisk radgräns,
7. resultaten överlever när osäkra ordgränser hanteras separat.

## Testdesign
A. Bygg bipartita/tripartita nätverk P-K, K-S, P-S och P-K-S.
B. Mät grad, villkorlig sannolikhet, mutual information och community-struktur.
C. Jämför med randomiserade nätverk som bevarar komponentfrekvenser och rad-/foliofördelning.
D. Holdout: dölj observerade kombinationer och försök förutsäga dem.
E. Kör page-blocked holdout så samma sida inte finns i både träning och test.
F. Testa fysisk radgräns mot slumpmässigt valda gränser.
G. Kör separat för P/L/C/R och därefter jämförelse mellan klasser.

## Försvagande resultat
H1 försvagas om:
- grupper försvinner vid page-blocking,
- randomiserade kontroller ger samma struktur,
- komponentkombinationer inte generaliserar till osedda folios,
- radöverskridande samband inte skiljer sig från slump,
- nätverket huvudsakligen förklaras av några få högfrekventa token.

## Stark evidens
H1 stärks först när modellen kan göra blinda, reproducerbara förutsägelser om osedda kombinationer/strukturer och slå förregistrerade baslinjer.

## Viktigt
Ingen komponent får ges en betydelse som art, släkte, egenskap, mängd etc. innan oberoende tester stödjer en sådan funktion.
