class Hissi:
    def __init__(self,ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.nykyinen = alin
    def kerros_ylos(self):
        self.nykyinen += 1

    def kerros_alas(self):
        self.nykyinen -= 1
    def siirry_kerrokseen(self, kerros):
        if self.nykyinen < kerros:
            while kerros != self.nykyinen:
                h.kerros_ylos()
        elif self.nykyinen > kerros:
            while kerros != self.nykyinen:
                h.kerros_alas()
        else:
            print("Olet jo kyseisessä kerroksessa")

h = Hissi(20, -3)
h.siirry_kerrokseen(5)
print(h.nykyinen)
h.siirry_kerrokseen(h.alin)
print(h.nykyinen)