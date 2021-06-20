import eel
import random
from datetime import datetime
from instagram import get_user
from link_shortener import get_url

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
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))

@eel.expose
def get_date():
    eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

@eel.expose
def get_ip():
    eel.prompt_alerts('127.0.0.1')

my_options = {
    'mode': "chrome", #or "chrome-app",
    'host': 'localhost',
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

eel.start('index.html', option=my_options)