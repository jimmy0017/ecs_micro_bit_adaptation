# This code was written for the Stitch the Loop e-textiles curriculum by the
# Exploring Computer Science e-textiles team. ECS 2018 GPL V3 for non commercial use.  
# ECS 2018 CC- BY NC SA.  


# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
# This program is an EXAMPLE of the many possible solutions.  This code will compile as is.
# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇

# STUDENT META HERE
# STUDENT NAME(S)
# Date Written
# Brief description of what program does here.


# The first section is where to declare global objects and call up additional files the program needs to use.  

from microbit import *
import random

# NAMING SECTION: We name things to keep track of them easily.
# What will you name your other lights?

# 1,2,9,12
led1 = pin0
led2 = pin1
led3 = pin2
blinkCounter = 1
heartCounter = 1
fadeBrightness = 5
fadeUp = True


# The second section is for functions that will be called up by the third section.
# You must write the function before it is called.
def randomPattern(led):
    # random brightness 50-250
    chance = random.randint(1, 1000)
    brightness = random.randint(1, 1000) + 23
    if chance < 500:
        led.write_analog(brightness) #The value may be either an integer or a floating point number between 0 (0% duty cycle) and 1023 (100% duty).
    else:
        off(led)

def twinkle(led):
    brightness = random.randint(1, 250)
    led.write_analog(brightness)

def blinkPattern(led):
    global blinkCounter #in python, if you want to change to a global variable
    if blinkCounter == 1:
        on(led)
    elif (blinkCounter == 6):
        off(led)
    elif(blinkCounter > 10):
        blinkCounter = 0
    blinkCounter = blinkCounter+1

def heartBeat(led):
    global heartCounter #in python, if you want to change to a global variable
    if (heartCounter == 1):
        on(led)
    elif (heartCounter == 3):
        off(led)
    elif (heartCounter == 5):
        on(led)
    elif (heartCounter == 7):
        off(led)
    elif (heartCounter > 15):
        heartCounter = 0
    heartCounter = heartCounter + 1

def fade(led):
    global fadeBrightness #in python, if you want to change to a global variable
    if fadeUp:
        if fadeBrightness >= 200 :
            fadeUp = false
            #fadeBrightness = 5;
        else:
            fadeBrightness += 10
    else:
        if (fadeBrightness <= 5):
            fadeUp = true
            #fadeBrightness = 5
        else:
            fadeBrightness -= 10
    led.write_analog(fadeBrightness)
 
def on(led):
    led.write_digital(1) 

def off(led):
    led.write_digital(0) #turn off the light

while True:
# The third section is for things that happen repeatedly in the program loop
# while the program is running. The code is executed in the order coded. 
    blinkPattern(led1)
    twinkle(led2)
    fade(led3)
    sleep(100)

