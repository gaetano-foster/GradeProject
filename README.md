# GradeProject
Unit 1.1 Project for AP CSP
It is a command line program that helps grade students.

## Goal
The goal of the project is to provide a simple and effective way to input grades for a class. All the user must do is input the different categories for their class (i.e. Participation, Quizzes, Homework), and put their grades in with the `put` command. This simplifies the grading process, as all the math is done for you. It is also convenient for giving you a quick, general idea of what your own grades might be if you have access to the grade book as a student.

## Planning Process
First, we went over a general idea of what we wanted the program to look like. Together, we came to the conclusion that a command prompt would be the most useful and effective way of implementing this program. Over time, we used a strategy in which every command would call a certain procedure, and we would have a function called `process_command` to process the user input and decide which function to call. The user's input would be stored in a list of strings called `args`, a shorthand for "arguments". Finally, it would be run in a loop that only terminates when the user tells it to.

Another strategy you could use is writing a GUI, like X2. This is more user friendly, but takes more effort and often external libraries. In other words, you can achieve very similar results for less work with a command prompt app. On the other hand, A GUI is much more user-friendly, which is a huge advantage for any production-ready application.

## Problems Solved
Initially, the dictionary `categories` was a list of tuples, but we came across a problem when we needed to be able to access categories by name and not by index. We solved the problem by changing the variable type to a dictionary, which allows this functionality (ex. `categories['Participation']`. We avoided many errors by being safe in the way that we code in advance. First, we included type checks and read all input before using it to ensure a lack of runtime errors. If, for example, a user would input the incorrect type, the command prompt will let them know that there is something wrong with their syntax. 
