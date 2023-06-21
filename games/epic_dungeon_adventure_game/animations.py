import pygame
from .entitty import Animation

def get_animations():
    
    animations = {
        "knight":{},
        "demon":{},
        "Dragon monster":{},
        "fire monster":{},
        "fire worm":{},
        "Evil Wizard":{},
        "fire man":{},
    }


#idle and walk menstor
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/FireMonester/idle/idle_'+str(num)+'.png' for num in range(1,7)]
    fireMonster_idle = Animation(path_list, 200, 200)
    animations['fire monster']['idle'] = fireMonster_idle.farme_list
    ####
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster2/01_demon_idle/demon_idle_'+str(num)+'.png' for num in range(1,7)]
    Dragon_idle = Animation(path_list, 400, 400)
    animations['Dragon monster']['idle'] = Dragon_idle.farme_list

    ####
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster3/idle/Idle_'+str(num)+'.png' for num in range(1,7)]
    worm_idle = Animation(path_list, 200, 200)
    animations['fire worm']['idle'] = worm_idle.farme_list
    ###
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster4/idle/Idle_'+str(num)+'.png' for num in range(1,8)]
    Evil_idle=Animation(path_list,200,200)
    animations['Evil Wizard']['idle']=Evil_idle.farme_list
   ###
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster5/idle/idle'+str(num)+'.png' for num in range(1,6)]
    fire_man=Animation(path_list,200,200)
    animations['fire man']['idle']=fire_man.farme_list
#attack monester
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/FireMonester/attack/attack_'+str(num)+'.png' for num in range(1,10)]
    fireMonster_walk = Animation(path_list, 200, 200)
    animations['fire monster']['attack'] = fireMonster_walk.farme_list

    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster2/03_demon_cleave/demon_cleave_'+str(num)+'.png' for num in range(1,16)]
    Dragon_attack = Animation(path_list, 200, 200)
    animations['Dragon monster']['attack'] = Dragon_attack.farme_list
    
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster3/attack/Attack_'+str(num)+'.png' for num in range(1,12)]
    worm_attack = Animation(path_list, 200, 200)
    animations['fire worm']['attack'] = worm_attack.farme_list

    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster4/Attack/Attack'+str(num)+'.png' for num in range(1,9)]
    Evil_attack=Animation(path_list,200,200)
    animations['Evil Wizard']['attack']=Evil_attack.farme_list


    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster5/attack/attack'+str(num)+'.png' for num in range(1,18)]
    fire_man=Animation(path_list,200,200)
    animations['fire man']['attack']=fire_man.farme_list
# death
    path_list=['games/epic_dungeon_adventure_game/assests/Fire/FireMonester/death/death_'+str(num)+'.png' for num in range(1,9)]
    fireMonster_death = Animation(path_list, 200, 200)
    animations['fire monster']['death'] = fireMonster_death.farme_list

    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster2/05_demon_death/demon_death_'+str(num)+'.png' for num in range(1,23)]
    Dragon_monster = Animation(path_list, 200, 200)
    animations['Dragon monster']['death'] = Dragon_monster.farme_list

    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster3/death/Death_'+str(num)+'.png' for num in range(1,8)]
    worm_death= Animation(path_list, 200, 200)
    animations['fire worm']['death'] = worm_death.farme_list

    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster4/Death/Death_'+str(num)+'.png' for num in range(1,6)]
    Evil_death=Animation(path_list,200,200)
    animations['Evil Wizard']['death']=Evil_death.farme_list


    path_list=['games/epic_dungeon_adventure_game/assests/Fire/firemonster5/death/death'+str(num)+'.png' for num in range(1,8)]
    fire_man=Animation(path_list,200,200)
    animations['fire man']['death']=fire_man.farme_list
    
    return animations