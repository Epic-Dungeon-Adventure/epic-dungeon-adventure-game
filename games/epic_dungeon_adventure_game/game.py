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

game = Game(screen, inital_state = "main menu")

def play_game_class():
   global game 
   game = Game(screen)



game_over_menu = GameOverMenu(screen, play_game_class)
main_menu = MainMenu(screen, play_game_class)


def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        
        if game.state == "main menu":
            main_menu.run_menu()
        elif game.state == "game over" and game.user.animation_complete:
            game_over_menu.run_menu()
        else:
            screen.fill((0, 0, 0))
            game.draw()
            game.update_state()
            
        pygame.display.update()
        # print(clock.get_fps())
        clock.tick(60)
