import pygame
from components.entitty import Animation

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
        "demon_ice1": {},
        "demon_ice2": {},
        "demon_ice3": {},
        "icecream": {},
        "ice_boss": {},
        "ice_witch": {},
        "Dragon monster":{},
        "fire monster":{},
        "fire worm":{},
        "Evil Wizard":{},
        "fire man":{},
    }

    path_list=['./games/epic_dungeon_adventure_game/assets/knight/knight walk animation'+str(num)+'.png' for num in range(1,9)]
    knight_walk = Animation(path_list, 200, 200)
    animations['knight']['walk'] = knight_walk.farme_list








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

  
    

    
############ demon_ice1

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice1/ice_idel/' + str(num) + '.png' for num in range(1, 5)]
    ice_idel = Animation(path_list, 230, 200)
    animations['demon_ice1']['idle'] =ice_idel.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice1/ice_attack/' + str(num) + '.png' for num in range(1, 10)]
    ice_walk = Animation(path_list, 230, 200)
    animations['demon_ice1']['attack'] =ice_walk.farme_list

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice1/ice_death/' + str(num) + '.png' for num in range(1,8)]
    ice_death = Animation(path_list, 230, 200)
    animations['demon_ice1']['death'] =ice_death.farme_list






########## demon_ice2

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice2/ice2_attack/' + str(num) + '.png' for num in range(1,6)]
    ice_death = Animation(path_list, 200, 200)
    animations['demon_ice2']['idle'] =ice_death.farme_list



    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice2/ice2_attack/' + str(num) + '.png' for num in range(1,5)]
    ice_death = Animation(path_list, 200, 200)
    animations['demon_ice2']['attack'] =ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice1/ice_death/' + str(num) + '.png' for num in range(1,12)]
    ice_death = Animation(path_list, 200, 200)
    animations['demon_ice2']['death'] =ice_death.farme_list

