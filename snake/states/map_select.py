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

# map_select.py is holds the Map_Select class
# this class is the map selection screen

# Map Select Widget Structure:
#   header_frame
#       title_label
#       main_menu_button
#   content_frame
#       content_frame_left
#           map_display
#       content_frame_right
#           content_frame_right_top
#               control_panel
#                   map_select_menubutton_wrapper
#                       map_select_label
#                       map_select_menubutton
#                   row_select_wrapper
#                       row_limit_label
#                       row_select_label
#                       row_select_entry
#                       row_select_set_button
#                   column_select_wrapper
#                       column_limit_label
#                       column_select_label
#                       column_select_entry
#                       column_select_set_button
#           content_frame_right_bottom
#               play_button


import tkinter as tk
import sys
from snake.global_helpers import assets, map_class, maps

class Map_Select(tk.Frame):
    def __init__(self, master, load_new_game, load_main_menu, data, play_again=False):
        super().__init__(master)

        self.load_new_game = load_new_game
        self.load_main_menu = load_main_menu
        self.data = data

        self.map_list = []
        for map in self.data["maps"]:
            self.map_list.append(map["name"])
        
        self.map = self.data["settings"]["map"]
        self.speed_modifier = self.data["settings"]["speed_modifier"]

        # Limits for settings
        self.min_map_rows = 1
        self.max_map_rows = 20
        self.min_map_columns = 1
        self.max_map_columns = 35
        self.max_speed_modifier = 2
        self.min_speed_modifier = 0.5


        if not play_again:
            self.render()
        else:
            self.destroy()
            self.load_new_game(self.map, self.speed_modifier, play_again=True)

    def render(self):
        # Header frame
        self.header_frame_bg = "lavender"
        self.header_frame = tk.Frame(self, bg=self.header_frame_bg)
        self.header_frame.pack(side="top", expand=True, fill="both")

        self.title_label = tk.Label(self.header_frame, text="Map Selection", font="Arial, 25", bg=self.header_frame_bg)
        self.title_label.pack(anchor="nw", side="top", padx=50, pady=(30, 15))

        self.main_menu_button = tk.Button(self.header_frame, text="<- Back to Main Menu", command=self.load_main_menu)
        self.main_menu_button.pack(anchor="nw", side="top", padx=50, pady=(0, 30))

        # Content frame
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side="bottom", fill="both")

        # Content frame left
        self.content_frame_left_bg = "gray90"
        content_frame_left_width = assets.SCREEN_GEOMETRY[0] * assets.DISPLAY_SHRINK
        content_frame_left_height = assets.SCREEN_GEOMETRY[1] * assets.DISPLAY_SHRINK
        self.content_frame_left = tk.Frame(self.content_frame, bg=self.content_frame_left_bg, 
            width=content_frame_left_width, height=content_frame_left_height)
        self.content_frame_left.pack(side="left")

        # Generate display map
        initial_map_array = self.get_map_array(self.map)
        self.map_display = map_class.Map(self.content_frame_left, initial_map_array)
        self.map_display.render(display=True)
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)

        # Content frame right
        self.content_frame_right_bg = "gray70"
        self.content_frame_right = tk.Frame(self.content_frame, bg=self.content_frame_right_bg)
        self.content_frame_right.pack(side="right", expand=True, fill="both")

        self.content_frame_right_top = tk.Frame(self.content_frame_right, bg=self.content_frame_right_bg)
        self.content_frame_right_top.pack(side="top", expand=True, fill="both")
        self.content_frame_right_bottom = tk.Frame(self.content_frame_right, bg=self.content_frame_right_bg, height="200")
        self.content_frame_right_bottom.pack(side="bottom", fill="x")

        # Control panel
        self.control_panel_frame_bg = "gray80"
        self.control_panel_frame = tk.Frame(self.content_frame_right_top, bg=self.control_panel_frame_bg)
        self.control_panel_frame.place(anchor="center", relx=0.5, rely=0.5)
        
        # Map select
        self.map_select_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.map_select_wrapper.pack(pady=20, padx=20)
        self.map_select_label = tk.Label(self.map_select_wrapper, text="Select Map: ", bg=self.control_panel_frame_bg)
        self.map_select_label.pack(side="left")
        self.map_select_menubutton_var = tk.StringVar()
        self.map_select_menubutton_var.set(self.map)
        self.map_select_menubutton = tk.Menubutton(self.map_select_wrapper, textvariable=self.map_select_menubutton_var, 
            indicatoron=True)
        self.map_select_menu = tk.Menu(self.map_select_menubutton)
        self.map_select_menubutton.configure(menu=self.map_select_menu)
        def update_map_menu(new_map):
            self.map = new_map
            self.map_select_menubutton_var.set(new_map)
            self.update_map()
        for map in self.map_list:
            self.map_select_menu.add_command(label=map, command=lambda map=map: update_map_menu(map))
        
        self.map_select_menubutton.pack(side="left")

        # Speed modifier
        self.speed_modifier_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.speed_modifier_wrapper.pack(pady=15, padx=20)
        self.speed_modifier_limit_label_var = tk.StringVar()
        self.speed_modifier_limit_label_var.set(
            "Minimum speed modifier: " + str(self.min_speed_modifier) + "\nMaximum speed modifier: " + str(self.max_speed_modifier))
        self.speed_modifier_limit_label = tk.Label(self.speed_modifier_wrapper, bg=self.control_panel_frame_bg, textvariable=self.speed_modifier_limit_label_var)
        self.speed_modifier_limit_label.pack(side="top")
        self.speed_modifier_current_label_var = tk.StringVar()
        self.speed_modifier_current_label_var.set("Current speed modifier: " + str(float(self.speed_modifier)))
        self.speed_modifier_current_label = tk.Label(self.speed_modifier_wrapper, bg=self.control_panel_frame_bg, textvariable=self.speed_modifier_current_label_var)
        self.speed_modifier_current_label.pack(side="top")
        self.speed_modifier_label = tk.Label(self.speed_modifier_wrapper, bg=self.control_panel_frame_bg, text="Speed Modifier:")
        self.speed_modifier_label.pack(side="left")
        def validate_speed_modifer_entry(input):
            if input == "":
                return True
            try:
                float(input)
            except ValueError:
                return False
            return True
        validate_speed_modifer_command = self.register(validate_speed_modifer_entry)
        self.speed_modifier_entry = tk.Entry(self.speed_modifier_wrapper, validate="key", width=3, 
            validatecommand=(validate_speed_modifer_command, "%P"))
        self.speed_modifier_entry.insert(tk.END, str(float(self.speed_modifier)))
        self.speed_modifier_entry.pack(side="left", padx=(0, 15))
        def set_speed_modifier(speed_modifier):
            if self.validate_speed_modifier(speed_modifier):
                num = float(speed_modifier)
                self.speed_modifier = num
                self.speed_modifier_current_label_var.set("Current speed modifier: " + str(num))
        self.speed_modifier_set_button = tk.Button(self.speed_modifier_wrapper, text="Set",
            command=lambda: set_speed_modifier(self.speed_modifier_entry.get()))
        self.speed_modifier_set_button.pack(side="left")

        # Play button
        self.play_button = tk.Button(
            self.content_frame_right_bottom, text="Play ->", font="Arial, 16", bg="green2", 
            command=lambda: self.load_new_game(self.map, self.speed_modifier))
        self.play_button.pack(anchor="se", padx=50, pady=30)


        self.pack(expand=True, fill="both")
    
    def update_map(self):
        self.map_display.destroy()
        del self.map_display

        new_map_array = self.get_map_array(self.map)
        self.map_display = map_class.Map(self.content_frame_left, new_map_array)
        self.map_display.render(display=True)
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)

    # Validation functions for settings
    def validate_map(self, map):
        if map in self.map_list:
            return True
        return False

    def validate_rows(self, rows):
        try:
            num = int(rows)
        except ValueError:
            return False
        if self.min_map_rows <= num <= self.max_map_rows:
            return True
        return False

    def validate_columns(self, columns):
        try:
            num = int(columns)
        except ValueError:
            return False
        if self.min_map_columns <= num <= self.max_map_columns:
            return True
        return False
    
    def validate_speed_modifier(self, speed_modifier):
        try:
            num = float(speed_modifier)
        except ValueError:
            return False
        if self.min_speed_modifier <= num <= self.max_speed_modifier:
            return True
        return False

    def get_map_array(self, name):
        # Verify map exists
        if not name in self.map_list:
            return False

        # Search for map
        for map in self.data["maps"]:
            if map["name"] == name:
                return map["array"]
        
        # Some error occured, map exists but not found in data
        print("Map exists but wasn't found in data")
        sys.exit()
    