class Hissi:
    def __init__(self,alink,ylink,nykyinen,nimi):
        self.alin = alink
        self.ylin = ylink
        self.nykyinen = alink
        self.nimi= nimi
    def kerros_ylos(self):
        self.nykyinen += 1
        print(f"hissin kerros:{self.nykyinen}")
    def kerros_alas(self):
        self.nykyinen -= 1
        print(f"hissin kerros:{self.nykyinen}")
    def siirry_kerrokseen(self, kerros):
        if self.nykyinen < kerros:
            while kerros != self.nykyinen:
                self.kerros_ylos()
        elif self.nykyinen > kerros:
            while kerros != self.nykyinen:
                self.kerros_alas()
        else:
            print("Olet jo kyseisessä kerroksessa")
class Talo:
    def __init__(self, alink,ylink, määrä ):
        self.alink = alink
        self.ylink = ylink
        self.määrä = määrä
        self.hissit = []
        for i in range(self.määrä):
            self.hissit.append(Hissi(alink,ylink,alink,f"{i +1}"))


    def aja_hissiä(self,nimi,kerros):
        if kerros > self.ylink or kerros < self.alink:
            print("talossa ei ole sellaista kerrosta")


        else:
            self.hissit[nimi - 1].siirry_kerrokseen(kerros)






talo=Talo(0,10,5)

talo.aja_hissiä(3,-1)
