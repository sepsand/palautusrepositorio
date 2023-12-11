import unittest
import pytest

from player_reader import PlayerReader
from query_builder import QueryBuilder
from statistics import Statistics

class TestQueryBuilder(unittest.TestCase):
# class TestQueryBuilder:
    def setUp(self):
        self.url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
        self.reader = PlayerReader(self.url)
        self.stats = Statistics(self.reader)
        self.query = QueryBuilder()
        self.query.reset()


    def testHasAtLeast(self):
        GOALS = 10
        matcher = self.query.hasAtLeast(GOALS, "goals").build()
        players = self.stats.matches(matcher)
        for player in players:
            self.assertGreaterEqual(player.goals, GOALS)

    def testHasFewerThan(self):
        ASSISTS = 5
        matcher = self.query.hasFewerThan(ASSISTS, "assists").build()
        players = self.stats.matches(matcher)
        for player in players:
            self.assertLess(player.assists, ASSISTS)

    def testPlaysIn(self):
        matcher = self.query.playsIn("NYR").build()
        players = self.stats.matches(matcher)
        for player in players:
            self.assertAlmostEqual(player.team, "NYR")

## No idea why these test do not work. It seems that pytest does not handle QueryBuilder instantiation properly.
    def testSmoke(self):
        matcher = self.query.build()
        players = self.stats.matches(matcher)
        self.assertEqual(1058, len(players))
        # assert 1058 == len(players)

    def testTehtävä4(self):
        correctOutput = [   "Barclay Goodrow      NYR          11 + 20 = 31",
                            "Jimmy Vesey          NYR          11 + 14 = 25",
                            "Adam Fox             NYR          12 + 60 = 72",
                            "Kaapo Kakko          NYR          18 + 22 = 40",
                            "Alexis Lafrenière    NYR          16 + 23 = 39"  ]
        matcher = self.query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()
        output = []
        for player in self.stats.matches(matcher):
            output.append(str(player))
        self.assertEqual(output, correctOutput)