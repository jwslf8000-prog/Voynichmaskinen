# H1 tabelltest – pass 1

## Förregistrerad konstruktion
Utgår från Korpus 2.0 och Nyckel 2.0 pass 1.

Produktivitetströskel:
- tvåteckens vänsterdel: minst 100 olika återstående former
- tvåteckens högerdel: minst 100 olika föregående former
- mittdelen måste vara icke-tom

## Struktur
- produktiva vänsterdelar: 18
- produktiva högerdelar: 15
- användbara token: 18 608
- observerade olika mittdelar: 1 985

## Blind folio-blockerad förutsägelse
Uppgift: förutsäg högerdel S från (P,K) med endast träningsfolios.
Endast testfall där (P,K) observerats i träningen poängsätts.

Fem deterministiska foliofolds:

| Fold | N | P+K -> S | global S-baslinje |
|---|---:|---:|---:|
| 0 | 3052 | 60.03% | 24.71% |
| 1 | 2826 | 61.18% | 28.80% |
| 2 | 3065 | 60.29% | 24.67% |
| 3 | 3398 | 61.39% | 27.37% |
| 4 | 3928 | 60.85% | 30.07% |

Viktat:
- P+K -> S: **60.76%**
- global frekvensbaslinje: **27.26%**
- skillnad: **+33.50 procentenheter**

## Vanliga P×S-kombinationer
Exempel på frekventa strukturella par:
- qo × dy: 1277
- ch × dy: 974
- qo × in: 922
- da × in: 848
- qo × ey: 722
- sh × dy: 671
- ch × hy: 537

Dessa är strukturkoder, inte semantiska översättningar.

## Bedömning
Resultatet visar starkt reproducerbart beroende mellan vänster/mitt och högerstruktur över folios.
Det räcker INTE ännu för slutsatsen att texten är en implicit tabell eller taxonomi.

Nästa obligatoriska kontroll:
1. frekvensbevarande permutation,
2. kontroll mot en modell som bara använder K respektive bara P,
3. held-out (P,K)-kombinationer,
4. test av radöverskridande struktur,
5. jämförelse mellan P/L/C/R.
