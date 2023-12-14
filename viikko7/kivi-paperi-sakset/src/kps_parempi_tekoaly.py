from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self) -> None:
        super().__init__(TekoalyParannettu(10))

    def aseta_siirto(self, siirto):
        self.tekoaly.aseta_siirto(siirto)
