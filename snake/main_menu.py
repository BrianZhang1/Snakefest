# main_menu.py holds the class for the main menu

import tkinter as tk
from snake import assets

class Main_Menu(tk.Frame):
    def __init__(self, master, load_new_game):
        bg_color = "AntiqueWhite1"
        super().__init__(master, bg=bg_color)

        self.button_panel = tk.Frame(self)

        self.start_new_game_button = tk.Label(self, image=assets.start_new_game_button, bg=bg_color)
        self.start_new_game_button.bind("<Button-1>", lambda _: load_new_game())
        self.start_new_game_button.bind("<Enter>", lambda _: self.start_new_game_button.configure(image=assets.start_new_game_button_highlighted))
        self.start_new_game_button.bind("<Leave>", lambda _: self.start_new_game_button.configure(image=assets.start_new_game_button))
        self.start_new_game_button.pack()

        self.button_panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    