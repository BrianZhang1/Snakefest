# maps.py is a list of maps that can be used and rendered by other files.

from snake.game_classes.tile import Tile

def default(canvas, rows, columns):
    map = []
    land_tiles = []     # Store land tiles so program can randomly choose one to place apple on
    for row_num in range(rows):
        row = []
        for column_num in range(columns):
            if row_num == 0 or row_num == rows - 1 or column_num == 0 or column_num == columns - 1:
                tile = Tile((column_num, row_num), "barrier", canvas)
                row.append(tile)
            else:
                tile = Tile((column_num, row_num), "land", canvas)
                row.append(tile)
                land_tiles.append(tile)

        map.append(row)
    
    return (map, land_tiles)

def plain(canvas, rows, columns):
    map = []
    land_tiles = []     # Store land tiles so program can randomly choose one to place apple on
    for row_num in range(rows):
        row = []
        for column_num in range(columns):
            tile = Tile((column_num, row_num), "land", canvas)
            row.append(tile)
            land_tiles.append(tile)

        map.append(row)
    
    return (map, land_tiles)