# assets.py allows all assets to be represented as python objects.
# They can be imported into other modules and used from there.

from PIL import Image, ImageTk

SCREEN_GEOMETRY = (1280, 720)
TILE_LENGTH = 32
SNAKE_HEAD_LENGTH = 24
DISPLAY_SHRINK = 3/4        # ratio to shrink when displaying in map select
TILE_BUTTON_LENGTH = 20     # length of tile buttons in map creator

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
snake_body_sprite = load_image("snake/assets/snake_body.png", SNAKE_HEAD_LENGTH)

wasd_to_start_label = load_image("snake/assets/wasd_to_start_label.png", 50)
you_died_label = load_image("snake/assets/you_died_label.png", 50)

play_again_button = load_image("snake/assets/play_again_button.png", 75)
play_again_button_highlighted = load_image("snake/assets/play_again_button_highlighted.png", 75)
main_menu_button = load_image("snake/assets/main_menu_button.png", 75)
main_menu_button_highlighted = load_image("snake/assets/main_menu_button_highlighted.png", 75)

land_tile = load_image("snake/assets/land_tile.png", TILE_LENGTH)
barrier_tile = load_image("snake/assets/barrier_tile.png", TILE_LENGTH)
ice_tile = load_image("snake/assets/ice_tile.png", TILE_LENGTH)

land_tile_display = load_image("snake/assets/land_tile.png", int(TILE_LENGTH*DISPLAY_SHRINK))
barrier_tile_display = load_image("snake/assets/barrier_tile.png", int(TILE_LENGTH*DISPLAY_SHRINK))
ice_tile_display = load_image("snake/assets/ice_tile.png", int(TILE_LENGTH*DISPLAY_SHRINK))

land_tile_button = load_image("snake/assets/land_tile.png", TILE_BUTTON_LENGTH)
barrier_tile_button = load_image("snake/assets/barrier_tile.png", TILE_BUTTON_LENGTH)
ice_tile_button = load_image("snake/assets/ice_tile.png", TILE_BUTTON_LENGTH)

start_new_game_button = load_image("snake/assets/start_new_game_button.png", 100)
start_new_game_button_highlighted = load_image("snake/assets/start_new_game_button_highlighted.png", 100)

map_creator_button = load_image("snake/assets/map_creator_button.png", 100)
map_creator_button_highlighted = load_image("snake/assets/map_creator_button_highlighted.png", 100)
