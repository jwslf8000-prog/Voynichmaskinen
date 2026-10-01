# Adaptiv betydelseserie – 100 000 tester

## Huvudmål
Flytta fokus från enbart konstruktion till vilken typ av information Voynichtextens strukturer kan bära.

## Grundregel
Varje test T_n måste producera:
1. fråga,
2. metod,
3. resultat,
4. osäkerhet/kontroll,
5. minst en ny fråga som resultatet väcker,
6. prioriterad nästa fråga.

T_(n+1) väljs från den prioriterade frågan i T_n och hela tidigare resultathistoriken.

## Frågebanker
A. Kärnans möjliga referens/funktion
B. Prefixets möjliga kontextfunktion
C. Suffixets möjliga egenskaps-/relationsfunktion
D. ordposition och närmiljö
E. fysisk rad kontra fortsättande sekvens
F. folio/sektion/locusklass
G. minimalpar
H. återkommande konstruktioner
I. bildetiketter och mätbara bildegenskaper
J. omvänd förutsägelse
K. tabell-/klassifikationsmodell
L. konkurrerande språk-/morfologimodell
M. konkurrerande generativ/kodningsmodell

## Adaptiv prioritering
Nästa test prioriterar den fråga som bäst kan skilja mellan minst två levande förklaringar.

Prioritet ökar om:
- resultatet är reproducerbart över folios,
- två modeller gör olika förutsägelser,
- testet kan falsifiera en modell,
- en komponent kan kopplas till en extern mätbar egenskap,
- testet kan genomföras utan semantisk gissning.

Prioritet minskar om:
- samma information redan testats,
- resultatet huvudsakligen drivs av frekvens,
- testet kräver efterhandsval,
- det saknas oberoende kontroll.

## Betydelsehypoteser
Funktioner hålls neutrala tills de stöds:
- F1 kontext/tillhörighet
- F2 referent/klass
- F3 egenskap/relation
- F4 sekvens/position
- F5 generativ formregel

Ord som växt, rot, vatten, stjärna, mängd, namn etc. får endast bli kandidater efter extern bild-/textmiljöevidens.

## Konkurrerande modeller
Minst dessa hålls levande:
1. naturlig språk/morfologi,
2. implicit tabell/klassifikation,
3. nomenklatur/etikettsystem,
4. generativ eller kodad textstruktur,
5. blandmodell.

Ingen modell vinner på rå träffsäkerhet ensam.

## Stoppregler
Serien stoppas eller omdesignas om:
- dataläckage upptäcks,
- parser/korpus ändras,
- samma testfamilj upprepas utan ny information,
- kontrollmodell förklarar effekten lika bra,
- extern data krävs men saknas.

## Reproducerbarhet
Varje test får:
- test_id 000001–100000
- parent_test_id
- fråga
- hypoteser som skiljs åt
- dataurval
- seed
- resultatmått
- ny fråga
- nästa testfamilj

Resultaten sparas append-only. Tidigare resultat skrivs aldrig om.
