# PKT 1.0 – återställd definition

## Kontrollankare
N = 49 139.

Platonska T-positioner och vikter:
- T4 -> 5
- T6 -> 7
- T8 -> 9
- T12 -> 13
- T20 -> 21

## Regel
För ett kandidatprimtal N och en T-position med vikt w:

1. Kräv att (N+1) är delbart med w.
2. Sätt k = (N+1)/w.
3. Bygg pentaven:
   - 5k-1
   - 7k-1
   - 9k-1
   - 13k-1
   - 21k-1
4. T-värdet är antalet primtal i detta femtal.
5. PKT-profilen är (T4,T6,T8,T12,T20).
6. PKT-styrkan är summan av de fem T-värdena.

## Verifiering 49 139
T4, k=9828:
49139 P; 68795 C; 88451 C; 127763 P; 206387 C -> 2

T6, k=7020:
35099 P; 49139 P; 63179 P; 91259 C; 147419 P -> 4

T8, k=5460:
27299 P; 38219 P; 49139 P; 70979 P; 114659 P -> 5

T12, k=3780:
18899 P; 26459 P; 34019 P; 49139 P; 79379 P -> 5

T20, k=2340:
11699 P; 16379 C; 21059 P; 30419 C; 49139 P -> 3

Profil = (2,4,5,5,3)
PKT-styrka = 19.

Den senare yttre styrkan som användes i projektet var 19-5 = 14/20.

## Korrigering
En felaktig rekonstruktion 2026-10-01 använde (D+1) som divisor. Den är ogiltig. Divisorn är själva vikten 5,7,9,13,21.

## Voynichregel
PKT-specifikationen är fristående. Voynich-PKT får inte ändra denna regel för att passa Voynichdata.
