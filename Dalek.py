'''
http://microbit-micropython.readthedocs.io/en/latest/tutorials/speech.html

'''
import speech
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        speech.say("DAALEK - DAALEK - EXTERMINATE", speed=120, pitch=100, throat=100, mouth=200)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()


