import unittest

from player_reader import PlayerReader
from statistics import Statistics
from matchers import All, And, HasAtLeast, PlaysIn, Not, HasFewerThan

class TestMatcher(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        self.reader = PlayerReader(self.url)
        self.stats = Statistics(self.reader)

    def testMatcherAll(self):
        correctLen = 1058

        players = self.stats.matches(All())
        self.assertEqual(len(players), correctLen)
    
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