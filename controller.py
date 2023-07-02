import eel
eel.init('Gui', allowed_extensions=['.js', '.html'])


# chosen_game = None

@eel.expose
def chose_game(name):
    # global chosen_game
    if name == "epic dungeon adventure":
        from games.epic_dungeon_adventure_game.game import play
    elif name == "flappy bird":
        from games.flappy_bird.game import play
    elif name == "whack mole":
        from games.whack_mole.game import play
    play()
    # chosen_game = play


eel.start('index.html')
# name = "epic dungeon adventure"
# chose_game(name)
# chosen_game()
