# Korpusdefinition 2.0

## Princip

Korpusen ska följa IVTFF-formatets dokumenterade gränser och inte anpassas till historiska totalsiffror.

## Ordgränser

Följande bevaras som ordgränser:
- `. ` / punkt: säker ordgräns
- `,`: osäker ordgräns
- `<->`: ritningsintrång; innebär ordgräns
- `<~>`: ritningsintrång med vertikal felställning; innebär ordgräns

Varje gräns får en typ i den bearbetade datan. Därmed kan framtida tester välja att:
A. räkna alla dokumenterade gränser,
B. endast använda säkra gränser,
utan att rådata ändras.

## Läsosäkerhet

- `[a:o]` är alternativa läsningar av samma teckenposition, inte flera ord.
- `?` bevaras som oläslig/osäker position.
- ligaturmarkeringar bevaras separat från ordsegmenteringen.
- kommentarer och metadata räknas inte som text.

## Loci

P, L, C och R bevaras som separata locus-klasser. De blandas inte automatiskt.
Ingen klass tas bort för att få ett önskat antal rader eller ord.

## Nyckel 2.0

Nyckeln härleds först efter denna segmentering.

För varje observerat token sparas:
- folio/locus
- locus-klass
- position i locus
- vänster och höger gränstyp
- rå EVA-form
- normaliserad analysform
- osäkerhetsflagga
- alternativ-läsningsflagga

Prefix, kärna, suffix och kopplingstillstånd härleds därefter från observerade mönster.
Antalen är resultat, inte parametrar.

## Historiska tal

3 541 rader, 31 650 ordpositioner, 13 prefix, 2 976 kärnor, 16 suffix och 91 tillstånd används endast för jämförelse med den gamla maskinen.
