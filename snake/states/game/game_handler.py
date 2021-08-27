#    Snakefest is an extended version of the popular Snake game.
#    Copyright (C) 2021  Brian Zhang
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>

# game.py controls as the actual snake game.
# It does not include, for example, the main menu or tile rendering.
# all classes that help game.py can be found under the snake/game_classes directory

import tkinter as tk
from snake.states.game import snake, apple
from snake.global_helpers import assets, coord_converter, map_class
import random

class Game(tk.Frame):
    def __init__(self, master, play_again, load_main_menu, map_array, speed_modifier):
        super().__init__(master)
        self.master = master
        self.play_again = play_again
        self.load_main_menu = load_main_menu
        self.map_array = map_array
        self.speed_modifier = speed_modifier
        self.bind("<Key>", self.key_handler)
        self.started = False
        self.converter = coord_converter.Coord_Converter()

        # Create Map
        self.map = map_class.Map(self, self.map_array)
        self.map.render()
        self.map.place(anchor="center", relx=0.5, rely=0.5)

        # Find all land tiles in map
        self.land_tiles = []
        for row in self.map.array:
            for tile in row:
                if tile.type == "land":
                    self.land_tiles.append(tile)

        self.snake = snake.Snake(self.map, self.map.array)

        # WASD TO START label
        self.wasd_to_start_label = tk.Label(self, image=assets.wasd_to_start_label)
        self.wasd_to_start_label.place(anchor="center", relx=0.5, rely=0.2)

        # Score label
        self.score_label_text = tk.StringVar()
        self.score_label_text.set("Score: " + str(len(self.snake.body)))
        self.score_label = tk.Label(self, textvariable=self.score_label_text,
            font="Times 20")
        self.score_label.pack(anchor=tk.NW)

        self.pack(expand=True, fill="both")
        self.focus_set()

    # Input Handler
    def key_handler(self, event):
        if not self.started:
            def start_game():
                self.started = True
                self.wasd_to_start_label.destroy()
                del self.wasd_to_start_label
                self.create_new_apple()
                self.update_snake()

            if event.char == 'w':
                self.snake.new_direction = 'n'
                start_game()
            elif event.char == 'a':
                self.snake.new_direction = 'w'
                start_game()
            elif event.char == 's':
                self.snake.new_direction = 's'
                start_game()
            elif event.char == 'd':
                self.snake.new_direction = 'e'
                start_game()

            
        elif self.started:
            if event.char == 'w' and self.snake.direction != 's':
                self.snake.new_direction = 'n'
            elif event.char == 'a' and self.snake.direction != 'e':
                self.snake.new_direction = 'w'
            elif event.char == 's' and self.snake.direction != 'n':
                self.snake.new_direction = 's'
            elif event.char == 'd' and self.snake.direction != 'w':
                self.snake.new_direction = 'e'

    # This loop manages the snake, collisions, and basically the whole playing part of the game
    def update_snake(self):
        self.snake.update_position()

        # Finds the tile object the snake is currently on
        snake_column = self.snake.snake_pos[0]
        snake_row = self.snake.snake_pos[1]
        tile = self.map.array[snake_row][snake_column]

        # Check if snake hit barrier tile
        if tile.type == "barrier" or tile.is_holding(snake.Snake_Part) != None:
            self.snake_death_handler()
            return

        self.snake.draw_snake()

        # Checking if snake hit apple
        apple_index = tile.is_holding(apple.Apple)
        if apple_index != None:
            tile.drop(apple_index)
            self.create_new_apple()
            self.snake.create_new_body()
            self.score_label_text.set("Score: " + str(len(self.snake.body)))

        # Loop
        self.after(int(120/self.speed_modifier), self.update_snake)
    
    def create_new_apple(self):
        # Choose one of the land tiles to spawn an apple on
        land_tiles = self.land_tiles
        random_tile_index = random.randint(0, len(land_tiles)-1)
        random_tile = land_tiles[random_tile_index]

        # Create apple and assign to chosen tile
        new_apple = apple.Apple(self.map)
        random_tile.holding.append(new_apple)
        random_tile.render()

    def snake_death_handler(self, is_first_call=True):

        if is_first_call:
            self.after(750, lambda: self.snake_death_handler(is_first_call=False))

        else:
            bg_color = "lightcyan2"
            self.death_frame = tk.Frame(self, bg=bg_color, pady=30, padx=10)

            self.you_died_label = tk.Label(self.death_frame, image=assets.you_died_label, bg=bg_color)

            final_score_label_text = tk.StringVar()
            final_score_label_text.set("Final Score: " + str(len(self.snake.body)))
            self.final_score_label = tk.Label(self.death_frame, textvariable=final_score_label_text, font="Times 22", bg=bg_color)

            self.play_again_button = tk.Label(self.death_frame, image=assets.play_again_button, bg=bg_color)
            self.play_again_button.bind("<Button-1>", lambda _: self.play_again())
            self.play_again_button.bind("<Enter>", lambda _: 
                self.play_again_button.configure(image=assets.play_again_button_highlighted))
            self.play_again_button.bind("<Leave>", lambda _: 
                self.play_again_button.configure(image=assets.play_again_button))

            self.main_menu_button = tk.Label(self.death_frame, image=assets.main_menu_button, bg=bg_color)
            self.main_menu_button.bind("<Button-1>", lambda _: self.load_main_menu())
            self.main_menu_button.bind("<Enter>", lambda _: 
                self.main_menu_button.configure(image=assets.main_menu_button_highlighted))
            self.main_menu_button.bind("<Leave>", lambda _: 
                self.main_menu_button.configure(image=assets.main_menu_button))

            self.you_died_label.pack()
            self.final_score_label.pack(pady=(0, 30))
            self.play_again_button.pack()
            self.main_menu_button.pack()

            self.death_frame.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
