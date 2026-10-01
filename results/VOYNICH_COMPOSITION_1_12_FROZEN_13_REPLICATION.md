# Voynich-komposition 1.12 — fryst {1,3}-replikation

## Fryst regel
Efter första återkomsthändelsen mäts avståndet till den andra.
Träff = exakt +1 eller +3 positioner.
Regeln valdes i 1.11 och ändrades inte här.

Folios delades deterministiskt i fem separata folds.

## Verkliga folds
Andra återkomstfall / {1,3}-träffar / andel:
- fold0: 30 / 17 / 56,67 %
- fold1: 48 / 24 / 50,00 %
- fold2: 23 / 11 / 47,83 %
- fold3: 27 / 9 / 33,33 %
- fold4: 43 / 24 / 55,81 %

Olika-tema {1,3}-andel av alla andra-återkomstfall:
- f0 33,33 %
- f1 31,25 %
- f2 43,48 %
- f3 29,63 %
- f4 25,58 %

## Fold-specifika nuller
För varje fold kördes 300 nya folio-lokala token-shuffle nuller endast på den foldens folios.

{1,3} total:
- f0 real 56,67 %, nullmean 43,13 %, p≈0,136
- f1 50,00 %, null 39,37 %, p≈0,146
- f2 47,83 %, null 43,87 %, p≈0,372
- f3 33,33 %, null 38,64 %, p≈0,714
- f4 55,81 %, null 34,77 %, p≈0,0199

Olika teman:
- f0 real 33,33 %, null 24,65 %, p≈0,259
- f1 31,25 %, null 22,89 %, p≈0,166
- f2 43,48 %, null 24,04 %, p≈0,0399
- f3 29,63 %, null 21,68 %, p≈0,186
- f4 25,58 %, null 19,64 %, p≈0,209

## Slutsats
Den frysta {1,3}-rytmen är inte en universell regel som är individuellt signifikant i varje foliofold.
Riktningen är över null i folds 0,1,2,4 för total {1,3}, men fold3 går åt motsatt håll. Endast fold4 är individuellt tydlig för totalrytmen; fold2 för olika-tema-varianten.

Detta är ändå förenligt med en manuskriptomfattande statistisk tendens som är heterogen mellan delar, men 1.12 ger inte stöd för att låsa {1,3} som en generell kompositionsregel.

Den viktiga nya frågan är därför vad som skiljer fold3 från fold4. För att undvika efterhandsanpassning bör nästa test inte optimera en ny rytm per fold. I stället bör vi öppna extern metadata först efter denna frysta skillnad och fråga om rytmstyrkan samvarierar med en redan existerande manuskriptindelning, t.ex. Currier A/B eller etablerad sektion.
