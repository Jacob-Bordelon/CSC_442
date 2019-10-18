from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform





keyboard = Controller()
string = "this is my string"

for c in string:
    keyboard.press(c)
    sleep(uniform(0.02,0.2)) # key press
    keyboard.release(c)
    sleep(0.1) # key interval

keyboard.press(Key.enter)
keyboard.release(Key.enter)
