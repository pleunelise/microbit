from microbit import *
import random

duim = Image("00009:"
             "00009:"
             "00999:"
             "00999:"
             "00999")
             
pink = Image("00000:"
             "00090:"
             "00090:"
             "99990:"
             "99990")

wijsvinger = Image("09000:"
                   "09000:"
                   "09999:"
                   "99999:"
                   "99999")
                   
plaatjes = [duim, pink, wijsvinger]
score = 0
while True:
    if accelerometer.current_gesture() == "shake":
       display.show(random.choice(plaatjes))
    if button_a.is_pressed() and button_b.is_pressed():
         display.scroll(str(score))
    if button_a.is_pressed():
        score += 1
        sleep(100)
    if button_b.is_pressed():
         score -= 1
         sleep(100)
    print (score)
""""
        while True:
        if button_b.is_pressed():
            #display.show("B")
             score -= 1
        if button_a.is_pressed():
           #display.show("A")
           score += 1
        if button_a.is_pressed() and button_b.is_pressed():
           display.show(int(score))
    """
    
    
    