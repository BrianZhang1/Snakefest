# snake_control.py creates and controls the snake (head and body)
# It manages movement, growth, and rendering

from snake.game import tiles
from snake import assets

class Snake():
    dist_from_origin = assets.snake_head_length/2 + (assets.rect_length - assets.snake_head_length)/2 + 3
    # Image generation is center-based, so if you give the coords (2, 2) then the
    # centre is located at (2, 2). With tiles, they are top-left based. This formula
    # aligns the tiles with the snake.
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_head = self.canvas.create_image((self.dist_from_origin, self.dist_from_origin), image=assets.snake_head_right)
        self.snake_pos = (0, 0)         # (x, y)
        self.snake_direction = 'e'      # north, east, south, west
        self.previous_moves = []
        self.snake_body = []

    def move(self):
        self.previous_moves.insert(0, self.snake_pos)
        if len(self.previous_moves) - len(self.snake_body) > 1:
            self.previous_moves.pop()

        # Move one tile in the direction the snake faces
        if self.snake_direction == 'w':
            new_x = self.snake_pos[0] - 1
            new_y = self.snake_pos[1]
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_left)
        elif self.snake_direction == 'e':
            new_x = self.snake_pos[0] + 1
            new_y = self.snake_pos[1]
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_right)
        elif self.snake_direction == 's':
            new_x = self.snake_pos[0]
            new_y = self.snake_pos[1] + 1
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_down)
        elif self.snake_direction == 'n':
            new_x = self.snake_pos[0]
            new_y = self.snake_pos[1] - 1
            self.canvas.itemconfig(self.snake_head, image=assets.snake_head_up)
        self.snake_pos = (new_x, new_y)

        self.check_bounds()


        self.draw_snake_head()

        # Move last snake body part to front of snake body.
        if len(self.snake_body) > 0:
            new_coords_x = self.previous_moves[0][0]*assets.rect_length + self.dist_from_origin
            new_coords_y = self.previous_moves[0][1]*assets.rect_length + self.dist_from_origin
            new_coords = (new_coords_x, new_coords_y)

            self.canvas.coords(self.snake_body[-1], (new_coords))
            self.snake_body.insert(0, self.snake_body[-1])
            self.snake_body.pop()

    # Check bounds. If out of bounds, teleport to opposite side.
    def check_bounds(self):
        if self.snake_pos[0] < 0:
            new_x = tiles.columns - 1
            new_y = self.snake_pos[1]
        elif self.snake_pos[0] > tiles.columns - 1:
            new_x = 0
            new_y = self.snake_pos[1]
        elif self.snake_pos[1] < 0:
            new_x = self.snake_pos[0]
            new_y = tiles.rows - 1
        elif self.snake_pos[1] > tiles.rows - 1:
            new_x = self.snake_pos[0]
            new_y = 0
        else:
            return

        self.snake_pos = (new_x, new_y)
    
    # Doesn't actually redraw, it just changes coords.
    def draw_snake_head(self):
        new_x_coord = self.dist_from_origin + self.snake_pos[0]*assets.rect_length
        new_y_coord = self.dist_from_origin + self.snake_pos[1]*assets.rect_length
        self.canvas.coords(self.snake_head, (new_x_coord, new_y_coord))

    def create_new_body(self):
        column = self.previous_moves[len(self.snake_body)][0]
        row = self.previous_moves[len(self.snake_body)][1]
        new_coords_x = self.dist_from_origin + column*assets.rect_length
        new_coords_y = self.dist_from_origin + row*assets.rect_length
        new_coords = (new_coords_x, new_coords_y)
        self.snake_body.append(self.canvas.create_image(new_coords, image=assets.snake_body_sprite))

