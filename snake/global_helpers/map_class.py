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
from snake.global_helpers import assets

class Map(tk.Canvas):
    def __init__(self, master, map_array):
        super().__init__(master)
        self.array = map_array
        self.rows = len(map_array)
        self.columns = len(map_array[0])

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
