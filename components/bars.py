import pygame

class Bar:
    def __init__(self, x, y, width, height, max,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max = max
        self.current_value = max
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        

    def draw(self, screen):
        bar_ratio = self.current_value / self.max
        health_width = int(self.width * bar_ratio)
        pygame.draw.rect(screen, self.color, self.rect, 2, border_radius=20)
        pygame.draw.rect(screen, self.color, (self.x, self.y, health_width, self.height))


    def update_health(self, damage):
        self.current_value -= damage
        
    def update_stamina(self, stamina):
        self.current_value -= stamina