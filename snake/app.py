import tkinter as tk
root = tk.Tk()
import time
from snake.game import game as game_    # trailing _ to avoid name conflicts

def run():
    # Initialize important objects
    game = game_.Game(root)

    # Event loop
    start_time = time.time()
    while True:
        if time.time() - start_time > 0.12:
            start_time = time.time()
            game.snake.move_snake()
            if tuple(game.snake.snake_pos) == game.apple.apple_pos:
                game.apple.apple_pos = game.apple.rand_apple_pos()
                game.snake.create_new_body()

        root.update_idletasks()
        root.update()

