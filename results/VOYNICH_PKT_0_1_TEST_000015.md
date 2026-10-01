# Voynich-PKT 0.1 – 000015 blind exakt nästa-ord-gissning

## Upplägg
Fem folio-holdouts. Nästa ord hålls dolt.
Endast ord som förekommer i träningsmaterialets vokabulär räknas, så modellen har en faktisk möjlighet att välja facit.

Baseline:
global träningsfrekvens för ord.

Kontextmodell:
backoff-rangordning med
- exakt föregående ord
- föregående ords sista två tecken
- sista tecken
- grov position i locus (early/mid/last)
- föregående ords PKT-aktivitet

Ingen testfolio används för träning.

Totalt utvärderbara blinda mål: 24 814.

## Viktat resultat
Top-1:
- baseline 2,5429 %
- kontext+PKT 3,1514 %
- relativ lift 1,2393x (+23,9 %)

Top-5:
- baseline 8,4992 %
- kontext+PKT 9,8896 %
- lift 1,1636x (+16,4 %)

Top-10:
- baseline 13,8027 %
- kontext+PKT 14,5684 %
- lift 1,0555x (+5,5 %)

Top-1 förbättrades i samtliga fem folds:
- f0 2,359 % -> 3,061 %
- f1 1,856 % -> 2,887 %
- f2 2,782 % -> 3,283 %
- f3 3,019 % -> 3,265 %
- f4 2,951 % -> 3,355 %

## Tolkning
Detta är första direkta blindtestet i serien där det exakta nästa Voynichordet rangordnas bättre än global ordfrekvens i alla fem folds.

Absolut top-1 är fortfarande låg (3,15 %), så detta är inte läsning/översättning. Modellen blandar vanlig lokal ordformskontext med en PKT-bit; testet visar ännu inte hur mycket av förbättringen som specifikt kommer från PKT.

Nästa obligatoriska ablation:
kör exakt samma kontextmodell utan PKT-biten. Skillnaden mellan med/utan PKT avgör om PKT faktiskt bidrar till exakt ordgissning.
