# Rekonstruktion

## Steg 0
1. Hämta IT2a-n.txt från den låsta källan.
2. Kör:
   python reconstruction/rebuild_stage0.py IT2a-n.txt data/stage0.tsv
3. Jämför utskriften mot 3541 rader / 31650 ordpositioner.

Ingen maskinparameter justeras för att artificiellt nå kontrollvärdena.

## Nästa steg efter korpusmatchning
- återhämta/återhärleda 13 prefix
- återhämta/återhärleda 16 suffix
- definiera kärnextraktion
- reproducera 2976 kärnor
- implementera hjul-i-hjul (+x,+2x,+3x,+5x,...)
- reproducera 91 kopplingstillstånd och fem restfamiljer
- separera IVTFF-etiketter för bild–text-test
