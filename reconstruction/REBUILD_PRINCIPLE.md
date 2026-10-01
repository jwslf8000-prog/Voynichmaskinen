# Ombyggnadsprincip – korpus och nyckel

## Beslut

Voynichmaskinen byggs om från råtranskriptionen utan att försöka träffa tidigare antal.

Tidigare värden som 3 541 rader och 31 650 ordpositioner är från och med nu **historiska jämförelsevärden**, inte facit.

## Ordning

1. Lås råkälla och version.
2. Definiera vad en transkriberad rad är.
3. Definiera vad ett ord/token är enligt källformatet.
4. Definiera behandling av osäkra tecken, alternativa läsningar, avbrott och markup.
5. Definiera vilka texttyper som ingår.
6. Kör reglerna utan målanpassning.
7. Det observerade rad- och ordantalet blir den nya korpusens kontrollvärden.
8. Bygg därefter om nyckeln från den nya korpusen.

## Nyckeln byggs om

Den gamla uppdelningen används som hypotes och jämförelse, inte som tvång:

- prefix
- kärna / kopplingsstruktur
- suffix
- rest / kopplingstillstånd

Antalet prefix, kärnor, suffix och resttillstånd får ändras om råmaterialet kräver det.

Tidigare värden (13 prefix, 2 976 kärnor, 16 suffix, 91 kopplingstillstånd och fem restfamiljer) sparas endast som historiska referenser.

## Krav på en ny nyckel

En komponent får behållas endast om den:
- kan definieras deterministiskt,
- kan reproduceras från samma rådata,
- förbättrar täckning eller strukturell förklaring,
- inte införs bara för att matcha gamla totalsiffror.

## Validering

Den nya nyckeln ska testas på data som inte användes när reglerna byggdes.

Vi ska särskilt mäta:
- ordtäckning,
- radtäckning,
- antal undantag,
- stabilitet mellan folios/sektioner,
- minimalpar,
- omvänd förutsägelse,
- bild–text-samband när bildetiketterna återinförs.

Ingen semantisk betydelse tilldelas innan strukturen generaliserar.
