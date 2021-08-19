# app.py manages the entire app from the highest level.
# It manages the tkinter event loop and different pages (swapping between main menu, game, etc.)

import tkinter as tk
root = tk.Tk()
root.geometry("1280x720")
from snake.game import game as game_    # trailing _ to avoid name conflicts

class App():
    def __init__(self):
        self.root = root
        self.game = None

    def load_main_menu(self):
        pass

    def start_new_game(self):
        if self.game != None:
            self.game.destroy()

        self.game = game_.Game(self.root, self.start_new_game, self.load_main_menu)
        self.game.pack(expand=True)
        self.game.focus_set()

        root.mainloop()
