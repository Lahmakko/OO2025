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

def laske_parilliset(luvut):
    """Laskee ja palauttaa parillisten lukujen määrän listassa."""
    return sum(1 for luku in luvut if luku % 2 == 0)

def paaohjelma():
    """Ohjelman pääfunktio."""
    # Pyydetään käyttäjältä luvut
    luvut = kysy_luvut()

    # Lasketaan negatiiviset luvut
    negatiiviset = laske_negatiiviset(luvut)

    # Lasketaan parilliset luvut
    parilliset = laske_parilliset(luvut)

    # Tulostetaan tulokset
    print(f"\nNegatiivisten lukujen määrä: {negatiiviset}")
    print(f"Parillisten lukujen määrä: {parilliset}")

# Suoritetaan ohjelma
if __name__ == "__main__":
    paaohjelma()
