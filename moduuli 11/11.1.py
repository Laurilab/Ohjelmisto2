class Julkaisu():
    def __init__(self,nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"{self.nimi}")
class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivut):
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja:{self.kirjoittaja}, sivut:{self.sivut}")

class Lehti(Julkaisu):
    def __init__(self,nimi,toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja:{self.toimittaja}")

julkaisut = []
julkaisut.append(Lehti("Aku Ankka","Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6","Rosa Liksom",200))

for j in julkaisut:
    j.tulosta_tiedot()
