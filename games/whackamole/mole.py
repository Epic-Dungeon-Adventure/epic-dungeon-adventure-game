import pygame
import sys
import random

# Game Constants
SCREEN_WIDTH = 771
SCREEN_HEIGHT = 606
GAME_DURATION = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Fonts
FONT_PATH = "C:/Windows/Fonts/cour.ttf"
menu_font = pygame.font.Font(FONT_PATH, 28)

# Load Images
mole_base = pygame.image.load("games/whackamole/assets/base1.png")
mole_images = [
    pygame.image.load("games/whackamole/assets/mole1.png").convert_alpha(),
    pygame.image.load("games/whackamole/assets/mole2.png").convert_alpha(),
    pygame.image.load("games/whackamole/assets/mole3.png").convert_alpha()
]
menu_images = pygame.image.load("games/whackamole/assets/menu.jpeg")
palu_images = [
    pygame.image.load("games/whackamole/assets/palu1.png").convert_alpha(),
    pygame.image.load("games/whackamole/assets/palu2.png").convert_alpha(),
]
background_image = pygame.image.load("games/whackamole/assets/back2.jpeg")

# Game Variables
score = 0
moles_whacked = 0
best_score = 0
game_start_time = 0
current_frame=0

# Game buttons and texts
play_text = menu_font.render("Play", True, WHITE)
quit_text = menu_font.render("Quit", True, WHITE)
best_score_text = menu_font.render("Best Score: " + str(best_score), True, BLACK)

# Game Rect
play_text_rect = play_text.get_rect(topleft=(15, SCREEN_HEIGHT // 3 + 15))
quit_text_rect = quit_text.get_rect(topleft=(15, SCREEN_HEIGHT // 3 + 90))

# Game State
game_state = "menu"
is_palu_active = False

clock = pygame.time.Clock()

# Mole Class
class Mole:
    def __init__(self):
        self.positions = [(50, 450), (210, 460), (350, 460), (550, 460), (150, 370), (400, 360), (570, 370), (300, 400)]
        self.respone = 0
        self.position = (50, 450)
        self.whacked = False

    def move(self):
        self.reset()

    def check_collision(self, mouse_pos):
        if not self.whacked:
            mole_rect = pygame.Rect(self.position, mole_images[0].get_size())
            if mole_rect.collidepoint(mouse_pos):
                self.whacked = True
                return True
        return False

    def reset(self):
        if int(self.respone % 6) == 0:
            self.position = random.choice(self.positions)
            self.whacked = False
            self.respone = 1

mole = Mole()

def draw_menu():
    screen.blit(menu_images, (0, 0))
    screen.blit(play_text, (15, SCREEN_HEIGHT // 3 + 15))
    screen.blit(quit_text, (15, SCREEN_HEIGHT // 3 + 90))
    screen.blit(best_score_text, (SCREEN_WIDTH // 2 - best_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 200))

def draw_gameplay():
    screen.blit(background_image, (0, 0))
    for position in mole.positions:
        screen.blit(mole_base, position)
    screen.blit(mole_images[int(current_frame)], mole.position)

    score_text = menu_font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    time_left = max(0, GAME_DURATION - (pygame.time.get_ticks() - game_start_time) // 1000)
    timer_text = menu_font.render("Time Left: " + str(time_left), True, BLACK)
    screen.blit(timer_text, (SCREEN_WIDTH - timer_text.get_width() - 200, 10))

    quit_text = menu_font.render("Quit", True, BLACK)
    screen.blit(quit_text, (SCREEN_WIDTH - quit_text.get_width() - 10, 10))

def play():
    global game_state, score, moles_whacked, game_start_time, is_palu_active, current_frame, best_score

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "menu":
                    draw_menu()

                    if play_text_rect.collidepoint(mouse_pos):
                        game_state = "gameplay"
                        score = 0
                        moles_whacked = 0
                        game_start_time = pygame.time.get_ticks()
                        mole.reset()
                    elif quit_text_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                elif game_state == "gameplay":
                    mouse_pos = pygame.mouse.get_pos()
                    is_palu_active = True

                    if mole.check_collision(mouse_pos):
                        score += 1
                        moles_whacked += 1
                        mole.reset()

            elif event.type == pygame.MOUSEBUTTONUP:
                if game_state == "gameplay":
                    is_palu_active = False
                    quit_text_rect = pygame.Rect(SCREEN_WIDTH - menu_font.size("Quit")[0] - 10, 10, menu_font.size("Quit")[0], menu_font.size("Quit")[1])

                    if quit_text_rect.collidepoint(mouse_pos):
                        game_state = "menu"
                        if score > best_score:
                            best_score = score
                        score = 0
                        moles_whacked = 0

        if game_state == "menu":
            draw_menu()
        elif game_state == "gameplay":
            draw_gameplay()
            mole.move()

            if is_palu_active:
                palu_rect = palu_images[0].get_rect(center=mouse_pos)
                screen.blit(palu_images[0], palu_rect)

            if event.type == pygame.MOUSEBUTTONUP:
                quit_text_rect = pygame.Rect(SCREEN_WIDTH - menu_font.size("Quit")[0] - 10, 10, menu_font.size("Quit")[0], menu_font.size("Quit")[1])
                if quit_text_rect.collidepoint(mouse_pos):
                    game_state = "menu"
                    if score > best_score:
                        best_score = score
                    score = 0
                    moles_whacked = 0

        mole.respone += 0.1
        current_frame += 0.1
        current_frame = (current_frame) % len(mole_images)

        pygame.display.flip()
        clock.tick(60)
