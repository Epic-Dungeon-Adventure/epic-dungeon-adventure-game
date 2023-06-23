import pygame
from random import randint, choice
from components.entitty import Entity
from components.text_box import TextBox
from components.sound import Sound

class Game():
    def __init__(self):
        self.state = "walk"
        

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
            # animate user take damage
            # give user damage
            # check if user is dead
            pass
        if self.state == "walk":
            # animate walk
            # check for collision with event box
            pass

    def draw(self, screen):
        # draw background
        # draw entittys
        pass