# tile_manager.py creates and renders tiles.

from snake import assets
rows = 17
columns = 17

class Tile_Manager():
    def __init__(self, canvas):
        # Create grid
        tile_colour = "khaki"
        for rect_row in range(rows):
            row_coord = rect_row*(assets.rect_length) + 2
            # +2 is to show border. Without it, top and left borders are cut off.
            for rect_column in range(columns):
                column_coord = rect_column*(assets.rect_length) + 2
                # +2 is to show border. Without it, top and left borders are cut off.
                canvas.create_rectangle(column_coord, row_coord, column_coord + assets.rect_length, row_coord + assets.rect_length, fill=tile_colour)

