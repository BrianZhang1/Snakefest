# game.py controls as the actual snake game.
# It does not include, for example, the main menu or tile rendering.

import tkinter as tk
from typing import final
from snake.game import snake_handler, apple, tile_manager, coord_converter
from snake import assets
import random

class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.bind("<Key>", self.key_handler)
        self.started = False
        self.converter = coord_converter.Coord_Converter()

        # Create Canvas
        canvas_width = assets.TILE_LENGTH * tile_manager.COLUMNS
        canvas_height = assets.TILE_LENGTH * tile_manager.ROWS
        self.canvas_dimensions = (canvas_width, canvas_height)
        # +1 so tile borders aren't cut off.
        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.pack(side=tk.BOTTOM)

        self.tile_manager = tile_manager.Tile_Manager(self.canvas)
        self.tile_manager.draw_grid()

        self.snake = snake_handler.Snake(self.canvas, tile_manager.ROWS, tile_manager.COLUMNS)

        # WASD TO START label
        self.wasd_to_start_label = self.canvas.create_image(
            (self.canvas_dimensions[0]/2, assets.wasd_to_start_label_height/2 + 40), 
            image=assets.wasd_to_start_label)

        # Score label
        self.score_label_text = tk.StringVar()
        self.score_label_text.set("Score: " + str(len(self.snake.body)))
        self.score_label = tk.Label(self, textvariable=self.score_label_text,
            font="Times 20")
        self.score_label.pack(anchor=tk.NW)

    # Input Handler
    def key_handler(self, event):
        if not self.started:
            if event.char == 'w':
                self.snake.new_direction = 'n'
            elif event.char == 'a':
                self.snake.new_direction = 'w'
            elif event.char == 's':
                self.snake.new_direction = 's'
            elif event.char == 'd':
                self.snake.new_direction = 'e'

            self.started = True
            self.canvas.delete(self.wasd_to_start_label)
            del self.wasd_to_start_label
            self.create_new_apple()
            self.update_snake()
            
        elif self.started:
            if event.char == 'w' and self.snake.direction != 's':
                self.snake.new_direction = 'n'
            elif event.char == 'a' and self.snake.direction != 'e':
                self.snake.new_direction = 'w'
            elif event.char == 's' and self.snake.direction != 'n':
                self.snake.new_direction = 's'
            elif event.char == 'd' and self.snake.direction != 'w':
                self.snake.new_direction = 'e'

    def update_snake(self):
        self.snake.update_position()

        if self.snake_is_dead():   # if dead
            self.snake_death_handler()
            return
        else:
            self.snake.draw_snake()

        # Checking if snake hit apple
        snake_column = self.snake.snake_pos[0]
        snake_row = self.snake.snake_pos[1]
        tile = self.tile_manager.tile_array[snake_row][snake_column]
        apple_index = tile.is_holding(apple.Apple)
        if apple_index != None:
            tile.drop(apple_index)
            self.create_new_apple()
            self.snake.create_new_body()
            self.score_label_text.set("Score: " + str(len(self.snake.body)))

        # Loop
        self.after(120, self.update_snake)
    
    def create_new_apple(self):
        # Choose one of the land tiles to spawn an apple on
        land_tiles = self.tile_manager.land_tiles
        random_tile_index = random.randint(0, len(land_tiles)-1)
        random_tile = land_tiles[random_tile_index]

        # Create apple and assign to chosen tile
        new_apple = apple.Apple(self.canvas)
        random_tile.holding.append(new_apple)
        random_tile.render()

    def snake_is_dead(self):

        raw_snake_pos = self.converter.to_raw(self.snake.snake_pos)

        # Check if snake hit itself
        for snake_part in self.snake.body:
            if tuple(self.canvas.coords(snake_part)) == raw_snake_pos:
                return True

        # Check if snake hit barrier
        snake_column = self.snake.snake_pos[0]
        snake_row = self.snake.snake_pos[1]
        tile = self.tile_manager.tile_array[snake_row][snake_column]
        if tile.type == "barrier":
            return True

        return False

    def snake_death_handler(self):
        distance_from_top = 100
        distance_between = 30
        def display_you_died_label(self):
            self.you_died_label = self.canvas.create_image(
                (self.canvas_dimensions[0]/2, assets.you_died_label_height/2 + distance_from_top), 
                image=assets.you_died_label)
            self.after(1000, lambda: display_the_rest(self))

        def display_the_rest(self):
            self.play_again_button = self.canvas.create_image(self.canvas_dimensions[0]/2,
                assets.you_died_label_height + assets.play_again_button_height/2 + distance_from_top + distance_between,
                image = assets.play_again_button)

            self.main_menu_button = self.canvas.create_image(self.canvas_dimensions[0]/2,
                assets.you_died_label_height + assets.play_again_button_height + assets.main_menu_button_height/2 + distance_from_top + distance_between*2,
                image = assets.main_menu_button)
            
            def play_again_button_on_click(self):
                pass

            def play_again_button_on_enter(self):
                self.canvas.itemconfig(self.play_again_button, image=assets.play_again_button_highlighted)

            def play_again_button_on_leave(self):
                self.canvas.itemconfig(self.play_again_button, image=assets.play_again_button)

            def main_menu_button_on_click(self):
                pass

            def main_menu_button_on_enter(self):
                self.canvas.itemconfig(self.main_menu_button, image=assets.main_menu_button_highlighted)

            def main_menu_button_on_leave(self):
                self.canvas.itemconfig(self.main_menu_button, image=assets.main_menu_button)

            self.canvas.tag_bind(self.play_again_button, "<Button-1>", lambda _: play_again_button_on_click(self))
            self.canvas.tag_bind(self.play_again_button, "<Enter>", lambda _: play_again_button_on_enter(self))
            self.canvas.tag_bind(self.play_again_button, "<Leave>", lambda _: play_again_button_on_leave(self))
            self.canvas.tag_bind(self.main_menu_button, "<Button-1>", lambda _: main_menu_button_on_click(self))
            self.canvas.tag_bind(self.main_menu_button, "<Enter>", lambda _: main_menu_button_on_enter(self))
            self.canvas.tag_bind(self.main_menu_button, "<Leave>", lambda _: main_menu_button_on_leave(self))

        self.after(1000, lambda: display_you_died_label(self))