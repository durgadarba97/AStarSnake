# AStarSnake

[![Run on Repl.it](https://repl.it/badge/github/durgadarba97/AStarSnake)](https://repl.it/github/durgadarba97/AStarSnake)

This is my first exploration in trying to automate the game snake. 
In the folders you find the Snake file that's used to house a lot of the main classes, 
a world file that's used to house the gameplay and game states, and an A* file that's used to 
house a alot of the automation aspects of the snake. If you want to run the game itself, run the
World.py file. I have to be honest though, this isn't the most effecient way to write program and 
I'll probably push a lot of things in the future to fix the big-O. 

The gradient branch is where a lot of my test code in making a gradient calculation is going. 
If you check out the notes folder, you can see my thought process and notes on everything. 
I'm not really sure if this is a good way of doing it and I'm definitly second guessing myself on 
many decisions, but so far it's working out in my favor. Also, using a gradient to calculate "closeness"
of the snake in one region as opposed to another isn't a method I've learned how to do or even thought about
doing in the past. 

## Update March 23, 2020
So it's been a while since I've worked on this, but I've leanred all about coding design and organization in the
past year so here's how I'm rewriting this. 

Firstly, I want to make this much more object oriented than I orginally designed it. I'm doing this by
implementing it like this:


                                               :--------:
                                              |    AI    |</br >
                                              |:--------:|</br >
                                              |Game Logic|</br >
                                              |:--------:|</br >
                                              |   GUI    |</br >
                                              |:--------:|</br >
                                              
Essentially, game logic abstracts the gui and lets me not have to worry about pixels or working with pygame when 
coding the logic. The AI then implements the game logic and acts as if a regular playing the game. I've found this
method to be a lot cleaner than what I had before. This also let me add the "no gui" feature. To run the game, 
if you type "python3 ./GameLogic.py nogui", it'll let the game logic run on it's own without spinning up the GUI. 
This feature needs more work, but it'll let me run it on AWS to train the AI.

Finally, I'm rethinking the whole gradient descent problem. I realized in order to reorganize the snake, I can run
A* so that the snake takes the longest path to get to the food instead. I can make the neural net so that the snake
takes in length, density, and distance from the food as input nodes and decides between taking the longest or
shortest path. Tbh, I have I long way to go before I implement this and I still need to figure out the density thing.


