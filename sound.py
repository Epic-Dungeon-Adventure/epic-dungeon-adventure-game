import pygame
screen=pygame.display.set_mode((400,800))
class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.game_sound = pygame.mixer.Sound("game_sound.wav")
        self.shoot_sound = pygame.mixer.Sound("shoot_sound.wav")
        self.shoot_sound.set_volume(1.0) 
        self.game_sound.set_volume(0.5)   
    def play_game_sound(self):
        self.game_sound.play(-1)  # Play the game sound in a loop
    def play_shoot_sound(self):
        pygame.mixer.pause()      # Pause the game sound
        self.shoot_sound.play()   # Play the shoot sound
        pygame.mixer.unpause()    # Resume the game sound
game = Sound()
game.play_game_sound()
game.play_shoot_sound()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()