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

# Debugging Scenario:  Joy wrote the following code for 
# her Mural Project.  
# She wants to see:
# allOn() if both buttons are pushed
# blink() if button1 is pushed and button2 is not pushed
# blinkFast() if button1 is not pushed and button2 is pushed
# allOff() if neither is pushed
# Help her debug it.  

# BUILDING BLOCKS SECTION: write functions that you can call 
# when you want
#
def allOn():
    pin0.write_digital(1)
    pin1.write_digital(1)
    pin2.write_digital(1) 

def allOff():
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)

def blink():
    allOn
    sleep(500)
    allOff
    sleep(500)

def blinkFast():
    allOn
    sleep(100)
    allOff
    sleep(100)

# ACTIVITY SECTION: This is one big loop. Whatever you put in here 
# will run over and over and over again.

while True: 
    # The third section is for things that happen repeatedly in the program loop
    # while the program is running. The code is executed in the order coded.  
    # put your main code here, to run repeatedly:

    # both buttons pushed
    if button_b.is_pressed() and button_a.is_pressed():
        allOn()
    # button1 pushed and button2 not pushed
    elif (button_b.is_pressed()):
        blink()
    # button1 not pushed and button2 pushed
    elif (button_a.is_pressed()):
        blinkFast()
    # neither button pushed
    else:
        allOff()






