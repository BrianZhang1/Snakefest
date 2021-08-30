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

# Holds the Snake_Part class which comprises the body of the snake.

from snake.global_helpers import coord_converter, assets

class Snake_Part():
    def __init__(self, canvas):
        self.canvas = canvas
        self.rendered = False
        self.id = None
        self.converter = coord_converter.Coord_Converter()

    def render(self, position):
        raw_position = self.converter.to_raw(position)
        if not self.rendered:
            self.id = self.canvas.create_image(raw_position, image=assets.snake_body_sprite)
            self.rendered = True
        else:
            self.canvas.coords(self.id, raw_position)