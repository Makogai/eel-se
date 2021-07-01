from typing import Tuple, Any
from pathlib import Path
from pygame_menu.examples import create_example_window
from pygame_menu import Theme
import pygame_menu
import pygame
import time
import random
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()  # to hide the main window


def play_racing(user_name):

    pygame.init()

    display_width = 800
    display_height = 600
    car_width = 51
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("PyFy Racing!")
    clock = pygame.time.Clock()

    # colors
    black = (255, 255, 255)
    white = (11, 22, 34)
    red = (200, 0, 0)
    green = (0, 200, 0)

    pause = False

    bright_red = (255, 0, 0)
    bright_green = (0, 255, 0)
    block_color = (53, 115, 255)
    block_color_bright = (94, 144, 255)
    # Car image
    car_file = open(Path(__file__).parent / "car.png", 'r')
    hs_file = open(Path(__file__).parent / "racing_hs.txt", 'r+')
    carImg = pygame.image.load(car_file)
    font = pygame.font.SysFont(None, 25)

    def get_highscore():
        hs_file_hs = open(Path(__file__).parent /
                          "racing_hs.txt", 'r+').readline()
        hs = hs_file_hs.strip()
        return int(hs)

    def message_to_screen(msg, color, x, y):
        screen_text = font.render(msg, True, color)
        gameDisplay.blit(screen_text, [x, y])

    def add_hs_to_db(score):
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
        cursor = cnx.cursor()

        query = ("INSERT into racing_highscores(username,score) VALUES(%s,%s)")

        query_data = (user_name, score)
        print(query_data)
        cursor.execute(query, query_data)

        cnx.commit()
        cursor.close()
        cnx.close()

    def things_dodged(count):
        font = pygame.font.SysFont(None, 50)
        message_to_screen(''.join(["Score: ", str(count)]), black, 10, 10)
        message_to_screen(''.join(["High Score: ", str(
            get_highscore()) if get_highscore() > count else str(count)]), black, 10, 30)
        message_to_screen(''.join(["Username: ", user_name]), black, 10, 50)

    def things(thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

    def thing_2(thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

    def car(x, y):
        gameDisplay.blit(carImg, (x, y))

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

        game_loop()

    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action is not None:
                action()

        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

    def crash(count):
        crash = True
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("You Crashed!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        while crash:
            if count > get_highscore():
                hs_file.seek(0)
                hs_file.write(str(count))
                hs_file.truncate()
                add_hs_to_db(count)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            button("Again", 150, 450, 100, 50, green, bright_green, game_loop)
            button("QUIT", 550, 450, 100, 50, red, bright_red, quit_game)

            pygame.display.update()
            clock.tick(15)

    def quit_game():
        pygame.quit()
        quit()

    def unpause():
        global pause
        pause = False

    def paused():
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Paused!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
            button("QUIT", 550, 450, 100, 50, red, bright_red, quit_game)

            pygame.display.update()
            clock.tick(15)

    def game_intro():
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("PyFy Racing!", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(TextSurf, TextRect)

            button("GO! "+user_name, 150, 450, 200, 50,
                   block_color, block_color_bright, game_loop)
            button("QUIT", 550, 450, 100, 50, red, bright_red, quit_game)

            pygame.display.update()
            clock.tick(15)

    def game_loop():
        global pause

        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0

        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 4
        thing_width = 100
        thing_height = 100

        thing_startx2 = random.randrange(0, display_width)
        thing_starty2 = -600
        thing_speed2 = 5
        thing_width2 = 100
        thing_height2 = 100

        dodged = 0

        gameExit = False

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change

            gameDisplay.fill(white)

            things(thing_startx, thing_starty,
                   thing_width, thing_height, block_color)
            thing_starty += thing_speed

            thing_2(thing_startx2, thing_starty2,
                    thing_width2, thing_height2, block_color)
            thing_starty2 += thing_speed2
            car(x, y)
            things_dodged(dodged)
            if x > display_width - car_width or x < 0:
                crash(dodged)

            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, display_width)
                dodged += 1
                thing_speed += 0.4
                thing_width += (dodged * 1.04)
            if thing_starty2 > display_height:
                thing_starty2 = 0 - thing_height2
                thing_startx2 = random.randrange(0, display_width)
                dodged += 1
                thing_speed2 += 0.4
                thing_width2 += (dodged * 1.02)
            if y < thing_starty + thing_height:
                if thing_startx < x < thing_startx + thing_width or thing_startx < x + car_width < thing_startx \
                        + thing_width:
                    crash(dodged)
            if y < thing_starty2 + thing_height2:
                if thing_startx2 < x < thing_startx2 + thing_width2 or thing_startx2 < x + car_width < thing_startx2 \
                        + thing_width2:
                    crash(dodged)

            pygame.display.update()
            clock.tick(90)

    game_intro()

    game_loop()

    pygame.quit()

    quit()


surface = create_example_window('PyFy - Snake Game', (800, 600))


def start_the_game() -> None:
    global user_name
    print('{0}!'.format(user_name.get_value()))
    play_racing(user_name.get_value())


mytheme = Theme(background_color=(11, 22, 34),
                title_background_color=(53, 115, 255),
                )

menu = pygame_menu.Menu(
    height=600,
    theme=mytheme,
    title='Welcome to PyFy Racing!',
    width=800
)
menu._theme.background_color = (11, 25, 48)
user_name = menu.add.text_input('Username: ', default='Racer', maxchar=16)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


def play_racing_menu():
    menu.mainloop(surface)
    play_racing_menu()
# play_racing_menu()
