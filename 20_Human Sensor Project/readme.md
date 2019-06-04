# Instructional Days:20-31. Human Sensor Project.

## Topic Description:
Students will design and craft a Human Sensor Project.

**Note: PLEASE BE AWARE THAT ALUMINUM PATCHES WILL NEED TO BE MADE IN ADVANCE OF THE “TESTING ALUMINUM FOIL SENSORS” LESSON. EXTRA PREP TIME WILL BE NECESSARY.**

## Objectives:
Students will be able to:
* Apply their knowledge of E-Textiles to create a human sensor project
* Craft a sensor from aluminum foil
* Demonstrate understanding that humans can vary in their conductivity when interacting with the aluminum foil sensor



## Detailed Outline of the Lesson:
### DESIGN project
* Introduce Project (20 minutes)
	* Brainstorming (25 minutes)
	* Introduce Portfolio (10 minutes)
* Design Human Sensor Project (50 minutes) 
	* Design Notebook (5 minutes)

### CONSTRUCT & TEST LIGHTS
* Crafting and debugging of lights (105 minutes)
* Design Notebook (5 minutes)

### LESSON: SENSOR RANGES
* Testing aluminum foil sensors (reading a range in a program) (30 minutes) 
	* Debugging Activities (35 minutes)

### CONSTRUCT & TEST PATCHES
* Creating aluminum foil sensors (45 minutes)
	* Design Notebook (5 min)
* Crafting, programming, and debugging (155 minutes)
	* Design Notebook (5 minutes)

### PORTFOLIO
* Portfolio Formation (110 minutes)
* Human Sensor Demos (55 minutes)

## Student Activities:
* Participate in project introduction
* Brainstorm human sensor project ideas
* Participate in portfolio introduction
* Design their Human Sensor Project (aesthetic design, circuit design, storyboard for code)
* Respond to Design Notebook entry
* Craft and debug light portion of project
* Respond to Design Notebook entry
* Test aluminum foil sensors
* Debug existing code
* Design and craft aluminum foil sensors
* Respond to Design Notebook entry
* Craft, program, and debug project
* Respond to Design Notebook entry
* Assemble portfolio
* Demo human sensor project to class

## Preparation:
* Before the project begins, it is helpful to iron aluminum foil to the iron-on adhesive in large sheets. These will be necessary for students’ patches.

## Teaching/Learning Strategies:
### Introduce Project (20 min)
* Project can modify an existing textile object like a hoodie, a stuffed animal, or something flat like a placemat, or can be made from scratch using felt. 
	* Demo teacher project
		* Point out the aluminum foil sensors and how the circuit between them has to be complete for the project to work
		* The sensors give different readings, just like the light analog sensor
		* Larger sensors usually give a wider range of values
* Talk about humans as conductive entities (we’re mostly made of water!). Computers can measure the electricity we conduct with our human body.
	* Make connections to Human-Computer Interaction (can connect to other types of wearables such as Fitbits or heartrate shirts)
	* If making a wearable, where would be appropriate places to put patches that people might touch?
* Share Human Sensor Sample Rubric

