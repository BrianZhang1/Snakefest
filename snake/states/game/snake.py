# snake_control.py creates and controls the snake (head and body)
# It manages movement, growth, and rendering of snake.
# It does not manage collisions of the snake with other objects, those are managed in game.py

from snake.global_helpers import assets

class Snake():
    def __init__(self, canvas, map_array):
        self.canvas = canvas
        self.rows = len(map_array)
        self.columns = len(map_array[0])
        self.map_array = map_array
        self.snake_pos = (int(self.columns/2), int(self.rows/2))         # (column, row)/(x, y)

        self.direction = 's'      # north, east, south, west
        self.new_direction = self.direction

        initial_tile = map_array[self.snake_pos[1]][self.snake_pos[0]]
        initial_tile.pick_up("snake_head", assets.snake_head_down)

        self.slippery = False
        self.previous_moves = []
        self.body = []
        self.body_last_index = None     # Index (in self.body) of the last body part of the snake

    def update_position(self):
        self.previous_moves.insert(0, self.snake_pos)
        if len(self.previous_moves) - len(self.body) > 1:
            self.previous_moves.pop()

        if not self.slippery:
            # Change direction and move one tile in the direction the snake faces
            if self.new_direction == 'w':
                self.direction = 'w'
                new_x = self.snake_pos[0] - 1
                new_y = self.snake_pos[1]
            elif self.new_direction == 'e':
                self.direction = 'e'
                new_x = self.snake_pos[0] + 1
                new_y = self.snake_pos[1]
            elif self.new_direction == 's':
                self.direction = 's'
                new_x = self.snake_pos[0]
                new_y = self.snake_pos[1] + 1
            elif self.new_direction == 'n':
                self.direction = 'n'
                new_x = self.snake_pos[0]
                new_y = self.snake_pos[1] - 1
        else:
            if self.direction == 'w':
                self.new_direction = 'w'
                new_x = self.snake_pos[0] - 1
                new_y = self.snake_pos[1]
            elif self.direction == 'e':
                self.new_direction = 'e'
                new_x = self.snake_pos[0] + 1
                new_y = self.snake_pos[1]
            elif self.direction == 's':
                self.new_direction = 's'
                new_x = self.snake_pos[0]
                new_y = self.snake_pos[1] + 1
            elif self.direction == 'n':
                self.new_direction = 'n'
                new_x = self.snake_pos[0]
                new_y = self.snake_pos[1] - 1
        self.snake_pos = (new_x, new_y)

        self.check_bounds()


    # Check bounds. If out of bounds, teleport to opposite side.
    def check_bounds(self):
        if self.snake_pos[0] < 0:
            new_x = self.columns - 1
            new_y = self.snake_pos[1]
        elif self.snake_pos[0] > self.columns - 1:
            new_x = 0
            new_y = self.snake_pos[1]
        elif self.snake_pos[1] < 0:
            new_x = self.snake_pos[0]
            new_y = self.rows - 1
        elif self.snake_pos[1] > self.rows - 1:
            new_x = self.snake_pos[0]
            new_y = 0
        else:
            return

        self.snake_pos = (new_x, new_y)
    
    # Doesn't actually redraw, it just changes coords.
    def draw_snake(self):

        # Determine snake image based on direction
        snake_head_image = None
        if self.direction == 'w':
            snake_head_image = assets.snake_head_left
        elif self.direction == 'e':
            snake_head_image = assets.snake_head_right
        elif self.direction == 's':
            snake_head_image = assets.snake_head_down
        elif self.direction == 'n':
            snake_head_image = assets.snake_head_up

        # Drop previous snake head an draw new
        previous_snake_head_tile = self.map_array[self.previous_moves[0][1]][self.previous_moves[0][0]]
        previous_snake_head_tile.drop("snake_head")
        new_snake_head_tile = self.map_array[self.snake_pos[1]][self.snake_pos[0]]
        new_snake_head_tile.pick_up("snake_head", snake_head_image)

        # Move last snake body part to front of snake body.
        if len(self.body) > 0:
            # Delete from last tile
            last_snake_part_position = self.body[self.body_last_index]
            last_snake_part_tile = self.map_array[last_snake_part_position[1]][last_snake_part_position[0]]
            last_snake_part_tile.drop("snake_part")

            # Spawn on new tile
            new_tile_coords = self.previous_moves[0]
            new_tile = self.map_array[new_tile_coords[1]][new_tile_coords[0]]
            new_tile.pick_up("snake_part", assets.snake_body_sprite)

            self.body[self.body_last_index] = new_tile_coords
            
            if self.body_last_index == 0:
                self.body_last_index = len(self.body) - 1
            else:
                self.body_last_index -= 1



    # Turns snake right before it dies
    def turn_snake(self):

        # Determine snake image based on direction
        snake_head_image = None
        if self.direction == 'w':
            snake_head_image = assets.snake_head_left
        elif self.direction == 'e':
            snake_head_image = assets.snake_head_right
        elif self.direction == 's':
            snake_head_image = assets.snake_head_down
        elif self.direction == 'n':
            snake_head_image = assets.snake_head_up

        # Find snake_head and turn it
        current_tile = self.map_array[self.previous_moves[0][1]][self.previous_moves[0][0]]
        for item in current_tile.holding:
            if item["name"] == "snake_head":
                self.canvas.itemconfigure(item["render_id"], image=snake_head_image)


    def create_new_body(self):
        # body_last is the index of the last snake part in the body.
        # A new snake part is inserted after the last snake part, and becomes the last snake part.
        coords = self.previous_moves[len(self.body)]
        if self.body_last_index != None:
            self.body.insert(self.body_last_index+1, coords)
            self.body_last_index += 1
        else:
            self.body.append(coords)
            self.body_last_index = 0
        tile = self.map_array[coords[1]][coords[0]]
        tile.pick_up("snake_part", assets.snake_body_sprite)
    
    def set_slippery(self, mode):
        if mode == True:
            self.slippery = True
        if mode == False:
            self.slippery = False
    