import pygame
from random import randint, choice
from components.entitty import Entity
from components.text_box import TextBox
from components.sound import Sound
from components.terrain import Terrain
from .animations import get_animations
from components.bars import Bar

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
   pygame.K_1:('water heavy'),
   pygame.K_2:('water light'),
   pygame.K_3:('fire heavy'),
   pygame.K_4:('fire light'),
   pygame.K_5:('electric heavy'),
   pygame.K_6:('electric light'),
}

animation_settings = {
    ("water heavy"):{
        "repeat speed":0.2,
        "element":"water",
        "trigger_percentage":90,
    },

    ("water light"):{
        "start speed":0.1,
        "repeat speed":0.5,
        "end speed":0.3,
        "element":"water",
        "trigger_percentage":100,
    },

    ("fire heavy"):{
        "repeat speed":0.12,
        "element":"fire",
        "trigger_percentage":90,
    },

    ("fire light"):{
        "start speed":0.2,
        "repeat speed":0.5,
        "end speed":0.4,
        "element":"fire",
        "trigger_percentage":100,
    },

    ("electric heavy"):{
        "repeat speed":0.09,
        "element":"electric",
        "trigger_percentage":90,
    },

    ("electric light"):{
        "start speed":0.1,
        "repeat speed":0.2,
        "end speed":0.15,
        "element":"electric",
        "trigger_percentage":100,
    },
    
}

class Game:
    def __init__(self, screen):
        self.level = "dark woods"
        self.state = "walk"
        self.font = pygame.font.SysFont("Inkfree", 30)
        self.screen = screen
        self.user = Entity(animations["main character"]["idle"], 250)
        self.monster = Entity(animations["ice boss"]["idle"], 40)
        self.spell = Entity(animations['water heavy']['repeat'])

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
        self.spell_movement = 0
        self.spell_started = False

        self.backgrounds = [Terrain(levels[self.level]["background"][0]+str(num)+".png", 1600, 800, (0,0),num / 3) for num in range(1,levels[self.level]["background"][1])]
        self.user_health_bar = Bar(10, 10, 200, 20, 250, (255, 0, 0))
        self.user_stamina_bar = Bar(10, 40, 200, 20, 200, (0, 255, 255))
        self.monster_health_bar =  Bar(1390, 10, 200, 20, 40, (0, 0, 255))
       
        
        # self.user_health_bar.rect.midbottom = self.user.rect.midtop
        
    def get_input(self):
        return pygame.key.get_pressed()

    def create_text_box(self, text):
        ground_margin = 10
        self.text_box = TextBox(self.screen, (1600, 300), "gray", text, self.font, "black", 0.1)
        self.ground_hight = self.text_box.box_size[1] + ground_margin

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

    @staticmethod
    def animation_percentage(entity):
        if entity.animation_complete:
            return 100
        return entity.animation_index / len(entity.current_animation) * 100

    def get_user_attack(self):
        keys = self.get_input()
        for key in spells.keys():
            if spells[key] and keys[key]:
                self.current_spell = spells[key]
                kill_spell = False
                if 'heavy' in self.current_spell:
                    kill_spell = True
                    self.user.animate(animations["main character"]["heavy"][animation_settings[self.current_spell]["element"]], True, True)
                else: 
                    self.user.animate(animations["main character"]["light"][animation_settings[self.current_spell]["element"]], True, True)
                self.user_attacked = True
                self.spell = Entity(animations[self.current_spell]['repeat'], default_speed = animation_settings[self.current_spell]["repeat speed"])
                self.spell.kill_after_animation = kill_spell              


    def user_turn(self):
        if self.text_box == None:
            text = "1 attack 10 damage \n \n 2 attack 30 damage \n \n 3 heal potion"
            self.create_text_box(text)

        self.get_user_attack()
        if self.current_spell != False:
            if self.animation_percentage(self.user) >= animation_settings[self.current_spell]["trigger_percentage"] and self.user_attacked:
                self.group.add(self.spell)
                
                if not 'heavy' in self.current_spell and not self.spell_started:
                    self.spell.animate(animations[self.current_spell]['start'],True,True,speed=animation_settings[self.current_spell]["start speed"])
                    self.spell_started = True
                    self.spell.rect.midleft = self.user.rect.midright
                if self.spell.animation_complete and self.spell_started:
                    self.spell_movement = 5

                if 'heavy' in self.current_spell:
                    self.spell.rect.bottomleft = self.monster.rect.bottomleft
                    self.spell.animation_index = 0

                if self.spell.rect.colliderect(self.monster.rect):
                    self.monster_health_bar.update_health(10) # Husam  
                    self.user_stamina_bar.update_stamina(30)
                    if not 'heavy' in self.current_spell:
                        self.spell.animate(animations[self.current_spell]['end'], True, True, kill=True,speed=animation_settings[self.current_spell]["end speed"])
                        self.spell_movement = 0
                    if self.monster.take_damage(10) <= 0:
                        self.monster.animate(animations[self.boss_queue[0]]["death"], True, True,False,True)
                        self.state = "walk"
                        self.boss_queue.pop(0)
                        self.user_attacked = False
                        self.monster_health_bar = Bar(1390, 10, 200, 20, 100, (0, 0, 255))  # Husam Create a new monster health bar

                        
                    
                    else:
                        self.monster.animate(animations[self.boss_queue[0]]["take hit"], True, True)
                        self.state = "monster turn"
                    self.current_spell = False
                    self.spell_movement = 0
                    self.spell_started = False
                    
                    


    def monster_turn(self):
        self.user_attacked = False
        if self.monster_attacked == False:
            self.monster.animate(animations[self.boss_queue[0]]["attack"], True, True)
            self.monster_attacked = True
            

        if self.monster_attacked and self.monster.animation_complete:
            self.user.animate(animations["main character"]["hurt"], True, True)
            self.state = "user turn"
            self.monster_attacked = False
            self.user_health_bar.update_health(50)  # Husam Decrease user's health
        

        if self.user.take_damage(50) <= 0:
            self.user.animate(animations["main character"]["death"], True, True)
        self.current_spell = False
        self.spell_movement = 0
        self.spell_started = False  
        

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

        if self.state == "user turn" and self.monster.animation_complete:
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
        self.spell.rect.x += self.spell_movement
        self.spell.update()
        self.spell.image.set_alpha(200)
        self.user.update()
        self.user.rect.bottom =  800 - self.ground_hight
        self.event_box.update()
        self.event_box.rect.bottom = 800 - self.ground_hight
        self.group.draw(self.screen)
        if self.text_box:
            self.text_box.render_words()
        

        
        if self.state != "walk":  # Only draw the bars if not in the "walk" state
            self.user_stamina_bar.draw(self.screen)   
            self.user_health_bar.draw(self.screen)
            self.monster_health_bar.draw(self.screen)
        

# cut sprites perfcetly
# use rect.center for consistant position