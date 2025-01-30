class JunanVaunu:
    def __init__(self, vaunu_id, kokonaispaikat):
        # Alustetaan vaunu yksilöllisellä tunnisteella ja paikkojen määrällä
        self.vaunu_id = vaunu_id ##1.uniikki identifieri
        self.kokonaispaikat = kokonaispaikat ##1.informaatio junan paikoista yhteensä
        self.varatut_paikat = set()  # 2.yksilöllisesti merkityty paikat, kuinka monta paikkaa varattu ja mitkä? 
    
    def varaa_paikka(self, paikka_numero): #3.tästä on mahdollista lisätä ja poistaa varauksia kerrallaan ja resetoimaan
        """Varaa paikka, jos se ei ole jo varattu."""
        if paikka_numero < 1 or paikka_numero > self.kokonaispaikat:
            print(f"Virheellinen paikkanumero. Valitse paikka välillä 1 ja {self.kokonaispaikat}.")
            return
        if paikka_numero in self.varatut_paikat:
            print(f"Paikka {paikka_numero} on jo varattu.")
        else:
            self.varatut_paikat.add(paikka_numero)
            print(f"Paikka {paikka_numero} varattu onnistuneesti.")
    
    def poista_varaus(self, paikka_numero):
        """Peruuta varaus tietylle paikalle."""
        if paikka_numero in self.varatut_paikat: #4. samaa paikkaa ei voi varata kahdesti
            self.varatut_paikat.remove(paikka_numero)
            print(f"Paikan {paikka_numero} varaus poistettu.")
        else:
            print(f"Paikka {paikka_numero} ei ole varattu.")
    
    def nollaa_varaukset(self):
        """Nollaa kaikki varaukset."""
        self.varatut_paikat.clear()
        print("Kaikki varaukset on peruutettu.")
    
    def onko_taysi(self): #6. onko vaunu täynnä inquire
        """Tarkistaa, onko vaunu täynnä."""
        return len(self.varatut_paikat) == self.kokonaispaikat
    
    def raportti(self):#tästä saa tilattua raportin junan tilanteesta
        """Tuottaa raportin varatuista ja varaamattomista paikoista."""
        varatut = sorted(self.varatut_paikat)
        varaamattomat = [i for i in range(1, self.kokonaispaikat + 1) if i not in self.varatut_paikat]
        varatut_str = ", ".join(map(str, varatut))
        varaamattomat_str = ", ".join(map(str, varaamattomat))
                    #uniikki identifieri vaunu esim A2
        return (f"Vaunu {self.vaunu_id} - Varatut paikat: {varatut_str}\n"
                f"Varaamattomat paikat: {varaamattomat_str}")
    
# Koodia voi käyttää esimerkiksi näin
vaunu = JunanVaunu("A1", 10) #uniikki identifieri A1 tässä tapauksessa

vaunu.varaa_paikka(1)
vaunu.varaa_paikka(3)
vaunu.varaa_paikka(5)

print(vaunu.raportti())

vaunu.poista_varaus(3)

print(vaunu.raportti())

vaunu.nollaa_varaukset()

print(vaunu.raportti())
