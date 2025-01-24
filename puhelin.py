# Määrittele puhelinluettelon sanakirja
puhelinluettelo = {}

# Aloita sovelluksen silmukka
while True:
    # Kysy komentoa
    komento = input("Komento (1 haku, 2 lisää, 3 lopeta): ").strip()
    
    if komento == "1":  # Hae yhteystieto
        nimi = input("Nimi: ").strip()
        if nimi in puhelinluettelo:
            print(puhelinluettelo[nimi])
        else:
            print("Ei numeroa")
    
    elif komento == "2":  # Lisää tai päivitä yhteystieto
        nimi = input("Nimi: ").strip()
        numero = input("Numero: ").strip()
        puhelinluettelo[nimi] = numero  # Lisää tai päivitä puhelinnumero
        print("OK!")
    
    elif komento == "3":  # Lopeta sovellus
        print("Lopetetaan...")
        break
    
    else:  # Käsittele virheellisiä komentoja
        print("Virheellinen komento. Valitse 1, 2 tai 3.")
