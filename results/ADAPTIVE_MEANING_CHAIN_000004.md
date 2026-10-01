# Adaptiv betydelsekedja – test 000004

## Fråga
Finns positionssignalen kvar när både folio och kärna hålls fasta?

## Metod
För varje folio×kärna jämfördes suffixfördelningen:
- radstart mot icke-start
- radslut mot icke-slut

Minimikrav: minst 3 observationer i positionsgruppen och minst 8 utanför den.
Skillnaden mäts med total variation distance (TV).

## Resultat
Radstart:
- 42 folio×kärna-celler
- medel-TV 0,313
- median-TV 0,300

Radslut:
- 27 folio×kärna-celler
- medel-TV 0,422
- median-TV 0,375

Positionsskillnaden finns alltså kvar när både sida och kärna hålls fasta.

## Försiktig tolkning
Det gör en ren mellan-folio-förklaring mindre tillräcklig. Position verkar samspela med suffixvalet för samma kärna på samma folio.

Men cellerna kan fortfarande vara små. Observerad TV kan därför vara uppblåst av stickprovsvariation.

## Ny fråga
Är den observerade positionsskillnaden större än vad samma små cellstorlekar producerar när positionsetiketterna slumpas inom varje folio×kärna?

## Nästa test
Permutation inom varje folio×kärna, med exakt samma antal start/slut-observationer. Jämför observerad medel/median-TV mot nulldistributionen.
