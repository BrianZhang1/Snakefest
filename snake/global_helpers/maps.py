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

# maps.py is a list of maps that can be used and rendered by other files.
# It also holds the Tile class.
# the map is comprised of many Tile objects.

import tkinter as tk
from snake.global_helpers import assets, coord_converter

map_list = ["default", "plain"]

class Tile():
    def __init__(self, position, type, canvas):
        self.canvas = canvas
        self.position = position
        self.type = type
        self.holding = []
        self.rendered = False
        self.id = None
        self.converter = coord_converter.Coord_Converter()
    
    # Returns index if holding, and None if not holding
    def is_holding(self, query):
        index = 0
        for item in self.holding:
            if type(item) == query:
                return index
            index += 1

        return None
    
    # Renders tile
    def render(self, display=False):
        if not self.rendered:
            tile_coords = None
            land_tile = None
            barrier_tile = None
            if not display:
                tile_coords = self.converter.to_raw(self.position)
                land_tile = assets.land_tile
                barrier_tile = assets.barrier_tile
            else:
                display_converter = coord_converter.Coord_Converter(display=True)
                tile_coords = display_converter.to_raw(self.position)
                land_tile = assets.land_tile_display
                barrier_tile = assets.barrier_tile_display


            if self.type == "land":
                self.id = self.canvas.create_image(tile_coords, image=land_tile)
            elif self.type == "barrier":
                self.id = self.canvas.create_image(tile_coords, image=barrier_tile)
            
            self.rendered = True
        elif self.rendered and not display:
            for item in self.holding:
                item.render(self.position)
    
    # Removes item from holding and deletes on canvas
    def drop(self, item_index):
        item = self.holding[item_index]
        if item.rendered:
            self.canvas.delete(item.id)
            item.rendered = False
        self.holding.pop(item_index)

class Map(tk.Canvas):
    def __init__(self, master, map_settings, map_type):
        super().__init__(master)
        self.array = None
        self.land = None
        self.rows = map_settings["rows"]
        self.columns = map_settings["columns"]
        if map_type == "default":
            self.generate_default()
        elif map_type == "plain":
            self.generate_plain()

    def render(self, display=False):
        size_modifier = 1
        if display:
            size_modifier = assets.DISPLAY_SHRINK

        canvas_width = assets.TILE_LENGTH * self.columns * size_modifier
        canvas_height = assets.TILE_LENGTH * self.rows * size_modifier
        self.configure(width=canvas_width, height=canvas_height)

        for row in self.array:
            for tile in row:
                tile.render(display=display)

    def generate_default(self):
        map = []
        land_tiles = []     # Store land tiles so program can randomly choose one to place apple on
        for row_num in range(self.rows):
            row = []
            for column_num in range(self.columns):
                if row_num == 0 or row_num == self.rows - 1 or column_num == 0 or column_num == self.columns - 1:
                    tile = Tile((column_num, row_num), "barrier", self)
                    row.append(tile)
                else:
                    tile = Tile((column_num, row_num), "land", self)
                    row.append(tile)
                    land_tiles.append(tile)

            map.append(row)

        self.array = map
        self.land = land_tiles

    def generate_plain(self):
        map = []
        land_tiles = []     # Store land tiles so program can randomly choose one to place apple on
        for row_num in range(self.rows):
            row = []
            for column_num in range(self.columns):
                tile = Tile((column_num, row_num), "land", self)
                row.append(tile)
                land_tiles.append(tile)

            map.append(row)
        
        self.array = map
        self.land = land_tiles