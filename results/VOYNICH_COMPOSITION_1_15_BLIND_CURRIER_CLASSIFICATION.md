# Voynich-komposition 1.15 — blind Currier-klassificering från bågarkitektur

## Fråga
Kan de frysta geometriska måtten från 1.14 ensamma identifiera Currier A/B på helt osedda folios?

Extern kontroll: Currier A/B är en etablerad statistisk uppdelning av Voynichtexten. Här används endast IVTFF-metadataetiketten som mål; inga ord- eller teckenformer används som prediktorer.

## Representation
Varje folio reducerades till fem mått per analyserbar rad:
1. antal återkomstbågar
2. korta gap 2–4
3. rader med flera bågar
4. nästlade bågpar mellan olika teman
5. korsande bågpar mellan olika teman

Folios med minst fem analyserbara rader:
197 totalt
- A 114
- B 83

## Blindtest
Deterministisk 5-fold folio-holdout.
Standardisering sker endast på träningsfolios.
En enkel regulariserad logistisk modell tränas på fyra folds och testas på den femte.

Resultat:
- accuracy 54,82 %
- log-loss 0,72183
- ROC AUC 0,5430

Accuracy per fold:
- f0 57,89 %
- f1 54,55 %
- f2 56,76 %
- f3 52,78 %
- f4 52,38 %

## Slutsats
De fem frysta bågarkitekturmåtten klassificerar inte Currier A/B väl på osedda folios.

Detta är förenligt med 1.14:
A och B har olika gruppmedel relativt sina egna nuller, men foliofördelningarna överlappar kraftigt.

Därför ska återkomstarkitekturen inte beskrivas som en enkel proxy för Currier A/B. Den verkar bära en strukturell dimension som endast delvis samvarierar med Currier-uppdelningen.

Detta negativa resultat är viktigt eftersom det minskar risken att kompositionsspåret bara återupptäcker den kända A/B-skillnaden.

Nästa steg bör söka den latenta dimensionen direkt, utan Currier-labels:
klustra folios eller loci enbart från bågarkitektur och först därefter öppna metadata för att se vad de framväxande grupperna sammanfaller med.
