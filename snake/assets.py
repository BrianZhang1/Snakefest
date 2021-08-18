# assets.py allows all assets to be represented as python objects.
# They can be imported into other modules and used from there.

from tkinter import *
from PIL import Image, ImageTk

tile_length = 32
snake_head_length = 24

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

wasd_to_start_label = Image.open("snake/assets/wasd_to_start_label.png")
wasd_to_start_label_aspect_ratio = wasd_to_start_label.size[0]/wasd_to_start_label.size[1]
wasd_to_start_label_height = 50
wasd_to_start_label_width = int(wasd_to_start_label_height * wasd_to_start_label_aspect_ratio)
wasd_to_start_label_resized = wasd_to_start_label.resize((wasd_to_start_label_width, wasd_to_start_label_height))
wasd_to_start_label = ImageTk.PhotoImage(wasd_to_start_label_resized)

land_tile = Image.open("snake/assets/land_tile.png").resize((tile_length, tile_length))
land_tile = ImageTk.PhotoImage(land_tile)
barrier_tile = Image.open("snake/assets/barrier_tile.png").resize((tile_length, tile_length))
barrier_tile = ImageTk.PhotoImage(barrier_tile)