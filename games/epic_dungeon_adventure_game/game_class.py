import pygame
from random import randint, choice
from components.entitty import Entity
from components.text_box import TextBox
from components.sound import Sound
from components.terrain import Terrain
from .animations import get_animations

animations = get_animations()


class Game:
    def __init__(self, screen):
        self.state = "walk"
        self.font = pygame.font.SysFont("Inkfree", 20)
        self.screen = screen
        self.user = Entity(animations["main character"]["idle"], 150)
        self.monster = Entity(animations["ice boss"]["idle"], 20)

        self.event_box = Entity([pygame.Surface((50, 50))])

        self.event_box.image.fill("white")
        self.event_box.image.set_alpha(100)
        self.event_box.rect.topleft = (800, 400)

        self.event_queue = ["tell story", "user turn", "walk"]
        self.text_box = None
        self.group = pygame.sprite.Group()
        self.group.add(self.user)
        self.group.add(self.event_box)
        self.user_attacked = False
        self.monster_attacked = False
        self.boss_queue = ["ice boss", "demon boss"]
        self.state_intilized = False

        self.backgrounds = [Terrain("./games/epic_dungeon_adventure_game/assets/background/dark_woods/Layer"+str(num)+".png", 1600, 800, (0,0),num / 3) for num in range(1,8)]



    def get_input(self):
        return pygame.key.get_pressed()

    def update_state(self):

        if self.state == "tell story":
            if self.text_box == None:
                text = "In the depths of a frozen cavern, amidst towering ice walls and glittering icicles, an awe-inspiring ice dragon awaits your arrival. Its colossal body, adorned with shimmering scales of ice, emanates an intense coldness that permeates the chamber. As the dragon fixes its piercing gaze upon you, its voice resonates with ancient wisdom, questioning your purpose in its icy domain. With a mixture of wonder and trepidation, your fate becomes intertwined with this majestic creature, as you stand on the threshold of a chilling and thrilling adventure."
                self.text_box = TextBox(
                    self.screen, (1600, 300), "gray", text, self.font, "black", 0.1
                )
            elif self.get_input()[pygame.K_SPACE]:
                self.text_box = None
                self.state = "user turn"






        if self.state == "user turn" and self.monster.animation_complete and self.user.animation_complete:
            if self.text_box == None:
                text = "1 attack 10 damage \n \n 2 attack 30 damage \n \n 3 heal potion"
                self.text_box = TextBox(self.screen, (1600, 300), "gray", text, self.font, "black", 0.1)

            if self.state_intilized == False:
                self.user.animate(animations["main character"]["idle"])
                self.monster.animate(animations[self.boss_queue[0]]["idle"])
                self.state_intilized = True

            keys = self.get_input()
            if keys[pygame.K_1]:
                self.user_attacked = True
                self.user.animate(animations["main character"]["attack"], True, True)
            
            if self.user.animation_complete and self.user_attacked:
                self.user.animate(self.user.default_animation)
                self.state_intilized = False
                if self.monster.take_damage(10) <= 0:
                    self.monster.animate(animations[self.boss_queue[0]]["death"], True, True)
                    self.state = "walk"
                    self.text_box = None
                    self.boss_queue.pop(0)
                    self.user_attacked = False
                    
                else:
                    self.monster.animate(animations[self.boss_queue[0]]["take hit"], True, True)
                    self.state = "monster turn"






        if self.state == "monster turn" and self.monster.animation_complete and self.user.animation_complete:
            self.user_attacked = False

            if self.monster_attacked == False:
                self.monster.animate(animations[self.boss_queue[0]]["attack"], True, True)
                self.monster_attacked = True
            print(self.monster.animation_complete)
            if self.monster_attacked and self.monster.animation_complete:
                self.user.animate(animations["main character"]["hurt"], True, True)
                self.state = "user turn"
                self.monster_attacked = False

            if self.user.take_damage(50) <= 0:
                self.user.animate(animations["main character"]["death"], True, True)







        if self.state == "walk" and self.monster.animation_complete and self.user.animation_complete:
            if self.state_intilized == False:
                self.monster.kill()
                self.monster = Entity(animations[self.boss_queue[0]]["idle"],20)
                self.state_intilized = True
            keys = self.get_input()
            if keys[pygame.K_d]:
                for background in self.backgrounds:
                    background.update()
                self.user.animate(animations["main character"]["walk"],False,False,True)
                self.event_box.rect.x -= 5
            else:
                self.user.animate(self.user.default_animation)
            if self.user.rect.colliderect(self.event_box.rect):
                self.state = self.event_queue.pop(0)
                self.state_intilized = False
                self.event_box.rect.topleft = (800, 400)
                self.user.animate(self.user.default_animation, True)
                self.group.add(self.monster)

    def draw(self):
        for background in self.backgrounds:
            background.render(self.screen)

        self.monster.update(1000, 100)
        self.user.update("default", 300)
        self.event_box.update("default", "default")
        self.group.draw(self.screen)
        if self.text_box:
            self.text_box.render_words()

        pass
