import pygame
from components.entitty import Animation

def get_animations():

    animations = {
        "bringer of death":{},
        "ice boss":{},
        "demon boss":{},
        "main character":{
            "heavy":{},
            "light":{},
                          },

        "water heavy":{},
        "water light":{},
        "electric heavy":{},
        "electric light":{},
        "fire heavy":{},
        "fire light":{},
        "shadow heavy":{},
    }




    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/walk/walk'+str(num)+'.png' for num in range(1,8)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['walk'] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/dead/dead'+str(num)+'.png' for num in range(1,5)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['death'] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/hurt/hurt'+str(num)+'.png' for num in range(1,5)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['take hit'] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/idle/tile00'+str(num)+'.png' for num in range(0,8)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']['idle'] = knight_walk.farme_list




    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/heavy_water/tile'+str(num).zfill(3)+'.png' for num in range(0,7)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']["heavy"]["water"] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/light_water/tile'+str(num).zfill(3)+'.png' for num in range(0,16)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']["light"]["water"] = knight_walk.farme_list



    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/heavy_fire/tile'+str(num).zfill(3)+'.png' for num in range(0,7)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']["heavy"]["fire"] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/light_fire/tile'+str(num).zfill(3)+'.png' for num in range(0,16)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']["light"]["fire"] = knight_walk.farme_list



    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/heavy_electric/tile'+str(num).zfill(3)+'.png' for num in range(0,7)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']["heavy"]["electric"] = knight_walk.farme_list

    path_list=['./games/epic_dungeon_adventure_game/assets/wizzard/light_electric/tile'+str(num).zfill(3)+'.png' for num in range(0,16)]
    knight_walk = Animation(path_list, 300, 200)
    animations['main character']["light"]["electric"] = knight_walk.farme_list

#                                               Monsters

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/idle/idle_' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 300, 300)
    animations['ice boss']['idle'] =ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/attack/1_atk_' + str(num) + '.png' for num in range(1,15)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice boss']['attack'] =ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/death/death_' + str(num) + '.png' for num in range(1,17)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice boss']['death'] =ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/take_hit/take_hit_' + str(num) + '.png' for num in range(1,8)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice boss']['take hit'] =ice_death.farme_list




    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/demon_boss/idle/demon_idle_' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['idle'] = ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/demon_boss/attack/demon_cleave_' + str(num) + '.png' for num in range(1,16)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['attack'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/demon_boss/death/demon_death_' + str(num) + '.png' for num in range(1,23)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['death'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/demon_boss/take_hit/demon_take_hit_' + str(num) + '.png' for num in range(1,5)]
    ice_death = Animation(path_list, 400, 400)
    animations['demon boss']['take hit'] = ice_death.farme_list



    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/bringer_of_death/idle/Bringer-of-Death_Idle_' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 400, 400)
    animations['bringer of death']['idle'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/bringer_of_death/attack/Bringer-of-Death_Cast_' + str(num) + '.png' for num in range(1,10)]
    ice_death = Animation(path_list, 400, 400)
    animations['bringer of death']['attack'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/bringer_of_death/death/Bringer-of-Death_Death_' + str(num) + '.png' for num in range(1,11)]
    ice_death = Animation(path_list, 400, 400)
    animations['bringer of death']['death'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/bringer_of_death/take_hit/Bringer-of-Death_Hurt_' + str(num) + '.png' for num in range(1,4)]
    ice_death = Animation(path_list, 400, 400)
    animations['bringer of death']['take hit'] = ice_death.farme_list




#                                                   Monsters


    path_list = ['games/epic_dungeon_adventure_game/assets/spells/heavy_water/tile' + str(num) + '.png' for num in range(1,21)]
    ice_death = Animation(path_list, 400, 400)
    animations['water heavy']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_water/start/tile' + str(num) + '.png' for num in range(0,4)]

    ice_death = Animation(path_list, 200, 200)
    animations['water light']['start'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_water/repeat/tile' + str(num) + '.png' for num in range(4,21)]
    ice_death = Animation(path_list, 200, 200)
    animations['water light']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_water/end/tile' + str(num) + '.png' for num in range(0,15)]
    ice_death = Animation(path_list, 200, 200)
    animations['water light']['end'] = ice_death.farme_list




    path_list = ['games/epic_dungeon_adventure_game/assets/spells/heavy_fire/tile' + str(num).zfill(3) + '.png' for num in range(0,18)]
    ice_death = Animation(path_list, 400, 400)
    animations['fire heavy']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_fire/start/tile' + str(num).zfill(3) + '.png' for num in range(0,4)]

    ice_death = Animation(path_list, 200, 200)
    animations['fire light']['start'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_fire/repeat/tile' + str(num).zfill(3) + '.png' for num in range(0,4)]
    ice_death = Animation(path_list, 200, 200)
    animations['fire light']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_fire/end/tile' + str(num).zfill(3) + '.png' for num in range(0,14)]
    ice_death = Animation(path_list, 400, 400)
    animations['fire light']['end'] = ice_death.farme_list




    path_list = ['games/epic_dungeon_adventure_game/assets/spells/heavy_electric/tile' + str(num).zfill(3) + '.png' for num in range(0,12)]
    ice_death = Animation(path_list, 400, 400)
    animations['electric heavy']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_electric/start/tile' + str(num).zfill(3) + '.png' for num in range(0,8)]

    ice_death = Animation(path_list, 200, 200)
    animations['electric light']['start'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_electric/repeat/tile' + str(num).zfill(3) + '.png' for num in range(8,16)]
    ice_death = Animation(path_list, 200, 200)
    animations['electric light']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_electric/end/tile' + str(num).zfill(3) + '.png' for num in range(0,5)]
    ice_death = Animation(path_list, 200, 200)
    animations['electric light']['end'] = ice_death.farme_list




    path_list = ['games/epic_dungeon_adventure_game/assets/spells/heavy_shadow/Bringer-of-Death_Spell_' + str(num) + '.png' for num in range(1,17)]
    ice_death = Animation(path_list, 400, 400)
    animations['shadow heavy']['repeat'] = ice_death.farme_list

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
