# Voynich-PKT 0.1 – 000014 ordform + position -> PKT-aktivitet

Fem blinda folio-holdouts.

Mål:
Förutsäg om nästa dolda ord är PKT-aktivt.

Tillåtna prediktorer:
- föregående synliga ordets första tecken
- sista tecken
- sista två tecken
- ordlängd
- grov position i raden/locus

Ingen information från testfolion används i träningen.

Eftersom aktiva ord bara är cirka 3,3–3,9 % används area under precision-recall curve (AUPRC) och lift över basfrekvens, inte vanlig accuracy.

Resultat per fold, AUPRC / lift:
- fold 0: 0,05748 / 1,715x
- fold 1: 0,07639 / 2,256x
- fold 2: 0,07184 / 1,863x
- fold 3: 0,06002 / 1,799x
- fold 4: 0,06361 / 1,783x

Mean lift: 1,883x.

Resultat:
PKT-aktivitet är blindt förutsägbar från lokal ordform/position bättre än basfrekvens i samtliga fem folds.

Begränsning:
Detta är inte översättning och inte exakt ordprediktion. Det visar endast att den numeriska PKT-egenskapen är kopplad till lokal textstruktur/position.

Nästa steg:
Testa om samma signal förbättrar rangordning av själva nästa ordet jämfört med ren träningsfrekvens.
