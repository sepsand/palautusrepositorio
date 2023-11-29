from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.getName():
            self.player1.won_point()
        else:
            self.player2.won_point()

    def getGameWon(self):
        if abs(self.player1.getScore() - self.player2.getScore()) >= 2:
            if self.player1.getScore() > self.player2.getScore():
                won = self.player1
            else:
                won = self.player2
            return "Win for " + won.getName()
        else:
            return None

    def getGameAdvantage(self):
        if abs(self.player1.getScore() - self.player2.getScore()) == 1:
            if self.player1.getScore() > self.player2.getScore():
                advantage = self.player1
            else:
                advantage = self.player2
            return "Advantage " + advantage.getName()
        else:
            return None

    def getGameEqual(self):
        if self.player1.getScore() < 3:
            score = self.player1.scoreToString() + "-All"
        else:
            score = "Deuce"
        return score

    def getGameNoAdvantage(self):
        score = self.player1.scoreToString() + \
            "-" + \
            self.player2.scoreToString()
        return score 

    def get_score(self):
        if self.player1.getScore() == self.player2.getScore():
            score = self.getGameEqual()
        elif self.player1.getScore() < 4 and \
             self.player2.getScore() < 4:
            score = self.getGameNoAdvantage()
        elif 1 == abs(self.player1.getScore() - self.player2.getScore()) :            
            score = self.getGameAdvantage()    
        else:
            score = self.getGameWon()
            
        return score
