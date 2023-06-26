import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Define game colors
BLACK = (0, 0, 0)


background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

snake_color = (0, 255, 0) 
food_colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0),(97,98,100)]  #colors for the food

game_over_sound = pygame.mixer.Sound('game_over.wav')
eat_food_sound = pygame.mixer.Sound('eat_food.mp3')
background_music = pygame.mixer.Sound('background_music.wav')
game_win_sound = pygame.mixer.Sound('win_game.wav')

# Set the volume for the background music and eating sound
background_music.set_volume(0.5)
eat_food_sound.set_volume(1.0)
game_win_sound.set_volume(0.8)

#  font for the score
font_style = pygame.font.SysFont(None, 30)

class SnakeGame:
    def __init__(self, level):
        self.snake_block_size = 20
        self.level = level
        self.snake_speed = 15 + 5 * level  # Increase snake speed based on level
        self.target_length = 10 + 5 * level  # Increase target length based on level
        self.snake_length = 1
        self.x1 = screen_width / 2
        self.y1 = screen_height / 2
        self.x1_change = 0
        self.y1_change = 0
        self.snake_list = []
        self.food_x = round(random.randrange(0, screen_width - self.snake_block_size) / 20.0) * 20.0
        self.food_y = round(random.randrange(0, screen_height - self.snake_block_size) / 20.0) * 20.0
        self.food_color = random.choice(food_colors)  # Randomly select a color for the food
        self.game_over = False
        self.game_won = False

    def start_game(self):
        pygame.mixer.Sound.play(background_music, loops=-1)

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.Sound.stop(background_music)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -self.snake_block_size
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = self.snake_block_size
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.y1_change = -self.snake_block_size
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y1_change = self.snake_block_size
                        self.x1_change = 0

            self.x1 += self.x1_change
            self.y1 += self.y1_change

            self.check_collision()
            self.update_display()
            self.clock_tick()

    def check_collision(self):
        if self.x1 >= screen_width or self.x1 < 0 or self.y1 >= screen_height or self.y1 < 0:
            pygame.mixer.Sound.stop(background_music)
            pygame.mixer.Sound.play(game_over_sound)
            self.game_over = True

        self.snake_head = []
        self.snake_head.append(self.x1)
        self.snake_head.append(self.y1)
        self.snake_list.append(self.snake_head)

        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

        for segment in self.snake_list[:-1]:
            if segment == self.snake_head:
                pygame.mixer.Sound.stop(background_music)
                pygame.mixer.Sound.play(game_over_sound)
                self.game_over = True

        if self.x1 == self.food_x and self.y1 == self.food_y:
            pygame.mixer.Sound.set_volume(background_music, 0.2)
            pygame.mixer.Sound.play(eat_food_sound)
            self.snake_length += 1
            self.food_x = round(random.randrange(0, screen_width - self.snake_block_size) / 20.0) * 20.0
            self.food_y = round(random.randrange(0, screen_height - self.snake_block_size) / 20.0) * 20.0
            self.food_color = random.choice(food_colors)  # Randomly select a new color for the food
            pygame.mixer.Sound.set_volume(background_music, 0.5)

            if self.snake_length - 1 >= self.target_length:  # Check if target length is reached
                pygame.mixer.Sound.stop(background_music)
                pygame.mixer.Sound.play(game_win_sound)
                self.game_over = True
                self.game_won = True

    def update_display(self):
        game_display.fill(BLACK)
        game_display.blit(background_image, (0, 0))
        pygame.draw.circle(game_display, self.food_color, (int(self.food_x), int(self.food_y)), self.snake_block_size // 2)

        self.draw_snake()

        self.display_score()

        pygame.display.update()

    def draw_snake(self):
        for x, y in self.snake_list:
            pygame.draw.circle(game_display, snake_color, (int(x), int(y)), self.snake_block_size // 2)

    def display_score(self):
        score_text = font_style.render("Score: " + str(self.snake_length - 1), True, snake_color)
        game_display.blit(score_text, [10, 10])

    def clock_tick(self):
        clock.tick(self.snake_speed)

class GameMenu:
    def __init__(self):
        self.menu_font = pygame.font.SysFont(None, 60)
        self.button_font = pygame.font.SysFont(None, 40)

    def show_menu(self):
        start_button_rect = pygame.Rect(screen_width // 2 - 75, 300, 150, 50)
        exit_button_rect = pygame.Rect(screen_width // 2 - 75, 375, 150, 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.Sound.stop(background_music)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button_rect.collidepoint(mouse_pos):
                        self.show_level_selection()
                    elif exit_button_rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound.stop(background_music)
                        pygame.quit()
                        sys.exit()

            game_display.fill(BLACK)
            game_display.blit(background_image, (0, 0))

            title_text = self.menu_font.render("Snake Game", True, snake_color)
            game_display.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 150))

            start_button_text = self.button_font.render("Start", True, BLACK)
            pygame.draw.rect(game_display, snake_color, start_button_rect)
            game_display.blit(start_button_text, (screen_width // 2 - start_button_text.get_width() // 2, 310))

            exit_button_text = self.button_font.render("Exit", True, BLACK)
            pygame.draw.rect(game_display, snake_color, exit_button_rect)
            game_display.blit(exit_button_text, (screen_width // 2 - exit_button_text.get_width() // 2, 385))

            pygame.display.update()
            clock.tick(60)

    def show_level_selection(self):
        level_buttons = []
        level_buttons.append(pygame.Rect(screen_width // 2 - 75, 250, 150, 50))
        level_buttons.append(pygame.Rect(screen_width // 2 - 75, 325, 150, 50))
        level_buttons.append(pygame.Rect(screen_width // 2 - 75, 400, 150, 50))

        level_texts = [self.button_font.render("Easy", True, BLACK),
                       self.button_font.render("Medium", True, BLACK),
                       self.button_font.render("Hard", True, BLACK)]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.Sound.stop(background_music)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(3):
                        if level_buttons[i].collidepoint(mouse_pos):
                            pygame.mixer.Sound.stop(background_music)
                            snake_game = SnakeGame(i)  # Pass the selected level as an argument
                            snake_game.start_game()

            game_display.fill(BLACK)
            game_display.blit(background_image, (0, 0))

            level_text = self.menu_font.render("Select Level:", True, snake_color)
            game_display.blit(level_text, (screen_width // 2 - level_text.get_width() // 2, 150))

            for i in range(3):
                pygame.draw.rect(game_display, snake_color, level_buttons[i])
                game_display.blit(level_texts[i], (screen_width // 2 - level_texts[i].get_width() // 2, 260 + i * 75))

            pygame.display.update()
            clock.tick(60)

menu = GameMenu()
menu.show_menu()
