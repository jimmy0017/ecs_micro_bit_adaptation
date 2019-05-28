
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

# Unlike pinMode(INPUT), there is no pull-down resistor necessary. An internal
# 20K-ohm resistor is pulled to 5V. This configuration causes the input to
# read HIGH when the switch is open, and LOW when it is closed.

# In other words, when the switch is 'on' (closed/connected), it will read as LOW. 
# If the switch is 'off' (open/disconnected), it will read as HIGH.

wristband1 = pin0
 
# ACTIVITY SECTION: This is one big loop. Whatever you put in here 
# will run over and over and over again.

while True:
  # The second section is for things that only need to be done once at the beginning of the program.  
  button_a_storage = button_a.is_pressed() #read true if button_a is pressed
    