######### demon_ice3

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice3/ice3_idle/' + str(num) + '.png' for num in range(1, 6)]
    demon_ice_walk = Animation(path_list, 200, 200)
    animations['demon_ice3']['idle'] = demon_ice_walk.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice3/ice3_attack/' + str(num) + '.png' for num in range(1,6)]
    demon_ice_walk = Animation(path_list, 200, 200)
    animations['demon_ice3']['attack'] = demon_ice_walk.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/demon_ice3/ice3_death/' + str(num) + '.png' for num in range(1, 7)]
    demon_ice_walk = Animation(path_list, 200, 200)
    animations['demon_ice3']['death'] = demon_ice_walk.farme_list


    ########## icecream

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/icecream/icecream-idle/' + str(num) + '.png' for num in range(1,6)]
    ice_death = Animation(path_list, 200, 200)
    animations['icecream']['idle'] =ice_death.farme_list



    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/icecream/icecream-attack/' + str(num) + '.png' for num in range(1,9)]
    ice_death = Animation(path_list, 200, 200)
    animations['icecream']['attack'] =ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/icecream/icecream-death/' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 200, 200)
    animations['icecream']['death'] =ice_death.farme_list


     ########## ice boss

    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/ice_boss/boss_idle/idle_' + str(num) + '.png' for num in range(1,7)]
    ice_death = Animation(path_list, 200, 200)
    animations['ice_boss']['idle'] =ice_death.farme_list



    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/ice_boss/boss_attack/1_atk_' + str(num) + '.png' for num in range(1,15)]
    ice_death = Animation(path_list, 200, 200)
    animations['ice_boss']['attack'] =ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/demon_ice/ice_boss/boss_death/death_' + str(num) + '.png' for num in range(1,17)]
    ice_death = Animation(path_list, 200, 200)
    animations['ice_boss']['death'] =ice_death.farme_list



 ########## ice_witch

    path_list = ['games/epic_dungeon_adventure_game/assets/ice_witch/01_idle/idle_' + str(num) + '.png' for num in range(1,9)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice_witch']['idle'] =ice_death.farme_list



    path_list = ['games/epic_dungeon_adventure_game/assets/ice_witch/07_1_atk/1_atk_' + str(num) + '.png' for num in range(1,8)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice_witch']['attack'] =ice_death.farme_list


    path_list = ['games/epic_dungeon_adventure_game/assets/ice_witch/14_death/death_' + str(num) + '.png' for num in range(1,17)]
    ice_death = Animation(path_list, 400, 400)
    animations['ice_witch']['death'] =ice_death.farme_list

#idle and walk menstor
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/FireMonester/idle/idle_'+str(num)+'.png' for num in range(1,7)]
    fireMonster_idle = Animation(path_list, 200, 200)
    animations['fire monster']['idle'] = fireMonster_idle.farme_list
    ####
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster2/01_demon_idle/demon_idle_'+str(num)+'.png' for num in range(1,7)]
    Dragon_idle = Animation(path_list, 400, 400)
    animations['Dragon monster']['idle'] = Dragon_idle.farme_list

    ####
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster3/idle/Idle_'+str(num)+'.png' for num in range(1,7)]
    worm_idle = Animation(path_list, 200, 200)
    animations['fire worm']['idle'] = worm_idle.farme_list
    ###
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster4/idle/Idle_'+str(num)+'.png' for num in range(1,8)]
    Evil_idle=Animation(path_list,200,200)
    animations['Evil Wizard']['idle']=Evil_idle.farme_list
   ###
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster5/idle/idle'+str(num)+'.png' for num in range(1,6)]
    fire_man=Animation(path_list,200,200)
    animations['fire man']['idle']=fire_man.farme_list
#attack monester
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/FireMonester/attack/attack_'+str(num)+'.png' for num in range(1,10)]
    fireMonster_walk = Animation(path_list, 200, 200)
    animations['fire monster']['attack'] = fireMonster_walk.farme_list

    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster2/03_demon_cleave/demon_cleave_'+str(num)+'.png' for num in range(1,16)]
    Dragon_attack = Animation(path_list, 200, 200)
    animations['Dragon monster']['attack'] = Dragon_attack.farme_list
    
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster3/attack/Attack_'+str(num)+'.png' for num in range(1,12)]
    worm_attack = Animation(path_list, 200, 200)
    animations['fire worm']['attack'] = worm_attack.farme_list

    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster4/Attack/Attack'+str(num)+'.png' for num in range(1,9)]
    Evil_attack=Animation(path_list,200,200)
    animations['Evil Wizard']['attack']=Evil_attack.farme_list


    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster5/attack/attack'+str(num)+'.png' for num in range(1,18)]
    fire_man=Animation(path_list,200,200)
    animations['fire man']['attack']=fire_man.farme_list
# death
    path_list=['games/epic_dungeon_adventure_game/assets/Fire/FireMonester/death/death_'+str(num)+'.png' for num in range(1,9)]
    fireMonster_death = Animation(path_list, 200, 200)
    animations['fire monster']['death'] = fireMonster_death.farme_list

    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster2/05_demon_death/demon_death_'+str(num)+'.png' for num in range(1,23)]
    Dragon_monster = Animation(path_list, 200, 200)
    animations['Dragon monster']['death'] = Dragon_monster.farme_list

    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster3/death/Death_'+str(num)+'.png' for num in range(1,8)]
    worm_death= Animation(path_list, 200, 200)
    animations['fire worm']['death'] = worm_death.farme_list

    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster4/Death/Death_'+str(num)+'.png' for num in range(1,6)]
    Evil_death=Animation(path_list,200,200)
    animations['Evil Wizard']['death']=Evil_death.farme_list


    path_list=['games/epic_dungeon_adventure_game/assets/Fire/firemonster5/death/death'+str(num)+'.png' for num in range(1,8)]
    fire_man=Animation(path_list,200,200)
    animations['fire man']['death']=fire_man.farme_list
    
    return animations
