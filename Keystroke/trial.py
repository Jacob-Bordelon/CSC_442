from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform

password = raw_input()
features = raw_input()


password = password.split(",")
password = password[:len(password)/2 + 1]
password = ''.join(password)

features = features.split(",")
features = [float(a) for a in features]

key_press = features[:len(features)/2 + 1]
key_inter = features[len(features)/2 + 1:]

print password
print key_press
print key_inter

keyboard = Controller()



for c in range(len(password)):
    keyboard.press(password[c])
    sleep(key_press[c]) # key press
    keyboard.release(password[c])
    if c < len(key_inter):
        sleep(key_inter[c]) # key interval










