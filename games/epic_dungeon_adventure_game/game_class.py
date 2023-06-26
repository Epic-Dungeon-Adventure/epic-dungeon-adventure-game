import pygame
from random import randint, choice
from components.entitty import Entity
from components.text_box import TextBox
from components.sound import Sound
from components.terrain import Terrain
from .animations import get_animations

animations = get_animations()

levels = {
    "dark woods":{
        "background":("./games/epic_dungeon_adventure_game/assets/background/dark_woods/Layer", 8),
        "monsters":["ice boss", "demon boss"],
    },
    "rock cave":{
        "background":("./games/epic_dungeon_adventure_game/assets/background/rock_cave/Layer", 5),
        "monsters":["ice boss", "demon boss"],
    }
}

spells = {
   pygame.K_1:('water heavy','start'),
   pygame.K_2:('water light','start'),
}

spell_flow = {
    ('water heavy','start'):('water heavy','start'),
    ('water light','start'):('water light','start'),
}

class Game:
    def __init__(self, screen):
        self.level = "rock cave"
        self.state = "walk"
        self.font = pygame.font.SysFont("Inkfree", 30)
        self.screen = screen
        self.user = Entity(animations["main character"]["idle"], 250)
        self.monster = Entity(animations["ice boss"]["idle"], 20)
        self.spell = Entity(animations['water heavy']['start'])

        self.event_box = Entity([pygame.Surface((50, 50))])
        self.event_box.image.fill("white")
        self.event_box.image.set_alpha(100)
        self.event_box.rect.topleft = (800, 400)

        self.event_queue = ["tell story", "user turn", "walk"]
        self.boss_queue = ["ice boss", "demon boss"]
        self.story_queue = ["In the depths of a frozen cavern, amidst towering ice walls and glittering icicles, an awe-inspiring ice dragon awaits your arrival. Its colossal body, adorned with shimmering scales of ice, emanates an intense coldness that permeates the chamber. As the dragon fixes its piercing gaze upon you, its voice resonates with ancient wisdom, questioning your purpose in its icy domain. With a mixture of wonder and trepidation, your fate becomes intertwined with this majestic creature, as you stand on the threshold of a chilling and thrilling adventure."]
        self.text_box = None
        self.group = pygame.sprite.Group()
        self.group.add(self.user)
        self.group.add(self.event_box)
        self.user_attacked = False
        self.monster_attacked = False
        self.ground_hight = 10
        self.current_spell = False
        self.spell_movement = 1

        self.backgrounds = [Terrain(levels[self.level]["background"][0]+str(num)+".png", 1600, 800, (0,0),num / 3) for num in range(1,levels[self.level]["background"][1])]

    def get_input(self):
        return pygame.key.get_pressed()

    def create_text_box(self, text):
        ground_margin = 10
        self.text_box = TextBox(self.screen, (1600, 300), "gray", text, self.font, "black", 0.1)
        self.ground_hight = self.text_box.box_size[1] + ground_margin

    def get_user_attack(self):
        keys = self.get_input()
        for key in spells.keys():
            if spells[key] and keys[key]:
                self.user_attacked = True
                self.user.animate(animations["main character"]["attack"], True, True)
                self.spell = Entity(animations[spells[key][0]][spells[key][1]])
                self.spell.rect.bottomleft = self.user.rect.bottomleft
                self.current_spell = spells[key]

    def event_box_collision(self):
        self.state = "tell story"
        self.state_intilized = False
        self.event_box.rect.topleft = (800, 400)
        self.user.animate(self.user.default_animation, True)
        self.monster = Entity(animations[self.boss_queue[0]]["idle"],20)
        self.group.add(self.monster)
    

    def tell_story(self):
        if self.text_box == None:
            text = self.story_queue[0]
            self.create_text_box(text)
        
        keys = self.get_input()
        if keys[pygame.K_SPACE]:
            self.text_box = None
            self.state = "user turn"

    def user_turn(self):
        if self.text_box == None:
            text = "1 attack 10 damage \n \n 2 attack 30 damage \n \n 3 heal potion"
            self.create_text_box(text)

        self.get_user_attack()

        if self.user.animation_complete and self.user_attacked:
            self.group.add(self.spell)

            if self.spell.rect.colliderect(self.monster.rect):
                self.spell.animate(animations[spell_flow[self.current_spell][0]][spell_flow[self.current_spell][1]],True,True,False,True)
                if self.monster.take_damage(10) <= 0:
                    self.monster.animate(animations[self.boss_queue[0]]["death"], True, True,False,True)
                    self.state = "walk"
                    self.boss_queue.pop(0)
                    self.user_attacked = False

                else:
                    self.monster.animate(animations[self.boss_queue[0]]["take hit"], True, True)
                    self.state = "monster turn"

    def monster_turn(self):
        self.user_attacked = False
        if self.monster_attacked == False:
            self.monster.animate(animations[self.boss_queue[0]]["attack"], True, True)
            self.monster_attacked = True

        if self.monster_attacked and self.monster.animation_complete:
            self.user.animate(animations["main character"]["hurt"], True, True)
            self.state = "user turn"
            self.monster_attacked = False

        if self.user.take_damage(50) <= 0:
            self.user.animate(animations["main character"]["death"], True, True)  

    def walk(self):
    
        self.ground_hight = 10
        self.text_box = None  
        keys = self.get_input()

        if keys[pygame.K_d]:
            for background in self.backgrounds:
                background.update()
            self.user.animate(animations["main character"]["walk"],False,False,True)
            self.event_box.rect.x -= 5
        else:
            self.user.animate(self.user.default_animation)

        if self.user.rect.colliderect(self.event_box.rect):
            self.event_box_collision()


    def update_state(self):
        if self.state == "tell story":
            self.tell_story()

        if self.state == "user turn" and self.monster.animation_complete and self.user.animation_complete:
            self.user_turn()

        if self.state == "monster turn" and self.monster.animation_complete and self.user.animation_complete and self.spell.animation_complete:
            self.monster_turn()

        if self.state == "walk" and self.monster.animation_complete and self.user.animation_complete:
            self.walk()

    def draw(self):
        for background in self.backgrounds:
            background.rect.bottom = 800 - self.ground_hight + 10
            background.render(self.screen)
        
        self.monster.update()
        self.monster.rect.bottomleft = (1000, 800 - self.ground_hight)
        # self.spell.rect.bottomleft = self.user.rect.bottomleft
        self.spell.rect.x += self.spell_movement
        self.spell.update()
        self.spell.image.set_alpha(150)
        self.user.update()
        self.user.rect.bottom =  800 - self.ground_hight
        self.event_box.update()
        self.event_box.rect.bottom = 800 - self.ground_hight
        self.group.draw(self.screen)
        if self.text_box:
            self.text_box.render_words()

