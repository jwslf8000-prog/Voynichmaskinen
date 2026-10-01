# Voynich-komposition 1.14 — Currier A/B:s bågarkitektur mot egen null

## Frysta mått
Samma mått som i komposition 1.6:
- alla exakta återkomstbågar
- korta gap 2–4
- rader med minst två bågar
- nästlade bågpar mellan olika temaord
- korsande bågpar mellan olika temaord

Inga nya gap eller arketyper valdes.

Varje Currier-grupp jämfördes med 300 egna folio-lokala token-shuffle nuller som bevarar folioordförråd/frekvenser och exakta radlängder.

## Currier A
1505 analyserbara rader.

Alla bågar:
313 vs null 257,20 = 1,217x; z=3,66; 0/300 >= real.

Korta gap 2–4:
163 vs 126,34 = 1,290x; z=3,35; 0/300.

Rader med flera bågar:
40 vs 28,43 = 1,407x; z=2,46; 3/300.

Nästlade olika teman:
16 vs 8,27 = 1,935x; z=2,04; 9/300.

Korsande olika teman:
20 vs 8,26 = 2,421x; z=3,30; 3/300.

## Currier B
2461 analyserbara rader.

Alla bågar:
763 vs null 556,47 = 1,371x; z=9,21; 0/300.

Korta gap 2–4:
420 vs 253,73 = 1,655x; z=11,58; 0/300.

Rader med flera bågar:
107 vs 64,05 = 1,671x; z=6,27; 0/300.

Nästlade olika teman:
48 vs 27,13 = 1,769x; z=2,53; 7/300.

Korsande olika teman:
43 vs 26,86 = 1,601x; z=2,10; 14/300.

## Tolkning
B visar större överskott relativt sin egen null för:
- total återkomsttäthet
- korta återkomster
- rader med flera bågar

A visar däremot större relativt överskott för korsande olika-tema-bågar, och något större ratio för nästling.

Det är därför för grovt att säga att B bara är "mer komponerat".
Bättre strukturell beskrivning:
- Currier B: tätare, kortare och oftare multipel återkomstarkitektur.
- Currier A: glesare återkomstarkitektur men relativt stark geometrisk korsning när flera olika teman återkommer.

Detta är förenligt med att A och B använder olika parametrar inom samma breda återkomstsystem.

Nästa test bör därför använda samma frysta geometriska mått för att klassificera A/B blindt på rad- eller folionivå. Om bågarkitekturen ensam kan förutsäga Currier-grupp på osedda folios visar det att kompositionsstrukturen bär information som sammanfaller med den etablerade språkdelningen.
