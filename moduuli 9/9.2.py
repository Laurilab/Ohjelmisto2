class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0,matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    def kiihdytä(self,muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

        print(auto.nopeus)
        return



auto = Auto("ABC-123",142)
print(f" Auton rekisteritunnus:{auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}km/h, tämän hetkinen nopeus:{auto.nopeus} ja kuljettu matka:{auto.matka} ")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)