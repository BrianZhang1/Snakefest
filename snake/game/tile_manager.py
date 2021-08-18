# tile_manager.py creates and renders tiles.

from snake.game import coord_converter, maps

ROWS = 17
COLUMNS = 17


class Tile_Manager():
    def __init__(self, canvas):
        # Create grid
        self.canvas = canvas
        self.converter = coord_converter.Coord_Converter()

        # Test tile array
        self.tile_array = maps.default(canvas, ROWS, COLUMNS)
    
    def draw_grid(self):
        current_row = 0
        for row in self.tile_array:
            current_column = 0
            for tile in row:
                tile.render()
                current_column += 1
            current_row += 1


