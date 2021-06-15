

# import pygame_menu
# from pygame_menu.examples import create_example_window

# from typing import Tuple, Any

# surface = create_example_window('Example - Simple', (600, 400))


# def set_difficulty(selected: Tuple, value: Any) -> None:
#     """
#     Set the difficulty of the game.

#     :return: None
#     """
#     print('Set difficulty to {} ({})'.format(selected[0], value))


# def start_the_game() -> None:
#     """
#     Function that starts a game. This is raised by the menu button,
#     here menu can be disabled, etc.

#     :return: None
#     """
#     global user_name
#     print('{0}, Do the job here!'.format(user_name.get_value()))


# menu = pygame_menu.Menu(
#     height=300,
#     theme=pygame_menu.themes.THEME_SOLARIZED,
#     title='Welcome',
#     width=400
# )

# user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
# menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2), ('Nadja', 3)], onchange=set_difficulty)
# menu.add.button('Play', start_the_game)
# menu.add.button('Quit', pygame_menu.events.EXIT)

# if __name__ == '__main__':
#     menu.mainloop(surface)

import mysql.connector

cnx = mysql.connector.connect(user='epiz_28218456', password='bGJDjsD5cDTnCiF',
                              host='sql200.epizy.com',
                              database='epiz_28218456_se')
cursor = cnx.cursor()

query = ("SELECT * from snake_highscores")


cursor.execute(query)

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()