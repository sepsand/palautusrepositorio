from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KpsBuilder:
    @staticmethod
    def luo_peli():
        print("Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
            )

        vastaus = input()

        if vastaus.endswith("a"):
            return KPSPelaajaVsPelaaja()
        elif vastaus.endswith("b"):
            return KPSTekoaly()
        elif vastaus.endswith("c"):
            return KPSParempiTekoaly()
        else:
            return None
