# game.py controls as the actual snake game. It does not include, for example, the main menu.

import tkinter as tk
from snake.game import snake_control
from snake.game import apples
from snake.game import tiles

class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.bind("<Key>", self.key_handler)

        # Create Canvas
        canvas_width = master.winfo_screenwidth()
        canvas_height = master.winfo_screenheight()
        self.canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
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