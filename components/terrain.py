import pygame
import math

class Terrain(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height,postion):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = postion[0]
        self.rect.y = postion[1]
        self.scroll = 0
        

    def update(self, scroll_speed):
        self.scroll-= scroll_speed

        if abs(self.scroll) > self.image.get_width():
            self.scroll = 0

    def render(self, screen):
        tiles = math.ceil(screen.get_width()  / self.image.get_width()) + 1
        for i in range(-1, tiles):
            screen.blit(self.image, (i * self.image.get_width() + self.scroll, self.rect.y))
        