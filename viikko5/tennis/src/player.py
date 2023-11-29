from enum import Enum


class Player:
    class Score(Enum):
        LOVE = 0
        FIFTEEN = 1
        THIRTY = 2
        FORTY = 3

    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1
        
    def scoreToString(self):
        return self.Score(self.score).name.lower().capitalize()
        
    def getScore(self):
        return self.score
    
    def getName(self):
        return self.name
