import pygame
from sys import exit
from random import randint, choice
from components.entitty import Entity
from components.text_box import TextBox
from components.sound import Sound
from .animations import get_animations
from .game_class import Game

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

animations = get_animations()

game = Game(screen)


def play():
    global posx
    global posy
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        

        screen.fill((0, 0, 0))
        game.draw()
        game.update_state()
       
        pygame.display.update()
        # print(clock.get_fps())
        clock.tick(60)
