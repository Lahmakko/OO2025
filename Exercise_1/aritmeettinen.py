def laske_termit(maara):
    """Laskee AP:n kaikki termit 3, 6, 9, ... annetun enimmäisarvon perusteella."""
    termit = []
    arvo = 3
    while arvo <= maara:
        termit.append(arvo)
        arvo += 3
    return termit

def laske_termeja(termit):
    """Laskee ja palauttaa termien määrän."""
    return len(termit)

def laske_summa(termit):
    """Laskee ja palauttaa termien summan."""
    return sum(termit)

def laske_nelioiden_summa(termit):
    """Laskee ja palauttaa termien neliöiden summan."""
    return sum(termi**2 for termi in termit)

def paaohjelma():
    """Ohjelman pääfunktio."""
    # Pyydetään käyttäjältä maksimiarvo
    maksimi = int(input("Anna AP:n maksimiarvo (esim. 50): "))

    # Lasketaan kaikki termit
    termit = laske_termit(maksimi)

    # Lasketaan termien määrä
    maara = laske_termeja(termit)

    # Lasketaan termien summa
    summa = laske_summa(termit)

    # Lasketaan termien neliöiden summa
    nelioiden_summa = laske_nelioiden_summa(termit)

    # Tulostetaan tulokset
    print(f"\nAP (3, 6, 9, ...) maksimiarvoon {maksimi} asti:")
    print(f"Termien määrä: {maara}")
    print(f"Termien summa: {summa}")
    print(f"Termien neliöiden summa: {nelioiden_summa}")

# Suoritetaan ohjelma
if __name__ == "__main__":
    paaohjelma()
