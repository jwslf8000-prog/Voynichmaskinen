# Voynich-komposition 1.9 — prefix-blind grammatik

## Viktig metodkorrigering
En första körning försökte använda första bågstart, gapklass och antal återkommande teman beräknade från hela raden för att klassificera hela radens bågarkitektur. Den gav extremt stora förbättringar men underkändes omedelbart som informationsläckage: prediktorerna var härledda ur samma bågar som målvariabeln.

De siffrorna räknas inte som evidens.

## Giltigt blindtest
För varje locus med minst fyra ord:
- visa endast första halvan av raden
- dölj andra halvan helt
- mål: kommer den dolda halvan att innehålla minst ett ord som återknyter till ett tema i den synliga halvan?
- hela folios hålls blinda i fem folds

3953 rader, 520 positiva mål.

Baseline använder endast total radlängd + synlig prefixlängd.
Baseline log-loss: 0,37027345.

Tillägg beräknade ENDAST från synlig halva:
- redan observerad intern repetition: 0,36715418; förbättring 0,00311927
- synligt internt gap: 0,36872025; förbättring 0,00155320
- synlig första återkomststart: 0,36777109; förbättring 0,00250236
- synlig unikhetsgrad: 0,36939597; förbättring 0,00087748
- alla tillsammans: 0,36951870; förbättring 0,00075475

## Slutsats
När informationsläckage tas bort finns en liten men konsekvent blind signal:
vad som redan har hänt geometriskt i första halvan hjälper något att förutsäga om den dolda halvan återknyter till ett tidigare tema.

Den största enskilda signalen är om den synliga halvan redan innehåller en intern repetition.

Att kombinera alla enkla variabler försämrar jämfört med bästa enskilda variabel, vilket talar mot att stapla regler utan starkare validering.

Nästa test bör isolera den bästa regeln ("synlig intern repetition") mot folio-lokala nullkorpusar och permutationer. Först om dess +0,00312 log-loss-förbättring överlever kontrollen ska den läggas till i grammatiken.
