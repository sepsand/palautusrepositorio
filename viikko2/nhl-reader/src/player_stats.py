from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, playerReader):
        self.players = playerReader.getPlayers()

    def top_scorers_by_nationality(self, nationality):
        def sortByPoints(player):
            return player.goals + player.assists
        
        players = filter(lambda x : x.nationality == nationality, self.players)
        players = sorted(players,
                        reverse=True,
                        key=sortByPoints)
        return players
        