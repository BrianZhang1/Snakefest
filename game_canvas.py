import assets
rows = 17
columns = 17

# Create grid
def create_grid(canvas):
    tile_colour = "khaki"
    for rect_row in range(rows):
        row_coord = 5 + rect_row*(assets.rect_length)
        for rect_column in range(columns):
            column_coord = 5 + rect_column*(assets.rect_length)
            canvas.create_rectangle(column_coord, row_coord, column_coord + assets.rect_length, row_coord + assets.rect_length, fill=tile_colour)
            if tile_colour == "khaki":
                tile_colour = "ivory"
            else:
                tile_colour = "khaki"

