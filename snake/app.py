# app.py manages the entire game from the highest level.
# It manages the tkinter event loop and different pages (swapping between main menu, game, etc.)

import tkinter as tk
root = tk.Tk()
import time
from snake.game import game as game_    # trailing _ to avoid name conflicts

def run():
    # Initialize game (usually would start at main menu, but that is todo)
    game = game_.Game(root)
    game.pack()
    game.focus_set()

    game.update_snake()
    root.mainloop()
