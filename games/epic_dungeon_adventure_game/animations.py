import pygame
from components.entitty import Animation

def get_animations():

    animations = {
        "evil_wizard":{},
        "Night_Borne":{},
        "Undead_executioner":{},
        "Individual_Sprite":{},
        "Ox":{},
        "Skeleton_Lighter":{},
        "ice boss":{},
        "demon boss":{},
        "main character":{},
        "water heavy":{},
    }




    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/walk/walk'+str(num)+'.png' for num in range(1,8)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['walk'] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/dead/dead'+str(num)+'.png' for num in range(1,5)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['death'] = knight_walk.farme_list
    
    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/attack/attack'+str(num)+'.png' for num in range(1,8)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['attack'] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/hurt/hurt'+str(num)+'.png' for num in range(1,5)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['hurt'] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/idle/tile00'+str(num)+'.png' for num in range(0,8)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['idle'] = knight_walk.farme_list






    path_list = ['games/epic_dungeon_adventure_game/assets/ice_boss/idle/idle_' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice boss']['idle'] =ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/ice_boss/attack/1_atk_' + str(num) + '.png' for num in range(1,15)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice boss']['attack'] =ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/ice_boss/death/death_' + str(num) + '.png' for num in range(1,17)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice boss']['death'] =ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/ice_boss/take_hit/take_hit_' + str(num) + '.png' for num in range(1,8)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice boss']['take hit'] =ice_death.farme_list







    path_list = ['games/epic_dungeon_adventure_game/assets/demon_boss/idle/demon_idle_' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['idle'] = ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/demon_boss/attack/demon_cleave_' + str(num) + '.png' for num in range(1,16)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['attack'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_boss/death/demon_death_' + str(num) + '.png' for num in range(1,23)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['death'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_boss/take_hit/demon_take_hit_' + str(num) + '.png' for num in range(1,6)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['take hit'] = ice_death.farme_list
    
    




    path_list = ['games/epic_dungeon_adventure_game/assets/spells/water/tile' + str(num) + '.png' for num in range(1,21)]
    ice_death = Animation(path_list, 400, 400)
    animations['water heavy']['start'] = ice_death.farme_list

    # Dark_Woods
    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/evil_wizard/Idle/Idle'+str(num)+'.png' for num in range(1,9)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['evil_wizard']['Idle'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/evil_wizard/Death/Death'+str(num)+'.png' for num in range(1,8)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['evil_wizard']['Death'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/evil_wizard/Attack/Attack'+str(num)+'.png' for num in range(1,9)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['evil_wizard']['Attack'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Night_Borne/Idle/Idle'+str(num)+'.png' for num in range(1,10)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Night_Borne']['Idle'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Night_Borne/Attack/Attack'+str(num)+'.png' for num in range(1,13)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Night_Borne']['Attack'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Night_Borne/Death/Death'+str(num)+'.png' for num in range(1,24)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Night_Borne']['Death'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Undead_executioner/Death/Death'+str(num)+'.png' for num in range(1,19)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Undead_executioner']['Death'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Undead_executioner/Attack/Attack'+str(num)+'.png' for num in range(1,7)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Night_Borne']['Attack'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Undead_executioner/Idle/Idle'+str(num)+'.png' for num in range(1,5)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Night_Borne']['Idle'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Individual_Sprite/Idle/Idle'+str(num)+'.png' for num in range(1,9)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Individual_Sprite']['Idle'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Individual_Sprite/Death/Death'+str(num)+'.png' for num in range(1,11)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Individual_Sprite']['Death'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Individual_Sprite/Attack/Attack'+str(num)+'.png' for num in range(1,11)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Individual_Sprite']['Attack'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Ox/Idle/Idle'+str(num)+'.png' for num in range(1,6)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Ox']['Idle'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Ox/Death/Death'+str(num)+'.png' for num in range(1,7)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Ox']['Death'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Ox/Attack/Attack'+str(num)+'.png' for num in range(1,10)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Ox']['Attack'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Skeleton_Lighter/Idle/Idle'+str(num)+'.png' for num in range(1,5)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Skeleton_Lighter']['Idle'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Skeleton_Lighter/Death/Death'+str(num)+'.png' for num in range(1,9)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Skeleton_Lighter']['Death'] = Evil_Idle.farme_list

    # path_list=['./games/epic_dungeon_adventure_game/assets/Dark_Woods/Skeleton_Lighter/Attack/Attack'+str(num)+'.png' for num in range(1,9)]
    # Evil_Idle = Animation(path_list, 200, 200)
    # animations['Skeleton_Lighter']['Attack'] = Evil_Idle.farme_list


    
    return animations
