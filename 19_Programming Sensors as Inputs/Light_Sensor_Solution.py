# This code was written for the Stitch the Loop e-textiles curriculum by the
# Exploring Computer Science e-textiles team. ECS 2018 GPL V3 for non commercial use.  
# ECS 2018 CC- BY NC SA.  


# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
# This program is a starter you will need to add code.  This code will compile as is.
# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇


#  STUDENT META HERE
# STUDENT NAME(S)
# Date Written
# Brief description of what program does here.

# The first section is where to declare global objects and call up additional files the program needs to use.  


from microbit import *

# brightness = 0
sound = False #not in starter file

lightSensor = pin0

# The fourth section is for functions that are called up by the third section.
def light0():
    newImage = Image("00000:"
                     "00000:"
                     "00000:"
                     "00000:"
                     "00000")
    display.show(newImage)

def light2():
    newImage = Image("11111:"
                     "11111:"
                     "11111:"
                     "11111:"
                     "11111")
    display.show(newImage)


def light4():
    newImage = Image("33333:"
                     "33333:"
                     "33333:"
                     "33333:"
                     "33333")
    display.show(newImage)

def light6():
    newImage = Image("55555:"
                     "55555:"
                     "55555:"
                     "55555:"
                     "55555")
    display.show(newImage)


def light8():
    newImage = Image("77777:"
                     "77777:"
                     "77777:"
                     "77777:"
                     "77777")
    display.show(newImage)
  
def light10():
    newImage = Image("99999:"
                     "99999:"
                     "99999:"
                     "99999:"
                     "99999")
    display.show(newImage)
    

while True:
    # The third section is for things that happen repeatedly in the program loop
    # while the program is running. The code is executed in the order coded. */

    # read the value from the sensor:
    brightness = display.read_light_level()
    print(brightness)
    # if (sound):
    #     CircuitPlayground.playTone(brightness, 100);
    # else
    #    sleep(100)
    
    # your code goes here:
    # this can also be done with an if-else-if chain
    if (brightness >= 200):
        light10()
    if (brightness >= 160 and brightness < 200):
        light8()
    if (brightness >= 120 and brightness < 160):
        light6()
    if (brightness >= 80 and brightness < 120):
        light4()
    if (brightness >= 40 and brightness < 80):
        light2()
    if (brightness < 40):
        light0()    
    sleep(1000)