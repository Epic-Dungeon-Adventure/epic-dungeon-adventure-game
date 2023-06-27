import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

BLACK = (0, 0, 0)


background_image = pygame.image.load('assists/background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

snake_color = (0, 255, 0) 
food_colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0),(97,98,100)]  

game_over_sound = pygame.mixer.Sound('sound/game_over.wav')
eat_food_sound = pygame.mixer.Sound('sound/eat_food.mp3')
background_music = pygame.mixer.Sound('sound/background_music.wav')
game_win_sound = pygame.mixer.Sound('sound/win_game.wav')

# Set the volume for the background music and eating sound
background_music.set_volume(0.5)
eat_food_sound.set_volume(1.0)
game_win_sound.set_volume(0.8)

#  font for the score
font_style = pygame.font.SysFont('font/Pixeltype.ttf', 30)

class SnakeGame:
    def __init__(self, level):
        self.snake_block_size = 20
        self.level = level
        self.snake_speed = 15 + 5 * level  
        self.target_length = 20 + 5 * level  
        self.snake_length = 1
        self.x1 = screen_width / 2
        self.y1 = screen_height / 2
        self.x1_change = 0
        self.y1_change = 0
        self.snake_list = []
        self.food_x = round(random.randrange(0, screen_width - self.snake_block_size) / 20.0) * 20.0
        self.food_y = round(random.randrange(0, screen_height - self.snake_block_size) / 20.0) * 20.0
        self.food_color = random.choice(food_colors) 
        self.game_over = False
        self.game_won = False
        self.button_font = pygame.font.Font('font/Pixeltype.ttf', 40)
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

    # ...

    def display_game_over(self):
            game_over_font = pygame.font.Font('font/Pixeltype.ttf', 80)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            game_display.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, 200))

            # Render start button
            start_button_rect = pygame.Rect(screen_width // 2 - 75, 300, 150, 50)
            pygame.draw.rect(game_display, (0, 255, 0), start_button_rect)
            start_button_text = self.button_font.render("Start", True, BLACK)
            game_display.blit(start_button_text, (screen_width // 2 - start_button_text.get_width() // 2, 310))

            # Render exit button
            exit_button_rect = pygame.Rect(screen_width // 2 - 75, 375, 150, 50)
            pygame.draw.rect(game_display, (255, 0, 0), exit_button_rect)
            exit_button_text = self.button_font.render("Exit", True, BLACK)
            game_display.blit(exit_button_text, (screen_width // 2 - exit_button_text.get_width() // 2, 385))

            pygame.display.update()

            self.handle_game_over_input(start_button_rect, exit_button_rect)

    def handle_game_over_input(self, start_button_rect, exit_button_rect):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.mixer.Sound.stop(background_music)
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if start_button_rect.collidepoint(mouse_pos):
                            self.restart_game()
                        elif exit_button_rect.collidepoint(mouse_pos):
                            pygame.mixer.Sound.stop(background_music)
                            pygame.quit()
                            sys.exit()

                pygame.display.update()
                clock.tick(60)

    def restart_game(self):
        # Reset game variables and start a new game
        self.snake_length = 1
        self.x1 = screen_width / 2
        self.y1 = screen_height / 2
        self.x1_change = 0
        self.y1_change = 0
        self.snake_list = []
        self.food_x = round(random.randrange(0, screen_width - self.snake_block_size) / 20.0) * 20.0
        self.food_y = round(random.randrange(0, screen_height - self.snake_block_size) / 20.0) * 20.0
        self.food_color = random.choice(food_colors)
        self.game_over = False
        self.game_won = False

        self.start_game()
    def check_collision(self):
        if self.x1 >= screen_width or self.x1 < 0 or self.y1 >= screen_height or self.y1 < 0:
            pygame.mixer.Sound.stop(background_music)
            pygame.mixer.Sound.play(game_over_sound)
            self.display_game_over()

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
                self.display_game_over()

        if self.x1 == self.food_x and self.y1 == self.food_y:
            pygame.mixer.Sound.set_volume(background_music, 0.2)
            pygame.mixer.Sound.play(eat_food_sound)
            self.snake_length += 1
            self.food_x = round(random.randrange(0, screen_width - self.snake_block_size) / 20.0) * 20.0
            self.food_y = round(random.randrange(0, screen_height - self.snake_block_size) / 20.0) * 20.0
            self.food_color = random.choice(food_colors)
            pygame.mixer.Sound.set_volume(background_music, 0.5)

            if self.snake_length - 1 >= self.target_length:
                pygame.mixer.Sound.stop(background_music)
                pygame.mixer.Sound.play(game_win_sound)
                self.display_game_over()
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
        self.menu_font = pygame.font.Font('font/Pixeltype.ttf', 60)
        self.button_font = pygame.font.Font('font/Pixeltype.ttf', 40)
        self.background_image = pygame.image.load('assists/start_page.png')
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))

    def show_menu(self):
        start_button_rect = pygame.Rect(screen_width // 2 - 75, 300, 150, 50)
        exit_button_rect = pygame.Rect(screen_width // 2 - 75, 375, 150, 50)

        start_button_alpha = 100  
        exit_button_alpha = 100  

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

            game_display.blit(self.background_image, (0, 0))



            start_button_surf = pygame.Surface((start_button_rect.width, start_button_rect.height), pygame.SRCALPHA)
            start_button_surf.fill((0, 255, 0, start_button_alpha))
            game_display.blit(start_button_surf, start_button_rect)
            start_button_text = self.button_font.render("Start", True, BLACK)
            game_display.blit(start_button_text, (screen_width // 2 - start_button_text.get_width() // 2, 310))

            exit_button_surf = pygame.Surface((exit_button_rect.width, exit_button_rect.height), pygame.SRCALPHA)
            exit_button_surf.fill((255, 0, 0, exit_button_alpha))
            game_display.blit(exit_button_surf, exit_button_rect)
            exit_button_text = self.button_font.render("Exit", True, BLACK)
            game_display.blit(exit_button_text, (screen_width // 2 - exit_button_text.get_width() // 2, 385))

            pygame.display.update()
            clock.tick(60)


 
    def show_level_selection(self):

        easy_button_rect = pygame.Rect(screen_width // 2 - 100, 275, 200, 50)
        medium_button_rect = pygame.Rect(screen_width // 2 - 100, 350, 200, 50)
        hard_button_rect = pygame.Rect(screen_width // 2 - 100, 425, 200, 50)

        easy_button_alpha = 100
        medium_button_alpha = 100
        hard_button_alpha = 100

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.Sound.stop(background_music)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if easy_button_rect.collidepoint(mouse_pos):
                        self.start_game(1)
                    elif medium_button_rect.collidepoint(mouse_pos):
                        self.start_game(2)
                    elif hard_button_rect.collidepoint(mouse_pos):
                        self.start_game(3)

            game_display.blit(self.background_image, (0, 0))

            mouse_pos = pygame.mouse.get_pos()

            if easy_button_rect.collidepoint(mouse_pos):
                easy_button_alpha = 255
            else:
                easy_button_alpha = 100

            if medium_button_rect.collidepoint(mouse_pos):
                medium_button_alpha = 255
            else:
                medium_button_alpha = 100

            if hard_button_rect.collidepoint(mouse_pos):
                hard_button_alpha = 255
            else:
                hard_button_alpha = 100

            easy_button_surf = pygame.Surface((200, 50), pygame.SRCALPHA)
            medium_button_surf = pygame.Surface((200, 50), pygame.SRCALPHA)
            hard_button_surf = pygame.Surface((200, 50), pygame.SRCALPHA)
            pygame.draw.rect(easy_button_surf, (255, 255, 255, easy_button_alpha), easy_button_surf.get_rect(), border_radius=15)
            pygame.draw.rect(medium_button_surf, (255, 255, 255, medium_button_alpha), medium_button_surf.get_rect(), border_radius=15)
            pygame.draw.rect(hard_button_surf, (255, 255, 255, hard_button_alpha), hard_button_surf.get_rect(), border_radius=15)
            game_display.blit(easy_button_surf, easy_button_rect)
            game_display.blit(medium_button_surf, medium_button_rect)
            game_display.blit(hard_button_surf, hard_button_rect)

            easy_button_text = self.button_font.render("Easy", True, (0, 0, 0))
            medium_button_text = self.button_font.render("Medium", True, (0, 0, 0))
            hard_button_text = self.button_font.render("Hard", True, (0, 0, 0))

            game_display.blit(easy_button_text, (screen_width // 2 - 40, 285))
            game_display.blit(medium_button_text, (screen_width // 2 - 40, 360))
            game_display.blit(hard_button_text, (screen_width // 2 - 40, 435))

            pygame.display.update()

    def start_game(self, level):
        game = SnakeGame(level)
        game.start_game()

menu = GameMenu()
menu.show_menu()