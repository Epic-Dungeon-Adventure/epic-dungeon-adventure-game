import pygame
class Sound():
    def __init__(self, sound_path, type = "sound", volume = 1):
        pygame.mixer.init()
        self.type = type
        self.path = sound_path
        if type == "sound":
            self.sound = pygame.mixer.Sound(sound_path).set_volume(volume)
            print(type(self.sound))
        
    def play(self):
        if self.type == "sound":
            pygame.mixer.Sound.play(self.sound)
            return
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play(-1)