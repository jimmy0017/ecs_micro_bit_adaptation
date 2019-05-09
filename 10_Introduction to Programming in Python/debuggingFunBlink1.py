

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
# NAMING SECTION: We name things to keep track of them easily.
# What will you name your other lights?


from microbit import *

led1 = pin0
led2 = pin1


# Debugging Scenario: Alicia wants the two lights to blink 
# on and off together every second.  She wrote the following 
# code.  Help her debug it.  



# ACTIVITY SECTION: This is one big loop. Whatever you put in here 
# will run over and over and over again.
while True:
    # The third section is for things that happen repeatedly in the program loop
    # while the program is running. The code is executed in the order coded. 
    led1.write_digital(1) # Turn the light on 
    sleep(1000) # waits for 1 second (1000 milliseconds)
    led1.write_digital(0) # Turn the light off
    sleep(1000) # waits for 1 second
    led2.write_digital(1) # Turn the light on 
    sleep(1000) # waits for 1 second (1000 milliseconds)
    led2.write_digital(0) # Turn the light off
    sleep(1000) # waits for 1 second

