# Converts raw coordinates to grid coordinates and vice versa.

from snake import assets

class Coord_Converter():
    def __init__(self):
        self.margin = assets.tile_length/2 + 2
        # +2 to make sure all tile borders aren't cut off

    def to_raw(self, coord):
        raw_x = self.margin + coord[0] * assets.tile_length
        raw_y = self.margin + coord[1] * assets.tile_length
        raw_coord = (raw_x, raw_y)
        return raw_coord
    
    def to_coord(self, raw):
        new_x = (raw[0] - self.margin) / assets.tile_length
        new_y = (raw[1] - self.margin) / assets.tile_length
        new_coord = (new_x , new_y)
        return new_coord
