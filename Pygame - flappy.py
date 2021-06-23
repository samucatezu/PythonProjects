import pygame
from pygame.locals import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('bluebird-upflap.png').convert_alpha(),
                       pygame.image.load('bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('bluebird-downflap.png').convert_alpha()]

        self.speed = SPEED

        self.speed = SPEED

        self.current_image = 0

        self.image = pygame.image.load('bluebird-midflap.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2


    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += GRAVITY

        # update height
        self.rect[1] = self.speed

    def bump(self):
        self.speed = -SPEED

class Ground(pygame.sprite.Sprite):

    def __init__(self,width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('base.png')
        self.image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.image.get_rect()
        self_rect[1] = SCREEN_HEIGHT - height

    def update(self):
        self.rect[0] -= GAME_SPEED


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))


bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()
ground = Ground(SCREEN_WIDTH, 2 * SCREEN_WIDTH, 100)
ground_group.add(ground)
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type ==KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()



    screen.blit(BACKGROUND, (0,0))

    bird_group.update()
    ground_group.update()

    bird_group.draw(screen)
    ground_group.draw(screen)

    pygame.display.update()