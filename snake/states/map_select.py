# map_select.py is holds the Map_Select class
# this class is the map selection screen

import tkinter as tk

class Map_Select(tk.Frame):
    def __init__(self, master, load_new_game, load_main_menu):
        super().__init__(master)