# Voynich-komposition 1.19 — blind brytpunkt längs manuskriptordningen

## Fryst representation
Samma 1.16-axel och samma urval: 93 folios med minst 15 analyserbara rader.
Folios ordnades efter folionummer och recto/verso.
Ingen quire-, illustration- eller Currier-metadata användes för att hitta brytpunkten.

## En-brytpunktsmodell
För varje tillåten position (minst 8 folios på vardera sidan) beräknades minskningen i SSE när serien delas i två medelregimer.

Starkaste blinda brytpunkt:
- mellan f69r och f70r2
- index 32/93
- SSE-vinst 53,8848

Topplösningarna låg samlat ungefär f58–f75, alltså ett övergångsområde snarare än en isolerad punkt.

## Global ordningsnull
5000 deterministiska permutationer av de 93 frysta axelvärdena; för varje permutation söktes den bästa brytpunkten på exakt samma sätt.

- real bästa vinst 53,8848
- null mean 19,2998
- null q95 43,3214
- 114/5000 nuller >= real
- empiriskt p = 0,0230

Det finns alltså evidens för ordningsberoende/regimstruktur i den faktiska manuskriptföljden.

## Quire öppnad efter brytpunkten
Den optimala punkten f69r | f70r2 ligger inom quire J, inte exakt på en quiregräns.
I det reducerade 93-foliourvalet ligger närmaste quiregränser:
- I -> J: f68v3 | f69r, en analyserad position före optimum
- J -> M: f70r2 | f75r, en position efter optimum

Därför ska resultatet inte beskrivas som att algoritmen exakt återfinner en quiregräns.
Säkrare beskrivning: ett blindt upptäckt övergångsbälte ligger kring I–J–M / ungefär f68–f75.

## Slutsats
Den frysta återkomstaxeln är inte slumpmässigt ordnad genom manuskriptet. En enkel tvåregimsmodell hittar en starkare brytpunkt än 97,7 % av helt ordningsslumpade kontroller.

Detta stödjer en sekventiell/sektionell förändring i återkomstarkitekturen, men avgör ännu inte om förändringen är:
1. en abrupt lokal regimväxling,
2. en gradvis drift genom manuskriptet,
3. flera regimskiften.

Nästa test ska jämföra en fryst linjär trendmodell mot en lokal brytpunktsmodell och blockbevarande nuller, utan metadataoptimering.
