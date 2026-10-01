# Sekvensnivå – fysisk rad är inte samma sak som språklig enhet

## Beslut
Voynichmaskinen 2.0 får inte anta att ett locus/rad motsvarar en mening.

Tre nivåer sparas parallellt:
1. tokenposition,
2. fysisk IVTFF-locus,
3. kontinuerlig sekvens av angränsande loci.

## Radgränstest
För varje fysisk radgräns mäts sambandet mellan slutet på föregående locus och början på nästa.
Det jämförs med:
- slumpade radgränser,
- gränser mellan folios,
- gränser mellan locus-klasser,
- inom samma P-sekvens.

Om verkliga angränsande rader visar starkare strukturellt beroende än kontrollerna får Nyckel 2.0 behandla dem som möjlig fortsättning.

Begreppet "mening" används inte förrän data ger stöd för en sådan enhet.
