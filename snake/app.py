# app.py manages the entire app from the highest level.
# It manages the tkinter event loop and different pages (swapping between main menu, game, etc.)

import tkinter as tk
root = tk.Tk()
root.geometry("1280x720")
from snake.game import game as game_    # trailing _ to avoid name conflicts

def run():
    # Initialize game (usually would start at main menu, but that is todo)
    game = game_.Game(root)
    game.pack(expand=True)
    game.focus_set()

    root.mainloop()
