# snake_part.py holds the class for Snake_Part.
# Snake.body[] is filled with these Snake_Parts.

from snake.game import coord_converter
from snake import assets

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

        