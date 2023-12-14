from kps import Kps
from tekoaly import Tekoaly

class KPSTekoaly(Kps):
    def __init__(self, tekoaly=Tekoaly()) -> None:
        super().__init__()
        self.tekoaly = tekoaly

    def getTokanSiirto(self):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