### Brainstorming (25 min)
* Have each student take a few minutes to come up with many different project ideas that can be used by them or someone else in the class.
* Have students share their ideas with elbow partners.
* Students will pair-share a few ideas with the whole class. They can be written on the board so undecided students can get inspiration.
* Have students decide what they want to do for their project. If they decide to use something from home, they should bring it in for the design phase.
### Introduction of Portfolio (10 min)
* Introduce the idea of the portfolio. Instead of a test or just a working project, the final evaluation of this project will include the project itself and a reflective “portfolio” where students can share things that went well, issues they had to address, and tips and tricks for future students working on this project.
	* See [ Portfolio Description](https://docs.google.com/document/d/1mefY64H6t2_xuC7kTYg9PHVDPmwTvear3KIQr9NQA_o/edit?usp=sharing)  and  [Sample Portfolio Rubric](https://docs.google.com/document/d/1CIimhNCREzHtE7vMdOQguVXKFjyI6IVo-X3h8uzvzJI/edit?usp=sharing) .
* Share the  [exemplar portfolio](https://drive.google.com/file/d/1l46nigRC0GXzgdMIgzYfK9_quhHlAMaD/view) . Feel free to use the  [Tips for Using Evidence handout](https://drive.google.com/open?id=1c5OrpDxdAxTFdpyYyZM-Jg7v6ZjdJXNR)  to help guide the discussion. Discuss as a class:
	* What makes a good portfolio? What helps you to understand the challenges people worked through?
	* What helps to make “evidence” understandable? (I.e., annotating pictures, putting an arrow to problem areas)
	* What could help you illustrate your progress? (taking pictures every day, taking screenshots of the code with error messages, noting things that you fixed along the way)
* Students may want to be especially aware of things that don’t go as they planned, changes they make, and solutions they come up with. These will be written out for several journal questions which they can use to make creating the portfolio easier. They can also take pictures during the creation of the project to use later.
* They should keep all versions of their circuit diagrams, journal responses, and any other things they want to note.
* /Every day before leaving class/: Take a picture of your project or save a version of your code. These can be used as artifacts in the portfolio.
### Design Human Sensor Project (50 min)
* Have students create a rough aesthetic drawing that focuses on design (what the project will look like, where electrical components things will be placed).
	* This should include the shape of their aluminum foil patches (which do not have to look the same, though should be of appropriate size for good conductivity - *at least* one-inch in diameter, bigger is generally better)
	* Have students take a picture of their drawing!
* Have students create a circuit diagram (blueprint):
	* Labeling the pin number next to each component and indicating negative and positive lines in different colors will make crafting and programming easier.
	* Have students take a picture of iterations of their design and circuit diagrams.
	* **WARNING: Do NOT use the 3V for anything. Ever.The voltage is too high and will burn out your components!**
	* The other aluminum foil patch should be connected directly to a negative pin. 
		* **TIP:** Other components can be connected to the negative patch or the specified GND pins as a ground
	* Other pins on the micro:bit can be made into additional grounds to make connections easier.
		* Just program the pin as OUTPUT and digitalWrite it to be LOW.
		* If students do this, make sure they indicate these changes clearly on their blueprint
### Design Notebook:
Based on your design, what are some things you’d like to keep in mind while crafting your Human Sensor Project? (5 min)

### Crafting and debugging of lights (105 min)
* Have students complete #1, #2, and #4 of  [Human Sensor Storyboard.pdf](https://docs.google.com/document/d/1UkhNSXk0uk0r5IxKnGA6rXNECIq7-f8SXIlXLGEw78E/edit?usp=sharing) 
* Have students sew all of their lights and the micro:bit, following their blueprints.
* Testing human sensor project lights:
	* Students should test each light with a simple program that just turns them on. They can use  [ECS_HumanSensor_Starter_BASIC.py](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/ECS_HumanSensor_Starter_BASIC.py)  as a starting point for their program.
	* Have students debug as necessary (lights that don’t turn on due to faulty sewing, etc.).
	* You can use this as an opportunity for a class discussion: Why is it useful to test your lights just by turning them on (as opposed to creating a blinking pattern)?
	* NOTE_: Students often have a hard time _breaking down a problem_into testable parts. ~Simply turning the lights on~, without coding for sensors or complex lighting patterns, can isolate whether the circuitry is functional. ~Remind students of the problem solving strategies in Unit 2!~ *Design Notebook:* Choose one or more of the following questions to answer (5 min):
* What were some modifications you had to make in your design?
* What were some bugs you had to fix and how did you fix them?
* What was one or more of your biggest challenges so far?
* *Cue students to remember that they can use these answers in their portfolio.*

### Exploring aluminum foil sensors (30 min)
	* Have sets of foil patches (enough for 1 set per pair of students)
		* A set would be two similar sized patches
		* Have various sized sets: small, medium, large, or extra large (optional)
	* Distribute a set of foil patches to pairs of students. 
	* Connect one of the student’s partially-completed micro:bit project using alligator clips to the provided sensors. 
		* Have each pair load the code for reading the human sensor patches:  [ReadYourHumanSensor_SAMPLE.py](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/ReadYourHumanSensor_SAMPLE.py)  
		* Invite students to connect patches based on the code. One patch must be connected to ground (negative). 
	* Class Discussion: Experimenting with patches while looking at sensor readings (Consider adapt the following questions & experimentation)
		* What happens when one of you squeezes both patches? 
		* What happens when you touch the patches together? Why do you think it goes down that low? 
		* What happens if each of you put one hand on one and then hold hands? [Optional but quite fun to experiment with]
	* Testing sensor ranges
		* In pairs, have students complete the first row in  [Testing Aluminum Foil Sensors handout](https://drive.google.com/open?id=1P7thCNTanTWcd66WFMksBdmgC42a-Uh0xQbfdEI3UDA) . 
		* Leave this form at each computer (either digitally open, or physically in front of the computer).
		* Each pair will then rotate to others’ projects, writing down the ranges on the form at each computer as they squeeze. Students should cover as many stations as they can within a limited amount of time.
		* Have students return to their original stations and look at the results of their classmates on the computer.
	* Class discussion:
		* As a class: Invite students to share the overall ranges that each group came up with (students may note some variance amongst individuals). 
		* Ask students the following questions:
			* Why are these ranges different? 
				* Answers might refer to the size of the patches or individual’s personal conductivity.
			* Is there a relationship between the patch size and the number? Talk to your partner about that.
	* Number line discussion:
		* Draw a number line on the board to talk through how students can translate the possible ranges on their sensor to useable ranges that they can use to program different effects
		* Ask students the following questions:
			* Where might you put different ranges, such as “not touching” or “squeezing really hard”? 
			* How can you write those mathematically? (i.e., with >, <, = expressions) 
	* Students complete the handout in pairs:
		* Tell students to take a look at the ranges that were written on their spreadsheet and to think about what ranges would be good for all users. Ask, “If you wanted everyone in this room to use this project, what would be the best ranges for the different patterns? Talk about this with your partner, then type some numbers in.”
		* Groups can come up with appropriate ranges and accompanying descriptions they would use for these sensors. Descriptions can be in their own words such as “not touching” or “lightly touching” 
	* Class discussion:
		* Have students share answers to questions at the bottom of the handout
		* Ask what existing code could help us manipulate the conditionals for our human sensor projects?  
			* Guide them to the light sensor code from Day 19.
	* Optional extension: Students could begin coding some lights to work with the practice sensors, if they figure out the ranges quickly [they could use the light sensor code as a model for how to do this.].

### Debugging activities (35 min)
	* Assign pairs to work on one of the following (distribute them across different pairs) “ [Debugging Fun Sensor1](https://drive.google.com/open?id=1DipMasLPhMleB3bXAzBmJLpYbstvji97asVoSn4YgLs) ,” “ [Debugging Fun Sensor2](https://drive.google.com/open?id=1fY6VGkhvFSbEjFq8zjdmC2jslWES7y1PoPegmmgBQBI) ,” “ [Debugging Fun Sensor3](https://drive.google.com/open?id=1Zzs2d98KmZs4ZI_p1I159rnk0cBLRcqRyipzZAZNg_U) ,” or “ [Debugging Fun Sensor4](https://drive.google.com/open?id=18JtNnBOQo2jnodbg8JvRNMlqr9_69VbFfZ-nSs-rWyk) ”.
		* Have them complete #1.
	* Have students load the corresponding code files, which they can test using their own Human Sensor project :  [debuggingFunSensor1 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor1.py) ,  [debuggingFunSensor2 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor2.py) ,  [debuggingFunSensor3 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor3.py) , or  [debuggingFunSensor4 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor4.py) 
		* If they use their own Human Sensor Project, make sure to remind them to modify the pin numbers to match their project in the Naming Section. Then have them run the code and answer #2.
		* Alternatively, you can run the program for the students as a whole class and have them complete #2.
		* Have students complete their debugging assignments.
	* After finishing, have each pair join another pair with the other debugging assignments and share their scenarios and answers.
	* See  [Debugging Fun Sensor1 solution](https://drive.google.com/open?id=1-lc_NSOBkt1GwX4hVZSpAhqcDCF9lIHGLrDglX8NCPU) ,  [Debugging Fun Sensor2 solution](https://drive.google.com/open?id=1gOJcJxnOFnzLQnc8ykgJmmtqBfzWuj_JY39SRlpZnL0) ,  [Debugging Fun Sensor3 solution](https://drive.google.com/open?id=1OLjao6dSUaSsyhaOkB-I3gZvWu9Ymhpwi8BNGyX6We0) , and  [Debugging Fun Sensor4 solution](https://drive.google.com/open?id=1SLCQNYANPEVLxjwYByS3-d_fQxvHnuSI0NpFQbQJ2qo) .

### Creating & testing aluminum foil sensors (45 min)
	* Set up an ironing station. Have students craft the aluminum foil patches for their individual projects, iron them on, and sew their sensor circuits. Have students debug as necessary (e.g., short circuits, loose stitches, patches that are too small).
	* Using the earlier activity/handout from “Testing Aluminum Foil Sensors” (see below) as a guide, ask students to test their own patches and write down the minimum and maximum ranges they can achieve. Students define appropriate ranges for their light behaviors and insert them in #3 of their  [Human Sensor Storyboard.pdf](https://drive.google.com/open?id=1UkhNSXk0uk0r5IxKnGA6rXNECIq7-f8SXIlXLGEw78E) .

### Design Notebook:
Write down/diagram some tips for crafting projects that use aluminum foil sensors. (5 min)

### Finish crafting, programming, and debugging (155 min)
	* Have students complete their  [Human Sensor Storyboard.pdf](https://drive.google.com/open?id=1UkhNSXk0uk0r5IxKnGA6rXNECIq7-f8SXIlXLGEw78E) 
	* Have students finish crafting, programming, and debugging their human sensor projects.
		* If students need more guidance programming the ranges for their senses they may use:  [ECS_HumanSensor_Starter_MOREHELP.py](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/ECS_HumanSensor_Starter_MOREHELP.py) 
	* Remember to have students take pictures regularly and jot notes in their Design Notebooks about changes they make.

### Design Notebook: 
Reflecting on your project, how did it turn out compared to your original plan? What changed? (5 min)

### Portfolio Formation (110 min)
	* Re-introduce the  [portfolio assignment](https://drive.google.com/open?id=1mefY64H6t2_xuC7kTYg9PHVDPmwTvear3KIQr9NQA_o)  (can be passed out as a one-page handout, see below). There are three sections: description of final project, description of process (revision or challenges), and reflection. 
	* Teacher may want to re-model sample portfolios or sections of them. Ask students to remember what makes a portfolio helpful for the viewer. If helpful, use the  [exemplar portfolio](https://drive.google.com/file/d/1l46nigRC0GXzgdMIgzYfK9_quhHlAMaD/view)  for reference again. Share the  [Tips for Using Evidence handout as a reference for students](https://drive.google.com/file/d/1c5OrpDxdAxTFdpyYyZM-Jg7v6ZjdJXNR/view?usp=sharing) .
	* Have students compile their artifacts, and choose which challenges or revisions they want to write about. 
	* See  [Portfolio Sample Rubric](https://drive.google.com/open?id=1CIimhNCREzHtE7vMdOQguVXKFjyI6IVo-X3h8uzvzJI) 

### Share Human Sensor Projects! (55 min)
	* Have students share their human sensor projects as a capstone to the unit. 
	* Options:
		* Gallery walk or e-textiles show. Have students walk around the class, interact with projects. For feedback: Put a piece of paper by each project and ask students to write down something they like
		* Have students do a brief show and tell (if time is a problem, use a timer for 1-2 min per student). 

## Resources:
* Materials for each student: micro:bit, computer, micro usb cable, Li-Po battery, ~6 LilyPad LEDs, pre-ironed aluminum patches
* Materials for each table groups: craft glue, thread wax, conductive thread, sewing thread, seam rippers, rulers, black and red pens, scotch tape, alligator clips, felt sheets and scraps of various colors
* Human Sensor Rubric:  [Portrait formatting](https://docs.google.com/document/d/1d4-_XQuok6nImBlOTVKTx_G97EpNXi52cUcEU8VCesA/edit?usp=sharing) ,  [Landscape formatting](https://docs.google.com/document/d/1pscRdUooy7ft11DNdZS_K_xFQDPStqIrEJD0L0dz7BU/edit?usp=sharing) .
*  [Human Sensor Storyboard.pdf](https://drive.google.com/open?id=1UkhNSXk0uk0r5IxKnGA6rXNECIq7-f8SXIlXLGEw78E) 
*  [ReadYourHumanSensor_SAMPLE.py](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/ReadYourHumanSensor_SAMPLE.py) 
* Testing Aluminum Foil Sensors (below)
*  [Human_Sensor_Starter_Basic code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/ECS_HumanSensor_Starter_BASIC.py) 
*  [ECS_HumanSensor_Starter_MOREHELP code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/ECS_HumanSensor_Starter_MOREHELP.py) 
* Example:  [example human sensor project code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/example/example.py) 
*  [Debugging Fun Sensor1](https://drive.google.com/open?id=1DipMasLPhMleB3bXAzBmJLpYbstvji97asVoSn4YgLs) 
*  [debuggingFunSensor1 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor1.py) 
*  [Debugging Fun Sensor1 solution](https://drive.google.com/open?id=1-lc_NSOBkt1GwX4hVZSpAhqcDCF9lIHGLrDglX8NCPU) 
*  [Debugging Fun Sensor2](https://drive.google.com/open?id=1fY6VGkhvFSbEjFq8zjdmC2jslWES7y1PoPegmmgBQBI) 
*  [debuggingFunSensor2 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor2.py) 
*  [Debugging Fun Sensor2 solution](https://drive.google.com/open?id=1gOJcJxnOFnzLQnc8ykgJmmtqBfzWuj_JY39SRlpZnL0) 
*  [Debugging Fun Sensor3](https://drive.google.com/open?id=1Qi-5FiHuuOLuC6nA2wtCQ4teBNDWFp5w7g5mg6pHFMA) 
*  [debuggingFunSensor3 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor3.py) 
*  [Debugging Fun Sensor3 solution](https://drive.google.com/open?id=1OLjao6dSUaSsyhaOkB-I3gZvWu9Ymhpwi8BNGyX6We0) 
*  [Debugging Fun Sensor4](https://drive.google.com/open?id=18JtNnBOQo2jnodbg8JvRNMlqr9_69VbFfZ-nSs-rWyk) 
*  [debuggingFunSensor4 code](https://github.com/jimmy0017/etextilesresearch/blob/master/20_Human%20Sensor%20Project/debuggingFunSensor4.py) 
*  [Debugging Fun Sensor4 solution](https://drive.google.com/open?id=1SLCQNYANPEVLxjwYByS3-d_fQxvHnuSI0NpFQbQJ2qo) 
*  [Human Sensor Portfolio Assignment](https://drive.google.com/open?id=1mefY64H6t2_xuC7kTYg9PHVDPmwTvear3KIQr9NQA_o)  
*  [Exemplar portfolios](https://drive.google.com/open?id=1l46nigRC0GXzgdMIgzYfK9_quhHlAMaD)  
*  [Tips for Using Evidence handout ](https://drive.google.com/file/d/1c5OrpDxdAxTFdpyYyZM-Jg7v6ZjdJXNR/view?usp=sharing) 
*  [Portfolio Sample Rubric](https://drive.google.com/open?id=1CIimhNCREzHtE7vMdOQguVXKFjyI6IVo-X3h8uzvzJI) 
