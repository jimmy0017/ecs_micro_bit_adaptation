
#  This code was written for the Stitch the Loop e-textiles curriculum by the
#Exploring Computer Science e-textiles team. ECS 2018 GPL V3 for non commercial use.  
#ECS 2018 CC- BY NC SA.  


#◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
#This program is an EXAMPLE of the many possible solutions.  This code will compile as is.
#◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇

# STUDENT META HERE
# STUDENT NAME(S)
# Date Written
# Brief description of what program does here.

# The first section is where to declare global objects and call up additional files the program needs to use.  
from microbit import *

led1 = pin0 
led2 = pin1
led3 = pin2
# led4 = 

def off(led):
    led.digital_write(1)

def off(led):
    led.digital_write(0)
  
def allOn():
    on(led1)
    on(led2)
    on(led3)
#   on(led4)

def allOff():
    off(led1)
    off(led2)
    off(led3)
#   off(led4)

def allBlink():
    allOn()
    sleep(1000)
    allOff()
    sleep(1000)

def blinkLed(led):
    on(led)
    sleep(500)
    off(led)
    sleep(500)

def cycle():
    allOff()
    blinkLed(led1)
    blinkLed(led2)
    blinkLed(led3)
#   blinkLed(led4)

while True:
    cycle()
    allBlink()

    