# Converts raw coordinates to grid coordinates and vice versa.

from snake.global_helpers import assets

class Coord_Converter():
    def __init__(self, display=False):
        self.display = display

        self.margin = None
        if not display:
            self.margin = assets.TILE_LENGTH/2 + 2
        else:
            self.margin = (assets.TILE_LENGTH*assets.DISPLAY_SHRINK)/2 + 2
        # +2 to make sure all tile borders aren't cut off

    def to_raw(self, coord):
        tile_length = None
        if not self.display:
            tile_length = assets.TILE_LENGTH
        else:
            tile_length = assets.TILE_LENGTH * assets.DISPLAY_SHRINK

        raw_x = self.margin + coord[0] * tile_length
        raw_y = self.margin + coord[1] * tile_length
        raw_coord = (raw_x, raw_y)
        return raw_coord
    
    def to_coord(self, raw):
        tile_length = None
        if not self.display:
            tile_length = assets.TILE_LENGTH
        else:
            tile_length = assets.TILE_LENGTH * assets.DISPLAY_SHRINK
        new_x = int((raw[0] - self.margin) / tile_length)
        new_y = int((raw[1] - self.margin) / tile_length)
        new_coord = (new_x , new_y)
        return new_coord
