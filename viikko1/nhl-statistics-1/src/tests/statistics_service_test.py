from player import Player
from statistics_service import SortBy, StatisticsService
import unittest

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_constructor_reads_players(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(90, player.points)

    def test_team_stats(self):
        players = self.stats.team("PIT")
        self.assertAlmostEqual(players[0].points, 99) 

    def test_search_not_found(self):
        player = self.stats.search("n/a")
        self.assertAlmostEqual(player, None)

    def test_top_byAssists(self):
        players = self.stats.top(1, SortBy.ASSISTS)
        self.assertAlmostEqual(players[0].assists, 89)

    def test_top_byGoals(self):
        players = self.stats.top(1, SortBy.GOALS)
        self.assertAlmostEqual(players[0].goals, 45)

    def test_top_byPoints(self):
        players = self.stats.top(1, SortBy.POINTS)
        self.assertAlmostEqual(players[0].points, 124)

