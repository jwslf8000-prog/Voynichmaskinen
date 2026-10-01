# Voynich-PKT 0.1 – 000016 obligatorisk PKT-ablation

Samma fem folio-holdouts, samma backoffmodell, samma kandidatord och samma 24 814 utvärderbara mål som test 000015. Enda ändringen: PKT-aktiviteten för föregående ord tas bort ur kontextnycklarna.

## Resultat

Exakt nästa ord, viktat:

Top-1
- kontext + PKT: 3,15145 %
- samma kontext utan PKT: 3,16757 %
- PKT-delta: -0,01612 procentenheter

Top-5
- kontext + PKT: 9,88958 %
- utan PKT: 9,91376 %
- PKT-delta: -0,02418 procentenheter

Top-10
- kontext + PKT: 14,56839 %
- utan PKT: 14,61675 %
- PKT-delta: -0,04836 procentenheter

## Slutsats

PKT bidrar INTE till förbättringen i exakt ordgissning i modell 000015. Den lilla skillnaden går tvärtom till modellen utan PKT.

Därför ska resultatet från 000015 omformuleras:
- lokal Voynich-ordkontext förbättrar blind exakt ordprediktion jämfört med global frekvens;
- test 000016 visar att denna förbättring inte kan tillskrivas den binära PKT-funktionen.

Separata PKT-resultat kvarstår:
- vissa tecken->tal-nycklar ger generaliserande låg PKT-aktivitet över folio-holdouts;
- denna effekt skiljer sig från enkla slump- och Markovkontroller;
- PKT-aktivitet kan förutsägas från lokal ordform/position med cirka 1,88x AUPRC-lift.

Men ingen förbättrad exakt ordgissning från PKT är etablerad.

Nästa rimliga PKT-test är att använda rikare numeriska egenskaper än binär aktiv/inaktiv och göra strikt ablation mot identisk ordkontext.
