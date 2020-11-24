import tkinter as tk
root = tk.Tk()

import time
import snake_controller
import apples
import game_canvas

class MainApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.bind("<Key>", self.key)
#        self.listener = keyboard.Listener(on_press=self.on_press)
#        self.listener.start()

        # Create Canvas
        canvas_width = root.winfo_screenwidth()
        canvas_height = root.winfo_screenheight()
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

        # Create Objects
        game_canvas.create_grid(self.canvas)
        self.snake = snake_controller.Snake(self.canvas)
        self.apple = apples.Apple(self.canvas)

    # Input Handler
    def key(self, event):
        if event.char == 'w':
            self.snake.snake_direction = 'n'
        elif event.char == 'a':
            self.snake.snake_direction = 'w'
        elif event.char == 's':
            self.snake.snake_direction = 's'
        elif event.char == 'd':
            self.snake.snake_direction = 'e'

    
#    # Create Keyboard Listener
#    def on_press(self, key):
#        try:
#            if key.char == 'w':
#                self.snake.snake_direction = 'n'
#            elif key.char == 'a':
#                self.snake.snake_direction = 'w'
#            elif key.char == 's':
#                self.snake.snake_direction = 's'
#            elif key.char == 'd':
#                self.snake.snake_direction = 'e'
#        except AttributeError:
#            pass



app = MainApp(root)
start_time = time.time()
while True:
    if time.time() - start_time > 0.15:
        start_time = time.time()
        app.snake.move_snake()
        if tuple(app.snake.snake_pos) == app.apple.apple_pos:
            app.apple.apple_pos = app.apple.rand_apple_pos()
            app.snake.create_new_body()

    root.update_idletasks()
    root.update()

