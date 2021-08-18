# maps.py is a list of maps that can be used and rendered by other files.

from snake.game.tile import Tile

def default(canvas, rows, columns):
    map = []
    for row_num in range(rows):
        row = []
        for column in range(columns):
            if row_num == 0 or row_num == rows - 1 or column == 0 or column == columns - 1:
                row.append(Tile((row_num, column), "barrier", canvas))
            else:
                row.append(Tile((row_num, column), "land", canvas))
        map.append(row)
    
    return map

def plain(canvas, rows, columns):
    map = []
    for row_num in range(rows):
        row = []
        for column_num in range(columns):
            row.append(Tile((row_num, column_num), "land", canvas))
        map.append(row)
    
    return map