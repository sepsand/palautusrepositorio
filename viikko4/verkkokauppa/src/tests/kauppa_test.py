import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_ostoksen_2eri_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "piimä", 4)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 9)

    def test_ostoksen_2sama_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 10)

    def test_ostoksen_2eri_1eisaldoa_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "piimä", 4)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")


        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    # def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
    #     pankki_mock = Mock()
    #     viitegeneraattori_mock = Mock()

    #     # palautetaan aina arvo 42
    #     viitegeneraattori_mock.uusi.return_value = 42

    #     varasto_mock = Mock()

    #     # tehdään toteutus saldo-metodille
    #     def varasto_saldo(tuote_id):
    #         if tuote_id == 1:
    #             return 10

    #     # tehdään toteutus hae_tuote-metodille
    #     def varasto_hae_tuote(tuote_id):
    #         if tuote_id == 1:
    #             return Tuote(1, "maito", 5)

    #     # otetaan toteutukset käyttöön
    #     varasto_mock.saldo.side_effect = varasto_saldo
    #     varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    #     # alustetaan kauppa
    #     kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    #     # tehdään ostokset
    #     kauppa.aloita_asiointi()
    #     kauppa.lisaa_koriin(1)
    #     kauppa.tilimaksu("pekka", "12345")

    #     # varmistetaan, että metodia tilisiirto on kutsuttu
    #     pankki_mock.tilisiirto.assert_called()
    #     # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    # def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
    #     pankki_mock = Mock()
    #     viitegeneraattori_mock = Mock()

    #     # palautetaan aina arvo 42
    #     viitegeneraattori_mock.uusi.return_value = 42

    #     varasto_mock = Mock()

    #     # tehdään toteutus saldo-metodille
    #     def varasto_saldo(tuote_id):
    #         if tuote_id == 1:
    #             return 10

    #     # tehdään toteutus hae_tuote-metodille
    #     def varasto_hae_tuote(tuote_id):
    #         if tuote_id == 1:
    #             return Tuote(1, "maito", 5)

    #     # otetaan toteutukset käyttöön
    #     varasto_mock.saldo.side_effect = varasto_saldo
    #     varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    #     # alustetaan kauppa
    #     kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    #     # tehdään ostokset
    #     kauppa.aloita_asiointi()
    #     kauppa.lisaa_koriin(1)
    #     kauppa.tilimaksu("pekka", "12345")

    #     # varmistetaan, että metodia tilisiirto on kutsuttu
    #     pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
    
    # def test_ostoksen_2eri_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
    #     pankki_mock = Mock()
    #     viitegeneraattori_mock = Mock()

    #     # palautetaan aina arvo 42
    #     viitegeneraattori_mock.uusi.return_value = 42

    #     varasto_mock = Mock()

    #     # tehdään toteutus saldo-metodille
    #     def varasto_saldo(tuote_id):
    #         if tuote_id == 1:
    #             return 10
    #         if tuote_id == 2:
    #             return 10

    #     # tehdään toteutus hae_tuote-metodille
    #     def varasto_hae_tuote(tuote_id):
    #         if tuote_id == 1:
    #             return Tuote(1, "maito", 5)
    #         if tuote_id == 2:
    #             return Tuote(1, "piimä", 4)

    #     # otetaan toteutukset käyttöön
    #     varasto_mock.saldo.side_effect = varasto_saldo
    #     varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    #     # alustetaan kauppa
    #     kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    #     # tehdään ostokset
    #     kauppa.aloita_asiointi()
    #     kauppa.lisaa_koriin(1)
    #     kauppa.lisaa_koriin(2)
    #     kauppa.tilimaksu("pekka", "12345")

    #     # varmistetaan, että metodia tilisiirto on kutsuttu
    #     pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 9)

    # def test_ostoksen_2sama_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
    #     pankki_mock = Mock()
    #     viitegeneraattori_mock = Mock()

    #     # palautetaan aina arvo 42
    #     viitegeneraattori_mock.uusi.return_value = 42

    #     varasto_mock = Mock()

    #     # tehdään toteutus saldo-metodille
    #     def varasto_saldo(tuote_id):
    #         if tuote_id == 1:
    #             return 10

    #     # tehdään toteutus hae_tuote-metodille
    #     def varasto_hae_tuote(tuote_id):
    #         if tuote_id == 1:
    #             return Tuote(1, "maito", 5)

    #     # otetaan toteutukset käyttöön
    #     varasto_mock.saldo.side_effect = varasto_saldo
    #     varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    #     # alustetaan kauppa
    #     kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    #     # tehdään ostokset
    #     kauppa.aloita_asiointi()
    #     kauppa.lisaa_koriin(1)
    #     kauppa.lisaa_koriin(1)
    #     kauppa.tilimaksu("pekka", "12345")

    #     # varmistetaan, että metodia tilisiirto on kutsuttu
    #     pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 10)

    # def test_ostoksen_2eri_1eisaldoa_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametrilla(self):
    #     pankki_mock = Mock()
    #     viitegeneraattori_mock = Mock()

    #     # palautetaan aina arvo 42
    #     viitegeneraattori_mock.uusi.return_value = 42

    #     varasto_mock = Mock()

    #     # tehdään toteutus saldo-metodille
    #     def varasto_saldo(tuote_id):
    #         if tuote_id == 1:
    #             return 10
    #         return 0

    #     # tehdään toteutus hae_tuote-metodille
    #     def varasto_hae_tuote(tuote_id):
    #         if tuote_id == 1:
    #             return Tuote(1, "maito", 5)
    #         if tuote_id == 2:
    #             return Tuote(1, "piimä", 4)

    #     # otetaan toteutukset käyttöön
    #     varasto_mock.saldo.side_effect = varasto_saldo
    #     varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    #     # alustetaan kauppa
    #     kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    #     # tehdään ostokset
    #     kauppa.aloita_asiointi()
    #     kauppa.lisaa_koriin(1)
    #     kauppa.lisaa_koriin(2)
    #     kauppa.tilimaksu("pekka", "12345")

    #     # varmistetaan, että metodia tilisiirto on kutsuttu
    #     pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
