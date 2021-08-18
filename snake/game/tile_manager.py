# tile_manager.py creates and renders tiles.

from snake import assets
from snake.game import coord_converter

rows = 17
columns = 17

class Tile():
    def __init__(self, position, type):
        self.position = position
        self.type = type
        self.holding = []
    
    def is_holding(self, item):
        if item in self.holding:
            return True
        else:
            return False


class Tile_Manager():
    def __init__(self, canvas):
        # Create grid
        self.canvas = canvas
        self.converter = coord_converter.Coord_Converter()

        # Test tile array
        self.tile_array = []
        for row in range(rows):
            tile_row = []
            for column in range(columns):
                if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
                    tile_row.append(Tile((row, column), "barrier"))
                else:
                    tile_row.append(Tile((row, column), "land"))
            self.tile_array.append(tile_row)
    
    def draw_grid(self):
        # tile_colour = "khaki"
        current_row = 0
        for row in self.tile_array:
            current_column = 0
            for tile in row:
                tile_coords = self.converter.to_raw((current_column, current_row))

                if tile.type == "land":
                    self.canvas.create_image(tile_coords, image=assets.land_tile)
                elif tile.type == "barrier":
                    self.canvas.create_image(tile_coords, image=assets.barrier_tile)

                current_column += 1
            current_row += 1


