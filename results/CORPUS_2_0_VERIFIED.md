# Korpus 2.0 – verifierad

## Resultat
IVTFF-tokenizer 2 reproducerar ZL3b-källans kontrollvärden exakt:

- loci: **5 385**
- long words: **36 278**

Därmed fryses long-word-vyn som primär Korpus 2.0.

## Osäkra ordgränser
När osäkra kommateckensgränser också delas:
- tokenpositioner: **39 026**
- skillnad: **+2 748**

39 026-vyn används endast som känslighetsanalys. Den ersätter inte primärkorpusen.

## Fördelning i primärkorpusen
- P: 4 130 loci / 32 612 long words
- L: 1 029 loci / 1 149 long words
- C: 84 loci / 2 184 long words
- R: 142 loci / 333 long words

## Beslut
Nyckel 2.0 härleds från 36 278-tokenkorpusen utan krav på tidigare antal prefix, kärnor, suffix eller kopplingstillstånd.

Fysisk locusgräns bevaras men betraktas inte automatiskt som meningsgräns.
