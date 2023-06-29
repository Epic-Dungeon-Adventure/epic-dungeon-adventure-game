import pygame
import sys
import random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 420))
    screen.blit(floor_surface, (floor_x_pos + 288, 420))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(400, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(400, random_pipe_pos - 180))

    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if bird_rect.colliderect(bird2_rect) or bird_rect.colliderect(bird3_rect):
        death_sound.play()
        return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 420:
        return False

    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 5, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(144, 40))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(144, 40))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center=(100, 400))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
game_font = pygame.font.Font('games/Flappy_Bird_Game/font/04B_19.TTF', 30)

# Game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

# Load assets
bg_surface = pygame.image.load('games/Flappy_Bird_Game/assets/background-night.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (288, 512))

floor_surface = pygame.image.load('games/Flappy_Bird_Game/assets/base.png').convert()
floor_x_pos = 0

bird_downflap = pygame.image.load('games/Flappy_Bird_Game/bird/redbird_1.png').convert_alpha()
bird_midflap = pygame.image.load('games/Flappy_Bird_Game/bird/redbird_2.png').convert_alpha()
bird_upflap = pygame.image.load('games/Flappy_Bird_Game/bird/redbird_3.png').convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 256))

bird2_surface = pygame.image.load('games/Flappy_Bird_Game/assets/parrot/Parrot_1.png').convert_alpha()  # Path to second bird image
bird2_width = 40  # Set the desired width for the second bird
bird2_height = 30  # Set the desired height for the second bird
bird2_surface = pygame.transform.scale(bird2_surface, (bird2_width, bird2_height))

bird2_x = 400  # Adjust the x-coordinate as per your needs
bird2_y = random.randint(100, 300)  # Adjust the y-coordinate as per your needs
bird2_rect = bird2_surface.get_rect(center=(bird2_x, bird2_y))

bird3_surface = pygame.image.load('games/Flappy_Bird_Game/assets/redbird/red_1.png').convert_alpha()  # Path to third bird image
bird3_width = 40  # Set the desired width for the third bird
bird3_height = 30  # Set the desired height for the third bird
bird3_surface = pygame.transform.scale(bird3_surface, (bird3_width, bird3_height))

bird3_x = 600  # Adjust the x-coordinate as per your needs
bird3_y = random.randint(100, 300)  # Adjust the y-coordinate as per your needs
bird3_rect = bird3_surface.get_rect(center=(bird3_x, bird3_y))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

pipe_surface = pygame.image.load('games/Flappy_Bird_Game/assets/pipe-red.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 300, 350]

game_over_surface = pygame.image.load('games/Flappy_Bird_Game/assets/message.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(144, 256))

flap_sound = pygame.mixer.Sound('games/Flappy_Bird_Game/sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('games/Flappy_Bird_Game/sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('games/Flappy_Bird_Game/sound/sfx_point.wav')
score_sound_countdown = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 256)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Score
        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    # Bird 2
    # Bird 2
    if random.randint(0, 300) == 0:
        new_bird2_y = random.randint(100, 300)
        bird2_rect.center = (400, new_bird2_y)
        while any(pipe.colliderect(bird2_rect) for pipe in pipe_list):
            new_bird2_y = random.randint(100, 300)
            bird2_rect.center = (400, new_bird2_y)
    bird2_rect.centerx -= 5
    screen.blit(bird2_surface, bird2_rect)

    # Bird 3
    if random.randint(0, 400) == 0:
        new_bird3_y = random.randint(100, 300)
        bird3_rect.center = (600, new_bird3_y)
        while any(pipe.colliderect(bird3_rect) for pipe in pipe_list):
            new_bird3_y = random.randint(100, 300)
            bird3_rect.center = (600, new_bird3_y)
    bird3_rect.centerx -= 5
    screen.blit(bird3_surface, bird3_rect)

    pygame.display.update()
    clock.tick(60)
