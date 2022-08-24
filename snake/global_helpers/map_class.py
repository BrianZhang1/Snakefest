# map_class.py holds the Map class, which is used for the game.
# It is also used as a display during map selection and creation.
# Below the Map class is the Tile class.
# The map is comprised of many Tile objects.

import tkinter as tk

from snake.global_helpers import assets

class Map(tk.Canvas):
    def __init__(self, master, map_array, display=False):
        super().__init__(master)
        self.rows = len(map_array)
        self.columns = len(map_array[0])
        self.display = display

        self.array = []
        for row in map_array:
            new_row = []
            for tile_info in row:
                new_tile = Tile(tile_info, self, display=self.display)
                new_row.append(new_tile)
            self.array.append(new_row)

    def render(self):
        size_modifier = 1
        if self.display:
            size_modifier = assets.DISPLAY_SHRINK

        canvas_width = assets.TILE_LENGTH * self.columns * size_modifier
        canvas_height = assets.TILE_LENGTH * self.rows * size_modifier
        self.configure(width=canvas_width, height=canvas_height)

        for row in self.array:
            for tile in row:
                tile.render()



# Maps are arrays of Tile objects
class Tile():
    def __init__(self, info, canvas, display):

        self.type = info["type"]
        self.position = info["position"]
        holding = info["holding"]
        self.canvas = canvas
        self.display = display

        self.holding = []
        for item in holding:
            self.holding.append({
                "name": item,
                "render_id": None,
            })

        self.raw_position = self.get_raw_position()
        self.rendered = False
        self.id = None


    # Returns index if holding, and None if not holding
    def is_holding(self, query):
        index = 0
        for item in self.holding:
            if item["name"] == query:
                return index
            index += 1

        return None
    

    # Renders tile
    def render(self):

        if not self.rendered:
            self.render_type()
            self.render_holding()
            
            self.rendered = True
        elif self.rendered:
            self.render_holding()
    

    # Renders items in self.holding
    def render_holding(self):
        for item in self.holding:
            if item["render_id"] == None:
                item["render_id"] = self.canvas.create_image(self.raw_position, image=item["image"])

            
    # Renders tile type
    def render_type(self):

        if not self.display:
            land_tile = assets.land_tile
            barrier_tile = assets.barrier_tile
            ice_tile = assets.ice_tile
        else:
            land_tile = assets.land_tile_display
            barrier_tile = assets.barrier_tile_display
            ice_tile = assets.ice_tile_display

        if self.id == None:
            if self.type == "land":
                self.id = self.canvas.create_image(self.raw_position, image=land_tile)
            elif self.type == "barrier":
                self.id = self.canvas.create_image(self.raw_position, image=barrier_tile)
            elif self.type == "ice":
                self.id = self.canvas.create_image(self.raw_position, image=ice_tile)
        else:
            if self.type == "land":
                self.canvas.itemconfigure(self.id, image=land_tile)
            elif self.type == "barrier":
                self.canvas.itemconfigure(self.id, image=barrier_tile)
            elif self.type == "ice":
                self.canvas.itemconfigure(self.id, image=ice_tile)

    
    # Removes item from holding and deletes on canvas
    def drop(self, item_name):

        item_index = self.is_holding(item_name)
        if item_index == None:
            print("can't drop item, tile isn't holding it")
            return

        item = self.holding[item_index]
        if item["render_id"] != None:
            self.canvas.delete(item["render_id"])
            item["render_id"] = None
        self.holding.pop(item_index)
    

    # Adds item to holding and renders on canvas
    def pick_up(self, item_name, image):

        self.holding.append({
            "name": item_name,
            "image": image,
            "render_id": None
        })
        self.render_holding()


    # Returns important tile data in record form
    def get_info(self):
        info = {
            "type": self.type,
            "position": self.position,
            "holding": self.holding
        }

        return info
    

    def get_raw_position(self):

        # Calculate margin
        margin = None
        if not self.display:
            margin = assets.TILE_LENGTH/2 + 2
        else:
            margin = (assets.TILE_LENGTH*assets.DISPLAY_SHRINK)/2 + 2
        # +2 to make sure all tile borders aren't cut off

        # Find tile_length
        tile_length = None
        if not self.display:
            tile_length = assets.TILE_LENGTH
        else:
            tile_length = assets.TILE_LENGTH * assets.DISPLAY_SHRINK

        raw_x = margin + self.position[0] * tile_length
        raw_y = margin + self.position[1] * tile_length
        return (raw_x, raw_y)
