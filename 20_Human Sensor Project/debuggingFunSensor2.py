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


sensor = pin0
led1 = pin1
led2 = pin2

# The fourth section is for functions that are called up by the third section.
def lightPattern1():
    led1.write_digital(0)
    led2.write_digital(0)
    
def lightPattern2():
    led1.write_digital(1)
    led2.write_digital(0)

def lightPattern3():
    led1.write_digital(0)
    led2.write_digital(1)

def lightPattern4():
    led1.write_digital(1)
    led2.write_digital(1)



while True:
    # The third section is for things that happen repeatedly in the program loop
    # while the program is running. The code is executed in the order coded. */

    # read the value from the sensor:
    sensorValue = sensor.read_analog() #read between 0 and 1023
    print(sensorValue)
    sleep(100)
    if (sensorValue >= 768):
        lightPattern1()
    if (sensorValue >= 640 and sensorValue < 768):
        lightPattern2()
    if (sensorValue >= 256 and sensorValue < 374):
        lightPattern3()
    if (sensorValue < 256):
        lightPattern4()

