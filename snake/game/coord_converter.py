# Converts raw coordinates to grid coordinates and vice versa.
from snake import assets

class Coord_Converter():
    def __init__(self):

        self.dist_from_origin = assets.snake_head_length/2 + (assets.rect_length - assets.snake_head_length)/2 + 3
        # This formula gives the raw coordinates of (0, 0).
        # Image generation is center-based, so if you give the coords (2, 2) then the
        # centre of the image is located at (2, 2). With tiles, they are top-left based.

    def to_raw(self, coord):
        raw_x = self.dist_from_origin + coord[0] * assets.rect_length
        raw_y = self.dist_from_origin + coord[1] * assets.rect_length
        raw_coord = (raw_x, raw_y)
        return raw_coord
    
    def to_coord(self, raw):
        new_x = (raw[0] - self.dist_from_origin) / assets.rect_length
        new_y = (raw[1] - self.dist_from_origin) / assets.rect_length
        new_coord = (new_x , new_y)
        return new_coord
