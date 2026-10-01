# Voynich-komposition 1.11 — återkomstrytm

## Låst sekventiell definition
Läs varje locus vänster till höger.
En återkomsthändelse är en position vars ord redan har förekommit tidigare i samma locus.
Hitta första återkomsthändelsen och mät positionsavståndet till den andra återkomsthändelsen.

Ingen framtida information används för att definiera den första händelsen.

## Verkligt
856 rader har minst en återkomsthändelse.
171 har minst två.
P(andra | första) = 19,98 %.

Avstånd första -> andra:
1: 55
2: 30
3: 30
4: 18
5: 11
6: 6
7: 6
8: 4
9: 2
10: 2
övriga: 7

Medelavstånd 3,532.

## 200 folio-lokala nuller
Samma folios tokenmängd och exakt samma radlängder; ordordning omblandad inom folio.

Andra-återkomstfrekvens:
- real 0,1998
- nullmedel 0,1674
- null q95 0,1929
- 4/200 >= real

Avstånd 1:
- real 55
- nullmedel 28,39
- null q95 37
- 0/200 >= real

Avstånd 3:
- real 30
- nullmedel 17,28
- null q95 24
- 0/200 >= real

Avstånd 2 och 4 passerade inte motsvarande individuella 5%-kontroll.

## Uppföljande rytmklass {1,3}
Efter att topparna 1 och 3 identifierats testades den samlade klassen med 500 nya deterministiska folio-lokala nuller.

Bland rader med en andra återkomst:
- real andel avstånd 1 eller 3 = 49,71 %
- nullmedel = 39,69 %
- null q95 = 46,61 %
- 4/500 >= real
- empiriskt p ≈ 0,010

Kontroll mot att samma tema ensam driver signalen:
kräv att första och andra återkomsthändelsen gäller OLIKA ordteman.
- real andel {1,3} med olika teman = 31,58 % av alla andra-återkomstfall
- nullmedel = 22,63 %
- null q95 = 29,01 %
- 4/500 >= real
- empiriskt p ≈ 0,010

## Slutsats
Det finns evidens för att återkomsthändelser i Voynich inte bara klustrar generellt utan har en kortdistansstruktur. Efter en första återkomst är nästa återkomst oproportionerligt ofta 1 eller 3 positioner senare.

Signalen kvarstår när de två återkomsterna måste gälla olika ordteman, så den förklaras inte enbart av att ett enda ord upprepas flera gånger.

Eftersom {1,3}-klassen valdes efter inspektion av samma verkliga histogram ska p≈0,010 betraktas som uppföljande evidens, inte som helt preregistrerad discovery-fri signifikans.

Nästa steg:
replikera rytmklassen {1,3} utan omval på en strikt uppdelning av manuskriptet (discovery-folios vs held-out confirmation-folios). Om {1,3} återkommer i helt osedda folios blir den en kandidat till en låst kompositionsregel.
