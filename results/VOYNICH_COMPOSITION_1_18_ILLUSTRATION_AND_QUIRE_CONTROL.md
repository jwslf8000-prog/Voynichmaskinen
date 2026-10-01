# Voynich-komposition 1.18 — illustrationstyper och quire-kontroll

## IVTFF-koder verifierade
Enligt IVTFF-formatdefinitionen betyder $I illustration type:
- A = astronomical (excluding zodiac)
- B = biological
- C = cosmological
- H = herbal
- P = pharmaceutical
- S = marginal stars only
- T = text-only
- Z = zodiac

Därmed kan 1.17:s frysta axelmedel beskrivas konkret:
H -0,635; S +0,168; T +0,857; B +1,453; P +1,631; C +2,470.
(A hade endast n=1 i det robusta 93-foliourvalet och ska inte tolkas.)

## Viktig alternativförklaring
Illustrationstyp/sektion och manuskriptets quire/placering är starkt kopplade. Därför testades om 1.17:s sidtypssignal finns kvar inom quire.

Axeln, urvalet och 1.16-loadings frystes oförändrade.

Quire $Q förklarar:
eta² = 0,26387 av axelvariationen.

Kontroll:
1. dra bort respektive quire-medel från axelvärdet;
2. permutera $I-labels endast inom samma quire;
3. 5000 permutationer.

Resultat för illustrationstyp efter quire:
- residual eta² = 0,05682
- null mean = 0,05204
- null q95 = 0,09219
- 1883/5000 >= real
- empiriskt p = 0,3767

## Korrigerad slutsats
1.17 visade ett verkligt samband mellan den frysta återkomstaxeln och IVTFF illustrationstyp, och sambandet kvarstod efter kontroll för Currier A/B.

1.18 visar däremot att sambandet inte kan separeras från quire/sektionell placering med denna analys. När quire hålls fast finns ingen tydlig extra effekt av illustrationstyp.

Vi ska därför INTE hävda att bildtypen i sig driver eller förklarar återkomstarkitekturen.

Säkrare resultat:
återkomstarkitekturen varierar systematiskt med manuskriptets sektionella/quire-organisation. Eftersom illustrationstyperna också är sektionellt organiserade samvarierar de med axeln.

Detta är fortfarande strukturell evidens, inte semantisk översättning.

## Nästa steg
Studera axelns förändring längs den faktiska manuskriptordningen utan kategorietiketter:
- testa gradvis trend kontra abrupta brytpunkter vid quire-/sektionsgränser;
- håll bågaxeln helt fryst;
- jämför brytpunkter mot permutation/block-null först efter att de upptäckts.
Det kan skilja mellan en allmän tids-/produktionsdrift och verkliga sektionella regimskiften.
