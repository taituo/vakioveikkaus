"""
Vakioveikkausrivien Generaattori

MIT License

Copyright (c) 2024 Tuomas Taini

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

DISCLAIMER: Tämä ohjelma on tarkoitettu vain viihde- ja opetuskäyttöön. Ohjelman tekijä ei ole 
vastuussa mistään tappioista, häviöistä tai muista ongelmista, jotka saattavat aiheutua tämän 
ohjelman käytöstä vedonlyöntitarkoituksiin. Käytä ohjelmaa omalla vastuullasi.
"""

import random

ASCII_LOGO = r"""
               __   .__                   .__ __    __                         
___  _______  |  | _|__| _______  __ ____ |__|  | _|  | _______   __ __  ______
\  \/ /\__  \ |  |/ /  |/  _ \  \/ // __ \|  |  |/ /  |/ /\__  \ |  |  \/  ___/
 \   /  / __ \|    <|  (  <_> )   /\  ___/|  |    <|    <  / __ \|  |  /\___ \ 
  \_/  (____  /__|_ \__|\____/ \_/  \___  >__|__|_ \__|_ \(____  /____//____  >
            \/     \/                   \/        \/    \/     \/           \/ 
            generaattori
"""

print(ASCII_LOGO)
print("DISCLAIMER: Tämä ohjelma on tarkoitettu vain viihde- ja opetuskäyttöön.")
print("Käytä ohjelmaa omalla vastuullasi.")
print()

def kysy_rivien_maara():
    while True:
        try:
            rivien_maara = int(input("Kuinka monta riviä haluat? (vähintään 10) "))
            if rivien_maara >= 10:
                return rivien_maara
            else:
                print("Rivejä pitää olla vähintään 10, jotta painotukset voivat toteutua.")
        except ValueError:
            print("Syötä kelvollinen numero.")

def arvo_painotukset():
    p = [0, 0, 0]
    while sum(p) != 100:
        p = [random.randint(0, 10) * 10 for _ in range(3)]
    return p

def kysy_painotukset():
    painotukset = []
    for i in range(13):
        while True:
            syote = input(f"Anna kohteen {i+1} painotukset 10:n tarkkuudella (esim. 80,10,10) tai paina Enter arpoaksesi: ")
            if syote == "":
                p = arvo_painotukset()
                print(f"Arvotut painotukset: {p[0]},{p[1]},{p[2]}")
                painotukset.append(p)
                break
            try:
                p = [int(x) for x in syote.split(',')]
                if len(p) == 3 and all(x % 10 == 0 for x in p) and sum(p) == 100:
                    painotukset.append(p)
                    break
                else:
                    print("Virheellinen syöte. Anna kolme lukua 10:n tarkkuudella, joiden summa on 100.")
            except ValueError:
                print("Virheellinen syöte. Käytä muotoa: 80,10,10")
    return painotukset

def luo_rivit(maara, painotukset):
    rivit = set()
    while len(rivit) < maara:
        rivi = tuple(random.choices(['1', 'X', '2'], weights=painot)[0] for painot in painotukset)
        rivit.add(rivi)
    return list(rivit)

def laske_jakauma(rivit):
    jakauma = {i: {'1': 0, 'X': 0, '2': 0} for i in range(13)}
    for rivi in rivit:
        for i, tulos in enumerate(rivi):
            jakauma[i][tulos] += 1
    return jakauma

def muotoile_jakauma(jakauma, maara):
    return [{
        'kohde': i + 1,
        '1': f"{j['1'] / maara * 100:.1f}%",
        'X': f"{j['X'] / maara * 100:.1f}%",
        '2': f"{j['2'] / maara * 100:.1f}%"
    } for i, j in jakauma.items()]

def main():
    rivien_maara = kysy_rivien_maara()
    painotukset = kysy_painotukset()
    
    rivit = luo_rivit(rivien_maara, painotukset)
    
    jakauma = laske_jakauma(rivit)
    muotoiltu_jakauma = muotoile_jakauma(jakauma, rivien_maara)
    
    print("\nLuodut rivit:")
    for i, rivi in enumerate(rivit, 1):
        print(f"Rivi {i}: {''.join(rivi)}")

    # Tulosta yhteenveto
    print("\nYhteenveto:")
    for i, j in enumerate(muotoiltu_jakauma, 1):
        print(f"Kohde {i}: 1: {j['1']}, x: {j['X']}, 2: {j['2']}")

if __name__ == "__main__":
    main()