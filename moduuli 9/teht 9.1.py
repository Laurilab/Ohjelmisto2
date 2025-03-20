class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0,matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto = Auto("ABC-123","142 km/h")
print(f" Auton rekisteritunnus:{auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}, tämän hetkinen nopeus:{auto.nopeus} ja kuljettu matka:{auto.matka} ")