import eel
import random
from datetime import datetime
from python.scripts.instagram import get_user
from python.scripts.link_shortener import get_url
from python.scripts.snake_hs import get_hs
from python.scripts.encrypt import AlphaShift,AlphaMix

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
def snake_hs():
    # get_user("makogai")
    eel.snake_fill_hs(get_hs())

@eel.expose
def snake():
    from python.scripts.snake_game import play_snake_menu
    # get_user("makogai")
    play_snake_menu()

@eel.expose
def encrypt_as(text):
    eel.encrypt_as_js(AlphaShift(text).encrypt())

@eel.expose
def decrypt_as(text):
    eel.decrypt_as_js(AlphaShift(text).decrypt())

@eel.expose
def encrypt_am(text,secret):
    eel.encrypt_am_js(AlphaMix(text,secret).encrypt())

@eel.expose
def decrypt_am(text,secret):
    eel.decrypt_am_js(AlphaMix(text,secret).decrypt())


page = "index.html"
def close_callbacka(page, sockets):
            pass

my_options = {
    'host': 'localhost',
    'port': 8080,
    'close_callback': close_callbacka,
    'all_interfaces':True,
    'block': False
}

eel.start('index.html', option=my_options)
# eel.start('index.html', option=my_options)