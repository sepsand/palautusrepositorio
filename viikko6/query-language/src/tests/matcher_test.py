import unittest

from player_reader import PlayerReader
from statistics import Statistics
from matchers import All, And, HasAtLeast, HasFewerThan, Not, Or, PlaysIn  

class TestMatcher(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        self.reader = PlayerReader(self.url)
        self.stats = Statistics(self.reader)

    def testMatcherAll(self):
        correctLen = 1058

        players = self.stats.matches(All())
        self.assertEqual(len(players), correctLen)

    def testMatcherAndOr(self):
        correctList = [ "Mika Zibanejad       NYR          39 + 52 = 91",
                        "Artemi Panarin       NYR          29 + 63 = 92",
                        "Adam Fox             NYR          12 + 60 = 72",
                        "David Pastrnak       BOS          61 + 52 = 113",
                        "Carter Verhaeghe     FLA          42 + 31 = 73",
                        "Aleksander Barkov    FLA          23 + 55 = 78",
                        "Brandon Montour      FLA          16 + 57 = 73",
                        "Matthew Tkachuk      FLA          40 + 69 = 109"]
        matcher = And(
                    HasAtLeast(70, "points"),
                    Or(
                        PlaysIn("NYR"),
                        PlaysIn("FLA"),
                        PlaysIn("BOS")
                    )
                )
        output = []
        for player in self.stats.matches(matcher):
            output.append(player.__str__())
        self.assertEqual(correctList, output)

    def testMatcherOr(self):
        correctList = [ "David Pastrnak       BOS          61 + 52 = 113",
                        "Tage Thompson        BUF          47 + 47 = 94",
                        "Nikita Kucherov      TBL          30 + 83 = 113",
                        "Brayden Point        TBL          51 + 44 = 95",
                        "Mikko Rantanen       COL          55 + 50 = 105",
                        "Leon Draisaitl       EDM          52 + 76 = 128",
                        "Connor McDavid       EDM          64 + 89 = 153",
                        "Jason Robertson      DAL          46 + 63 = 109",
                        "Erik Karlsson        SJS          25 + 76 = 101"]
        matcher = Or(
                    HasAtLeast(45, "goals"),
                    HasAtLeast(70, "assists")
                )
        output = []
        for player in self.stats.matches(matcher):
            output.append(player.__str__())

        self.assertEqual(correctList, output)

    def testMatcherHasFewerThan(self):
        correctList =  [f"Jonny Brodzinski     NYR          1  + 1  = 2",
                        f"Ben Harpur           NYR          1  + 5  = 6",
                        f"Ryan Carpenter       NYR          1  + 2  = 3",
                        f"Ryan Lindgren        NYR          1  + 17 = 18",
                        f"Libor Hajek          NYR          1  + 0  = 1",
                        f"Zac Jones            NYR          1  + 1  = 2",
                        f"Will Cuylle          NYR          0  + 0  = 0",
                        f"Jaroslav Halak       NYR          0  + 0  = 0",
                        f"Igor Shesterkin      NYR          0  + 0  = 0" ]
        
        matcher = And(
                    HasFewerThan(2, "goals"),
                    PlaysIn("NYR")
                )
        output = []
        for player in self.stats.matches(matcher):
            output.append(player.__str__())

        self.assertAlmostEqual(correctList, output)
    
    def testMatchersNotHasFewerThan(self):
        matcherNot = And(                        
                        Not(HasAtLeast(2, "goals")),
                        PlaysIn("NYR")
                    )
        playersNot = self.stats.matches(matcherNot)

        matcherHasFewerThan = And(
                                HasFewerThan(2, "goals"),
                                PlaysIn("NYR")
                            )
        playersHasFewerThan = self.stats.matches(matcherHasFewerThan)

        self.assertEqual(playersNot, playersHasFewerThan)