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

# snake_control.py creates and controls the snake (head and body)
# It manages movement, growth, and rendering of snake.
# It does not manage collisions of the snake with other objects, those are managed in game.py

from snake.global_helpers import assets, coord_converter

class Snake():
    def __init__(self, canvas, settings, tile_array):
        self.canvas = canvas
        self.settings = settings
        self.tile_array = tile_array
        self.converter = coord_converter.Coord_Converter()
        self.snake_pos = (int(settings["columns"]/2), int(settings["rows"]/2))         # (column, row)/(x, y)

        inital_coords = self.converter.to_raw(self.snake_pos)

        self.direction = 's'      # north, east, south, west
        self.new_direction = 's'

        initial_image = assets.snake_head_down
        if self.direction == 'w':
            initial_image = assets.snake_head_left
        elif self.direction == 'n':
            initial_image = assets.snake_head_up
        elif self.direction == 'e':
            initial_image = assets.snake_head_right

        self.snake_head = self.canvas.create_image(inital_coords, image=initial_image)
        self.previous_moves = []
        self.body = []
        # Index (in self.body) of the last body part of the snake
        self.body_last_index = None

    def update_position(self):
        self.previous_moves.insert(0, self.snake_pos)
        if len(self.previous_moves) - len(self.body) > 1:
            self.previous_moves.pop()

        # Move one tile in the direction the snake faces
        if self.new_direction == 'w':
            self.direction = 'w'
            new_x = self.snake_pos[0] - 1
            new_y = self.snake_pos[1]
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_left)
        elif self.new_direction == 'e':
            self.direction = 'e'
            new_x = self.snake_pos[0] + 1
            new_y = self.snake_pos[1]
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_right)
        elif self.new_direction == 's':
            self.direction = 's'
            new_x = self.snake_pos[0]
            new_y = self.snake_pos[1] + 1
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_down)
        elif self.new_direction == 'n':
            self.direction = 'n'
            new_x = self.snake_pos[0]
            new_y = self.snake_pos[1] - 1
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_up)
        self.snake_pos = (new_x, new_y)

        self.check_bounds()


    # Check bounds. If out of bounds, teleport to opposite side.
    def check_bounds(self):
        if self.snake_pos[0] < 0:
            new_x = self.settings["columns"] - 1
            new_y = self.snake_pos[1]
        elif self.snake_pos[0] > self.settings["columns"] - 1:
            new_x = 0
            new_y = self.snake_pos[1]
        elif self.snake_pos[1] < 0:
            new_x = self.snake_pos[0]
            new_y = self.settings["rows"] - 1
        elif self.snake_pos[1] > self.settings["rows"] - 1:
            new_x = self.snake_pos[0]
            new_y = 0
        else:
            return

        self.snake_pos = (new_x, new_y)
    
    # Doesn't actually redraw, it just changes coords.
    def draw_snake(self):
        # Draw snake head
        self.canvas.coords(self.snake_head, self.converter.to_raw(self.snake_pos))

        # Move last snake body part to front of snake body.
        if len(self.body) > 0:
            # Delete from last tile
            last_snake_part = self.body[self.body_last_index]
            last_snake_part_position = self.converter.to_coord(self.canvas.coords(last_snake_part.id))
            last_snake_part_tile = self.tile_array[last_snake_part_position[1]][last_snake_part_position[0]]
            last_snake_part_index = last_snake_part_tile.is_holding(Snake_Part)
            last_snake_part_tile.drop(last_snake_part_index)

            # Spawn on new tile
            new_tile_coords = self.previous_moves[0]
            new_tile = self.tile_array[new_tile_coords[1]][new_tile_coords[0]]
            new_tile.holding.append(last_snake_part)
            new_tile.render()

            
            if self.body_last_index == 0:
                self.body_last_index = len(self.body) - 1
            else:
                self.body_last_index -= 1



    def create_new_body(self):
        # body_last is the index of the last snake part in the body.
        # A new snake part is inserted after the last snake part, and becomes the last snake part.
        coords = self.previous_moves[len(self.body)]
        new_snake_part = Snake_Part(self.canvas)
        if self.body_last_index != None:
            self.body.insert(self.body_last_index+1, new_snake_part)
            self.body_last_index += 1
        else:
            self.body.append(new_snake_part)
            self.body_last_index = 0
        tile = self.tile_array[coords[1]][coords[0]]
        tile.holding.append(new_snake_part)
        tile.render()
        
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
    