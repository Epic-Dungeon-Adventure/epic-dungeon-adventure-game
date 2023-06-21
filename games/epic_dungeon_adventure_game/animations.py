import pygame
from .entitty import Animation

def get_animations():
    
    animations = {
        "knight":{},
        "demon":{},
        "evil_wizard":{},
        "Night_Borne":{},
        "Undead_executioner":{},
        "Individual_Sprite":{},
        "Ox":{},
        "Skeleton_Lighter":{},
    }

    # path_list=['./games/epic_dungeon/assets/knight/knight walk animation'+str(num)+'.png' for num in range(1,9)]
    # demon_idle = Animation(path_list, 800, 400)
    # animations['demon']['idle'] = demon_idle.farme_list








    # Dark_Woods
    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/evil_wizard/Idle/Idle'+str(num)+'.png' for num in range(1,9)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['evil_wizard']['Idle'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/evil_wizard/Death/Death'+str(num)+'.png' for num in range(1,8)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['evil_wizard']['Death'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/evil_wizard/Attack/Attack'+str(num)+'.png' for num in range(1,9)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['evil_wizard']['Attack'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Night_Borne/Idle/Idle'+str(num)+'.png' for num in range(1,10)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Night_Borne']['Idle'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Night_Borne/Attack/Attack'+str(num)+'.png' for num in range(1,13)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Night_Borne']['Attack'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Night_Borne/Death/Death'+str(num)+'.png' for num in range(1,24)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Night_Borne']['Death'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Undead_executioner/Death/Death'+str(num)+'.png' for num in range(1,19)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Undead_executioner']['Death'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Undead_executioner/Attack/Attack'+str(num)+'.png' for num in range(1,7)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Night_Borne']['Attack'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Undead_executioner/Idle/Idle'+str(num)+'.png' for num in range(1,5)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Night_Borne']['Idle'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Individual_Sprite/Idle/Idle'+str(num)+'.png' for num in range(1,9)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Individual_Sprite']['Idle'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Individual_Sprite/Death/Death'+str(num)+'.png' for num in range(1,11)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Individual_Sprite']['Death'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Individual_Sprite/Attack/Attack'+str(num)+'.png' for num in range(1,11)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Individual_Sprite']['Attack'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Ox/Idle/Idle'+str(num)+'.png' for num in range(1,6)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Ox']['Idle'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Ox/Death/Death'+str(num)+'.png' for num in range(1,7)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Ox']['Death'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Ox/Attack/Attack'+str(num)+'.png' for num in range(1,10)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Ox']['Attack'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Skeleton_Lighter/Idle/Idle'+str(num)+'.png' for num in range(1,5)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Skeleton_Lighter']['Idle'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Skeleton_Lighter/Death/Death'+str(num)+'.png' for num in range(1,9)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Skeleton_Lighter']['Death'] = Evil_Idle.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Skeleton_Lighter/Attack/Attack'+str(num)+'.png' for num in range(1,9)]
    Evil_Idle = Animation(path_list, 200, 200)
    animations['Skeleton_Lighter']['Attack'] = Evil_Idle.farme_list

    # path_list = [
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_1.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_2.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_3.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_4.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_5.png',
    # 'games/epic_dungeon/assets/demon_idle/demon_idle_6.png'
    # ]
    

    return animations