class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']
    
    def __str__(self):
        # return self.name + " team " + self.team + " goals " + str(self.goals) + " assists " + str(self.assists)
        return ( 
            f"{self.name} "
            f"team {self.team} "
            f"goals {self.goals} "
            f"assists {self.assists}"
        )