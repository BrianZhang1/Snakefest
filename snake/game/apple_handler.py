# apples.py creates and renders apples.

from snake.game import tiles
from snake import assets
import random

class Apple():
    dist_from_origin = assets.snake_head_length/2 + (assets.rect_length - assets.snake_head_length)/2 + 3
    # Image generation is center-based, so if you give the coords (2, 2) then the
    # centre is located at (2, 2). With tiles, they are top-left based. This formula
    # aligns the tiles with the apples.

    def __init__(self, canvas):
        self.canvas = canvas
        self.apple = canvas.create_image((self.dist_from_origin, self.dist_from_origin), image=assets.apple_sprite)
        self.apple_pos = self.rand_apple_pos()

    def rand_apple_pos(self):
        x = random.randint(1, tiles.columns)
        y = random.randint(1, tiles.rows)
        return self.set_apple_pos(x, y)

    def set_apple_pos(self, x, y):
        self.apple_pos = (x - 1, y - 1)
        apple_x = self.dist_from_origin + self.apple_pos[0]*assets.rect_length
        apple_y = self.dist_from_origin + self.apple_pos[1]*assets.rect_length
        self.canvas.coords(self.apple, (apple_x, apple_y))
        return self.apple_pos

