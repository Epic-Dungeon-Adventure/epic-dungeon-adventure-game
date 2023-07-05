# import eel
# eel.init('Gui', allowed_extensions=['.js', '.html'])


# @eel.expose
# def chose_game(name):
#     print(name)
#     if name == "epic dungeon adventure":
#         from games.epic_dungeon_adventure_game.game import play
#     elif name == "flappy bird":
#         from games.Flappy_Bird_Game.game import play
#     elif name == "whack mole":
#         from games.whackamole.mole import play
#     play()


# eel.start('index.html')

from games.epic_dungeon_adventure_game.game import play

play()
