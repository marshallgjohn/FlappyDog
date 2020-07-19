import pygame
from pygame.sprite import Sprite
import game_functions as gf
import math


class Obstacle(Sprite):

    def __init__(self, screen,x,y):
        super().__init__()
        self.screen = screen
        #self.settings = settings

        self.image = pygame.image.load('images/cat.png').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.x = x

        self.rect.x = float(self.x)
        self.rect.y = float(y)

    def move(self):
        self.x -= 0.10
        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)
