import pygame

pygame.display.init()
pygame.display.set_mode((1600, 800))


class Entity(pygame.sprite.Sprite):
    def __init__(self, default_animation, health=0, size=None, default_speed = 0.1):
        super().__init__()
        self.health = health
        self.default_animation = default_animation
        self.current_animation = default_animation
        self.image = default_animation[0]
        if size != None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.animation_index = 0 
        self.animation_speed = default_speed
        self.default_speed = default_speed
        self.animation_complete = True
        self.loop = False
        self.kill_after_animation = False

    def update(self, x_pos="default", y_pos="default"):
        if x_pos == "default":
            x_pos = self.rect.x
        if y_pos == "default":
            y_pos = self.rect.y
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.current_animation):
            self.animation_complete = True
            if self.loop == False:
                self.animation_index = 0
                self.current_animation = self.default_animation
                self.animation_speed = self.default_speed
            if self.kill_after_animation == True:
                self.kill()
        self.image = self.current_animation[
            int(self.animation_index) % len(self.current_animation)
        ]
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def animate(self, image_list, reset_index=False, reset_completion=False, loop=False, kill = False, speed = 0.1):
        self.current_animation = image_list
        self.loop = loop
        self.kill_after_animation = kill
        self.animation_speed = speed
        if reset_completion == True:
            self.animation_complete = False
        if reset_index == True:
            self.animation_index = 0

    def take_damage(self, damage):
        self.health -= damage
        return self.health


class Animation:
    def __init__(self, path_list, width, hight):
        self.farme_list = []
        for path in path_list:
            self.farme_list.append(pygame.transform.scale(pygame.image.load(path).convert_alpha(), (width, hight)))
