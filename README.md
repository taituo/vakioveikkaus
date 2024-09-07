# Vakioveikkausrivien Generaattori

Tämä Python-ohjelma luo vakioveikkausrivejä käyttäjän määrittelemien painotusten mukaisesti.

## Disclaimer

**TÄRKEÄÄ**: Tämä ohjelma on tarkoitettu vain viihde- ja opetuskäyttöön. Ohjelman tekijä ei ole 
vastuussa mistään tappioista, häviöistä tai muista ongelmista, jotka saattavat aiheutua tämän 
ohjelman käytöstä vedonlyöntitarkoituksiin. Käytä ohjelmaa omalla vastuullasi.

## Ohjelman toiminta

1. Ohjelma näyttää ASCII-logon käynnistyessään.
2. Ohjelma kysyy käyttäjältä, kuinka monta riviä halutaan luoda (vähintään 10).
3. Jokaiselle 13 kohteelle kysytään painotukset (kotivoitto, tasapeli, vierasvoitto).
   - Käyttäjä voi syöttää painotukset manuaalisesti (esim. 70,20,10).
   - Painamalla Enter-näppäintä ohjelma arpoo painotukset automaattisesti.
4. Ohjelma luo pyydetyn määrän uniikkeja rivejä annettujen painotusten mukaisesti.
5. Luodut rivit tulostetaan näytölle.

## Ominaisuudet

- Varmistaa, että painotusten summa on aina 100%.
- Tarjoaa mahdollisuuden korjata virheelliset painotukset automaattisesti.
- Arpoo painotukset automaattisesti, jos käyttäjä ei syötä niitä.
- Luo vain uniikkeja rivejä.
- Ilmoittaa, jos kaikkia pyydettyjä uniikkeja rivejä ei voida luoda.

## Käyttö

1. Suorita ohjelma komennolla: `python vakioveikkaus.py`
2. Seuraa näytölle tulevia ohjeita.

## Vaatimukset

- Python 3.x

## Lisenssi

Tämä ohjelma on julkaistu MIT-lisenssillä. Katso tarkemmat tiedot [LICENSE](LICENSE) tiedostosta.

Tämä ohjelma on suunniteltu helpottamaan vakioveikkausrivien luomista ja tarjoamaan joustavan tavan määritellä todennäköisyyksiä eri tuloksille.