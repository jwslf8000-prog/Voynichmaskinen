# Kontrollkörning 001

Källa: data/raw/IT2a-n.txt
Källans Git-blob SHA i spegeln: 7f491b574b65e5fba6b553e57372c3fa50e10fec

Regler:
- textloci med kommatecken
- punkt som ordseparator
- <-> behandlas som ordgräns
- <%> och <$> tas bort
- inline-kommentarer tas bort
- endast rader med 5–18 ord

## Faktiskt resultat

- Rader: 3 655
- Ordpositioner: 32 860
- Kontrollmål: 3 541 / 31 650
- Avvikelse: +114 rader / +1 210 ord

Status: EJ MATCHAD.

Ingen parameter har justerats för att framtvinga kontrollmålet.

## Nästa diagnos

Identifiera vilken tidigare urvalsregel som förklarar bortfallet av 114 rader. Kandidater att testa separat:
- locus-/texttyper (P/L/C/R och underklasser)
- osäkra/oläsbara token
- radmarkörer och avbrott
- normalisering av mellanslag/punkt
- eventuell sektion-/foliospärr
