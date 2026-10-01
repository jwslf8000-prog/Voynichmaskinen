# Adaptiv betydelsekedja – test 000001

## Fråga
Är kärna -> suffix stabilt över textmiljöer, vilket vore förenligt med en relativt stabil referent/klass, eller ändras relationen med position och locusklass?

## Data
Korpus 2.0. Samma frysta 18 prefix / 15 suffix. 18 608 användbara token.

Positioner:
- radstart: 2 646
- radmitt: 14 200
- radslut: 1 762

## Resultat – inom position
K -> S:
- start: 68,48 %
- mitt: 66,15 %
- slut: 73,61 %

## Resultat – över position
Träna start -> testa mitt: 54,51 %
Träna start -> testa slut: 50,66 %
Träna mitt -> testa start: 55,36 %
Träna mitt -> testa slut: 57,05 %
Träna slut -> testa start: 50,89 %
Träna slut -> testa mitt: 56,72 %

## Locusklass-holdout
Träna på övriga klasser -> testa:
- P: 50,42 %
- L: 42,82 %
- C: 47,30 %
- R: 44,83 %

## Tolkning
Kärna-suffixrelationen är stark men inte kontextfri. Radposition och locusklass innehåller information som förändrar den observerade relationen.

Det försvagar den enklaste modellen:
"en kärna = en fast referent och suffix = en fast egenskap oberoende av textmiljö".

Det är fortfarande förenligt med minst:
1. samma kärna med grammatisk/generativ positionsregel,
2. polyfunktionell kärna,
3. klassifikationssystem där fältets funktion beror på position,
4. flera textregister med delvis olika kodning.

## Ny fråga
Är positionsskillnaden huvudsakligen en generell suffixförskjutning vid radstart/radslut, eller ändrar enskilda kärnor sina suffixpreferenser på ett systematiskt sätt?

## Nästa test
Jämför för varje tillräckligt frekvent kärna dess suffixfördelning i start/mitt/slut och mät om förändringen kan förklaras av en global positionsregel eller kräver kärnspecifika interaktioner.
