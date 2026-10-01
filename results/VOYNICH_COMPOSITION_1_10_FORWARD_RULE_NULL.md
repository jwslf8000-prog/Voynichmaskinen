# Voynich-komposition 1.10 — nulltest av framåtriktad regel

## Låst regel
Från 1.9:
visa endast första halvan av raden.
Fråga om den synliga halvan redan innehåller en intern exakt ordrepetition.
Förutsäg om den dolda andra halvan innehåller minst ett ord som återknyter till ett tema från den synliga halvan.

## Blind log-loss, fem folio-holdouts
Verkligt:
- längdbaseline 0,37027345
- + synlig repetition 0,36715418
- förbättring 0,00311927

100 folio-lokala token-shuffle nuller:
- mean gain 0,00099111
- q95 0,00324551
- max 0,00412939
- 5/100 >= verkligt
- +1 empiriskt p ≈ 0,0594

Detta är nära men inte tillräckligt för att ensam godkänna regeln som fast grammatikregel.

## Direkt längdmatchad kontrast
Som sekundär kontroll mättes inom varje exakt radlängd skillnaden i sannolikhet för framtida återknytning mellan rader vars synliga halva redan har repetition och rader utan sådan repetition. Längdstrata kombinerades med balanserad viktning.

Verklig kontrast:
+0,11747 (cirka +11,75 procentenheter)

200 folio-lokala nuller:
- nullmedel +0,06571
- q95 +0,11341
- max +0,15148
- 5/200 >= verkligt
- +1 empiriskt p ≈ 0,0299

## Tolkning
Två tester pekar åt samma håll:
tidig intern repetition tenderar att följas av senare återknytning mer än väntat.

Evidensen är dock måttlig:
- det preregistrerade log-loss-testet missar 5%-nivån marginellt,
- den direkta längdmatchade kontrasten passerar den.

Regeln bör därför märkas KANDIDAT, inte låst grammatikregel.

Det viktiga strukturella resultatet är:
återkomstbågar verkar inte helt oberoende. En tidig återkomst ökar sannolikheten för ytterligare återknytning senare i samma rad, utöver en stor del av den effekt som uppstår mekaniskt av radlängd och foliospecifik ordfrekvens.

Nästa steg bör testa en striktare sekventiell hypotes:
efter en första observerad återkomst, är nästa återkomst mer sannolik inom ett specifikt antal positioner än i matchade nuller? Detta testar en möjlig "rytm" i bågarnas fortsättning utan att använda framtidsinformation.
