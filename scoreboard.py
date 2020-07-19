import pygame

class Scoreboard():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats


        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,24)

        self.prep_score()
        self.prep_highscore()


    def prep_score(self):
        score_str = "Score: " + str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (0,0,0)).convert()


        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_highscore(self):
        score_str = "High Score: " + str(self.stats.highscore)
        self.highscore_image = self.font.render(score_str, True, self.text_color, (0, 0, 0)).convert()

        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.left = self.screen_rect.centerx - self.highscore_rect.right / 2
        self.highscore_rect.top = 20

    def update_highscore(self):
        if (self.stats.score > self.stats.highscore):
            self.stats.highscore = self.stats.score
            self.prep_highscore()

        self.stats.score = 0


    def blitme(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)