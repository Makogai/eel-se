

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
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.environ.get("DB_USER")
db_host = os.environ.get("DB_HOST")
db_password = os.environ.get("DB_PASSWORD")
db_db = os.environ.get("DB_DB")

cnx = mysql.connector.connect(user=db_user, password=db_password,
                              host=db_host,
                              database=db_db)
# cnx = mysql.connector.connect(user='JFE91oFydO', password='2qsdEuu8SG',
#                               host='remotemysql.com',
#                               database='JFE91oFydO')
cursor = cnx.cursor()

query = ("SELECT * from snake_highscores")


cursor.execute(query)

for (id, username, score,date) in cursor:
  print("[{}] {}, Score: {} was achieved on {:%d %b %Y %H:%M}".format(
    id, username, score, date))

cursor.close()
cnx.close()