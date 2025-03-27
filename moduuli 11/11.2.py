import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,nopeus,matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, muutos):
            self.nopeus = self.nopeus + muutos
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            elif self.nopeus < 0:
                self.nopeus = 0

    def kulje(self, aika):
            self.matka += self.nopeus * aika
class Sähköauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,akkukw,nopeus,matka):
        self.akkukw = akkukw
        super().__init__(rekisteritunnus,huippunopeus,nopeus,matka)
class Pmauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,tankki,nopeus,matka):
        self.tankki = tankki
        super().__init__(rekisteritunnus,huippunopeus,nopeus,matka)

autot=[]
autot.append(Sähköauto("ABC-15",180,52.5,120,0))
autot.append(Pmauto("ACD-123",165,32.3,150,0))
for auto in autot:
    auto.kiihdytä(random.randint(-10, 15))
    auto.kulje(3)
for auto in autot:
    print(auto.rekisteritunnus,auto.matka)