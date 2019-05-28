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

#  The first section is where to declare global objects and call up additional files the program needs to use.  
from microbit import *

wristband1 = pin1

# SETUP SECTION: Put things here that you only need to do once:
# For instance, OUTPUTS (lights)

# The second section is for functions that will be called up by the third section.
# You must write the function before it is called.


while True:
# The third section is for things that happen repeatedly in the program loop
# while the program is running. The code is executed in the order coded. 

    wristband1.write_digital(1)  #Turn the light on 
    #(How would you turn the light off?)



