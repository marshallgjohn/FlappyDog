import pygame
from pygame.sprite import Sprite
import math


class Dog(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('images/dog.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.gravity_constant = 0
        self.neg_constant = 0

        self.is_jumping = False


    def update(self):
        if self.is_jumping:
            self.jump()
            self.gravity_constant = 0
            self.neg_constant += 0.0003
        else:
            self.gravity_constant += 0.20
            self.neg_constant = 0
            self.gravity()



    def jump(self):
        self.y -= 0.50 + self.neg_constant
        self.rect.y = self.y

    def gravity(self):
        self.y += 0.008 * self.gravity_constant
        self.rect.y = self.y

    def check_edges(self):
        if self.y < 0 or self.y > 490:
            return True
        else:
            return False

    def blitme(self):
        self.screen.blit(self.image, self.rect)