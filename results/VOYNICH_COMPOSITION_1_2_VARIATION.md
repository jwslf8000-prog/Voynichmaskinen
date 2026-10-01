# Voynich-komposition 1.2 — vad händer i variationen?

Utgångspunkt: de robusta korta återkomstbågarna A...A med gap 2–4 från Komposition 1.1.

## Material
614 återkomstbågar med gap 2–4.

För varje temaord A och båglängd samlades mellanorden B/C/D. PKT-fingeravtryckens koncentration mättes inom tema+båglängd-grupper.

Kontroll: variationsord samplades från samma folios tokenpool medan tema A och båglängd hölls fasta.

## PKT-resultat
80 tema+båglängd-grupper hade minst fyra variationstoken.

Medel Simpson-koncentration för PKT-fingeravtryck:
- verkligt: 0,146731
- 100 nuller, medel: 0,144678
- null 95-percentil: 0,148340
- null max: 0,151178
- 13/100 nuller >= verkligt

Alltså ingen robust evidens för att variationsplatserna väljs från snäva PKT-familjer i denna representation.

## Exempel på temaankare
daiin:
- gap 3: 23 bågar, 23 olika ordvariationer och 23 olika PKT-sekvenser
- gap 2: 19 bågar, 19 olika variationer
- gap 4: 15 bågar, 15 olika variationer

shedy gap 2:
- 16 bågar, 14 olika variationer

chedy gap 2:
- 14 bågar, 13 olika variationer

qokedy gap 2:
- 12 bågar, 8 olika variationer

## Tolkning
Kompositionssignalen från 1.1 kvarstår, men den enkla hypotesen "tema A väljer en begränsad PKT-familj i B/C/D" stöds inte.

Ett bättre arbetssätt är därför:
A fungerar som ram/ankare.
Mellanmaterialet är varierat och bör analyseras efter sina egna regler i stället för att tvingas in i PKT.

## Nästa test
Mät variationens form direkt:
- första/sista tecken
- ordlängd
- prefix/suffix-likhet
- relation mellan variationens position och båglängd
- övergångar in i och ut ur temaankaret
- blind prediktion av variationsklass från A och position

PKT behålls som separat matematisk kanal, inte som antagen huvudförklaring.
