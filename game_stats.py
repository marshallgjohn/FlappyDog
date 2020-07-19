

class GameStats():
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.active = False
        self.reset_stats()

    def reset_stats(self):
        self.score = 0