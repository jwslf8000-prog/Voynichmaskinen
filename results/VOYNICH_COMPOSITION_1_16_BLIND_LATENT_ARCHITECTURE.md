# Voynich-komposition 1.16 — metadata-blind latent bågarkitektur

## Första klusterförsök
Fem frysta foliomått från 1.14 användes utan metadata.
K-means k=2..6 gav högst silhouette för k=2: 0,834, men grupperna var 205 mot 6 folios.

De sex extrema foliosen var:
f68v1, f101r, f86v4, f67r1, f101v, fRos.
Flera hade bara 6–10 analyserbara rader. Tvåklusterlösningen underkändes därför som sannolik outlier/sample-size-effekt, inte accepterad latent textfamilj.

## Robust analys
Krav: minst 15 analyserbara rader per folio.
93 folios kvar.
De fem måtten robust-standardiserades med median/MAD.
En metadata-blind huvudaxel extraherades.

Loadings:
- alla bågar: 0,531
- korta gap 2–4: 0,429
- rader med flera bågar: 0,731
- nästlade olika teman: 0,014
- korsande olika teman: 0,018

Huvuddimensionen beskriver alltså främst återkomsttäthet/multiplicitet, inte korsningsgeometri.

Efter att axeln frysts öppnades metadata för lägsta och högsta kvartilen (23+23 folios).

Currier L:
- låg: A13, B8, okänd2
- hög: A6, B15, okänd2

IVTFF sidtyp I:
- låg: H15, S4, C1, B1, A1, P1
- hög: H3, S4, B8, P4, C3, T1

Q-koder visar också olika blandningar men tolkas inte här.

## Slutsats
Det finns inte stöd för två rena metadata-blinda bågkluster med de nuvarande måtten.
Däremot finns en tydlig kontinuerlig latent dimension från låg till hög återkomsttäthet/multiplicitet.

Denna dimension sammanfaller endast delvis med Currier A/B, vilket stämmer med 1.15, men dess ytterändar har också tydligt olika blandning av IVTFF sidtyp I.

Det mest intressanta nästa testet är därför inte mer fri klustring. Frys huvudaxeln och testa dess samband med etablerade sid-/sektionstyper på alla 93 välmätta folios, med permutation på folionivå och utan att optimera om axeln.
