# game.py controls as the actual snake game. It does not include, for example, the main menu.

import tkinter as tk
from snake.game import snake_control
from snake.game import apples
from snake.game import tiles
from snake import assets

class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.bind("<Key>", self.key_handler)

        # Create Canvas
        canvas_width = assets.rect_length * tiles.rows + 1
        canvas_height = assets.rect_length * tiles.columns + 1
        # +1 so tile borders aren't cut off.
        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        # Create Objects
        self.tiles = tiles.tiles(self.canvas)
        self.snake = snake_control.Snake(self.canvas)
        self.apple = apples.Apple(self.canvas)

    # Input Handler
    def key_handler(self, event):
        if event.char == 'w':
            self.snake.snake_direction = 'n'
        elif event.char == 'a':
            self.snake.snake_direction = 'w'
        elif event.char == 's':
            self.snake.snake_direction = 's'
        elif event.char == 'd':
            self.snake.snake_direction = 'e'