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

# Generates map templates

from snake.global_helpers.tile import Tile

def generate_default(rows, columns):
    map = []
    for row_num in range(rows):
        row = []
        for column_num in range(columns):
            if row_num == 0 or row_num == rows - 1 or column_num == 0 or column_num == columns - 1:
                tile = Tile((column_num, row_num), "barrier")
                row.append(tile)
            else:
                tile = Tile((column_num, row_num), "land")
                row.append(tile)

        map.append(row)

    return map

def generate_plain(rows, columns):
    map = []
    for row_num in range(rows):
        row = []
        for column_num in range(columns):
            tile = Tile((column_num, row_num), "land")
            row.append(tile)

        map.append(row)
    
    return map
