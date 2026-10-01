# Adaptiv betydelsekedja – test 000005–000008

## 000005 – permutation av positionsetiketter inom folio×kärna
Observerad medel-TV:
- start: 0,313 (42 celler)
- slut: 0,422 (27 celler)

Permutation, 1000 körningar:
- start null: ca 0,437; p=1,0 för null >= observerad
- slut null: ca 0,529; p=1,0

### Slutsats
000004:s stora positionsskillnader var inte evidens för en särskild positionsregel. Små grupper producerar ännu större TV under slumpning. Positionsspåret nedgraderas.

## 000006 – held-out folio: tillför position/locusklass suffixprediktion?
Viktad träff:
- K -> S: 57,55 %
- K+position -> S: 57,27 %
- K+locusklass -> S: 57,25 %
- K+position+locusklass -> S: 56,84 %

### Slutsats
Position/locusklass ger ingen robust förbättring över kärnan.

## 000007 – vad förutsäger prefixet?
Fem folio-blockerade folds, viktad träff:
- global prefixbaslinje: 23,92 %
- K -> P: 50,66 %
- S -> P: 26,56 %
- K+S -> P: 49,52 %
- position -> P: 24,98 %
- locusklass -> P: 26,17 %
- K+position -> P: 50,58 %
- K+locusklass -> P: 50,45 %

### Slutsats
Kärnan bär mycket information även om vänsterdelen. Suffix, position och locusklass ger liten/negativ marginalinformation.

## 000008 – rå mutual information
- P;K: 1,789 bit
- P;S: 0,150 bit
- P;position: 0,117 bit
- P;locusklass: 0,061 bit
- P;folio: 0,386 bit

MI är deskriptivt och inte bias-korrigerat; folio har hög kardinalitet.

## Samlad korrigering
Den tidigare semantiska skissen
prefix=context, core=referent, suffix=property
är för enkel.

Ny starkare strukturell fråga:
Kärnan kan vara centrum för en familj av tillåtna vänster- och högerformer.

## Ny fråga
Delar olika ytformer med samma kärna också liknande lokala textmiljöer?

Om ja stärks idén att kärnfamiljen bär något stabilt som kan närma sig en referent/klass/funktion.
Om nej kan kärnan främst vara en ortografisk/generativ mekanism.

## Nästa testfamilj
Held-out distributionell kontext:
- föregående/nästa tokenfamilj,
- samma kärna över olika prefix/suffix,
- jämför mot frekvensmatchade slumpkärnor,
- folio-blockera för att undvika sidämne som genväg.
