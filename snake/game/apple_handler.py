# apples.py creates and renders apples.

from snake.game import tile_manager, coord_converter
from snake import assets
import random

class Apple_Handler():
    def __init__(self, canvas):
        self.canvas = canvas
        self.converter = coord_converter.Coord_Converter()
        self.apple = canvas.create_image((0, 0), image=assets.apple_sprite)
        self.randomize_apple_pos()

    def randomize_apple_pos(self):
        x = random.randint(0, tile_manager.columns - 1)
        y = random.randint(0, tile_manager.rows - 1)
        self.apple_pos = (x, y)
        self.canvas.coords(self.apple, self.converter.to_raw(self.apple_pos))
        return self.apple_pos

