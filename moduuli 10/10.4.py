import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus = 200):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
            self.nopeus = self.nopeus + muutos
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            elif self.nopeus < 0:
                self.nopeus = 0

    def kulje(self, aika):
            self.matka += self.nopeus * aika
class Kilpailu:
    def __init__(self,nimi, pituuskm, autot):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.autot = autot
    def tunti_kuluu(self):
        for auto in autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
    def tulosta(self):
        for i in autot:
            print(f"Rekkari:{i.rekisteritunnus} ,  huippunopeus:{i.huippunopeus}km/h\n,  nopeus:{i.nopeus},  matka:{i.matka}km")
    def kilpailu_ohi(self):
        for auto in  autot:
            if auto.matka > self.pituuskm:
                print(f"{auto.rekisteritunnus} voitti kisan!")
                self.tulosta()
                return True
        return False



autot=[]
for i in range(10):
    auto = Auto(f"ABC-{i +1}",random.randint(100,200))
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli",8000,autot)
kerrat = 1
while kilpailu.kilpailu_ohi() is False:
    kilpailu.tunti_kuluu()
    kilpailu.kilpailu_ohi()
    kerrat += 1
    if kerrat % 10 == 0:
        kilpailu.tulosta()

