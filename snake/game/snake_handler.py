# snake_control.py creates and controls the snake (head and body)
# It manages movement, growth, and rendering

from snake.game import tile_manager, coord_converter
from snake import assets

class Snake():
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_pos = (5, 5)         # (x, y)
        self.converter = coord_converter.Coord_Converter()

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
        self.snake_body = []

    def move(self):
        self.previous_moves.insert(0, self.snake_pos)
        if len(self.previous_moves) - len(self.snake_body) > 1:
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

        if self.check_dead():
            return False    # Dead, exit function

        self.draw_snake_head()

        # Move last snake body part to front of snake body.
        if len(self.snake_body) > 0:
            raw_coords = self.converter.to_raw(self.previous_moves[0])

            self.canvas.coords(self.snake_body[-1], raw_coords)
            self.snake_body.insert(0, self.snake_body[-1])
            self.snake_body.pop()
        
        return True     # Didn't die.

    # Check bounds. If out of bounds, teleport to opposite side.
    def check_bounds(self):
        if self.snake_pos[0] < 0:
            new_x = tile_manager.columns - 1
            new_y = self.snake_pos[1]
        elif self.snake_pos[0] > tile_manager.columns - 1:
            new_x = 0
            new_y = self.snake_pos[1]
        elif self.snake_pos[1] < 0:
            new_x = self.snake_pos[0]
            new_y = tile_manager.rows - 1
        elif self.snake_pos[1] > tile_manager.rows - 1:
            new_x = self.snake_pos[0]
            new_y = 0
        else:
            return

        self.snake_pos = (new_x, new_y)
    
    # Doesn't actually redraw, it just changes coords.
    def draw_snake_head(self):
        self.canvas.coords(self.snake_head, self.converter.to_raw(self.snake_pos))

    def create_new_body(self):
        coords = self.previous_moves[len(self.snake_body)]
        raw_coords = self.converter.to_raw(coords)
        self.snake_body.append(self.canvas.create_image(raw_coords, image=assets.snake_body_sprite))
    
    def check_dead(self):
        for snake_part in self.snake_body:
            if tuple(self.canvas.coords(snake_part)) == self.converter.to_raw(self.snake_pos):
                return True
        return False
