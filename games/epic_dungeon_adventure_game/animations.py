import pygame
from components.entitty import Animation

def get_animations():

    animations = {
        "bringer of death":{},
        "necromancer":{},
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
        "halloween heavy":{},
        "ice light":{},
        "ice heavy":{},
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

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/idle/tile' + str(num).zfill(3) + '.png' for num in range(0,6)]
    ice_death = Animation(path_list, 400, 330)
    animations['ice boss']['idle'] =ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/attack/tile' + str(num).zfill(3) + '.png' for num in range(0,14)]
    ice_death = Animation(path_list, 400, 300)
    animations['ice boss']['attack'] =ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/death/tile' + str(num).zfill(3) + '.png' for num in range(0,16)]
    ice_death = Animation(path_list, 400, 300)
    animations['ice boss']['death'] =ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/ice_boss/take_hit/tile' + str(num).zfill(3) + '.png' for num in range(0,7)]
    ice_death = Animation(path_list, 400, 300)
    animations['ice boss']['take hit'] =ice_death.farme_list




    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/demon_boss/idle/demon_idle_' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 500, 500)
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
    ice_death = Animation(path_list, 600, 400)
    animations['bringer of death']['idle'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/bringer_of_death/attack/Bringer-of-Death_Cast_' + str(num) + '.png' for num in range(1,10)]
    ice_death = Animation(path_list, 600, 400)
    animations['bringer of death']['attack'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/bringer_of_death/death/Bringer-of-Death_Death_' + str(num) + '.png' for num in range(1,11)]
    ice_death = Animation(path_list, 600, 400)
    animations['bringer of death']['death'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/bringer_of_death/take_hit/Bringer-of-Death_Hurt_' + str(num) + '.png' for num in range(1,4)]
    ice_death = Animation(path_list, 600, 400)
    animations['bringer of death']['take hit'] = ice_death.farme_list



    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/necromancer/idle/tile' + str(num).zfill(3) + '.png' for num in range(1,9)]
    ice_death = Animation(path_list, 500, 500)
    animations['necromancer']['idle'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/necromancer/attack/tile' + str(num).zfill(3) + '.png' for num in range(1,14)]
    ice_death = Animation(path_list, 500, 500)
    animations['necromancer']['attack'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/necromancer/death/tile' + str(num).zfill(3) + '.png' for num in range(1,10)]
    ice_death = Animation(path_list, 500, 500)
    animations['necromancer']['death'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/monsters/necromancer/take_hit/tile' + str(num).zfill(3) + '.png' for num in range(1,6)]
    ice_death = Animation(path_list, 500, 500)
    animations['necromancer']['take hit'] = ice_death.farme_list

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
    ice_death = Animation(path_list, 600, 600)
    animations['shadow heavy']['repeat'] = ice_death.farme_list
    



    path_list = ['games/epic_dungeon_adventure_game/assets/spells/heavy_halloween/tile' + str(num).zfill(3) + '.png' for num in range(0,27)]
    ice_death = Animation(path_list, 400, 400)
    animations['halloween heavy']['repeat'] = ice_death.farme_list





    path_list = ['games/epic_dungeon_adventure_game/assets/spells/heavy_ice/' + str(num) + '.png' for num in range(1,37)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice heavy']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_ice/start/tile' + str(num).zfill(3) + '.png' for num in range(0,3)]  
    ice_death = Animation(path_list, 200, 200)
    animations['ice light']['start'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_ice/repeat/tile' + str(num).zfill(3) + '.png' for num in range(0,10)]
    ice_death = Animation(path_list, 200, 200)
    animations['ice light']['repeat'] = ice_death.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/spells/light_ice/end/tile' + str(num).zfill(3) + '.png' for num in range(0,8)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice light']['end'] = ice_death.farme_list
    return animations
