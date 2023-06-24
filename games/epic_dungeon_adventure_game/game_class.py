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
        self.font = pygame.font.SysFont("Inkfree", 40)
        self.screen = screen
        self.user = Entity(animations["main character"]["idle"], 150)
        self.user.animation_complete = True
        self.monster = Entity(animations["ice boss"]["idle"], 20)
        self.monster.animation_complete = True
        self.event_box = Entity([pygame.Surface((50, 50))])
        self.event_box.image.fill("white")
        self.event_box.image.set_alpha(100)
        self.event_box.rect.topleft = (400, 400)
        self.event_queue = ["tell story", "user turn", "walk"]
        self.text_box = None
        self.group = pygame.sprite.Group()
        self.group.add(self.user)
        self.group.add(self.event_box)
        self.user_attacked = False
        self.monster_attacked = False
        self.boss_queue = ["ice boss", "demon boss"]

        self.background = Terrain("./games/epic_dungeon_adventure_game/assets/bg.png", 1600, 800, (0, 0))

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
                text = "1.attack 10 damage"
                self.text_box = TextBox(self.screen, (1600, 300), "gray", text, self.font, "black", 0.1)

            self.user.animate(animations["main character"]["idle"])
            self.monster.animate(animations[self.boss_queue[0]]["idle"])

            keys = self.get_input()
            if keys[pygame.K_1]:
                print("pressed")
                self.user_attacked = True
                self.user.animate(animations["main character"]["attack"], True, True)
            
            if self.user.animation_complete and self.user_attacked:
                print(self.user_attacked)
                self.user.animate(self.user.default_animation)
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

            if self.monster_attacked and self.monster.animation_complete:
                self.user.animate(animations["main character"]["hurt"], True, True)
                self.state = "user turn"
                self.monster_attacked = False

            if self.user.take_damage(0) <= 0:
                self.user.animate(animations["main character"]["death"], True, True)







        if self.state == "walk" and self.monster.animation_complete and self.user.animation_complete:
            self.monster.kill()
            self.monster = Entity(animations[self.boss_queue[0]]["idle"],20)
            self.user.animate(self.user.default_animation)
            keys = self.get_input()
            if keys[pygame.K_w]:
                self.user.rect.y -= 3
            if keys[pygame.K_s]:
                self.user.rect.y += 3
            if keys[pygame.K_a]:
                self.background.update(-5)
                self.user.animate(animations["main character"]["walk"])
            if keys[pygame.K_d]:
                self.background.update(5)
                self.user.animate(animations["main character"]["walk"])
                self.event_box.rect.x -= 5
            if self.user.rect.colliderect(self.event_box.rect):
                self.state = self.event_queue.pop(0)
                self.event_box.rect.topleft = (400, 400)
                self.user.animate(self.user.default_animation, True)
                self.group.add(self.monster)

    def draw(self):
        # draw background
        # draw entittys
        self.background.render(self.screen)

        self.monster.update(1000, 100)
        self.user.update("default", 300)
        self.event_box.update("default", "default")
        self.group.draw(self.screen)
        if self.text_box:
            self.text_box.render_words()

        pass
