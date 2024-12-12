from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak()
        print("Design \t: ", self.design, 
              "\nRacun \t: ", self.racun)

anaconda = Ular("Anaconda", "daging", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()
Kobra = Ular("Kobra", "Tikus", "Hutan", "Bertelur", "abstrak", "Berbisa")
Kobra.cetak_ular()