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

# map_creator.py is holds the Map_Creator class
# this class is the map selection screen

# Map Creator Widget Structure:
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
from snake.global_helpers import map_class, assets
import copy, sys

class Map_Creator(tk.Frame):
    def __init__(self, master, load_new_game, load_main_menu, save_map, map_list):
        super().__init__(master)
        self.save_map = save_map
        self.map_list = map_list

        self.rows = 15
        self.columns = 15

        # Array is set during creation of display map
        DEFAULT_MAP_INFO = {
            "name": "Untitled Map",
            "array": None
        }

        self.map_info = DEFAULT_MAP_INFO

        self.current_tile_type = "land" # Current selected tile for map editor
        self.bordered = False           # Whether maps are bordered during row/column set

        # Limits for settings
        self.min_map_rows = 1
        self.max_map_rows = 20
        self.min_map_columns = 1
        self.max_map_columns = 35

        # Validation functions for settings
        def validate_rows(rows):
            try:
                num = int(rows)
            except ValueError:
                return False
            if self.min_map_rows <= num <= self.max_map_rows:
                return True
            return False

        def validate_columns(columns):
            try:
                num = int(columns)
            except ValueError:
                return False
            if self.min_map_columns <= num <= self.max_map_columns:
                return True
            return False


        # Header frame
        self.header_frame_bg = "lavender"
        self.header_frame = tk.Frame(self, bg=self.header_frame_bg)
        self.header_frame.pack(side="top", expand=True, fill="both")

        self.title_label_var = tk.StringVar()
        self.title_label_var.set(self.map_info["name"])
        self.title_label = tk.Label(self.header_frame, textvariable=self.title_label_var, font="Arial, 25", bg=self.header_frame_bg)
        self.title_label.pack(anchor="nw", side="top", padx=50, pady=(30, 15))

        self.main_menu_button = tk.Button(self.header_frame, text="<- Back to Main Menu", command=load_main_menu)
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
        self.resize_map()

        # Content frame right
        self.content_frame_right_bg = "gray70"
        self.content_frame_right = tk.Frame(self.content_frame, bg=self.content_frame_right_bg)
        self.content_frame_right.pack(side="right", expand=True, fill="both")

        self.content_frame_right_top = tk.Frame(self.content_frame_right, bg=self.content_frame_right_bg)
        self.content_frame_right_top.pack(side="top", expand=True, fill="both", padx=20, pady=20)
        self.content_frame_right_bottom = tk.Frame(self.content_frame_right, bg=self.content_frame_right_bg, height="200")
        self.content_frame_right_bottom.pack(side="bottom", fill="x")

        # Control panel
        self.control_panel_frame_bg = "gray80"
        self.control_panel_frame = tk.Frame(self.content_frame_right_top, bg=self.control_panel_frame_bg)
        self.control_panel_frame.pack(expand=True, fill="both")

        # Map Title Entry
        self.title_set_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.title_set_wrapper.pack(pady=(20, 0))
        self.title_set_label = tk.Label(self.title_set_wrapper, text="Title:", bg=self.control_panel_frame_bg)
        self.title_set_label.pack(side="left", padx=(0, 10))
        self.title_set_entry = tk.Entry(self.title_set_wrapper, width=20)
        self.title_set_entry.insert(tk.END, self.map_info["name"])
        self.title_set_entry.pack(side="left", padx=(0, 5))
        def set_title(title):
            if 0 < len(title) <= 20:
                self.title_label_var.set(title)
                self.map_info["name"] = title
        self.title_set_button = tk.Button(self.title_set_wrapper, text="Set",
            command=lambda: set_title(self.title_set_entry.get()))
        self.title_set_button.pack(side="left")

        # Base select
        self.map_select_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.map_select_wrapper.pack(pady=20, padx=20)
        self.map_select_label = tk.Label(self.map_select_wrapper, text="Base Map:", bg=self.control_panel_frame_bg)
        self.map_select_label.pack(side="left")
        self.map_select_menubutton_var = tk.StringVar()
        self.map_select_menubutton = tk.Menubutton(self.map_select_wrapper, textvariable=self.map_select_menubutton_var, 
            indicatoron=True)
        self.map_select_menu = tk.Menu(self.map_select_menubutton)
        self.map_select_menubutton.configure(menu=self.map_select_menu)
        def update_map_menu(new_map):
            self.map_select_menubutton_var.set(new_map)
            self.set_map(new_map)
        for map in self.map_list:
            self.map_select_menu.add_command(label=map["name"], command=lambda map_name=map["name"]: update_map_menu(map_name))
        self.map_select_menubutton.pack(side="left")

        # Map Resize Wrapper
        self.map_resize_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.map_resize_wrapper.pack(pady=(20, 0))

        self.row_column_select_warning_label = tk.Label(self.map_resize_wrapper, 
            text="Warning: resizing map results in a map reset", bg=self.control_panel_frame_bg, fg="red")
        self.row_column_select_warning_label.pack()
        
        # On keypress input validation for row and column entries
        def validate_rows_columns_entry(input):
            if input == "":
                return True
            try:
                int(input)
            except ValueError:
                return False
            return True
        validate_row_column_command = self.register(validate_rows_columns_entry)

        # Row select
        self.row_select_wrapper = tk.Frame(self.map_resize_wrapper, bg=self.control_panel_frame_bg)
        self.row_select_wrapper.pack(padx=20)
        self.row_select_label = tk.Label(self.row_select_wrapper, text="# of Rows: ", bg=self.control_panel_frame_bg)
        self.row_select_label.pack(side="left", padx=(0, 20))
        self.row_select_entry = tk.Entry(self.row_select_wrapper, validate="key", width=3, 
            validatecommand=(validate_row_column_command, "%P"))
        self.row_select_entry.insert(tk.END, str(len(self.map_display.array)))
        self.row_select_entry.pack(side="left", padx=(0, 15))

        # Column select
        self.column_select_wrapper = tk.Frame(self.map_resize_wrapper, bg=self.control_panel_frame_bg)
        self.column_select_wrapper.pack(pady=0, padx=20)
        self.column_select_label = tk.Label(self.column_select_wrapper, text="# of Columns: ", bg=self.control_panel_frame_bg)
        self.column_select_label.pack(side="left")
        self.column_select_entry = tk.Entry(self.column_select_wrapper, validate="key", width=3, 
            validatecommand=(validate_row_column_command, "%P"))
        self.column_select_entry.insert(tk.END, str(len(self.map_display.array[0])))
        self.column_select_entry.pack(side="left", padx=(0, 15))

        # Bordered checkbutton
        self.bordered_checkbutton_var = tk.IntVar()
        self.bordered_checkbutton_var.set(0)
        self.bordered_checkbutton = tk.Checkbutton(self.map_resize_wrapper, text="Bordered", 
            variable=self.bordered_checkbutton_var, bg=self.control_panel_frame_bg)
        self.bordered_checkbutton.pack()

        # Resize map button, validation happens here
        def validate_resize_map():
            rows = self.row_select_entry.get()
            columns = self.column_select_entry.get()
            if validate_rows(rows) and validate_columns(columns):
                self.rows = int(rows)
                self.columns = int(columns)
                self.resize_map()

        self.resize_map_button = tk.Button(self.map_resize_wrapper, text="Resize Map", font="Arial, 10", command=validate_resize_map)
        self.resize_map_button.pack()

        # Tile Selection Area
        self.tile_select_frame = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.tile_select_frame.pack(fill="x", padx=10, pady=10)
        self.tile_select_label = tk.Label(self.tile_select_frame, text="Tiles", bg=self.control_panel_frame_bg)
        self.tile_select_label.pack(anchor="nw")
        self.tile_select_buttons = tk.Frame(self.tile_select_frame, bg=self.control_panel_frame_bg)
        self.tile_select_buttons.pack(fill="x", pady=10)
        def set_current_tile_type(type):
            self.current_tile_type = type
        self.tile_select_land = tk.Label(self.tile_select_buttons, image=assets.land_tile_button, bg=self.control_panel_frame_bg)
        self.tile_select_land.bind("<Button-1>", lambda _: set_current_tile_type("land"))
        self.tile_select_land.pack(side="left")
        self.tile_select_barrier = tk.Label(self.tile_select_buttons, image=assets.barrier_tile_button, bg=self.control_panel_frame_bg)
        self.tile_select_barrier.bind("<Button-1>", lambda _: set_current_tile_type("barrier"))
        self.tile_select_barrier.pack(side="left")
        
        # Save button
        self.save_button = tk.Button(
            self.content_frame_right_bottom, text="Save ->", font="Arial, 16", bg="green2", 
            command=lambda: self.save_map(self.map_info))
        self.save_button.pack(side="right", anchor="e", padx=(30, 50), pady=30)

        # Preview button
        self.preview_button = tk.Button(
            self.content_frame_right_bottom, text="Preview", font="Arial, 14", bg="paleturquoise1", 
            command=lambda: load_new_game(self.map_display.array, 1))
        # Don't pack since it isn't finished yet
        #self.preview_button.pack(side="right", anchor="e", padx=(50, 0), pady=30)


        self.pack(expand=True, fill="both")
    
    def set_map(self, base_map):
        try:
            self.map_display.destroy()
            del self.map_display
        except AttributeError:
            pass

        new_map_array = None
        for map in self.map_list:
            if map["name"] == base_map:
                new_map_array = copy.deepcopy(map["array"])
        
        if new_map_array:
            self.map_info["array"] = new_map_array
        else:
            print("map_creator set_map: base map does not exist in map list")
            sys.exit()

        # Set row and column entries
        try:
            self.row_select_entry.delete(0, tk.END)
            self.column_select_entry.delete(0, tk.END)
            self.row_select_entry.insert(tk.END, str(len(self.map_info["array"])))
            self.column_select_entry.insert(tk.END, str(len(self.map_info["array"][0])))
        except AttributeError:
            pass
        
        self.generate_display_map()

    def resize_map(self):
        try:
            self.map_display.destroy()
            del self.map_display
        except AttributeError:
            pass

        try:
            bordered = self.bordered_checkbutton_var.get()
        except AttributeError:
            bordered = 0
        map = None
        if not bordered:
            # Generate plain map with rows and columns
            map = []
            for row_num in range(self.rows):
                row = []
                for column_num in range(self.columns):
                    tile_info = {
                        "type": "land",
                        "position": (column_num, row_num),
                        "holding": []
                    }
                    row.append(tile_info)
                map.append(row)
        else:
            # Generate bordered map with rows and columns
            map = []
            for row_num in range(self.rows):
                row = []
                for column_num in range(self.columns):
                    if row_num == 0 or row_num == self.rows - 1 or column_num == 0 or column_num == self.columns - 1:
                        tile_info = {
                            "type": "barrier",
                            "position": (column_num, row_num),
                            "holding": []
                        }
                        row.append(tile_info)
                    else:
                        tile_info = {
                            "type": "land",
                            "position": (column_num, row_num),
                            "holding": []
                        }
                        row.append(tile_info)
                map.append(row)

        if map:
            self.map_info["array"] = map
        else:
            print("map_creator resize_map(): map did not generate")
            sys.exit()

        # Clear base map select
        try:
            self.map_select_menubutton_var.set("")
        except AttributeError:
            pass

        self.generate_display_map()
    
    def generate_display_map(self):
        # Generate display map
        self.map_display = map_class.Map(self.content_frame_left, self.map_info["array"])
        self.map_display.render(display=True)
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)

        # Clicking tile on display map updates it
        for row in self.map_display.array:
            for tile in row:
                pos = tile.position
                self.map_display.tag_bind(tile.id, "<Button-1>", lambda _, pos=pos: self.update_tile(pos))

    def update_tile(self, pos):
        # Update in map_info
        tile = self.map_info["array"][pos[1]][pos[0]]
        tile["type"] = self.current_tile_type

        # Update in actual map and render
        tile_object = self.map_display.array[pos[1]][pos[0]]
        tile_object.type = self.current_tile_type
        tile_object.render_type(display=True)
