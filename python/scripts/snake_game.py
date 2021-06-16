import pygame
import time
import random
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
import pygame_menu
import pygame_menu
from pygame_menu.examples import create_example_window
from pathlib import Path

from typing import Tuple, Any



def play_snake(difficulty,user_name):
    pygame.init()

    white = (11, 22, 34)
    black = (159, 173, 189)
    red = (255,0,0)
    purple = (1,133,223)
    gameover = (1,133,223)

    display_width = 800
    display_height = 600

    difficulty = difficulty
    user_name = user_name

    print(difficulty, user_name)


    clock = pygame.time.Clock()
    fps = difficulty
    block_size = 50

    font = pygame.font.SysFont(None, 25)
    hs_file = open(Path(__file__).parent / "snake_hs.txt", 'r+')

    eat_sound = pygame.mixer.Sound(Path(__file__).parent / "../assets/sounds/eat.wav")
    game_over_sound = pygame.mixer.Sound(Path(__file__).parent / "../assets/sounds/game_over.wav")
    victory_sound = pygame.mixer.Sound(Path(__file__).parent / "../assets/sounds/victory.wav")
    #Setting high score
    def get_highscore():
        hs_file_hs = open(Path(__file__).parent / "snake_hs.txt", 'r+').readline()
        hs = hs_file_hs.strip()
        return int(hs)

    def snake(block_size, snakeList, snakeHead, lead_x, lead_y):
        for XnY in snakeList:
            pygame.draw.rect(gameDisplay, purple, [XnY[0],XnY[1],block_size,block_size])
            pygame.draw.rect(gameDisplay, red, [lead_x,lead_y,block_size,block_size])

    def start_the_game():
        gameLoop()

    def message_to_screen(msg,color,x,y):
        screen_text = font.render(msg, True, color)
        gameDisplay.blit(screen_text, [x,y])

    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption("PyFy - Snake")

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

        query = ("INSERT into snake_highscores(username,score) VALUES(%s,%s)")

        query_data = (user_name,score)
        print(query_data)
        cursor.execute(query, query_data)

        cnx.commit()
        cursor.close()
        cnx.close()

    def gameLoop():
        gameExit = False
        gameOver = False

        lead_x = display_width/2
        lead_y = display_height/2
        lead_x_change = 0
        lead_y_change = 0

        snakeList = []
        snakeLength = 1

        score = 0

        randAppleX = round(random.randrange(0, display_width - block_size)/block_size)*block_size
        randAppleY = round(random.randrange(0, display_height - block_size)/block_size)*block_size

        while not gameExit:
            while gameOver == True:
                gameDisplay.fill(gameover)
                message_to_screen("Poginuli ste! Kliknite ENTER da nastavite, ili Q da izađete.", white, 180,280)
                message_to_screen(''.join(["Vaš score je bio: ",str(score)]), white, 300, 325)
                pygame.display.update()

                play_game_over = True
                if play_game_over:
                    play_game_over = False

                #Overwriting highscore
                if score > get_highscore():
                    messagebox.showinfo('Čestitamo!','Novi Highscore!')
                    add_hs_to_db(score)

                    pygame.display.update()
                    print("NEW HIGHSCORE!")
                    hs_file.seek(0)
                    hs_file.write(str(score))
                    hs_file.truncate()


                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameLoop()
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                    elif event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_UP:
                        lead_y_change = -block_size
                        lead_x_change = 0

            if lead_x >= display_width or lead_x <0 or lead_y >= display_height or lead_y <0:
                gameOver = True

            lead_x += lead_x_change
            lead_y += lead_y_change
            gameDisplay.fill(white)
            message_to_screen(''.join(["Score: ",str(score)]), black, 10,10)
            message_to_screen(''.join(["High Score: ",str(get_highscore()) if get_highscore() > score else str(score)]), black, 10,30)
            pygame.draw.rect(gameDisplay, black, [randAppleX, randAppleY, block_size, block_size])

            snakeHead = []
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            snakeList.append(snakeHead)

            if len(snakeList) > snakeLength:
                del snakeList[0]
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver = True

            snake(block_size, snakeList, snakeHead, lead_x, lead_y)

            if lead_x == randAppleX and lead_y == randAppleY:
                randAppleX = round(random.randrange(0, display_width - block_size)/block_size)*block_size
                randAppleY = round(random.randrange(0, display_height - block_size)/block_size)*block_size
                snakeLength += 1
                score += 1
                eat_sound.play()
                message_to_screen(''.join(["Score: ",str(score)]), black, 10,10)

            pygame.display.update()

            clock.tick(fps)

        play_snake_menu()
        pygame.quit()
    # menu = pygame_menu.Menu(300, 400, 'Welcome',
    #                    theme=pygame_menu.themes.THEME_BLUE)

    # menu.add.text_input('Name :', default='John Doe')
    # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)])
    # menu.add.button('Play', start_the_game)
    # menu.add.button('Quit', pygame_menu.events.EXIT)
    gameLoop()
    # menu.mainloop(surface)
# play_snake()

global height
global width
surface = create_example_window('PyFy - Snake Game', (800, 600))


def set_difficulty(selected: Tuple, value: Any) -> None:
    global difficulty
    difficulty = value
    print('Set difficulty to ({})'.format(difficulty))


def start_the_game() -> None:
    global difficulty
    global user_name
    global height
    global width
    print('{0}, {1}!'.format(user_name.get_value(), difficulty))
    play_snake(difficulty,user_name.get_value())



menu = pygame_menu.Menu(
    height=600,
    theme=pygame_menu.themes.THEME_SOLARIZED,
    title='Dobrodošli u PyFy Snake Game',
    width=800
)

user_name = menu.add.text_input('Ime: ', default='Korisnik', maxchar=10)
menu.add.selector('Težina: ', [('Easy', 5), ('Normal', 10), ('Hard', 20), ('Impossible', 40)], onchange=set_difficulty)
difficulty = 5
menu.add.button('Igraj', start_the_game)
menu.add.button('Izađi', pygame_menu.events.EXIT)

def play_snake_menu():
    menu.mainloop(surface)
    play_snake_menu()


