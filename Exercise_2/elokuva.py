class Elokuva:
    def __init__(self, nimi, ohjaaja, genre, vuosi):
        self.nimi = nimi
        self.ohjaaja = ohjaaja
        self.genre = genre
        self.vuosi = vuosi

    def __str__(self):
        return f"{self.nimi} ({self.vuosi}), Ohjaaja: {self.ohjaaja}, Genre: {self.genre}"

tuulen_laakso = Elokuva("Tuulen laakso", "Hayao Miyazaki", "fantasia", 1984)
henkien_kansa = Elokuva("Henkien kansa", "Hayao Miyazaki", "seikkailu", 2001)

print(tuulen_laakso)  
print(f"Elokuvan {henkien_kansa.nimi} genre on {henkien_kansa.genre}")
