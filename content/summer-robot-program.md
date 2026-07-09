---
title: "Summer Robot Program"
date: 2022-03-21T16:18:25+00:00
draft: false
author: "eric"
---

![](/uploads/12/2022/03/IMG_4216-700x525.jpeg)

In the summer, I run a program for High School and College students to learn about building and programming robots. The main robot we are working on is a small 6-axis lab robot, which was built in 1994. We completely replaced all of the power supply, controller hardware and software.

The program is very flexible, with all dates, times and tasks customized to the availability and interests of each student. Students will meet with me, in my home workshop in Pacific Beach, San Diego, 1 to three days per week for up to 12 weeks. 

![](/uploads/12/2022/03/IMG_4317-700x525.jpeg)

Drew measures the distances between joints to build a kinematic model

The robot has 6 stepper motors and one rotary encoder for each join, with custom software to drive the motors and read the encoders. The software is implemented in the [Robot Operating System](<https://www.ros.org/>), running on Ubuntu Linux on a Raspberry Pi controller. The steppers are driven by custom C++ code on a [Teensy 4.0 micro controller](<https://www.pjrc.com/store/teensy40.html>), with trajectory planning implemented in Python running on the Raspberry Pi. The system has several other Arduino controllers that run the power supply and teaching pendant. All of our code and design documents [are in Github](<https://github.com/orgs/Busboombot/repositories>). 

Because of the broad range of hardware and software, students can learn a variety of practical skills, including: 

  * Basic Arduino programming for the state machines in the controllers and power supply
  * Low level step planning and motion control and how to implement complex equations in very fast low level code. 
  * High level robot programming in Python and the Robot Operating System
  * The mathematical basis of inverse kinematics
  * Homing and localization
  * 3-D route finding in joint-space and 3-space. 
  * Professional software development, deployment and version control. 


I have been working with youth and student for the last 30 years. I've had interns in my companies and run the [San Diego Regional Data Library](<https://sandiegodata.org>), where I teach high school and college students data analysis using pro-bono data projects for non profits. I'm on the board of a non-profit programming school, the [League of Amazing Programmers](<https://jointheleague.org>), and am the Scoutmaster for [Boy's troop 506, La Jolla](<https://www.lajollatroop506.com/>). I take regular training for working with youth ( both state mandated training, and BSA training for Scouting ) and follow BSA Youth Protection guidelines. 

If you are interested in joining the program, you should have very strong technical skills, with prior experience programming, working with robots, building electronic hardware. Solid algebra skill is very important, and Calculus is important for the more advanced topic. I usually recruit students directly, but if you are interested and think you have the required experience, please contact me at eric@wp.do.cnshost.net.
