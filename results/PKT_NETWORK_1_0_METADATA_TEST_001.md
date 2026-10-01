# PKT-nätverk 1.0 – metadata-test 001: folio

De 2 353 matematiska fingeravtrycken från PKT_NETWORK_1_0 frystes innan folioetiketter öppnades.

## Test
För alla ordpar inom samma fingeravtrycksklass mättes Jaccard-likhet mellan mängden folios där respektive ord förekommer.

Kontroll:
100 deterministiska permutationer där ord byttes endast inom strata matchade på:
- sista tecken
- ordlängd (cappad vid 10)
- frekvensbin

Detta är viktigt eftersom mod13 under bas26 är starkt kopplat till sista tecknet.

## Resultat
- inomklass-par: 31 914
- verklig medel-folio-Jaccard: 0,00896190
- nullmedel: 0,00828695
- null median: 0,00824734
- null 95-percentil: 0,00892798
- null max: 0,00972993
- 4/100 nullreplikat >= verkligt resultat

Empiriskt ensidigt p ungefär (4+1)/(100+1)=0,0495 om +1-korrigering används.

## Tolkning
Signalens riktning är positiv: ord i samma metadata-blint skapade matematiska klass delar folio något oftare än ändelse/längd/frekvensmatchade kontroller.

Effekten är liten och ligger nära signifikansgränsen. Den ska därför behandlas som en ledtråd, inte som bevis.

## Klassinspektion
689 klasser har minst 5 unika ord. De mest koncentrerade större klasserna är fortfarande spridda över många folios; ingen enskild klass ger ännu en stark foliospecifik etikett.

Exempel:
fingerprint 4,1,8,6,8:
8 unika ord, 10 tokens, 8 folios; största folioandel 30 % (fRos).

## Nästa steg
Folio är en mycket finmaskig etikett. Nästa externa test bör använda bredare manuskriptsektioner/bildmiljöer, men med samma frysta klasser och motsvarande ändelse/frekvenskontroll. Om signalen förstärks på sektionsnivå är det förenligt med att klasserna fångar kategori snarare än specifik sida.
