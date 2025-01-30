class Movie:
    def __init__(self, nimi: str, ohjaaja: str, genre: str, vuosi: int):
        self.nimi = nimi
        self.ohjaaja = ohjaaja
        self.genre = genre
        self.vuosi = vuosi

def movies_of_genre(movies: list, genre: str) -> list:
    return [movie for movie in movies if movie.genre == genre]

tuulen_laakso = Movie("Tuulen laakso", "Hayao Miyazaki", "fantasia", 1984)
henkien_kansa = Movie("Henkien kansa", "Hayao Miyazaki", "fantasia", 2001)
naapurini_totoro = Movie("Naapurini Totoro", "Hayao Miyazaki", "lasten", 1988)
kurenai_no_buta = Movie("Kurenai no buta", "Hayao Miyazaki", "seikkailu", 1992)

movies = [tuulen_laakso, henkien_kansa, naapurini_totoro, kurenai_no_buta]

print("Hayao Miyazakin fantasia-elokuvat:")
for movie in movies_of_genre(movies, "fantasia"):
    print(f"{movie.ohjaaja}: {movie.nimi}")