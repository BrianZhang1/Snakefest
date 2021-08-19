# tile_manager.py creates and renders tiles.

from snake.game import coord_converter, maps

ROWS = 17
COLUMNS = 17


class Tile_Manager():
    def __init__(self, canvas):
        self.canvas = canvas
        self.converter = coord_converter.Coord_Converter()
        self.map = "default"
        self.tile_array = None
        self.land_tiles = None
        self.ROWS = 17
        self.COLUMNS = 17

        map_return_value = None
        if self.map == "default":
            map_return_value = maps.default(canvas, ROWS, COLUMNS)
        if self.map == "plain":
            map_return_value = maps.plain(canvas, ROWS, COLUMNS)
        self.tile_array = map_return_value[0]
        self.land_tiles = map_return_value[1]
    
    def draw_grid(self):
        current_row = 0
        for row in self.tile_array:
            current_column = 0
            for tile in row:
                tile.render()
                current_column += 1
            current_row += 1


