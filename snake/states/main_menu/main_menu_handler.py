# main_menu.py holds the class for the main menu

import tkinter as tk

from snake.global_helpers import assets

class Main_Menu(tk.Frame):
    def __init__(self, master, load_map_select, load_map_creator):
        bg_color = "AntiqueWhite1"
        super().__init__(master, bg=bg_color)

        self.button_panel = tk.Frame(self, bg=bg_color)

        self.start_new_game_button = tk.Label(self.button_panel, image=assets.start_new_game_button, bg=bg_color)
        self.start_new_game_button.bind("<Button-1>", lambda _: load_map_select())
        self.start_new_game_button.bind("<Enter>", lambda _: self.start_new_game_button.configure(image=assets.start_new_game_button_highlighted))
        self.start_new_game_button.bind("<Leave>", lambda _: self.start_new_game_button.configure(image=assets.start_new_game_button))
        self.start_new_game_button.pack(pady=(0, 30))

        self.map_creator_button = tk.Label(self.button_panel, image=assets.map_creator_button, bg=bg_color)
        self.map_creator_button.bind("<Button-1>", lambda _: load_map_creator())
        self.map_creator_button.bind("<Enter>", lambda _: self.map_creator_button.configure(image=assets.map_creator_button_highlighted))
        self.map_creator_button.bind("<Leave>", lambda _: self.map_creator_button.configure(image=assets.map_creator_button))
        self.map_creator_button.pack()

        self.button_panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.pack(expand=True, fill="both")
    