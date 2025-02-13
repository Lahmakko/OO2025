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

def laske_positiiviset_jakautuvat_kolmella(luvut):
    """Laskee ja palauttaa positiivisten lukujen summan, jotka ovat jaollisia kolmella."""
    return sum(luku for luku in luvut if luku > 0 and luku % 3 == 0)

def paaohjelma():
    """Ohjelman pääfunktio."""
    # Pyydetään käyttäjältä luvut
    luvut = kysy_luvut()

    # Lasketaan negatiiviset luvut
    negatiiviset = laske_negatiiviset(luvut)

    # Lasketaan parilliset luvut
    parilliset = laske_parilliset(luvut)

    # Lasketaan positiivisten lukujen summa, jotka ovat jaollisia kolmella
    positiiviset_kolmella = laske_positiiviset_jakautuvat_kolmella(luvut)

    # Tulostetaan tulokset
    print(f"\nNegatiivisten lukujen määrä: {negatiiviset}")
    print(f"Parillisten lukujen määrä: {parilliset}")
    print(f"Positiivisten lukujen summa, jotka ovat jaollisia kolmella: {positiiviset_kolmella}")

# Suoritetaan ohjelma
if __name__ == "__main__":
    paaohjelma()
