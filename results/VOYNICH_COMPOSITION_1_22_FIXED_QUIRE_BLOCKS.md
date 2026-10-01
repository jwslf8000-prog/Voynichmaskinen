# Voynich-komposition 1.22 — externa fasta quire-block

## Fryst test
Samma 1.16-axel och samma robusta urval: 93 folios med minst 15 analyserbara rader.
IVTFF $Q användes som extern, redan existerande blocketikett. Ingen klustring eller brytpunktsoptimering.

16 quire-koder finns representerade i urvalet.

## Mellan-quire variation
Eta² för quire:
- real = 0,26387

5000 permutationer av quireetiketterna över folios, vilket exakt bevarar varje grupps storlek:
- null mean = 0,16295
- q95 = 0,30524
- 408/5000 >= real
- empiriskt p = 0,08178

Den råa förklaringsgraden 26,4 % är därför inte i sig ett 5 %-signifikant resultat när den stora mängden små grupper tas med i nullen.

## Gruppstorlekar och medel
A n5 -0,019
B n1 -0,825
C n4 -1,457
D n1 -0,616
E n6 -1,026
F n3 +2,270
G n6 -1,478
H n3 -0,352
I n2 +0,105
J n2 +0,081
M n20 +1,631
N n6 +2,213
O n6 +1,216
Q n1 -0,465
S n4 +0,760
T n23 +0,264

Små n gör flera enskilda quiremedel instabila och de ska inte rangordnas semantiskt.

## Leave-one-quire-out
För att kontrollera om associationen bärs av ett enda quire togs varje grupp bort i tur och ordning.

Kvarvarande eta² låg mellan:
- minimum 0,22099 när G togs bort
- maximum 0,30491 när N togs bort

Stora grupper:
- utan M (20 folios): eta² 0,23865
- utan T (23 folios): eta² 0,29355

Alltså kollapsar inte gruppstrukturen när något enskilt quire tas bort. Effekten är bred, men huvudtestet är endast suggestivt mot korrekt storleksbevarande null (p≈0,082).

## Slutsats
1.22 stöder inte ett starkt påstående att quire ensamt förklarar återkomstarkitekturen.
Det finns breda nivåskillnader mellan externa quire-block och de är inte beroende av ett enda quire, men med 16 ojämna grupper på 93 folios är evidensen måttlig.

Tillsammans med 1.21 är den säkraste modellen fortfarande:
- ingen reproducerad gemensam linjär drift inom manuskriptets tredjedelar;
- återkomstaxeln varierar mellan större manuskriptregioner;
- exakt vilken fysisk/sektionell indelning som bäst förklarar variationen är ännu inte fastställd.

Nästa starka test bör undvika 16 små kategorier. Använd externt definierade större sammanhängande sektioner eller en strikt hierarkisk quiremodell och testa på held-out folios, utan att välja grupper efter axelvärdet.
