# from games.epic_dungeon_adventure_game.game import play

# play()




# ---------------------
# GUI NARMEEN
import eel
eel.init('Gui', allowed_extensions=['.js', '.html'])
# print("Hello from Python!")

@eel.expose
def hello_from_python(name):
    print(name)
    return "Hello from Python!"

eel.start('index.html')
# GUI NARMEEN
# ---------------------
