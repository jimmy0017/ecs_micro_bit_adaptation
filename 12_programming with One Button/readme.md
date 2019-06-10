# Instructional Days:12. Programming with One Switch (simple conditionals).

## Topic Description
This lesson provides an introduction to using one switch to control the behavior of a micro:bit.

## Objectives
Students will be able to:
* Use a button as input
* Program their own computational circuit using conditionals
* Write functions to organize and reuse code

## Outline of the Lesson
* Journal Entry (5 minutes)
* Review conditionals (10 minutes)
* Button as input (10 minutes)
* Creating light pattern functions (30 minutes) 
* Recommended: One Button Roleplay activity (40 minutes)

## Student Activities
* Complete journal entry.
* Participate in review of conditionals.
* Discover how to use a button to turn an LED on and off.
* Program the micro:bit to perform a chosen light pattern based on the state of the button.

## Teaching/Learning Strategies 
### Journal Entry (5 min)
* What were some ways we have used the “if” and “if/else” block in Scratch?
	* It may help to display a visual of the “if” and “if/else” blocks from Scratch.
	* Share responses with elbow partners.

### Review conditionals (10 min)
* Have students share from their journal responses.
* Review how conditionals were used in Scratch for the Age project (Scratch Unit Day 15)
	* See age solution.sb from Unit 4.
