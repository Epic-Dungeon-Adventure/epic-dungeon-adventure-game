import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, default_animation):
        super().__init__()
        self.default_animation = default_animation
        self.animation_list = default_animation
        self.image = default_animation[0].convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.animation_index = 0
        self.animation_speed = 0.1

    def update(self, x_pos, y_pos):
        self.animation_index += self.animation_speed
        self.image = self.animation_list[int(self.animation_index) % len(self.animation_list)]
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def animate(self, image_list):
        self.image = image_list[self.animation_index]
        self.animation_list = image_list

class Animation():
    def __init__(self, path_list, width, hight):
        self.farme_list = []
        for path in path_list:
            self.farme_list.append(pygame.transform.scale(pygame.image.load(path).convert_alpha(),(width, hight)))