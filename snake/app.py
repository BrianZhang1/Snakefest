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

# Import all the screens
from snake.states.game import game_handler
from snake.states.main_menu import main_menu_handler
from snake.states.map_creator import map_creator_handler
from snake.states.map_select import map_select_handler
import json, copy

class App():
    def __init__(self):
        self.root = root
        self.state = None

        self.load_data()

        self.load_main_menu()
        root.mainloop()

    # Load data from data.txt. Validation is done in map select
    def load_data(self):
        self.data = None
        try:
            with open("snake/data.txt") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            with open("snake/default_data.txt") as default_file:
                with open ("snake/data.txt", "w") as file:
                    self.data = json.load(default_file)
                    json.dump(self.data, file)


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
        self.main_menu = main_menu_handler.Main_Menu(self.root, self.load_map_select, self.load_map_creator)

    def load_new_game(self, map_name, speed_modifier, play_again=False):
        if not play_again:
            self.clear_state()

        with open("snake/data.txt", "w") as file:
            self.data["settings"]["map"] = map_name
            self.data["settings"]["speed_modifier"] = speed_modifier
            json.dump(self.data, file)
        
        # Find map array in data
        map_array = None
        for map in self.data["maps"]:
            if map["name"] == map_name:
                map_array = copy.deepcopy(map["array"])

        self.state = "game"
        self.game = game_handler.Game(self.root, self.play_again, self.load_main_menu, map_array, speed_modifier)

    def load_map_select(self):
        self.clear_state()

        self.state = "map_select"
        self.map_select = map_select_handler.Map_Select(self.root, self.load_new_game, self.load_main_menu, self.data)
    
    # Loads map select with play again parameter
    def play_again(self):
        self.clear_state()

        self.state = "map_select"
        map_select_handler.Map_Select(self.root, self.load_new_game, self.load_main_menu, self.data, play_again=True)
    
    def load_map_creator(self):
        self.clear_state()

        self.state = "map_creator"
        self.map_creator = map_creator_handler.Map_Creator(self.root, self.load_new_game, self.load_main_menu, self.save_map, self.delete_map, self.data["maps"])

    def save_map(self, map_info):
        # Make sure map name is unique
        for map in self.data["maps"]:
            if map["name"] == map_info["name"]:
                return False

        self.data["maps"].append(map_info)
        with open("snake/data.txt", "w") as file:
            json.dump(self.data, file)

        self.load_main_menu()

    def delete_map(self, map_name):
        map_index = 0
        for map in self.data["maps"]:
            if map["name"] == map_name:
                self.data["maps"].pop(map_index)
                break
            map_index += 1
            if map_index == len(self.data["maps"]):
                return False
        
        if self.data["settings"]["map"] == map_name:
            self.data["settings"]["map"] = self.data["maps"][0]["name"]
            
        with open("snake/data.txt", "w") as file:
            json.dump(self.data, file)

        self.load_main_menu()
        return True
