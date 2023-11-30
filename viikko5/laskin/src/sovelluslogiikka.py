class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinenArvo = [arvo]

    def miinus(self, operandi):
        self.paivitaEdellinenArvo(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.paivitaEdellinenArvo(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.paivitaEdellinenArvo(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        if [] == self._edellinenArvo:
            pass
        else:
            self._arvo = self._edellinenArvo.pop()

    def paivitaEdellinenArvo(self, arvo):
        self._edellinenArvo.append(arvo)

