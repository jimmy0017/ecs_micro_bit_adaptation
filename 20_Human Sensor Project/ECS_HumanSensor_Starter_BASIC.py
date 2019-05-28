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


led1 = pin0
aluminumFoil = pin1


 
# The fourth section is for functions that are called up by the third section.

def LightingPattern1() # Sample function for a lighting pattern
    led1.write_digital(1)
    sleep(1000)
    led1.write_digital(0)
    sleep(1000)

while True:
    # The third section is for things that happen repeatedly in the program loop
    # while the program is running. The code is executed in the order coded. 

    foilStorage = aluminumFoil.read_analog() # the part of your code that reads information from the sensor
    print(foilStorage) //prints the value of the sensor to the serial monitor
    sleep(100)  # delay for 1/10 of a second

    # Write your actions here. Your sets of if/else statements 
    # for your human sensor along with which lighting patterns 
    # you want to call




