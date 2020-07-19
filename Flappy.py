import pygame, sys
from pygame.locals import *

from dog import Dog
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button




def create():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Flappy Dog')
    screen.fill((0, 0, 0))

    obstacles = Group()

    stats = GameStats()
    score = Scoreboard(screen, stats)
    dog = Dog(screen)

    gf.create_blockade(obstacles, screen)
    button = Button(screen, 'PLAY')


    while True:

        gf.check_events(button,dog, obstacles, score, screen, stats)
        pygame.draw.rect(screen, (255, 255, 255), Rect((100, 100), (130, 170)))
        gf.update_screen(button, obstacles, screen, dog, stats, score)



create()
