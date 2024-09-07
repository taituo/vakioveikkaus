"""
Vakioveikkausrivien Generaattori

MIT License

Copyright (c) 2023 [Tekijän nimi]

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

ASCII_LOGO = """
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
    p = [random.randint(1, 98) for _ in range(3)]
    summa = sum(p)
    return [round(x * 100 / summa) for x in p]

def kysy_painotukset():
    painotukset = []
    for i in range(13):
        while True:
            syote = input(f"Anna kohteen {i+1} painotukset (esim. 70,20,10) tai paina Enter arpoaksesi: ")
            if syote == "":
                p = arvo_painotukset()
                print(f"Arvotut painotukset: {p[0]},{p[1]},{p[2]}")
                painotukset.append(p)
                break
            try:
                p = [int(x) for x in syote.split(',')]
                if len(p) == 3:
                    summa = sum(p)
                    if summa == 100:
                        painotukset.append(p)
                        break
                    else:
                        print(f"Virheellinen syöte. Summa on {summa}, pitäisi olla 100.")
                        korjaus = input("Haluatko korjata automaattisesti? (k/e): ")
                        if korjaus.lower() == 'k':
                            kerroin = 100 / summa
                            p = [round(x * kerroin) for x in p]
                            p[-1] = 100 - sum(p[:-1])  # Varmistetaan, että summa on tasan 100
                            print(f"Korjatut painotukset: {p[0]},{p[1]},{p[2]}")
                            painotukset.append(p)
                            break
                else:
                    print("Virheellinen syöte. Anna kolme lukua pilkuilla erotettuna.")
            except ValueError:
                print("Virheellinen syöte. Käytä muotoa: 70,20,10")
    return painotukset

def luo_rivi(painotukset):
    return [random.choices(['1', 'x', '2'], weights=p)[0] for p in painotukset]

def main():
    rivien_maara = kysy_rivien_maara()
    painotukset = kysy_painotukset()
    
    rivit = set()
    yritykset = 0
    max_yritykset = rivien_maara * 10  # Asetetaan yläraja yrityksille

    while len(rivit) < rivien_maara and yritykset < max_yritykset:
        uusi_rivi = tuple(luo_rivi(painotukset))
        if uusi_rivi not in rivit:
            rivit.add(uusi_rivi)
        yritykset += 1

    if len(rivit) < rivien_maara:
        print(f"\nVaroitus: Pystyttiin luomaan vain {len(rivit)} uniikkia riviä {rivien_maara} pyydetyn sijaan.")
    
    print("\nLuodut rivit:")
    for i, rivi in enumerate(rivit, 1):
        print(f"Rivi {i}: {''.join(rivi)}")

if __name__ == "__main__":
    main()