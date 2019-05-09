# This code was written for the Stitch the Loop e-textiles curriculum by the
# Exploring Computer Science e-textiles team. ECS 2018 GPL V3 for non commercial use.  
# ECS 2018 CC- BY NC SA.  


# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
# This program is a starter you will need to add code.  This code will compile as is.
# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇


# STUDENT META HERE
# STUDENT NAME(S)
# Date Written
# Brief description of what program does here.




# One patch of aluminum foil should be connected to 
# 12 (A11), 6 (A7), 9 (A9) or 10 (A10). 
# The other patch should be connected to a ground (GND)
# Adjust the code for your A-pin, upload,
# and read the serial monitor to see the values.

# The first section is where to declare global objects and call up additional files the program needs to use.  


from microbit import *

aluminumFoil = pin1 # select your input pin for your sensor 
int foilStorage # this name (variable) stores readings from the sensor



# The second section is for things that only need to be done once at the beginning of the program.  

aluminumFoil.digital_write(1) # initializes the sensor




while True:
    # The third section is for things that happen repeatedly in the program loop
    # while the program is running. The code is executed in the order coded. 
    
    foilStorage = aluminumFoil.read_analog() # the part of your code that reads information from the sensor
    print(foilStorage) # print out the value you read: (literally, "print")
    sleep(100)  # delay for 1/10 of a second


