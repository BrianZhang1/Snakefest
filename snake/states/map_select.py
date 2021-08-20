# map_select.py is holds the Map_Select class
# this class is the map selection screen

import tkinter as tk
from snake.global_helpers import maps, assets

class Map_Select(tk.Frame):
    def __init__(self, master, load_new_game, load_main_menu):
        super().__init__(master)

        self.settings = {
            "rows": 15,
            "columns": 15,
            "map": "default"
        }

        # Header frame is just the title
        self.header_frame_bg = "lavender"
        self.header_frame = tk.Frame(self, bg=self.header_frame_bg)
        self.header_frame.pack(side="top", fill="x")

        self.title_label = tk.Label(self.header_frame, text="Map Selection", font="Arial, 25", bg=self.header_frame_bg)
        self.title_label.pack(anchor="nw", side="top", padx=50, pady=(30, 15))

        self.main_menu_button = tk.Button(self.header_frame, text="<- Back to Main Menu", command=load_main_menu)
        self.main_menu_button.pack(anchor="nw", side="top", padx=50, pady=(0, 30))

        # Content frame is further split into left and right
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side="bottom", expand=True, fill="both")

        # Content frame left holds the map display
        self.content_frame_left_bg = "gray90"
        self.content_frame_left = tk.Frame(self.content_frame, bg=self.content_frame_left_bg)
        self.content_frame_left.pack(side="left", expand=True, fill="both")

        self.map_display = tk.Canvas(self.content_frame_left, width=300, height=300)
        self.update_map()
        self.map_display.place(anchor="center", relx=0.5, rely=0.5)

        # Content frame right holds the control panel and the play button
        self.content_frame_right_bg = "gray70"
        self.content_frame_right = tk.Frame(self.content_frame, bg=self.content_frame_right_bg)
        self.content_frame_right.pack(side="right", fill="both")

        self.content_frame_right_top = tk.Frame(self.content_frame_right, bg=self.content_frame_right_bg, width=350)
        self.content_frame_right_top.pack(side="top", expand=True, fill="both")
        self.content_frame_right_bottom = tk.Frame(self.content_frame_right, bg=self.content_frame_right_bg, height="200")
        self.content_frame_right_bottom.pack(side="bottom", fill="x")

        self.control_panel_frame = tk.Frame(self.content_frame_right_top)
        self.control_panel_frame.place(anchor="center", relx=0.5, rely=0.5)

        self.play_button = tk.Button(
            self.content_frame_right_bottom, text="Play ->", font="Arial, 16", bg="green2", 
            command=lambda: load_new_game(self.settings))
        self.play_button.pack(anchor="se", padx=50, pady=30)


        self.pack(expand=True, fill="both")
    
    def update_map(self):
        self.map_display.delete("all")
        settings = self.settings
        rows = settings["rows"]
        columns = settings["columns"]
        map = settings["map"]
        self.map_display.configure(width=columns*assets.TILE_LENGTH, height=rows*assets.TILE_LENGTH)
        tile_array = None
        if map == "default":
            tile_array = maps.default(self.map_display, rows, columns)[0]
        elif map == "plain":
            tile_array = maps.plain(self.map_display, rows, columns)[0]
        
        for row in tile_array:
            for tile in row:
                tile.render()
