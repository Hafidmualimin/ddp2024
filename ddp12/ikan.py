from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.ukuran = ukuran
    def cetak_ikan(self):
        super().cetak()
        print("habitat \t: ", self.habitat, 
              "\nUkuran \t: ", self.ukuran)

cupang = Ikan("Hiu", "Daging", "sungai", "Telur", "sungai", "kecil")
cupang.cetak_ikan()
Mas= Ikan("Mas", "Pelet", "Air Tawar", "Telur", "aquarium", "Kecil")
Mas.cetak_ikan()