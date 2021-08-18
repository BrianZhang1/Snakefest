# tile.py holds the Tile class

from snake.game import coord_converter, apple
from snake import assets

class Tile():
    def __init__(self, position, type, canvas):
        self.canvas = canvas
        self.position = position
        self.type = type
        self.holding = []
        self.rendered = False
        self.converter = coord_converter.Coord_Converter()
    
    # Returns index if holding, and None if not holding
    def is_holding(self, query):
        index = 0
        for item in self.holding:
            if type(item) == query:
                return index
            index += 1

        return None
    
    # Renders tile
    def render(self):
        if not self.rendered:
            tile_coords = self.converter.to_raw(self.position)

            if self.type == "land":
                self.canvas.create_image(tile_coords, image=assets.land_tile)
            elif self.type == "barrier":
                self.canvas.create_image(tile_coords, image=assets.barrier_tile)
            
            self.rendered = True
        else:
            apple_index = self.is_holding(apple.Apple)
            if apple_index != None:
                self.holding[apple_index].render(self.position)
    
    # Removes item from holding and deletes on canvas
    def drop(self, item_index):
        item = self.holding[item_index]
        if item.rendered:
            self.canvas.delete(item.id)
        self.holding.pop(item_index)