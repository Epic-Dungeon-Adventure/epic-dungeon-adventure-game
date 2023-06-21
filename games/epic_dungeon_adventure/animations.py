import pygame
from components.entitty import Animation

def get_animations():
    
    animations = {
        "knight":{},
        "demon":{},
    }

    path_list=['./games/epic_dungeon_adventure/assets/knight/knight walk animation'+str(num)+'.png' for num in range(1,9)]

    kinght_walk = Animation(path_list, 200, 200)
    animations['knight']['walk'] = kinght_walk.farme_list


    path_list=['./games/epic_dungeon_adventure/assets/demon_idle/demon_idle_'+str(num)+'.png' for num in range(1,7)]
    demon_idle = Animation(path_list, 800, 400)
    animations['demon']['idle'] = demon_idle.farme_list


   
    path_list=['./games/epic_dungeon_adventure/assets/demon_attack/demon_cleave_'+str(num)+'.png' for num in range(1,16)]
    demon_attack = Animation(path_list, 800, 400)
    animations['demon']['cleave'] = demon_attack.farme_list

    return animations