# Adaptiv betydelsekedja – test 000021–000022

## 000021 – brokärnor mellan Currier A och B
Urvalet innehöll 4 902 reducerbara K-token i A och 12 047 i B.

Kärnor med hög balans och spridning i båda systemen inkluderar:
- kch: frekvensbalans 0,9998
- ckh: 0,9918
- ai: 0,9612
- ct: 0,9475
- l: 0,9401
- he: 0,8310
- d: 0,8456

Systemspecifika exempel:
- hai: 19 A, 0 B i detta urval
- hed: 0 A, 24 B
- lke: 0 A, 22 B
- eed: 0 A, 21 B
- lkee: 0 A, 20 B

## 000022 – behåller samma K samma P/S-miljö över A och B?
Cosinuslikhet mellan P- respektive S-fördelningen för samma K i A och B.

Särskilt stabila brokärnor:
- i: P 0,971; S 0,9999; medel 0,985
- ct: P 0,944; S 1,000; medel 0,972
- o: P 0,965; S 0,936; medel 0,951
- l: P 0,943; S 0,945; medel 0,944
- ai: P 0,855; S 0,999; medel 0,927

Exempel på asymmetrisk systemväxling:
- kch: P 0,991 men S 0,145
- d: P 0,218 men S 0,980
- e: P 0,974 men S 0,367
- ee: P 0,914 men S 0,298

## Tolkning
Det finns minst två typer av K:
1. systemöverbryggande kärnor vars yttre P/S-regler är mycket stabila över Currier A/B,
2. kärnor där en sida av P/K/S-konstruktionen ändras kraftigt mellan A/B.

Grupp 1 är hittills bättre kandidat för stabil funktion/referens än rått frekventa kärnor.
Grupp 2 visar att P och S inte bör ges en enda global semantisk roll.

## Nästa fråga
Har de stabilaste brokärnorna i, ct, o, l och ai även stabil lokal textfunktion över A/B?

Testa:
- start/mitt/slut i locus,
- föregående/nästa kärnfamilj,
- korsfolio-generaliserbarhet,
- A->B överföring och B->A överföring.

Om både yttre form och lokal textfunktion överlever A/B blir dessa kärnor de starkaste kandidaterna hittills för systemoberoende innehåll/funktion.
