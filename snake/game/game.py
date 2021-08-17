# game.py controls as the actual snake game. It does not include, for example, the main menu.

import tkinter as tk
from snake.game import snake_handler, apple_handler, tiles
from snake import assets

class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.bind("<Key>", self.key_handler)
        self.started = False

        # Create Canvas
        canvas_width = assets.rect_length * tiles.rows + 1
        canvas_height = assets.rect_length * tiles.columns + 1
        # +1 so tile borders aren't cut off.
        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        # Create Objects
        self.tiles = tiles.tiles(self.canvas)
        self.snake = snake_handler.Snake(self.canvas)
        self.apple_handler = apple_handler.Apple_Handler(self.canvas)

        # WASD TO START label
        self.wasd_to_start_label = self.canvas.create_image(
            (canvas_width/2, assets.wasd_to_start_label_height/2 + 10), 
            image=assets.wasd_to_start_label)

    # Input Handler
    def key_handler(self, event):
        if not self.started:
            if event.char == 'w' and self.snake.direction != 's':
                self.snake.new_direction = 'n'
            elif event.char == 'a' and self.snake.direction != 'e':
                self.snake.new_direction = 'w'
            elif event.char == 's' and self.snake.direction != 'n':
                self.snake.new_direction = 's'
            elif event.char == 'd' and self.snake.direction != 'w':
                self.snake.new_direction = 'e'

            self.started = True
            self.canvas.delete(self.wasd_to_start_label)
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
        if not self.snake.move():   # if dead
            self.snake_death_handler()
            return

        if self.snake.snake_pos == self.apple_handler.apple_pos:
            self.apple_handler.randomize_apple_pos()
            self.snake.create_new_body()

        # Loop
        self.after(120, self.update_snake)

    def snake_death_handler(self):
        pass