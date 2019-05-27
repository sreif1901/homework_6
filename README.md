# homework_6

Homework 6.1
Let's make our program for basketball and football players a bit more useful. Add an option that a user can enter data (via input()) and at the end of the program the data gets saved in a text file (using json library).
Hint: you can easily convert object into a dictionary via the in-built __dict__ method. Try this in your program: lebron.__dict__ (note that there are 2 underscores on each side).
Use the knowledge that you gained while building the Guess the secret number game.

Homework 6.2: Model for "Guess the secret number" results
Design your "Guess the secret number" game in a way that every result will be stored as an object.
Create a model called Result, that takes the following data:
score
player_name
date
Then save the objects via json into a results.txt file (use the __dict__ method, like in the previous homework).

note: 
Players.txt belongs to 6.1
score_list.txt belongs to 6.2 (instead of results.txt)
