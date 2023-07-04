import pygame
from sys import exit
from .animations import get_animations
from .game_class import Game
from .menu import GameOverMenu,MainMenu,PauseMenu

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Epic Dungeon Adventure")
clock = pygame.time.Clock()

animations = get_animations()

game = Game(screen)

def play():
   global game 
   game = Game(screen)
   game.state = "walk"



# game_over_menu = GameOverMenu(screen, play)
main_menu = MainMenu(screen, play)
# pause_menu = PauseMenu(screen, play)

def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # will handle pause menu here if esc pressed
        
        if game.state == "main menu":
            main_menu.run_menu()
        else:
            screen.fill((0, 0, 0))
            game.draw()
            game.update_state()
       
        pygame.display.update()
        print(game.state)
        # print(clock.get_fps())
        clock.tick(60)
