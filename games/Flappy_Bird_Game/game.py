import pygame
import sys
import random
from .game_class import FlappyBirdGame

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
game = FlappyBirdGame()
def play():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and game.game_active:
                        game.bird_movement = 0
                        game.bird_movement -= 6
                        game.sound3.play()
                    if event.key == pygame.K_SPACE and not game.game_active:
                        game.game_active = True
                        game.pipe_list.clear()
                        game.bird_rect.center = (100, 256)
                        game.bird_movement = 0
                        game.score = 0

                if event.type == game.SPAWNPIPE:
                    game.pipe_list.extend(game.create_pipe())

                if event.type == game.BIRDFLAP:
                    if game.bird_index < 2:
                        game.bird_index += 1
                    else:
                        game.bird_index = 0

                    game.bird_surface, game.bird_rect = game.bird_animation()

            game.screen.blit(game.bg_surface, (0, 0))

            if game.game_active:
                game.bird_movement += game.gravity
                rotated_bird = game.rotate_bird()
                game.bird_rect.centery += game.bird_movement
                game.screen.blit(rotated_bird, game.bird_rect)
                game.game_active = game.check_collision()

                game.move_pipes()
                game.draw_pipes()
                game.bird2_rect.centerx -= 5
                game.screen.blit(game.bird2_surface, game.bird2_rect)
                game.bird3_rect.centerx -= 5
                game.screen.blit(game.bird3_surface, game.bird3_rect)
                game.screen.blit(game.bird2_surface, game.bird2_rect)
                game.screen.blit(game.bird3_surface, game.bird3_rect)
                game.score += 0.012
                game.score_sound_countdown -= 1
                if game.score_sound_countdown <= 0:
                    game.sound2.play()
                    game.score_sound_countdown = 100
            else:
                game.screen.blit(game.game_over_surface, game.game_over_rect)
                game.update_score()
                game.score_display('game_over')

            game.floor_x_pos -= 1
            game.draw_floor()
            if game.floor_x_pos <= -288:
                game.floor_x_pos = 0

            if random.randint(0, 300) == 0:
                new_bird2_y = random.randint(100, 300)
                game.bird2_rect.center = (400, new_bird2_y)
                while any(pipe.colliderect(game.bird2_rect) for pipe in game.pipe_list):
                    new_bird2_y = random.randint(100, 300)
                    game.bird2_rect.center = (400, new_bird2_y)
            

            if random.randint(0, 400) == 0:
                new_bird3_y = random.randint(100, 300)
                game.bird3_rect.center = (600, new_bird3_y)
                while any(pipe.colliderect(game.bird3_rect) for pipe in game.pipe_list):
                    new_bird3_y = random.randint(100, 300)
                    game.bird3_rect.center = (600, new_bird3_y)
            

            
            score_surface = game.game_font.render(f'Score: {int(game.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(144, 40))
            game.screen.blit(score_surface, score_rect)

            pygame.display.update()
            game.clock.tick(60)

play()
