
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

wristband1 = pin0
 
# ACTIVITY SECTION: This is one big loop. Whatever you put in here 
# will run over and over and over again.

while True:
    # The second section is for things that only need to be done once at the beginning of the program.  
    button_a_storage = button_a.is_pressed() #read true if button_a is pressed
    # In other words, when the button is 'pressed' , it will read as TRUE. 
    # If the button is NOT 'pressed', it will read as FALSE.
    if button_a_storage:
        wristband1.write_digital(1)
    else:
        wristband1.write_digital(0)
    