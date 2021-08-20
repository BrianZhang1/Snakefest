# apple.py holds the Apple class.

from snake.global_helpers import assets, coord_converter

class Apple():
    def __init__(self, canvas):
        self.canvas = canvas
        self.rendered = False
        self.id = None
        self.converter = coord_converter.Coord_Converter()

    def render(self, position):
        if not self.rendered:
            raw_position = self.converter.to_raw(position)
            self.id = self.canvas.create_image(raw_position, image=assets.apple_sprite)
            self.rendered = True