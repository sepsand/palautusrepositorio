from abc import abstractmethod
from tuomari import Tuomari

class Kps:
    def __init__(self) -> None:
        self.tuomari = Tuomari()

    def aseta_siirto(self, siirto):
        pass

    def getEkanSiirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    @abstractmethod
    def getTokanSiirto(self):
        pass

    def pelaa(self):
        print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )
        ekan_siirto = self.getEkanSiirto()
        tokan_siirto = self.getTokanSiirto()
        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):           
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)
            ekan_siirto = self.getEkanSiirto()
            tokan_siirto = self.getTokanSiirto()
            self.aseta_siirto(ekan_siirto)
        print("Kiitos!")
        print(self.tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
