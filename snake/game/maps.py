# maps.py is a list of maps that can be used and rendered by other files.

from snake.game.tile import Tile

def default(canvas, rows, columns):
    map = []
    land_tiles = []     # Store land tiles so program can randomly choose one to place apple on
    for row_num in range(rows):
        row = []
        for column in range(columns):
            if row_num == 0 or row_num == rows - 1 or column == 0 or column == columns - 1:
                tile = Tile((row_num, column), "barrier", canvas)
                row.append(tile)
            else:
                tile = Tile((row_num, column), "land", canvas)
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
            tile = Tile((row_num, column_num), "land", canvas)
            row.append(tile)
            land_tiles.append(tile)

        map.append(row)
    
    return (map, land_tiles)