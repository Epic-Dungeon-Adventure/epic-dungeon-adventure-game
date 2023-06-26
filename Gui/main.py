import eel
eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def tryjs():
    print("narmeen")
    return "narmeen"



# ---------------------

# ---------------------

# say_hello_py('Python World!')

eel.start('index.html')