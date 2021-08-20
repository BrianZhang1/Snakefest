# app.py manages the entire app from the highest level.
# It manages the tkinter event loop and different pages (swapping between main menu, game, etc.)

import tkinter as tk

from PIL.Image import init
root = tk.Tk()
root.geometry("1280x720")
from snake.game import game
from snake import main_menu

class App():
    def __init__(self, inital_state):
        self.root = root
        self.state = None

        if inital_state == "main_menu":
            self.load_main_menu()
            root.mainloop()

        if inital_state == "game":
            self.load_new_game()
            root.mainloop()

    def clear_state(self):
        if self.state == "game":
            self.game.destroy()
            del self.game

        elif self.state == "main_menu":
            self.main_menu.destroy()
            del self.main_menu
        
        self.state = None

    def load_main_menu(self):
        self.clear_state()

        self.state = "main_menu"
        self.main_menu = main_menu.Main_Menu(self.root, self.load_new_game)
        self.main_menu.pack(expand=True)

    def load_new_game(self):
        self.clear_state()

        self.state = "game"
        self.game = game.Game(self.root, self.load_new_game, self.load_main_menu, "default")
        self.game.pack(expand=True)
        self.game.focus_set()

