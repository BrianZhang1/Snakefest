from snake.game.tiles import rows, columns
from snake.assets import snake_body_sprite, snake_head_up, snake_head_down, snake_head_left, snake_head_right, rect_length

class Snake():
    dist_from_origin = 5.5 + rect_length/2
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_head = self.canvas.create_image((self.dist_from_origin, self.dist_from_origin), image=snake_head_right)
        self.snake_pos = [0, 0]
        self.snake_direction = 'e'
        self.previous_moves = []
        self.snake_body = []

    def move_snake(self):
        if self.snake_direction == 'w':
            self.snake_pos[0] -= 1
            self.canvas.itemconfig(self.snake_head, image=snake_head_left)
        elif self.snake_direction == 'e':
            self.snake_pos[0] += 1
            self.canvas.itemconfig(self.snake_head, image=snake_head_right)
        elif self.snake_direction == 's':
            self.snake_pos[1] += 1
            self.canvas.itemconfig(self.snake_head, image=snake_head_down)
        elif self.snake_direction == 'n':
            self.snake_pos[1] -= 1
            self.canvas.itemconfig(self.snake_head, image=snake_head_up)

        self.check_bounds(self.snake_pos)

        new_x = self.dist_from_origin + self.snake_pos[0]*rect_length
        new_y = self.dist_from_origin + self.snake_pos[1]*rect_length

        self.canvas.coords(self.snake_head, (new_x, new_y))
        self.previous_moves.insert(0, tuple(self.snake_pos))

        if len(self.previous_moves) - len(self.snake_body) > 2:
            self.previous_moves.pop()

        if len(self.snake_body) > 0:
            new_coords_x = self.previous_moves[1][0]*rect_length + self.dist_from_origin
            new_coords_y = self.previous_moves[1][1]*rect_length + self.dist_from_origin
            new_coords = (new_coords_x, new_coords_y)

            self.canvas.coords(self.snake_body[-1], (new_coords))
            self.snake_body.insert(0, self.snake_body[-1])
            self.snake_body.pop()

    def check_bounds(self, snake_pos):
        # Bound Checking
        if snake_pos[0] < 0:
            self.snake_pos[0] = columns - 1
        elif snake_pos[0] > columns - 1:
            snake_pos[0] = 0;
        elif self.snake_pos[1] < 0:
            snake_pos[1] = rows - 1
        elif self.snake_pos[1] > rows - 1:
            snake_pos[1] = 0

    # Check if snake hits itself
#    def check_intercept(self, snake_pos):
#        for body in snake_pos:
#            if 

    def create_new_body(self):
        column = self.previous_moves[len(self.snake_body) + 1][0]
        row = self.previous_moves[len(self.snake_body) + 1][1]
        new_coords_x = self.dist_from_origin + column*rect_length
        new_coords_y = self.dist_from_origin + row*rect_length
        new_coords = (new_coords_x, new_coords_y)
        self.snake_body.append(self.canvas.create_image(new_coords, image=snake_body_sprite))

