#    Snakefest is an extended version of the popular Snake game.
#    Copyright (C) 2021  Brian Zhang
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>

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
    