import pygame
from .entitty import Animation

def get_animations():

    animations = {
        "knight": {},
        "demon": {},
        "demon_ice1": {},
        "demon_ice2": {},
        "demon_ice3": {},
        "icecream": {},
        "ice_boss": {},
        "ice_witch": {},


    }







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














    return animations
