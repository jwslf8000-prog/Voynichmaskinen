# Adaptiv betydelsekedja – test 000023–000024

## 000023 – lokal kontextstabilitet för brokärnor
Jämför Currier A mot B för position samt föregående/nästa K.

- o: position 0,971; föregående 0,782; nästa 0,654; medel 0,802
- ai: 0,996; 0,734; 0,649; medel 0,793
- i: 0,925; 0,801; 0,591; medel 0,773
- l: 0,964; 0,207; 0,407; medel 0,526
- ct: 0,993; 0,154; 0,135; medel 0,427

o och ai såg bäst ut deskriptivt.

## 000024 – hård korssystem-prediktion
Träna enkel grannprofil i A och identifiera mål-K bland B-token, samt omvänt.
Mått AUC, där 0,5 ≈ slump.

o:
- A->B 0,497
- B->A 0,509

ai:
- A->B 0,517
- B->A 0,521

i:
- A->B 0,581
- B->A 0,519

ct:
- A->B 0,481
- B->A 0,523

l:
- A->B 0,541
- B->A 0,392

## Slutsats
Hög aggregerad P/S- och kontextlikhet räcker inte för att visa stabil individuell lokal funktion.
o och ai klarar inte det hårdare prediktionstestet.

Detta försvagar hypotesen att enskild K direkt motsvarar ett vanligt språkoberoende "ord" med stabil lokal semantisk miljö.

## Ny riktning
Testa återkommande flerords-/K-konstruktioner:
- K-bigram och K-trigram
- konstruktioner som återkommer i både A och B
- folio-blockerad generalisering
- kontroll mot marginalfrekvens
- därefter bild-/sektionkoppling

Om Voynichtexten är tabell-, nomenklatur- eller formelartad kan betydelsebärande enhet ligga över enskild K.
