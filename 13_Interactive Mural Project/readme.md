# Instructional Days:13-18. Interactive Mural Project.

Table of Contents
=================
* [Topic Description](#topic-description)
* [Objectives](#objectives)
* [Outline of the Lesson](#outline-of-the-lesson)
* [Student Activities](#student-activities)
* [Teaching/Learning Strategies](#teachinglearning-strategies)
	 * [Journal Entry(5 min)](#journal-entry5-min)
	 * [Introduce Interactive Mural Project (20 min)](#introduce-interactive-mural-project-20-min)
	 * [Aesthetic and circuit design (30 min)](#aesthetic-and-circuit-design-30-min)
	 * [Students pairs begin crafting and programming (35 min)](#students-pairs-begin-crafting-and-programming-35-min)
	 * [Design Notebook (10 min)](#design-notebook-10-min)
	 * [Two Button Roleplay (45 min)](#two-button-roleplay-45-min)
	 * [Journal Entry](#journal-entry)
	 * [Crafting and programming (35 min)](#crafting-and-programming-35-min)
	 * [Debugging Activity (20 min)](#debugging-activity-20-min)
	 * [Crafting and Programming (100 min)](#crafting-and-programming-100-min)
	 * [Assemble the class mural and explore (20 min)](#assemble-the-class-mural-and-explore-20-min)
	 * [Design Notebook entry (10 min)](#design-notebook-entry-10-min)
* [Resources](#resources)

## Topic Description
This lesson has students create an interactive mural.

## Objectives
Students will be able to:
* Craft part of a collaborative mural that uses a computational circuit and switches 
* Program a computational circuit with complex conditionals that respond to user input

## Outline of the Lesson
* Journal Entry (5 minutes)
* Introduction of project (20 minutes)
* Aesthetic and circuit design (30 minutes) 
* Crafting and programming (35 minutes)
* Two Button Roleplay: Review of complex conditionals (45 minutes) 
* Crafting and programming (35 minutes)
* Design Notebook (10 minutes)
* Debugging activities (20 minutes)
* Crafting and programming (100 minutes)
* Class mural exploration (20 minutes)
* Design Notebook entry (10 minutes)

## Student Activities
* Respond to journal entry
* Participate in the introduction of project.
* Collaborate with a partner to design their project.
* Begin crafting and programming
* Participate in review of complex conditionals.
* Craft and program.
* Debug existing program
* Finish crafting and programming.
* Explore class mural.
* Complete Design Notebook entry.

## Teaching/Learning Strategies
### Journal Entry(5 min)
* If you have 2 buttons, how many different ways could you arrange them (i.e., On and Off)? How many ways are there total? 
* Share with elbow partner.
* Have a student share their answers with the class.
* Guide students to the fact that there are 4 configurations - OFF/OFF, OFF/ON, ON/OFF, and ON/ON. Write this on the board.
	* Relate the switch configurations to binary numbers (Unit 2, Days 10-12) and the amount of numbers that can be represented with 2 bits.

### Introduce Interactive Mural Project (20 min)
* Have class decide on a theme for their quilt-style mural considering how many panels the class can make. 
	* It could feature different parts of the school (mascot, stadium, cafeteria, hang-out areas, ECS classroom) or their neighborhood/school community.
	* Another idea could be a banner with letters such as: “ECS Rocks!” or “Go Bears!” - (insert chosen slogan).
	* Or you can pick a favorite theme (Pacman, local plants, etc.).
	* The class may want to agree on a color scheme or other aesthetic details.
	* Each pair will craft one piece of the mural, each panel will feature one micro:bit and 4-6 LEDs.
	* Review where the switches are on the micro:bit (button switches: button_a and button_b). They will program both of them (i.e., two buttons). Explain how a button acts as a switch (by closing a circuit, but instead of left /right, it’s up /down).
* See Interactive Mural Sample Rubric
	* Students may be assessed in pairs - one rubric for the group.

### Aesthetic and circuit design (30 min)
* Have student pairs draw both an aesthetic design and a circuit design for their panel. 
* They should consider where to place the micro:bit and LEDs in both designs. 
	* People will need to operate the buttons on the micro:bit to make the lights change pattern.
* Students should especially consider how to connect (sew) the components to the micro:bit (circuit design).
	* They may use a common ground, but they will want to avoid stitches crossing over each other as it will cause crossed signals or shorts.
	* The multiple ground (GND) pins on the micro:bit may provide additional flexibility in circuit diagrams. 
	* Note how the Li-Po battery needs to be attached after the project is finished. It will either hang in front of the micro:bit when connected, or students will need to find a place to store it (e.g., felt pocket, a slit in project to put it in the back, etc.). 

### Students pairs begin crafting and programming (35 min)
* Have pair groups complete #1 - #5 of the  [Mural Storyboard](https://docs.google.com/document/d/1QDSUQ-ZAhRD--2DEGfU0WFJv176_jcjwjS9W8ejqVxc/edit?usp=sharing) .
* They may use  [Mural_Starter code](Mural_Starter.py)  to begin their programs. They can enter the code from steps #1 - #5 of the storyboard. They will complete the storyboard after reviewing conditionals.
* One member may want to work on the program while the other is crafting. Ensure that each member gets a chance to craft and program.

### Design Notebook (10 min)
*  [*Can be completed at the end of class, either after aesthetic & circuit design or after some crafting time - whichever is more convenient.*]
* Take a picture of your work so far. What is something you have had to fix or something you have made a change to since you started on this project?

### Two Button Roleplay (45 min)

* This activity is a revisit of the previous activity One Button Roleplay (recommended on Instructional Day 12) with the addition of another Button. Students revisit CS concepts of coding structure, conditional statements, variables, buttons, and digitalRead. In addition, students will explore the mathematical concept of possible combinations and the CS concept of nested conditional statements.
* **Review One Button Roleplay Activity (5 min)**
* **Explore possible combinations (10 min)**
	* **Journal Entry:**Given two buttons how many possible combinations of switch states for two switches? 
	* Students pair share. 
* Students share what they discussed as pairs. Explore the different strategies used to determine the total possible combinations. 
* After class discussion students add to their journal entry.
* **Two Buttons Roleplay (30 min)**
	* One of the most difficult concepts for students to understand is the need for a variable to hold the information from the button (i.e., why “button_a_storage” in the sample code is needed in addition to a name for the button as in “button_a”). The activity below helps them to grasp this and to review DC circuit conditions versus microcontroller programming logic and nested conditional statements. Use this activity as an introduction to the mural project two switches coding challenge. Students will understand the CS concepts of nested conditionals and variables.
* **Roleplay Setup Two Buttons**
	* Two students stand in front of class as the variables “button_a_storage” and “button_b_storage” with two-sided cards or felt such that one side represents HIGH and the other side represents LOW. The two cards should be differentiated so students can tell which card represents which variable, such as each card is a different color.
	* Two students stand in the back of the classroom facing the front (and can see the students that represent the variables, but cannot be seen by the class) with two sided cards or felt such that one side represents HIGH and the other side represents LOW. The two cards should be differentiated so students can tell which card represents which variable, such as each card is a different color.
	* The rest of class represents the processor in the micro:bit that executes the code written. They face forward and can only see the variable students and not the switch students.
* **Roleplay Activity Two Buttons**
	* Teacher or student conducts a discussion on the 4 parts of code on board or projected. Have someone (teacher or student) write the code on the board. Leave space in each section to write additional code later.

```
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

* Class discussion. As a class:
	* Decide the first section of code to declare pins and variables and write it on the board. Discuss what the class wrote and why.
	* Decide what four behaviors happen for each possible combination of the variable values. Such behaviors could be clapping or standing up. Write the four functions in the second section. Discuss what the class wrote and why. Add comment lines.
	* Decide the third section of code to determine if button_a and/or button_b is pressed or not. Discuss what the class wrote and why. Add comment lines.
	* Add nested conditional statements to the third section that calls up the four behavior functions in second section for the four possible variable value combinations. Discuss what the class wrote and why. Add comment lines.
* Once the code is done, lead the class through the code one line at a time and have the class roleplay their given roles. Have the button students randomly pick their states to be in. Start from first section of code. Students will need to be reminded not to do the behaviors until digitalRead, the code assigns value to the variables, and students have read the conditional code that applies in the third section.
* Repeat the loop code in the third section. The button students change their states randomly and the teacher continues to loop through the third section until the instructor feels the students understand the CS concepts addressed in the lesson.

### Journal Entry 
* Why do we need to have a variable and digital read in our code for one button? If we used three three instead of two how many possible behaviors could we have? Justify your response.

### Crafting and programming (35 min)
* Pairs will complete the rest of  [Mural Storyboard](https://docs.google.com/document/d/1QDSUQ-ZAhRD--2DEGfU0WFJv176_jcjwjS9W8ejqVxc/edit?usp=sharing) 
* Pairs will continue programming. One member may want to work on the program while the other is crafting. Codes can be tested by alligator clipping wristbands, paper circuits, or LEDs to the micro:bit. At this stage, there could be extra micro:bits that could be made available for testing at your discretion.
* Ensure that each member gets a chance to craft and program.
* Extension: Groups who finish early can program all ~three~ switches for their panel of the mural

### Debugging Activity (20 min)

* Assign half of the pairs to “ [Debugging Fun Mural1](https://docs.google.com/document/d/1A8rpYnPL1KUnDpNW9HvymOrYEatFA5RsbgVRvX8wuZM/edit?usp=sharing) ,” and the other half to “ [Debugging Fun Mural2](https://docs.google.com/document/d/1MTYGLAqP8dnv7uOU7tHp57zJB1CaruR0Qhy_y-CB0qI/edit?usp=sharing) ”
	* Have them complete #1 in pairs.
* Have students load the corresponding python files:  [debuggingFunMural1 code](debuggingFunMural1.py)  or  [debuggingFunMural2 code](debuggingFunMural2.py) 
	* Have them run the code in pairs and answer #2.
		* Alternatively, you can run the program for the students as a whole class and have them complete #2
		* Note - the code will work with the onboard micro:bit light, so no LEDs need to be connected. Similarly, *any* LED connected to one of the pins on the micro:bit will work.
* Have students complete their debugging assignment
* Have each pair form a group with another pair that had the other debugging assignment, and have each pair share their scenarios and answers with each other.
* See  [Debugging Fun Mural1 solution](https://docs.google.com/document/d/10jTGro7Uzqo4s3UXrYxgJfCEFe3FeZKPgAJCcVqidZM/edit?usp=sharing)  and  [Debugging Fun Mural2 solution](https://drive.google.com/open?id=13F2SAPFFfy1d5OjGNvGD-d_OWyylf7-QZX0ruTh3prI) 

### Crafting and Programming (100 min)
* Groups finish crafting and programming their mural piece.

### Assemble the class mural and explore (20 min)
* Have students interact with different parts of the mural to discover the different programmed behaviors of the different pieces

### Design Notebook entry (10 min)
* Students can reflect on one or more of the following topics. They should include details and examples:
	* What are some things you learned from working in a group on this project?
	* What are you most proud of from this project?
	* What parts of this project were the most challenging?
	* Was there something you would do differently, if you were to do the project again?
	* What are some tips from this project that you would want to share with someone just starting out?
	* Thinking back on this project, what are some tips that you would like to remember for future projects?

## Resources
* Materials for each pair: micro:bit board, micro usb cable, computer, 4-6 sewable LEDs, felt pieces for base and decoration 
* Materials for each table group: craft glue, thread wax, sewing thread, seam rippers, rulers, black and red pens, scotch tape, alligator clip set
* Design Notebooks
* Interactive Mural Sample Rubric
*  [Mural_Starter code](Mural_Starter.py) 
*  [Mural Storyboard](https://docs.google.com/document/d/1QDSUQ-ZAhRD--2DEGfU0WFJv176_jcjwjS9W8ejqVxc/edit?usp=sharing) 
*  [Debugging Fun Mural1 ](https://drive.google.com/open?id=1A8rpYnPL1KUnDpNW9HvymOrYEatFA5RsbgVRvX8wuZM) 
*  [Debugging Fun Mural2](https://docs.google.com/document/d/1MTYGLAqP8dnv7uOU7tHp57zJB1CaruR0Qhy_y-CB0qI/edit?usp=sharing) 
*  [debuggingFunMural1 code](debuggingFunMural1.py) 
*  [debuggingFunMural2 code](debuggingFunMural2.py) 
*  [Debugging Fun Mural1 solution](https://docs.google.com/document/d/10jTGro7Uzqo4s3UXrYxgJfCEFe3FeZKPgAJCcVqidZM/edit?usp=sharing) 
*  [Debugging Fun Mural2 solution](https://drive.google.com/open?id=13F2SAPFFfy1d5OjGNvGD-d_OWyylf7-QZX0ruTh3prI) 

