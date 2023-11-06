import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1, -2)
        self.varasto3 = Varasto(9,8)
        self.varasto4 = Varasto(8, 9)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_pienempi_alku_saldo_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto3.saldo, 8)

    def test_suurempi_alku_saldo_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto4.saldo, 8)

    def test_negatiivinen_lisays_varastoon(self):
        self.varasto3.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto3.saldo, 8)

    def test_pienempi_lisays_kuin_paljonko_mahtuu(self):
        self.varasto3.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto3.saldo, 9)

    def test_suurempi_lisays_kuin_paljonko_mahtuu(self):
        self.varasto3.lisaa_varastoon(2)
        self.assertAlmostEqual(self.varasto3.saldo, 9)

    def test_negatiivinen_maara_ottaa_varastosta(self):
        self.varasto3.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto3.saldo, 8)

    def test_suurempi_maara_ottaa_varastosta_kuin_saldo(self):
        self.varasto3.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto3.saldo, 0)

    def test_palautus(self):
        self.assertAlmostEqual(str(self.varasto3), 'saldo = 8, vielä tilaa 1')
        