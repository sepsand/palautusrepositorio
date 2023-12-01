KAPASITEETTI = 5
OLETUSKASVATUS = 5
TYHJA = None


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [TYHJA] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS) -> None:
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko") 
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0


    def kuuluu(self, n):
        if n in self.ljono:
            return True
        else:
            return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                ljono_nyt = self.ljono
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(ljono_nyt, self.ljono)

            return True

        return False

    def poista(self, n):
        try:
            if TYHJA == n:
                raise Exception("Ei voi poistaa arvoa tyhjä")
            self.ljono.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        except:
            return False


    def kopioi_lista(self, a, b):
        for i in range(0, self.alkioiden_lkm):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm)
        self.kopioi_lista(self.ljono, uusi_lista)
        return uusi_lista

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()

        for i in range(0, len(a.ljono)):
            yhdiste.lisaa(a.ljono[i])

        for i in range(0, len(b.ljono)):
            yhdiste.lisaa(b.ljono[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()

        for i in range(0, len(a.ljono)):
            for j in range(0, len(b.ljono)):
                if a.ljono[i] == b.ljono[j]:
                    leikkaus.lisaa(b.ljono[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()

        for i in range(0, len(a.ljono)):
            erotus.lisaa(a.ljono[i])

        for i in range(0, len(b.ljono)):
            erotus.poista(b.ljono[i])

        return erotus

    def __str__(self):
        arvo_lista = ""
        try:
            for i in range(0, self.alkioiden_lkm):
                arvo_lista = arvo_lista + str(self.ljono[i])
                
                #Ei lisätä erotinpilkkua viimeisen arvon perään
                if i < self.alkioiden_lkm-1:
                    arvo_lista = arvo_lista + ", "
        except:
            pass
        return "{" + arvo_lista + "}"
