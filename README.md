# Vakioveikkausrivien Generaattori (Web-sovellus)

Tämä web-sovellus luo vakioveikkausrivejä käyttäjän määrittelemien painotusten mukaisesti.

## Disclaimer

**TÄRKEÄÄ**: Tämä sovellus on tarkoitettu vain viihde- ja opetuskäyttöön. Sovelluksen tekijä ei ole 
vastuussa mistään tappioista, häviöistä tai muista ongelmista, jotka saattavat aiheutua tämän 
sovelluksen käytöstä vedonlyöntitarkoituksiin. Käytä sovellusta omalla vastuullasi.

## Sovelluksen toiminta

1. Käyttäjä syöttää halutun rivien määrän (vähintään 10).
2. Jokaiselle 13 kohteelle käyttäjä voi syöttää painotukset (kotivoitto, tasapeli, vierasvoitto) tai arpoa ne.
3. Sovellus luo pyydetyn määrän uniikkeja rivejä annettujen painotusten mukaisesti.
4. Luodut rivit ja niiden jakauma näytetään käyttäjälle.

## Ominaisuudet

- Varmistaa, että painotukset ovat aina 10:n tarkkuudella ja niiden summa on 100%.
- Luo rivit suoraan painotusten mukaisesti.
- Mahdollisuus arpoa painotukset automaattisesti.
- Luo vain uniikkeja rivejä.
- Näyttää yhteenvedon luotujen rivien jakaumasta.

## Käyttö

1. Asenna tarvittavat kirjastot: `pip install flask`
2. Käynnistä sovellus komennolla: `python app.py`
3. Avaa selain osoitteessa `http://localhost:5000`
4. Seuraa käyttöliittymän ohjeita.

## Vaatimukset

- Python 3.x
- Flask

## Lisenssi

Tämä sovellus on julkaistu MIT-lisenssillä. Katso tarkemmat tiedot [LICENSE](LICENSE) tiedostosta.