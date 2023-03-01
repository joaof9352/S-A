'''
  Python script that logs mouse movements and clicks and sends them to an Adafruit feed
'''

from pynput import mouse
import datetime
from Adafruit_IO import Client, Feed, MQTTClient
import threading
import time
import os
from secrets import ADAFRUIT_IO_KEY, ADAFRUIT_IO_USERNAME

ADAFRUIT_IO_FEED = 'joaof9352/feeds/feedteste'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
feed = aio.feeds(ADAFRUIT_IO_FEED)

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def on_move(x, y):
    # aio.send_data(feed.key, (get_current_time() + '|' + "MouseMoved" + '|' + str(x) + ',' + str(y) + '\n'))
    with open('log2.txt','a') as f:
        f.write(get_current_time() + '|' + "MouseMoved" + '|' + str(x) + ',' + str(y) + '\n')

def on_scroll(x, y, dx, dy):
    #aio.send_data(feed.key, (get_current_time() + '|' + "MouseScrolled" + '|' + str(x) + ',' + str(y) + ',' + str(dx) + ',' + str(dy) + '\n'))
    with open('log2.txt','a') as f:
        f.write(get_current_time() + '|' + "MouseScrolled" + '|' + str(x) + ',' + str(y) + ',' + str(dx) + ',' + str(dy) + '\n')

    
def on_click(x, y, button, pressed):
    if pressed:
        #aio.send_data(feed.key, (get_current_time() + '|' + "MouseClicked" + '|' + str(button) + '\n'))
        with open('log2.txt','a') as f:
            f.write(get_current_time() + '|' + "MouseClicked" + '|' + str(button) + '\n')  
    
    if button == mouse.Button.right:
        print('Gracefully Stopping!')
        return False

def send_to_Adafruit():
    time.sleep(1)
    while True:
        with open('log2.txt','r') as f:
            all = f.read()
        os.remove('log2.txt')
        print('Enviando...')
        aio.send_data(feed.key, all)
        time.sleep(0.005)

if __name__ == "__main__":
    x = threading.Thread(target=send_to_Adafruit)
    x.start()
    with mouse.Listener(
         on_move=on_move,
         on_click=on_click,
         on_scroll=on_scroll) as listener:
        listener.join()
    x.join()
