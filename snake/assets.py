# assets.py allows all assets to be represented as python objects.
# They can be imported into other modules and used from there.

from PIL import Image, ImageTk

TILE_LENGTH = 32
SNAKE_HEAD_LENGTH = 24

def load_image(path, height):
    raw_image = Image.open(path)
    aspect_ratio = raw_image.size[0]/raw_image.size[1]
    width = int(height * aspect_ratio)
    resized = raw_image.resize((width, height))
    new_image = ImageTk.PhotoImage(resized)

    return new_image


apple_sprite = load_image("snake/assets/apple.png", SNAKE_HEAD_LENGTH)

snake_head_up = load_image("snake/assets/snake_head_up.png", SNAKE_HEAD_LENGTH)
snake_head_down = load_image("snake/assets/snake_head_down.png", SNAKE_HEAD_LENGTH)
snake_head_left = load_image("snake/assets/snake_head_left.png", SNAKE_HEAD_LENGTH)
snake_head_right = load_image("snake/assets/snake_head_right.png", SNAKE_HEAD_LENGTH)

snake_body_sprite = Image.open("snake/assets/snake_body.png").resize((SNAKE_HEAD_LENGTH, SNAKE_HEAD_LENGTH))
snake_body_sprite = ImageTk.PhotoImage(snake_body_sprite)

wasd_to_start_label = load_image("snake/assets/wasd_to_start_label.png", 50)
you_died_label = load_image("snake/assets/you_died_label.png", 50)

play_again_button = load_image("snake/assets/play_again_button.png", 75)
play_again_button_highlighted = load_image("snake/assets/play_again_button_highlighted.png", 75)
main_menu_button = load_image("snake/assets/main_menu_button.png", 75)
main_menu_button_highlighted = load_image("snake/assets/main_menu_button_highlighted.png", 75)

land_tile = load_image("snake/assets/land_tile.png", TILE_LENGTH)
barrier_tile = load_image("snake/assets/barrier_tile.png", TILE_LENGTH)

