

import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any


surface = create_example_window('PyFy - Snake Game', (800, 600))


def set_difficulty(selected: Tuple, value: Any) -> None:
    global difficulty
    difficulty = value
    print('Set difficulty to ({})'.format(difficulty))


def start_the_game() -> None:
    global difficulty
    global user_name
    print('{0}, {1}!'.format(user_name.get_value(), difficulty))


menu = pygame_menu.Menu(
    height=600,
    theme=pygame_menu.themes.THEME_SOLARIZED,
    title='Dobrodošli u PyFy Snake Game',
    width=800
)

user_name = menu.add.text_input('Ime: ', default='', maxchar=10)
menu.add.selector('Težina: ', [('Easy', 1), ('Normal', 2), ('Hard', 3)], onchange=set_difficulty)
difficulty = 1
menu.add.button('Igraj', start_the_game)
menu.add.button('Izađi', pygame_menu.events.EXIT)

def play_snake():
    menu.mainloop(surface)

