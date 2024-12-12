from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_burung(self):
        super().cetak()
        print("jenis \t: ", self.jenis, 
              "\nBunyi \t: ", self.bunyi)

Merpati = Burung("Merpati", "Biji-bijian", "Udara", "Telur", "Kolumbidae", "wi wi wit")
Merpati.cetak_burung()
puyuh = Burung("puyuh", "seranga", "Udara", "Telur", "Sparrow", "cicwit-cicwit")
puyuh.cetak_burung()