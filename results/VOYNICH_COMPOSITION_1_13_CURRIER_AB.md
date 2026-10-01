# Voynich-komposition 1.13 — fryst {1,3} mot Currier A/B

Currier-språk lästes från IVTFF sidmetadata ($L=A/B). Regeln {1,3} var fryst från 1.11 och ändrades inte.

Analyserbart material med minst fyra rena ord:
- A: 114 folios, 1393 rader
- B: 83 folios, 2407 rader

## Verkligt
Rader med minst två återkomsthändelser:
- A: 40 / 1393 = 2,872 %
- B: 107 / 2407 = 4,445 %

Bland dessa, fryst {1,3}:
- A: 21/40 = 52,50 %
- B: 59/107 = 55,14 %

Olika-tema {1,3}:
- A 16/40 = 40,0 %
- B 36/107 = 33,64 %

Alltså är själva {1,3}-andelen likartad i A och B; skillnaden ligger mer i hur ofta en andra återkomst uppstår.

## 300 folio-lokala nuller per språk
Orden blandades endast inom respektive folio, så A/B-vokabulär och radlängder bevarades.

A:
- andra-återkomsttäthet real 2,872 %, nullmedel 2,095 %, 2/300 null >= real
- {1,3}-andel real 52,50 %, nullmedel 47,23 %, 82/300 >= real

B:
- andra-återkomsttäthet real 4,445 %, nullmedel 2,686 %, 0/300 >= real
- {1,3}-andel real 55,14 %, nullmedel 41,55 %, 3/300 >= real

## Slutsats
Currier A/B förklarar inte den tidigare fold-heterogeniteten genom en enkel skillnad i {1,3}-rytmstyrka: den råa rytmandelen är nästan samma i A och B.

Men nullkontrollen visar asymmetri:
- I A är {1,3} inte tydligt över dess egen folio-lokala null.
- I B är {1,3} klart högre än B-null (3/300 >= real).
- B har dessutom mycket mer andra-återkomststruktur än dess null (0/300).
- A har också förhöjd andra-återkomsttäthet, men svagare (2/300).

Detta stödjer inte påståendet att rytmen är en universell regel. Det pekar snarare på att samma råa {1,3}-andel kan uppstå ovanpå olika basstrukturer, och att Currier B bär en tydligare ordningssignal.

Nästa test bör frysa denna nya observation och jämföra sekventiell bågarkitektur A vs B med en effektstorlek som är korrigerad mot respektive grupps egen null, utan att söka nya optimala gap.
