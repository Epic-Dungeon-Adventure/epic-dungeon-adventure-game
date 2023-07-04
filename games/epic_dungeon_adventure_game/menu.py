import pygame
import sys
import os
from games.epic_dungeon_adventure_game.game import play

class Menu:
    def __init__(self, window_width, window_height, caption, background_image_path):
        pygame.init()
        self.window_width = window_width
        self.window_height = window_height
        
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(caption)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "assets", "menu")

        self.background_image = pygame.image.load(os.path.join(assets_dir, background_image_path)).convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (window_width, window_height))

        self.button_group = pygame.sprite.Group()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.button_group.update(event)

    def update_screen(self):
        self.window.blit(self.background_image, (0, 0))
        self.button_group.draw(self.window)
        pygame.display.flip()

    def run_menu(self):
        while True:
            self.handle_events()
            self.update_screen()


class MainMenu(Menu):
    def __init__(self, window_width, window_height):
        super().__init__(window_width, window_height, "menu", "background.png")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "assets", "menu")

        button_x = window_width // 2
        play_button_y = window_height // 2 - 120
        about_button_y = window_height // 2
        quit_button_y = window_height // 2 + 120

        class MenuButton(pygame.sprite.DirtySprite):
            def __init__(self, x, y, on_image_path, off_image_path, func):
                super().__init__()
                self.on_image = pygame.image.load(os.path.join(assets_dir, on_image_path)).convert_alpha()
                self.off_image = pygame.image.load(os.path.join(assets_dir, off_image_path)).convert_alpha()
                self.image = self.on_image
                self.rect = self.image.get_rect(center=(x, y))
                self.state = "on"
                self.func = func

            def handle_event(self, event):
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(mouse_pos):
                        self.state = "off"
                    else:
                        self.state = "on"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.rect.collidepoint(mouse_pos):
                            self.func()

            def update(self, event=None):
                self.dirty = True
                if event:
                    self.handle_event(event)
                if self.state == "on":
                    self.image = self.on_image
                else:
                    self.image = self.off_image

        play_button = MenuButton(button_x, play_button_y, "on/play_on.png", "off/play_off.png", play)
        about_button = MenuButton(button_x, about_button_y, "on/about_on.png", "off/about_off.png", self.about_screen)
        quit_button = MenuButton(button_x, quit_button_y, "on/quit_on.png", "off/quit_off.png", sys.exit)

        self.button_group.add(play_button, about_button, quit_button)

    @staticmethod
    def about_screen():
        about_menu = Menu(1600, 800, "About", "background.png")

        instructions_text = [
            "Welcome to the Epic Dungeon Adventure Game!",
            "",
            "Instructions:",
            "- Use the arrow keys to move the character.",
            "- Collect treasures and defeat enemies to earn points.",
            "- Be careful of traps and obstacles.",
            "- Reach the exit to advance to the next level.",
            "- Have fun and enjoy the game!",
            "",
            "Press any key to return to the main menu."
        ]

        font = pygame.font.Font(None, 30)

        text_surfaces = [font.render(text, True, (255, 255, 255)) for text in instructions_text]

        total_height = sum(surface.get_height() for surface in text_surfaces)
        y = (about_menu.window_height - total_height) // 2

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    return

            about_menu.window.blit(about_menu.background_image, (0, 0))

            current_y = y

            for surface in text_surfaces:
                x = (about_menu.window_width - surface.get_width()) // 2
                about_menu.window.blit(surface, (x, current_y))
                current_y += surface.get_height() + 10

            pygame.display.flip()


class PauseMenu(Menu):
    def __init__(self, window_width, window_height, resume_game_callback):
        super().__init__(window_width, window_height, "Pause", "pause_menu.png")


        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "assets", "menu")

        button_x = window_width // 2
        continue_button_y = window_height // 2 - 120
        quit_button_y = window_height // 2

        class MenuButton(pygame.sprite.DirtySprite):
            def __init__(self, x, y, on_image_path, off_image_path, func):
                super().__init__()
                self.on_image = pygame.image.load(os.path.join(assets_dir, on_image_path)).convert_alpha()
                self.off_image = pygame.image.load(os.path.join(assets_dir, off_image_path)).convert_alpha()
                self.image = self.on_image
                self.rect = self.image.get_rect(center=(x, y))
                self.state = "on"
                self.func = func

            def handle_event(self, event):
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(mouse_pos):
                        self.state = "off"
                    else:
                        self.state = "on"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.rect.collidepoint(mouse_pos):
                            self.func()

            def update(self, event=None):
                self.dirty = True
                if event:
                    self.handle_event(event)
                if self.state == "on":
                    self.image = self.on_image
                else:
                    self.image = self.off_image

            def continue_game(self):
                pygame.quit()  # Close the pause menu
                self.resume_game_callback()  # Call the provided callback to resume the game
                
        continue_button = MenuButton(button_x, continue_button_y, "on/continue_on.png", "off/continue_off.png", self.continue_game)
        quit_button = MenuButton(button_x, quit_button_y, "on/quit_on.png", "off/quit_off.png", sys.exit)

        self.button_group.add(continue_button, quit_button)

    def continue_game(self):
        pygame.quit()  # Close the pause menu
        # Add code here to resume the game


class GameOverMenu(Menu):
    def __init__(self, window_width, window_height):
        super().__init__(window_width, window_height, "menu", "game_over.png")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "assets", "menu")

        button_x = window_width // 2
        play_again_button_y = window_height // 2 - 120
        quit_button_y = window_height // 2 + 120

        class MenuButton(pygame.sprite.DirtySprite):
            def __init__(self, x, y, on_image_path, off_image_path, func):
                super().__init__()
                self.on_image = pygame.image.load(os.path.join(assets_dir, on_image_path)).convert_alpha()
                self.off_image = pygame.image.load(os.path.join(assets_dir, off_image_path)).convert_alpha()
                self.image = self.on_image
                self.rect = self.image.get_rect(center=(x, y))
                self.state = "on"
                self.func = func

            def handle_event(self, event):
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(mouse_pos):
                        self.state = "off"
                    else:
                        self.state = "on"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.rect.collidepoint(mouse_pos):
                            self.func()

            def update(self, event=None):
                self.dirty = True
                if event:
                    self.handle_event(event)
                if self.state == "on":
                    self.image = self.on_image
                else:
                    self.image = self.off_image

        play_again_button = MenuButton(button_x, play_again_button_y, "on/again_on.png", "off/again_off.png", self.play_again)
        quit_button = MenuButton(button_x, quit_button_y, "on/quit_on.png", "off/quit_off.png", sys.exit)

        self.button_group.add(play_again_button, quit_button)

    def play_again(self):
        pygame.quit() 
        play() 

def game_over():
    pygame.init()  
    window_width = 1600
    window_height = 800
    game_over_menu = GameOverMenu(window_width, window_height)
    game_over_menu.run_menu()

def main():
    window_width = 1600
    window_height = 800
    main_menu = MainMenu(window_width, window_height)
    main_menu.run_menu()



