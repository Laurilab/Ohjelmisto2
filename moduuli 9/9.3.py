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
    def kulje(self, aika):
        self.matka = self.matka + self.nopeus * aika


auto = Auto("ABC-123",142, 60, 2000)
auto.kulje(1.5)
print(f" Auton rekisteritunnus:{auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus} km/h"
f", tämän hetkinen nopeus:{auto.nopeus}km/h"
f"ja kuljettu matka:{auto.matka}km "
)

