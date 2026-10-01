# Voynich-komposition 1.3 — formroller i variationen

614 A...A-bågar med gap 2–4 analyserades. PKT användes inte i huvudtestet.

För varje tema A, båglängd och variationsposition mättes koncentration av:
- ordlängd
- första tecken
- sista tecken
- första två tecken
- sista två tecken

Kontroll: 100 nuller där variationsord drogs från samma folios tokenpool. Tema, båglängd och variationsposition hölls fasta.

## Huvudresultat
Simpson-koncentration, verkligt / nullmedel / lift / nuller >= real:

- längd: 0,29180 / 0,28740 / 1,015x / 32 av 100
- första tecken: 0,31335 / 0,27560 / 1,137x / 0 av 100
- sista tecken: 0,45025 / 0,38257 / 1,177x / 0 av 100
- prefix2: 0,25806 / 0,21857 / 1,181x / 0 av 100
- suffix2: 0,29671 / 0,24912 / 1,191x / 0 av 100

Ordlängd visar ingen robust organisation. Ordkanterna gör det.

## Roller inne i bågen

Prefix2:
- enda variationsplatsen (ABA): lift 1,366x, 0/100 null >= real
- första plats i längre båge: 1,144x, 4/100
- sista plats före återkomst: 1,179x, 0/100
- mitten: 0,988x, 51/100

Suffix2:
- ABA-platsen: 1,327x, 0/100
- första plats: 1,125x, 2/100
- sista plats före återkomst: 1,212x, 0/100
- mitten: 1,085x, 21/100

## Tolkning
Variationerna är inte bara fria ordval. Givet samma tema och båglängd finns återkommande ortografiska formroller, särskilt:
1. den enda B-platsen i ABA,
2. den sista variationsplatsen precis före A återkommer.

Mittpositioner i längre variationer är mycket friare.

Detta ger en konkret kompositionsmodell:
A → [formstyrd ingång] → [friare mitt] → [formstyrd återgång] → A.

Resultatet etablerar struktur, inte semantik och inte bokstavlig musik.

## Nästa test
Blind prediktion:
håll ut folios och försök förutsäga prefix/suffix-klassen på B/C/D enbart från tema A, båglängd och position. Om detta generaliserar till osedda folios är formrollerna en verklig återanvänd kompositionsregel snarare än lokala egenheter.
