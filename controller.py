

chosen_game = None
def chose_game(name):
    global chosen_game
    if name == "epic dungeon adventure":
        from games.epic_dungeon_adventure_game.game import play
    if name == "flappy bird":
        from games.flappy_bird.game import play
    if name == "whack mole":
        from games.whack_mole.game import play
    chosen_game = play


name = "epic dungeon adventure"

chose_game(name)

chosen_game()

