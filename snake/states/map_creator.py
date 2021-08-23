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
import sys
from snake.global_helpers import maps, assets

class Map_Creator(tk.Frame):
    def __init__(self, master, load_new_game, load_main_menu):
        super().__init__(master)

        DEFAULT_SETTINGS = {
            "name": "Untitled Map",
            "rows": 15,
            "columns": 15,
            "map": []
        }

        self.settings = DEFAULT_SETTINGS

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

        self.title_label = tk.Label(self.header_frame, text="Map Selection", font="Arial, 25", bg=self.header_frame_bg)
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

        self.map_display = maps.Map(self.content_frame_left, self.settings, "plain")
        self.map_display.render(display=True)
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)

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
        self.row_select_entry.insert(tk.END, str(self.settings["rows"]))
        self.row_select_entry.pack(side="left", padx=(0, 15))
        def set_rows(rows):
            if validate_rows(rows):
                self.settings["rows"] = int(rows)
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
        self.column_select_entry.insert(tk.END, str(self.settings["columns"]))
        self.column_select_entry.pack(side="left", padx=(0, 15))
        def set_columns(columns):
            if validate_columns(columns):
                self.settings["columns"] = int(columns)
                self.set_map()
        self.column_select_set_button = tk.Button(self.column_select_wrapper, text="Set",
            command=lambda: set_columns(self.column_select_entry.get()))
        self.column_select_set_button.pack(side="left")


        # Play button
        self.play_button = tk.Button(
            self.content_frame_right_bottom, text="Play ->", font="Arial, 16", bg="green2", 
            command=lambda: load_new_game(self.settings))
        self.play_button.pack(anchor="se", padx=50, pady=30)


        self.pack(expand=True, fill="both")
    
    def set_map(self):
        self.map_display.destroy()
        del self.map_display

        self.map_display = maps.Map(self.content_frame_left, self.settings, "plain")
        self.map_display.render(display=True)
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)
