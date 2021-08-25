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

# app.py manages the entire app from the highest level.
# It manages the tkinter event loop and different pages (swapping between main menu, game, etc.)

import tkinter as tk
root = tk.Tk()
root.geometry("1280x720")
root.resizable(False, False)

from snake.states import game, main_menu, map_select, map_creator
import json

class App():
    def __init__(self):
        self.root = root
        self.state = None

        self.DATA_INDENT = 4
        self.map_list = ["default", "plain"]

        self.load_data()
        self.settings = self.data["settings"]

        self.load_main_menu()
        root.mainloop()

    # Load data from data.txt. Validation is done in map select
    def load_data(self):
        self.data = None
        try:
            with open("snake/data.txt") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            with open("snake/data.txt", "w") as file:
                settings = {
                    "rows": 15,
                    "columns": 15,
                    "map": "default",
                    "speed_modifier": 1
                }
                self.data = {
                    "settings": settings,
                    "maps": []
                }
                json.dump(self.data, file, indent=self.DATA_INDENT)


    def clear_state(self):
        if self.state == "game":
            self.game.destroy()
            del self.game

        elif self.state == "main_menu":
            self.main_menu.destroy()
            del self.main_menu

        elif self.state == "map_select":
            self.map_select.destroy()
            del self.map_select
        
        elif self.state == "map_creator":
            self.map_creator.destroy()
            del self.map_creator
        
        self.state = None

    def load_main_menu(self):
        self.clear_state()

        self.state = "main_menu"
        self.main_menu = main_menu.Main_Menu(self.root, self.load_map_select, self.load_map_creator)

    def load_new_game(self, map_array, speed_modifier, play_again=False):
        if not play_again:
            self.clear_state()

        with open("snake/data.txt", "w") as file:
            self.data["settings"] = self.settings
            json.dump(self.data, file, indent=self.DATA_INDENT)

        self.state = "game"
        self.game = game.Game(self.root, self.play_again, self.load_main_menu, map_array, speed_modifier)

    def load_map_select(self):
        self.clear_state()

        self.state = "map_select"
        self.map_select = map_select.Map_Select(self.root, self.load_new_game, self.load_main_menu, self.settings, self.map_list)
    
    # Loads map select with play again parameter
    def play_again(self):
        self.clear_state()

        self.state = "map_select"
        map_select.Map_Select(self.root, self.load_new_game, self.load_main_menu, self.settings, self.map_list, play_again=True)
    
    def load_map_creator(self):
        self.clear_state()

        self.state = "map_creator"
        self.map_creator = map_creator.Map_Creator(self.root, self.load_new_game, self.load_main_menu, self.save_map)

    def save_map(self, map_info):
        # Jsonify map
        tile_array = map_info["array"]
        jsonified_tile_array = []
        for row in tile_array:
            new_row = []
            for tile in row:
                new_row.append(tile.get_info())
            jsonified_tile_array.append(new_row)
        
        jsonified_map = map_info
        jsonified_map["array"] = jsonified_tile_array

        self.data["maps"].append(jsonified_map)
        with open("snake/data.txt", "w") as file:
            json.dump(self.data, file, indent=self.DATA_INDENT)

        self.load_main_menu()
