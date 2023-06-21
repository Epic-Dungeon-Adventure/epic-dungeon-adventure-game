import pygame
from sys import exit
from random import randint, choice
from components.entitty import Entity
from components.text_box import TextBox
from components.sound import Sound
from .animations import get_animations

pygame.init()
screen = pygame.display.set_mode((1600,800))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

animations = get_animations()
game_state = "walk"

head = Entity(animations['demon']['idle'])
head.animate(animations['demon']['cleave'])
head_group = pygame.sprite.Group()
head_group.add(head)
head.animation_speed *= 1.5


posx = 50
posy = 50



class MainCharacter():
    def __init__(self, default_animation):
        self.entity = Entity(default_animation)

    


sound = Sound("./games/epic_dungeon_adventure/assets/game_sound.wav")

sound.play()


text = "In the depths of a frozen cavern, amidst towering ice walls and glittering icicles, an awe-inspiring ice dragon awaits your arrival. Its colossal body, adorned with shimmering scales of ice, emanates an intense coldness that permeates the chamber. As the dragon fixes its piercing gaze upon you, its voice resonates with ancient wisdom, questioning your purpose in its icy domain. With a mixture of wonder and trepidation, your fate becomes intertwined with this majestic creature, as you stand on the threshold of a chilling and thrilling adventure."
font = pygame.font.SysFont("Inkfree",40)

text_box = TextBox(screen, (1600,300), 'gray', text, font, 'black', 0.1)

def play():
    global posx
    global posy
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        head.update(posx, posy)
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            posy -= 3
        if keys[pygame.K_s]:
            posy += 3
        if keys[pygame.K_a]:
            posx -= 3
        if keys[pygame.K_d]:
            posx += 3
        
        


        screen.fill((0, 0, 0))
        text_box.render_word()
        head_group.draw(screen)
        pygame.display.update()
        clock.tick(60)