# tile.py holds the Tile class
# Maps are all made of Tile objects

from snake.global_helpers import coord_converter, assets

class Tile():
    def __init__(self, position, type):
        self.canvas = None
        self.position = position
        self.type = type
        self.holding = []
        self.rendered = False
        self.id = None
        self.converter = coord_converter.Coord_Converter()

    def set_canvas(self, canvas):
        self.rendered = False
        self.canvas = canvas
    
    # Returns index if holding, and None if not holding
    def is_holding(self, query):
        index = 0
        for item in self.holding:
            if type(item) == query:
                return index
            index += 1

        return None
    
    # Renders tile
    def render(self, display=False):
        if not self.rendered:
            tile_coords = None
            land_tile = None
            barrier_tile = None
            if not display:
                tile_coords = self.converter.to_raw(self.position)
                land_tile = assets.land_tile
                barrier_tile = assets.barrier_tile
            else:
                display_converter = coord_converter.Coord_Converter(display=True)
                tile_coords = display_converter.to_raw(self.position)
                land_tile = assets.land_tile_display
                barrier_tile = assets.barrier_tile_display

            if self.type == "land":
                self.id = self.canvas.create_image(tile_coords, image=land_tile)
            elif self.type == "barrier":
                self.id = self.canvas.create_image(tile_coords, image=barrier_tile)
            
            self.rendered = True
        elif self.rendered and not display:
            for item in self.holding:
                item.render(self.position)
            
    # Only renders tile type
    def render_type(self, display=False):
        if not display:
            land_tile = assets.land_tile
            barrier_tile = assets.barrier_tile
        else:
            land_tile = assets.land_tile_display
            barrier_tile = assets.barrier_tile_display

        if self.type == "land":
            self.canvas.itemconfigure(self.id, image=land_tile)
        elif self.type == "barrier":
            self.canvas.itemconfigure(self.id, image=barrier_tile)

    
    # Removes item from holding and deletes on canvas
    def drop(self, item_index):
        item = self.holding[item_index]
        if item.rendered:
            self.canvas.delete(item.id)
            item.rendered = False
        self.holding.pop(item_index)