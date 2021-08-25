# Generates map templates

from snake.global_helpers.tile import Tile

def generate_default(rows, columns):
    map = []
    for row_num in range(rows):
        row = []
        for column_num in range(columns):
            if row_num == 0 or row_num == rows - 1 or column_num == 0 or column_num == columns - 1:
                tile = Tile((column_num, row_num), "barrier")
                row.append(tile)
            else:
                tile = Tile((column_num, row_num), "land")
                row.append(tile)

        map.append(row)

    return map

def generate_plain(rows, columns):
    map = []
    for row_num in range(rows):
        row = []
        for column_num in range(columns):
            tile = Tile((column_num, row_num), "land")
            row.append(tile)

        map.append(row)
    
    return map