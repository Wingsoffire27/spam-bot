import random
import AppOpener
import keyboard
import pyautogui
import time
import webbrowser
from fastnumbers import isfloat
#checks if shift is not pressed
def is_shift_not_pressed():
    return not keyboard.is_pressed('shift')
Sentence = str(input("give me a sentence: "))
#checks if it is more then 500 bc max discord is 2000 but when chill zone it pastes 4 times
while not len(Sentence) < 500 and len(Sentence) > 0:
    Sentence = str(input("give me a sentence: "))
while True:
    timewait= input("how long do you want in between typing?(The larger the text the longer the suggested wait time. GIfs and Images need a more of time)")
    if isfloat(timewait):
        timewait = float(timewait)
        break
WhatApp = str(input("what app do you want to open?(say 'website for websites') ")).lower()
#opens webbiste if you type "webiste"
if WhatApp == "website":
    StartOfWebsite = "http://"
    Site = (input("give me a website: "))
else:
    AppOpener.open(WhatApp)
keyboard.wait('shift')
#waits until shift key not pressed


while not is_shift_not_pressed():
    time.sleep(0.1)
#repeats until it detects the shift key being pressed
mouseX, mouseY = pyautogui.position()
while 1 > 0:
        if keyboard.is_pressed("shift"):
            break
        pyautogui.write(Sentence)
        pyautogui.press("enter")
        pyautogui.click(900, 600)
        pyautogui.click(mouseX, mouseY)
        time.sleep(timewait)
