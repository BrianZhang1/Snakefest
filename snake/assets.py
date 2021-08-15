# assets.py allows all assets to be represented as python objects.
# They can be imported into other modules and used from there.

from tkinter import *
from PIL import Image, ImageTk

rect_length = 30
snake_head_length = int(rect_length*0.8)

apple_sprite = Image.open("snake/assets/apple.png").resize((snake_head_length, snake_head_length))
apple_sprite = ImageTk.PhotoImage(apple_sprite)

snake_head_up = Image.open("snake/assets/snake_head_up.png").resize((snake_head_length, snake_head_length))
snake_head_up = ImageTk.PhotoImage(snake_head_up)

snake_head_down = Image.open("snake/assets/snake_head_down.png").resize((snake_head_length, snake_head_length))
snake_head_down = ImageTk.PhotoImage(snake_head_down)

snake_head_left = Image.open("snake/assets/snake_head_left.png").resize((snake_head_length, snake_head_length))
snake_head_left = ImageTk.PhotoImage(snake_head_left)

snake_head_right = Image.open("snake/assets/snake_head_right.png").resize((snake_head_length, snake_head_length))
snake_head_right = ImageTk.PhotoImage(snake_head_right)

snake_body_sprite = Image.open("snake/assets/snake_body.png").resize((snake_head_length, snake_head_length))
snake_body_sprite = ImageTk.PhotoImage(snake_body_sprite)

