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

# map_class.py holds the Map class, which is used for the game.
# It is also used as a display during map selection and creation.
# Below the Map class is the Tile class.
# The map is comprised of many Tile objects.

import tkinter as tk
from snake.global_helpers import assets, coord_converter

class Map(tk.Canvas):
    def __init__(self, master, map_array):
        super().__init__(master)
        self.rows = len(map_array)
        self.columns = len(map_array[0])

        self.array = []
        for row in map_array:
            new_row = []
            for tile_info in row:
                new_tile = Tile(tile_info)
                new_row.append(new_tile)
            self.array.append(new_row)

    def render(self, display=False):
        size_modifier = 1
        if display:
            size_modifier = assets.DISPLAY_SHRINK

        canvas_width = assets.TILE_LENGTH * self.columns * size_modifier
        canvas_height = assets.TILE_LENGTH * self.rows * size_modifier
        self.configure(width=canvas_width, height=canvas_height)

        for row in self.array:
            for tile in row:
                tile.set_canvas(self)
                tile.render(display=display)



# Map are made of Tile objects
class Tile():
    def __init__(self, info):
        self.type = info["type"]
        self.position = info["position"]
        self.holding = info["holding"]

        self.canvas = None
        self.rendered = False
        self.id = None
        self.converter = coord_converter.Coord_Converter()

    def set_canvas(self, canvas):
        self.rendered = False
        self.canvas = canvas
    
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
            
    # Only renders tile type
    def render_type(self, display=False):
        if not display:
            land_tile = assets.land_tile
            barrier_tile = assets.barrier_tile
        else:
            land_tile = assets.land_tile_display
            barrier_tile = assets.barrier_tile_display

        if self.type == "land":
            self.canvas.itemconfigure(self.id, image=land_tile)
        elif self.type == "barrier":
            self.canvas.itemconfigure(self.id, image=barrier_tile)

    
    # Removes item from holding and deletes on canvas
    def drop(self, item_index):
        item = self.holding[item_index]
        if item.rendered:
            self.canvas.delete(item.id)
            item.rendered = False
        self.holding.pop(item_index)

    # Returns important tile data in record form
    def get_info(self):
        info = {
            "type": self.type,
            "position": self.position,
            "holding": self.holding
        }

        return info