import tkinter as tk
from tkinter import ttk
import subprocess

def start_game():
    print("Here we will do the game logic")

def quit_game():
    window.destroy()

def open_game():
    subprocess.Popen(["epic", "path"])

window = tk.Tk()
window.title("Epic Dungeon Adventure Game")

label = tk.Label(window, text="Welcome to Epic Dungeon Adventure Game", font=("Arial", 24))
label.pack(pady=20)

start_button = tk.Button(window, text="Start Game", command=start_game, font=("Arial", 16))
start_button.pack(pady=10)

quit_button = tk.Button(window, text="Quit Game", command=quit_game, font=("Arial", 16))
quit_button.pack(pady=10)

option_label = tk.Label(window, text="Choose Game:", font=("Arial", 16))
option_label.pack(pady=10)

options = ["Epic Dungeon Adventure Game"]
selected_option = tk.StringVar()
dropdown = ttk.Combobox(window, textvariable=selected_option, values=options)
dropdown.pack(pady=10)

open_button = tk.Button(window, text="Open Game", command=open_game, font=("Arial", 16))
open_button.pack(pady=10)

window.mainloop()
