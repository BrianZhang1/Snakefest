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

# Converts raw coordinates to grid coordinates and vice versa.

from snake.global_helpers import assets

class Coord_Converter():
    def __init__(self, display=False):
        self.display = display

        self.margin = None
        if not display:
            self.margin = assets.TILE_LENGTH/2 + 2
        else:
            self.margin = (assets.TILE_LENGTH*assets.DISPLAY_SHRINK)/2 + 2
        # +2 to make sure all tile borders aren't cut off

    def to_raw(self, coord):
        tile_length = None
        if not self.display:
            tile_length = assets.TILE_LENGTH
        else:
            tile_length = assets.TILE_LENGTH * assets.DISPLAY_SHRINK

        raw_x = self.margin + coord[0] * tile_length
        raw_y = self.margin + coord[1] * tile_length
        raw_coord = (raw_x, raw_y)
        return raw_coord
    
    def to_coord(self, raw):
        tile_length = None
        if not self.display:
            tile_length = assets.TILE_LENGTH
        else:
            tile_length = assets.TILE_LENGTH * assets.DISPLAY_SHRINK
        new_x = int((raw[0] - self.margin) / tile_length)
        new_y = int((raw[1] - self.margin) / tile_length)
        new_coord = (new_x , new_y)
        return new_coord
