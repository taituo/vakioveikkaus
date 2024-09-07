# Vakioveikkausrivien Generaattori

Tämä Python-ohjelma luo vakioveikkausrivejä käyttäjän määrittelemien painotusten mukaisesti.

## Disclaimer

**TÄRKEÄÄ**: Tämä ohjelma on tarkoitettu vain viihde- ja opetuskäyttöön. Ohjelman tekijä ei ole 
vastuussa mistään tappioista, häviöistä tai muista ongelmista, jotka saattavat aiheutua tämän 
ohjelman käytöstä vedonlyöntitarkoituksiin. Käytä ohjelmaa omalla vastuullasi.

## Ohjelman toiminta

1. Ohjelma näyttää ASCII-logon käynnistyessään.
2. Ohjelma kysyy käyttäjältä, kuinka monta riviä halutaan luoda (vähintään 10).
3. Jokaiselle 13 kohteelle kysytään painotukset (kotivoitto, tasapeli, vierasvoitto) 10:n tarkkuudella.
   - Käyttäjä voi syöttää painotukset manuaalisesti (esim. 80,10,10).
   - Painamalla Enter-näppäintä ohjelma arpoo painotukset automaattisesti.
4. Ohjelma luo pyydetyn määrän uniikkeja rivejä annettujen painotusten mukaisesti.
5. Luodut rivit tulostetaan näytölle.
6. Ohjelma näyttää yhteenvedon luotujen rivien jakaumasta verrattuna annettuihin painotuksiin.

## Ominaisuudet

- Varmistaa, että painotukset ovat aina 10:n tarkkuudella ja niiden summa on 100%.
- Luo rivit suoraan painotusten mukaisesti (esim. 80,10,10 tarkoittaa, että 10 riviä kohden on 8 kpl 1, 1 kpl x ja 1 kpl 2).
- Arpoo painotukset automaattisesti 10:n tarkkuudella, jos käyttäjä ei syötä niitä.
- Luo vain uniikkeja rivejä.
- Ilmoittaa, jos kaikkia pyydettyjä uniikkeja rivejä ei voida luoda.
- Näyttää yhteenvedon luotujen rivien jakaumasta.

## Käyttö

1. Suorita ohjelma komennolla: `python vakioveikkaus.py`
2. Seuraa näytölle tulevia ohjeita.

## Vaatimukset

- Python 3.x

## Lisenssi

Tämä ohjelma on julkaistu MIT-lisenssillä. Katso tarkemmat tiedot [LICENSE](LICENSE) tiedostosta.

Tämä ohjelma on suunniteltu helpottamaan vakioveikkausrivien luomista ja tarjoamaan tarkan tavan määritellä todennäköisyyksiä eri tuloksille.