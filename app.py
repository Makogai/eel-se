import eel
import random
from datetime import datetime
from python.scripts.instagram import get_user
from python.scripts.link_shortener import get_url

eel.init('web')

@eel.expose
def get_profile(username):
    # get_user("makogai")
    eel.instagram_show(get_user(username))

@eel.expose
def get_shortened_url(link):
    # get_user("makogai")
    eel.shorten_link(get_url(link))

@eel.expose
def snake():
    from python.scripts.snake_game import play_snake_menu
    # get_user("makogai")
    play_snake_menu()



my_options = {
    'mode': "chrome", #or "chrome-app",
    'host': 'localhost',
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

eel.start('index.html', option=my_options)
# eel.start('index.html', option=my_options)