# H1 – 100-testserie 001

## Fråga
Hur stabil är förutsägelsen av suffix på osedda folios, och hur mycket information tillför prefix respektive kärna?

## Fryst metod
- Korpus 2.0
- 18 produktiva tvåteckens-prefix
- 15 produktiva tvåteckens-suffix
- 18 608 användbara token
- 100 deterministiska folio-holdout-delningar
- alfabetisk deterministisk tie-break
- endast testfall vars nödvändiga featurevärde finns i träningen poängsätts

Modeller:
A. global suffixfrekvens
B. P -> S
C. K -> S
D. (P,K) -> S

## Resultat över 100 tester

| Modell | Medel | SD | Min | Max |
|---|---:|---:|---:|---:|
| Global suffixbaslinje | 27,22% | 2,19 pp | 20,84% | 32,44% |
| P -> S | 31,35% | 1,90 pp | 25,82% | 35,93% |
| K -> S | 60,66% | 1,47 pp | 55,20% | 64,11% |
| (P,K) -> S | **61,15%** | 1,40 pp | 55,92% | 64,30% |

(P,K) slog global baslinje i **100/100** tester.

Genomsnittlig marginalnytta:
- (P,K) jämfört med K: **+0,49 procentenheter**
- (P,K) jämfört med P: **+29,80 procentenheter**

Skillnaden (P,K)-K varierade från -1,64 till +2,32 procentenheter mellan delningarna.

## Viktig förfining av H1
Det tidigare starka resultatet för (P,K)->S ska inte tolkas som att prefix och kärna bidrar ungefär lika mycket.

I denna serie bär **kärnan nästan hela den prediktiva signalen för suffixet**.
Prefixet har en mycket mindre marginaleffekt när kärnan redan är känd.

Detta passar med flera möjliga modeller:
- morfologisk/generativ struktur,
- klass-/tillhörighetsstruktur,
- skrivregel eller kodningsregel.

Testet skiljer ännu inte mellan dessa.

## Konsekvens för Nyckel 2.0
Kärnan prioriteras nu som den primära länken till högerfamiljen.
Prefixet behandlas som en separat dimension vars funktion måste testas mot andra mål än bara suffix.

## Nästa serie
- förutsäg prefix från K+S kontra K/S var för sig,
- held-out helt nya kärnor och kombinationer,
- folio- och locusklass-stabilitet,
- sekvens/radgräns,
- jämförelse med enklare tecken-/n-grammodell.
