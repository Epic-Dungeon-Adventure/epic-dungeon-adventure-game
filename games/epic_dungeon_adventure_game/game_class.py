import pygame
from random import randint, choice
from components.entitty import Entity
from components.text_box import TextBox
from components.sound import Sound
from components.terrain import Terrain
from .animations import get_animations

animations = get_animations()

class Game():
    def __init__(self, screen):
        self.state = "walk"
        self.font = pygame.font.SysFont("Inkfree",40)
        self.screen = screen
        self.user = Entity(animations['Dragon monster']['idle'])
        self.background = Terrain("./games/epic_dungeon_adventure_game/assets/bg.png", 1600,800,(0,0))

    def get_input(self):
        return pygame.key.get_pressed()

    def update_state(self):
        if self.state == "tell story":
            # show text box + dungeon master
            # check is text is done
            pass
        if self.state == "combat user turn":
            # get user choice using text box
            # animate user attack
            # animate monster take dmage
            # give monster damage
            # check if monster is dead
            pass
        if self.state == "combat monster turn":
            # animate monster attack
            self.monster.animate(self.animations["ice_witch"]['attack'])
            # animate user take damage
            self.user.animate(self.animations["icecream"]['idle'])
            # give user damage
            self.user.take_damage(10)
            # check if user is dead
            if self.user.health <= 0:
                self.user.animate(self.animations["icecream"]['death'])
                pygame.quit()
        if self.state == "walk":
            # animate walk
            # check for collision with event box
            self.user.animate(self.user.default_animation)
            keys = self.get_input()
            if keys[pygame.K_w]:
                self.user.rect.y -= 3
            if keys[pygame.K_s]:
                self.user.rect.y += 3
            if keys[pygame.K_a]:
                self.background.update(-5)
                self.user.animate(animations['knight']['walk'])
            if keys[pygame.K_d]:
                self.background.update(5)
                self.user.animate(animations['knight']['walk'])
            

    def draw(self, screen):
        # draw background
        # draw entittys
        
        head_group = pygame.sprite.Group()
        head_group.add(self.user)


        self.user.update(self.user.rect.x,self.user.rect.y,True)
        self.background.render(screen)
        head_group.draw(screen)
        pass