* Show how conditionals are coded in Python vs Scratch
	* Place an “if/else” block from Scratch on the board and write the Python if/else code next to it point out the corresponding elements:
		* The condition come right after the “if” keyword
		* The colon (:) after the condition in the “if” statement along with the single-tab indentation of the statements that follow the colon encompass the code that will execute in case the “if” condition is true .
		* See Python Reference - if/else:  [https://www.w3schools.com/python/python_conditions.asp](https://www.w3schools.com/python/python_conditions.asp) 

### Using the button to turn an LED on and off (10 min)
* Invite students to identify the two buttons on the micro:bit and understand how to access the button through MicroPython. 
	* Note: There are two buttons on the micro:bit . We are using only one of them for now.
	* Let students to explore #1,2,3 by themselves  [One Button Storyboard](https://docs.google.com/document/d/1sJXzpyopJHPfDxYFEWaTyioI7CTev-vnMSKq3Yn4oL8/edit?usp=sharing) 
* Lead class through completing #4 
	* Have students open  [One_Switch_Starter](https://github.com/jimmy0017/etextilesresearch/blob/master/12_programming%20with%20One%20Button/One_Button_Starter.py) 
	* See  [One_Switch_ON_OFF](https://github.com/jimmy0017/etextilesresearch/blob/master/12_programming%20with%20One%20Button/One_Button_ON_OFF.py)  for the solution In pairs, students complete #5 and #6.
	* Remember to connect one Wristband to the correct pin!
	
### Create light pattern functions (30 min)
* Introduce the BUILDING BLOCKS Section of their program.
	* They will create their own function for their light patterns.
		* They can reuse the light patterns by cutting and pasting from the previous lesson, or they can create new light patterns.
	* The syntax will be similar to the “while True:” function they have been using.
		* “def” - meaning that it is defining a function.
		* The name of the function (e.g., slowblink, funkyblink).
		* “()” - since we are not passing any arguments. 
		* “:” - marks the end of the definition statement and beginning of the actual function definition. 
		* The body of the function gets indented after “:”
	* The helper function mentioned below is an example of a personalized light function. 
		* See  [Helper_Functions](https://github.com/jimmy0017/etextilesresearch/blob/master/12_programming%20with%20One%20Button/Helper_Functions.py) 
	* See Python Reference - Functions:  [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp) 
* Students complete complete #6 to #12 on  [One Switch Storyboard.pdf](https://docs.google.com/document/d/1sJXzpyopJHPfDxYFEWaTyioI7CTev-vnMSKq3Yn4oL8/edit?usp=sharing) 
* OPTIONAL EXTENSION: Helper Functions
	* Optionally, share how functions can be used as building blocks
		* See  [Helper_Functions](https://github.com/jimmy0017/etextilesresearch/blob/master/12_programming%20with%20One%20Button/Helper_Functions.py) 
	* Use  [Helper Function Storyboard.pdf](https://drive.google.com/open?id=0B505sHFnjLeMM2tVUGltSGYxQzA) 

## Recommended addition: One Button Class Roleplay (40 min total)

### Review of buttons and variables (5-10 min)
* Discuss with class that the buttons on the micro:bit are not part of the processor. The micro:bit designer added the buttons to the board so that one would not need to connect external buttons to the micro:bit. Remind students that buttons, like the ones students made previously, are basically two wires that are not connected, thus are an open circuit. The buttons can be manipulated so that the two wires touch and close the circuit. A button does not have a “brain.”
* Discuss what a class is and how all the pins and the buttons are classes that we are making copies of for the purposes of programming here.


### One Button Roleplay (30 min)
One of the most difficult concepts for students to understand is the need for a variable to hold the information from “button_a” (i.e., why “button_a_storage” in the sample code is needed in addition to a name for the button as in “button_a”). The activity below helps them to grasp this and to review DC circuit conditions versus microcontroller programming logic. Use this activity as an introduction to the button coding lesson. Students will understand the CS conditionals and variables. 

*Note: We have used “button_a_storage” as a variable name because it helps us remember what that variable does – stores the information from reading the switch. However, it can help if students make up their own name: swoosh, Bob, switchvalue, etc. Just like naming LEDs for convenience, we should name our data-storing variables with something that makes sense to us.*

### Roleplay Setup One Button
* One student in front of class as the variable button_a_storage with a two-sided card or felt such that one side represents 1 and the other side represents 0. This student only changes the card when told to read the human “button” person in the back of the room (see next bullet).
* One student in the back of the classroom as the button, (facing the front and can see the student that represents the variable, but cannot be seen by the class) with a two-sided card or felt such that one side represents PRESSED and the other side represents NOT PRESSED.
* The rest of class represents the processor in the micro:bit that executes the code written. They face forward and can only see the variable student and not the button student.

### Roleplay Activity One Button
* Teacher or student conducts a discussion on the 4 parts of code on board or projected. Have someone (teacher or student) write the code on the board. Leave space in each section to write additional code later.

```
# This code was written for the Stitch the Loop e-textiles curriculum by the
# Exploring Computer Science e-textiles team. ECS 2018 GPL V3 for non commercial use. 
# ECS 2018 CC- BY NC SA. 

# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
# This program is an EXAMPLE of the many possible solutions. This code will compile as is.
# ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇

# STUDENT META HERE
# STUDENT NAME(S)
# Date Written
# Brief description of what program does here.


# The first section is where to declare global classes and call up additional files the program needs to use. 

from microbit import *

# NAMING SECTION: We name things to keep track of them easily.

# The second section is for functions that will be called up by the third section.
# You must write the function before it is called.
def yourFunction(led):

while True:
# The third section is for things that happen repeatedly in the program loop
# while the program is running. The code is executed in the order coded. 
```
 

* Class writes the first section of code to import the micro:bit package, initialize pin and variables. Class discusses what they wrote and why. Add comment lines.
* Class then writes second section of code lead by teacher to create functions to be able to use repeatedly for the while True section.
* Class then writes the while True section of code lead by teacher to use button_is_pressed and assign variable values to button_a_storage. Class discusses what they wrote and why. Add comment lines.
* Class decides what behavior happens when the variable value is 1 and another behavior when the variable value is 0. Such behaviors could be clapping or standing up. Class then writes the two functions in the fourth section. Class discusses what they wrote and why. 
* Class then adds conditional statements to the third section that calls up the behavior functions in the second section for the two possible variable values. Class discusses what they wrote and why. Add comment lines.
* Once code is done teacher leads the class through the code one line at a time and class roleplay their given roles. Have the switch student randomly pick a state to be in. Start from first section of code. Students will need to be reminded not to do the behavior until button_is_pressed, the code assigns a value to the human button_a_storage variable, and have read the conditional code in the third section. 
* Repeat the loop code and the while True section. The switch student changes their state randomly and the teacher continues to loop through the third section until they feel the students understand the CS concepts addressed in the lesson.
* Journal Entry: Why do we need to have a variable and is_pressed() in our code for one button?

## Resources
* Materials: micro:bit, micro usb cable, computer, wristbands, alligator clips
* W3 School Python Reference - If/Else:  [https://www.w3schools.com/python/python_conditions.asp](https://www.w3schools.com/python/python_conditions.asp)  
*  [One Switch Storyboard.pdf](https://drive.google.com/open?id=1WNgTiD0sWECxDkIKOc97ncY3actTX78t) 
*  [One_Switch_Starter](https://github.com/jimmy0017/etextilesresearch/blob/master/12_programming%20with%20One%20Button/One_Button_Starter.py) 
*  [One_Switch_ON_OFF](https://github.com/jimmy0017/etextilesresearch/blob/master/12_programming%20with%20One%20Button/One_Button_ON_OFF.py) 
* W3 School Python Reference - Functions:  [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp)  
*  [Helper_Functions](https://github.com/jimmy0017/etextilesresearch/blob/master/12_programming%20with%20One%20Button/Helper_Functions.py) 
*  [Helper Function Storyboard.pdf](https://drive.google.com/open?id=0B505sHFnjLeMM2tVUGltSGYxQzA) 
