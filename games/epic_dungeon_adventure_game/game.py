import pygame
from sys import exit
from random import randint, choice
from .entitty import Entity
from .animations import get_animations

pygame.init()
screen = pygame.display.set_mode((1300,600))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

animations = get_animations()


head = Entity(animations['icecream']['death']) #<=====      eddit here
head_group = pygame.sprite.Group()
head_group.add(head)
head.animation_speed *= 2 #<=====      eddit here (not necessary)


posx = 50
posy = 50

def play():
    global posx
    global posy
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        head.update(posx, posy)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            posy -= 3
        if keys[pygame.K_s]:
            posy += 3
        if keys[pygame.K_a]:
            posx -= 3
        if keys[pygame.K_d]:
            posx += 3




        screen.fill((0, 0, 0))
        head_group.draw(screen)
        pygame.display.update()
        clock.tick(60)