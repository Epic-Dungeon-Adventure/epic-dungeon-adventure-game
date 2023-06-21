import pygame
class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.game_sound = pygame.mixer.Sound("game_sound.wav")
        self.shoot_sound = pygame.mixer.Sound("shoot.wav")
        self.shoot_sound.set_volume(1.0)  # Adjust the volume of the shooting sound
        self.game_sound.set_volume(0.5)   # Adjust the volume of the game sound
    def play_game_sound(self):
        self.game_sound.play(-1)  # Play the game sound in a loop
    def play_shoot_sound(self):
        pygame.mixer.pause()      # Pause the game sound
        self.shoot_sound.play()   # Play the shoot sound
        pygame.mixer.unpause()    # Resume the game sound
# Create an instance of the Game class
game = Sound()
# Play the game sound
game.play_game_sound()
# When there is a shooting event, play the shoot sound
game.play_shoot_sound()