def kysy_luvut():
    """Lukee kokonaislukuja käyttäjältä, kunnes annetaan 0, ja palauttaa listan luvuista."""
    luvut = []
    print("Anna kokonaislukuja (0 lopettaa):")
    while True:
        luku = int(input("Anna luku: "))
        if luku == 0:
            break
        luvut.append(luku)
    return luvut

def laske_negatiiviset(luvut):
    """Laskee ja palauttaa negatiivisten lukujen määrän listassa."""
    return sum(1 for luku in luvut if luku < 0)

def paaohjelma():
    """Ohjelman pääfunktio."""
    # Pyydetään käyttäjältä luvut
    luvut = kysy_luvut()

    # Lasketaan negatiiviset luvut
    negatiiviset = laske_negatiiviset(luvut)

    # Tulostetaan tulos
    print(f"\nSyötit nollan! Negatiivisten määrä: {negatiiviset}")

# Suoritetaan ohjelma
if __name__ == "__main__":
    paaohjelma()
