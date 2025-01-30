class Lemmikki:
    def __init__(self, nimi: str, rotu: str, syntymavuosi: int):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymavuosi = syntymavuosi

def uusi_lemmikki(nimi: str, rotu: str, syntymavuosi: int) -> Lemmikki:
    return Lemmikki(nimi, rotu, syntymavuosi)


kassu = uusi_lemmikki("Kassu", "kultainen noutaja", 2024)
print(kassu.nimi)
print(kassu.rotu)
print(kassu.syntymavuosi)