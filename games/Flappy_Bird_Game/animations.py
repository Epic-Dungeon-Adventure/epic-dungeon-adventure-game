import pygame
from components.entitty import Animation

def get_animations():

    animations = {
        
        "bird":{},
        "parrot":{},
        "redbird":{},

    }

    path_list=['games/Flappy_Bird_Game/bird/redbird_'+str(num)+'.png' for num in range(1,4)]
    knight_walk = Animation(path_list)
    animations['bird'] = knight_walk.farme_list

    path_list=['games/Flappy_Bird_Game/assets/parrot/Parrot_'+str(num)+'.png' for num in range(1,21)]
    knight_walk = Animation(path_list, 30, 40)
    animations['parrot'] = knight_walk.farme_list

    path_list=['games/Flappy_Bird_Game/assets/redbird/red_'+str(num)+'.png' for num in range(1,8)]
    knight_walk = Animation(path_list, 30, 40)
    animations['redbird'] = knight_walk.farme_list





    return animations
