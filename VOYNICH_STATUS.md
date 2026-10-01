# Voynichmaskinen

Separat forskningsrepo för den strukturella Voynichmaskinen.

## Bevarad referensstatus

Dessa värden kommer från tidigare arbete och används som kontrollpunkter vid rekonstruktion:

- Korpus: 3 541 rader
- Ordpositioner: 31 650
- Grundmaskin: 13 prefix, 2 976 kärnor, 16 suffix
- Hjul-i-hjul-modell: cirka 99,855 % ordtäckning
- Kompletta rader: cirka 98,70 %
- Reststruktur: 91 unika kopplingstillstånd, senare grupperade i fem familjer
- Bild–text-spår: 734 etikett-token från 52 sidor
- Bild–text-test: 80 tidigare tester bevaras som historisk referens; nya resultat ska inte fyllas i utan faktisk reproducerbar körning.

## Forskningsprincip

Ingen semantisk betydelse tilldelas i förväg.

Arbetsordning:
1. rekonstruera transkriptionen och radindelningen,
2. rekonstruera prefix / kärna-kopplingsgrad / suffix / rest,
3. verifiera mot kontrollpunkterna ovan,
4. återskapa bildetikett-datasetet,
5. köra blinda och reproducerbara tester,
6. testa minimala par och omvänd förutsägelse,
7. först därefter undersöka möjlig funktion och betydelse.

## Nästa mål

Återskapa 3 541-radersmaskinen från offentlig Voynich-transkription och dokumentera varje regel så att hela experimentet kan köras om från början.

## Regel

Alla nya testresultat ska sparas i GitHub tillsammans med metod, dataurval och parametrar. Inga uppskattade eller simulerade resultat får blandas ihop med faktiska körningar.
