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

autot=[]
for i in range(10):
    auto = Auto(f"ABC-{i +1}")
    auto.nopeus = random.randint(100,200)
    autot.append(auto)

while auto.matka <= 10000:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka > 10000:
            print(f"{auto.rekisteritunnus}, voitti kilpailun")
            break

for i in autot:
    print(f"Rekkari:{i.rekisteritunnus} ,  huippunopeus:{i.huippunopeus}km/h\n,  nopeus:{i.nopeus},  matka:{i.matka}km")










