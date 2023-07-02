import pygame
# from random import randint, choice
import random
import sys

from components.entitty import Entity
from .animations import get_animations

class FlappyBirdGame:
    def __init__(self, screen):
        pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
        pygame.init()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font('games/Flappy_Bird_Game/assets/font/04B_19.TTF', 30)
        self.bird2_surface = pygame.image.load('games/Flappy_Bird_Game/assets/parrot/Parrot_1.png').convert_alpha()
        self.bird2_width = 40
        self.bird2_height = 30
        self.bird2_surface = pygame.transform.scale(self.bird2_surface, (self.bird2_width, self.bird2_height))
        self.bird2_x = 400
        self.bird2_y = random.randint(100, 300)
        self.bird2_rect = self.bird2_surface.get_rect(center=(self.bird2_x, self.bird2_y))

        self.bird3_surface = pygame.image.load('games/Flappy_Bird_Game/assets/redbird/red_1.png').convert_alpha()
        self.bird3_width = 40
        self.bird3_height = 30
        self.bird3_surface = pygame.transform.scale(self.bird3_surface, (self.bird3_width, self.bird3_height))
        self.bird3_x = 600
        self.bird3_y = random.randint(100, 300)
        self.bird3_rect = self.bird3_surface.get_rect(center=(self.bird3_x, self.bird3_y))

        self.gravity = 0.25
        self.bird_movement = 0
        self.game_active = True
        self.score = 0
        self.high_score = 0
        self.game_font = pygame.font.Font('games/Flappy_Bird_Game/assets/font/04B_19.TTF', 30)



        self.load_assets()
        self.create_birds()
        self.create_pipes()

        self.BIRDFLAP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.BIRDFLAP, 200)

        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1200)

    def load_assets(self):
        self.bg_surface = pygame.image.load('games/Flappy_Bird_Game/assets/background-night.png').convert()
        self.bg_surface = pygame.transform.scale(self.bg_surface, (288, 512))

        self.floor_surface = pygame.image.load('games/Flappy_Bird_Game/assets/base.png').convert()
        self.floor_x_pos = 0

        bird_downflap = pygame.image.load('games/Flappy_Bird_Game/assets/bird/redbird_1.png').convert_alpha()
        bird_midflap = pygame.image.load('games/Flappy_Bird_Game/assets/bird/redbird_2.png').convert_alpha()
        bird_upflap = pygame.image.load('games/Flappy_Bird_Game/assets/bird/redbird_3.png').convert_alpha()
        self.bird_frames = [bird_downflap, bird_midflap, bird_upflap]
        self.bird_index = 0
        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird_surface.get_rect(center=(100, 256))

        self.game_over_surface = pygame.image.load('games/Flappy_Bird_Game/assets/message.png').convert_alpha()
        self.game_over_rect = self.game_over_surface.get_rect(center=(144, 256))

        self.flap_sound = pygame.mixer.Sound('games/Flappy_Bird_Game/sound/sfx_wing.wav')
        self.death_sound = pygame.mixer.Sound('games/Flappy_Bird_Game/sound/sfx_hit.wav')
        self.score_sound = pygame.mixer.Sound('games/Flappy_Bird_Game/sound/sfx_point.wav')
        self.score_sound_countdown = 100

    def create_birds(self):
        bird2_surface = pygame.image.load('games/Flappy_Bird_Game/assets/parrot/Parrot_1.png').convert_alpha()
        bird2_width = 40
        bird2_height = 30
        bird2_surface = pygame.transform.scale(bird2_surface, (bird2_width, bird2_height))

        bird2_x = 400
        bird2_y = random.randint(100, 300)
        self.bird2_rect = bird2_surface.get_rect(center=(bird2_x, bird2_y))

        bird3_surface = pygame.image.load('games/Flappy_Bird_Game/assets/redbird/red_1.png').convert_alpha()
        bird3_width = 40
        bird3_height = 30
        bird3_surface = pygame.transform.scale(bird3_surface, (bird3_width, bird3_height))

        bird3_x = 600
        bird3_y = random.randint(100, 300)
        self.bird3_rect = bird3_surface.get_rect(center=(bird3_x, bird3_y))

    def create_pipes(self):
        self.pipe_surface = pygame.image.load('games/Flappy_Bird_Game/assets/pipe-red.png').convert()
        self.pipe_list = []
        self.pipe_height = [200, 300, 350]

    def draw_floor(self):
        self.screen.blit(self.floor_surface, (self.floor_x_pos, 420))
        self.screen.blit(self.floor_surface, (self.floor_x_pos + 288, 420))

    def create_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_surface.get_rect(midtop=(400, random_pipe_pos))
        top_pipe = self.pipe_surface.get_rect(midbottom=(400, random_pipe_pos - 180))

        return bottom_pipe, top_pipe

    def move_pipes(self):
        for pipe in self.pipe_list:
            pipe.centerx -= 5

    def draw_pipes(self):
        for pipe in self.pipe_list:
            if pipe.bottom >= 512:
                self.screen.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                self.screen.blit(flip_pipe, pipe)

    def check_collision(self):
        for pipe in self.pipe_list:
            if self.bird_rect.colliderect(pipe):
                self.death_sound.play()
                return False

        if (
            self.bird_rect.colliderect(self.bird2_rect)
            or self.bird_rect.colliderect(self.bird3_rect)
        ):
            self.death_sound.play()
            return False

        if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 420:
            return False

        return True

    def rotate_bird(self):
        new_bird = pygame.transform.rotozoom(
            self.bird_surface, -self.bird_movement * 5, 1
        )
        return new_bird

    def bird_animation(self):
        new_bird = self.bird_frames[self.bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, self.bird_rect.centery))
        return new_bird, new_bird_rect

    def score_display(self, game_state):
        if game_state == 'main_game':
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(144, 40))
            self.screen.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(144, 40))
            self.screen.blit(score_surface, score_rect)

            high_score_surface = self.game_font.render(f'High Score: {int(self.high_score)}', True, (255, 255, 255))
            high_score_rect = score_surface.get_rect(center=(100, 400))
            self.screen.blit(high_score_surface, high_score_rect)

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score


