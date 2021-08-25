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
from snake.global_helpers import map_class, assets, maps

class Map_Creator(tk.Frame):
    def __init__(self, master, load_new_game, load_main_menu, save_map):
        super().__init__(master)
        self.save_map = save_map

        self.rows = 15
        self.columns = 15

        DEFAULT_MAP_INFO = {
            "name": "Untitled Map",
            "array": maps.generate_plain(self.rows, self.columns)
        }

        self.map_info = DEFAULT_MAP_INFO

        # Current selected tile for map editor
        self.current_tile_type = "land"

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
        self.map_display = map_class.Map(self.content_frame_left, self.map_info["array"])
        self.map_display.render(display=True)
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)

        # Clicking tile on display map updates it
        for row in self.map_display.array:
            for tile in row:
                pos = tile.position
                self.map_display.tag_bind(tile.id, "<Button-1>", lambda _, pos=pos: self.update_tile(pos))

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
        self.title_set_entry.pack(side="left", padx=(0, 5))
        def set_title(title):
            if 0 < len(title) <= 20:
                self.title_label_var.set(title)
                self.map_info["name"] = title
        self.title_set_button = tk.Button(self.title_set_wrapper, text="Set",
            command=lambda: set_title(self.title_set_entry.get()))
        self.title_set_button.pack(side="left")

        # Row/Column Select
        self.row_column_select_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.row_column_select_wrapper.pack(pady=(20, 0))

        self.row_column_select_warning_label = tk.Label(self.row_column_select_wrapper, 
            text="Warning: resizing map results in a map reset", bg=self.control_panel_frame_bg, fg="red")
        self.row_column_select_warning_label.pack()
        
        # Row select
        self.row_select_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.row_select_wrapper.pack(padx=20)
        self.row_select_label = tk.Label(self.row_select_wrapper, text="# of Rows: ", bg=self.control_panel_frame_bg)
        self.row_select_label.pack(side="left", padx=(0, 20))
        def validate_rows_columns_entry(input):
            if input == "":
                return True
            try:
                int(input)
            except ValueError:
                return False
            return True
        validate_row_column_command = self.register(validate_rows_columns_entry)
        self.row_select_entry = tk.Entry(self.row_select_wrapper, validate="key", width=3, 
            validatecommand=(validate_row_column_command, "%P"))
        self.row_select_entry.insert(tk.END, str(len(self.map_display.array)))
        self.row_select_entry.pack(side="left", padx=(0, 15))
        def set_rows(rows):
            if validate_rows(rows):
                self.rows = int(rows)
                self.set_map()
        self.row_select_set_button = tk.Button(self.row_select_wrapper, text="Set",
            command=lambda: set_rows(self.row_select_entry.get()))
        self.row_select_set_button.pack(side="left")

        # Column select
        self.column_select_wrapper = tk.Frame(self.control_panel_frame, bg=self.control_panel_frame_bg)
        self.column_select_wrapper.pack(pady=0, padx=20)
        self.column_select_label = tk.Label(self.column_select_wrapper, text="# of Columns: ", bg=self.control_panel_frame_bg)
        self.column_select_label.pack(side="left")
        self.column_select_entry = tk.Entry(self.column_select_wrapper, validate="key", width=3, 
            validatecommand=(validate_row_column_command, "%P"))
        self.column_select_entry.insert(tk.END, str(len(self.map_display.array[0])))
        self.column_select_entry.pack(side="left", padx=(0, 15))
        def set_columns(columns):
            if validate_columns(columns):
                self.columns = int(columns)
                self.set_map()
        self.column_select_set_button = tk.Button(self.column_select_wrapper, text="Set",
            command=lambda: set_columns(self.column_select_entry.get()))
        self.column_select_set_button.pack(side="left")

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
        self.preview_button.pack(side="right", anchor="e", padx=(50, 0), pady=30)


        self.pack(expand=True, fill="both")
    
    def set_map(self):
        self.map_display.destroy()
        del self.map_display

        map_generation_array = maps.generate_plain(self.rows, self.columns)
        self.map_display = map_class.Map(self.content_frame_left, map_generation_array)
        self.map_display.render(display=True)
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)

    def update_tile(self, pos):
        tile = self.map_display.array[pos[1]][pos[0]]
        tile.type = self.current_tile_type
        tile.render_type(display=True)
