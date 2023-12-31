import pygame
class Sound():
    def __init__(self, sound_path, volume = 1):
        pygame.mixer.init()
        self.type = type
        self.path = sound_path
        self.sound = pygame.mixer.Sound(sound_path)
        self.sound.set_volume(volume)
        self.playing = False
        
    def play(self, loop = False):
        if self.playing == False:
            if loop == False:
                self.sound.play()
                return
            self.sound.play(-1)
            self.playing = True

    def pause(self):
        self.sound.stop()