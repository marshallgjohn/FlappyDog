import sys, math, pygame
from random import randint

from dog import Dog
from obstacle import Obstacle



def activate_play_button(button,dog, obstacles, score, screen, stats, x,y):
    button_clicked = button.rect.collidepoint(x,y)

    if button_clicked and not stats.active:
        game_reset(dog, obstacles, score, screen)
        stats.active = True

def check_keydown_events(event, dog):
    if event.key == pygame.K_SPACE:
        dog.is_jumping = True
        play_sound('sound\\woof.wav')

def check_keyup_events(event, dog):
    if event.key == pygame.K_SPACE:
        dog.is_jumping = False

def check_events(button,dog, obstacle, score, screen, stats):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, dog)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,dog)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            activate_play_button(button,dog, obstacle, score, screen, stats, x,y)


def create_blockade(obstacles,screen):
    hole = randint(1,5)
    for i in range(1,6,1):
        if (i != hole):
            create_obstacle(obstacles, screen, 500, 100 * (i - 1))

def create_obstacle(obstacles,screen,x,y):
    ob = Obstacle(screen, x, y)
    obstacles.add(ob)

def clear_obstacles(obstacle, obstacles, screen):
    if obstacle.x <= -100:
        obstacles.empty()
        create_blockade(obstacles, screen)

def update_obstacles(obstacle, obstacles, dog, screen, score, stats):
    obstacle.move()
    clear_obstacles(obstacle, obstacles, screen)
    if stats.active:
        check_collision(dog, obstacle, obstacles, score, screen)
        score_update(dog, obstacle, score, stats)
    obstacle.blitme()


def check_collision(dog, obstacle, obstacles, score, screen):
    if pygame.sprite.spritecollideany(dog,obstacles):
        disable_game(dog, obstacle)
    if dog.check_edges():
        game_reset(dog,obstacles,score,screen)

def disable_game(dog, obstacle):
    play_sound('sound\\dead.wav')
    pygame.event.set_blocked(pygame.KEYDOWN)
    dog.is_jumping = False
    obstacle.x += 0.05

def game_reset(dog, obstacles, score, screen):
    obstacles.empty()
    create_blockade(obstacles,screen)

    dog.x = dog.screen_rect.centerx
    dog.y = dog.screen_rect.centery
    dog.gravity_constant = 0
    dog.neg_constant = 0
    score.update_highscore()

    pygame.event.set_allowed(pygame.KEYDOWN)




def play_sound (sound):
    pygame.mixer.Sound.play(pygame.mixer.Sound(sound))


def score_update(dog,obstacle, score, stats):
    if dog.rect.x == obstacle.rect.x:
        stats.score += 1
        play_sound('sound\\coin.wav')
    score.prep_score()



def update_screen(button, obstacles, screen, dog, stats, score):

    screen.fill((0,0,0))
    for x in obstacles:
        update_obstacles(x, obstacles, dog, screen, score, stats)


    score.blitme()


    if not stats.active:
        button.draw_button()
    else:
        dog.update()
        dog.blitme()

    pygame.display.update()




