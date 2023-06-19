import pygame
from .entitty import Animation

def get_animations():
    
    animations = {
        "knight":{},
        "demon":{},
    }

    # path_list=['./games/epic_dungeon/assets/knight/knight walk animation'+str(num)+'.png' for num in range(1,9)]

    # kinght_walk = Animation(path_list, 200, 200)
    # animations['knight']['walk'] = kinght_walk.farme_list


    # path_list = [
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_1.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_2.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_3.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_4.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_5.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_6.png'
    # ]
    # demon_idle = Animation(path_list, 800, 400)
    # animations['demon']['idle'] = demon_idle.farme_list
    return animations