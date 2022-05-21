"""
So far, we've managed to get our starting segments for our snake to appear on screen.
And then we managed to get our snake to automatically move forwards and to
figure out a way for the tail of the snake to follow where the head is going.

Now it's time to tidy up our code a little bit so that all the parts that are

related to the snake's behavior and the snake's appearance go into a separate class. 
So that by the end of the whole project, we should end up with three classes; 

a snake class, a food class, and a scoreboard.

And all of these classes will be in separate files, managing only one thing.

And the goal of the refactoring is so that you could create a separate file called snake184.py, 
import the snake class that you've created in that file.
from snake import Snake
And then once you initialize this snake, it will do everything that we have so far and create our three segments snake
onto the screen. 
snake = Snake() ## this creates the snake

And then finally, while the game loop is running, 
we're going to get the snake to continuously move forward just by calling snake.move(). 
"""

## This is what you're aiming for:
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on: 
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
screen.exitonclick()


## Challenge
"""
Have a think about how you can take the existing code that you've got in the main184.py 
and extract all of the snake related functionality into a separate
snake class and make your main184.py end up looking like above:



The program should do the exact same things as before.
The only difference is how the code is organized. Have a think about this.

You might need to revise some of the things you learned about how to create
classes, how to create objects from the previous lessons.

But pause the video,I want you to give this a good try before you come back when we'll go through the solution together.
"""

## Step 1
"""
Alright.
So the first thing we need to do is of course, to create our snake class. And remember that in Python, 
class names are in Pascal case, so the first letter needs to be capitalized.
"""class Snake:"""

And then inside this class, I'm going to create my init.
"""def __init__(self):"""
"""

## Step 2
"""
Now the code in here is going to determine what should happen when we initialize a new snake object. 
So firstly, I'm going to take the starting positions and take it over to our snake184.py.
Now, I'm actually going to put this in as a constant. So right at the top, and remember that in Python,
the constants are named with all caps like this, and also with snake case with underscores separating each of the words.
"""STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]"""
"""

## Step 3
"""
Now we can use these starting positions inside our snake class to create our new snake. 
So we're going to need to move our segments over as well. 
So let's create a new attribute that's associated with our snake class called segments. 
And remember, we're going to need to use self when we're working within a class.
"""self.segments = []"""
"""

## Step 4
"""
After that, we're going to create our snake.
"""self.create_snake()"""

So I'm going to create a method called create_snake down here.
"""def create_snake(self):"""

And this method is going to do everything that we previously had over here, 
but we're going to move that into this method. Now there's a couple of things we need to change. 
Firstly, we change these starting positions into a constant, so let's make that: 
STARTING_POSITIONS

Second thing is that we need to import turtle into this file from the turtle module 
in order to use it to create a new segment.
"""from turtle import Turtle"""

And then finally, in order to refer to our attribute segments,
we have to say """self.segments""" and then append this new segment to our snake segments. This part is done.
"""
        self.create_snake()
        
    def create_snake(self):
        for positions in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(positions)
            self.segments.append(new_segment)
"""
"""

## Step 5
"""
The next thing we need to do is to get rid of this code and move it inside the snake184.py. 
            for seg_num in range(len(segments) - 1, 0, -1):
                new_x = segments[seg_num - 1].xcor()
                new_y = segments[seg_num - 1].ycor()
                segments[seg_num].goto(new_x, new_y)

            segments[0].forward(20)


So again, I'm going to create another method that's associated with the snake class called move.
"""
def move(self):
"""
So when the snake moves, it's going to look to this code to figure out how it should do that. 

Again, because we're inside our class, it's no longer just segments. It's now self.segments.

So let's go ahead and replace it in all the places where we have our red
underlines and now that's pretty much it for our snake class.
"""
    for seg_num in range(len(self.segments) - 1, 0, -1):
                    new_x = self.segments[seg_num - 1].xcor()
                    new_y = self.segments[seg_num - 1].ycor()
                    self.segments[seg_num].goto(new_x, new_y)

              self.segments[0].forward(20)
"""

## recap
So we created a new snake object and each time we do that, it creates a three-segment snake using the starting positions
which are declared at the top.
"""

## Step 6
"""
So in main184.py if we want the snake to show up on screen, 
then we're going to have to first import the snake class from the snake file,
"""
from snake import Snake
"""
"""

## Step 7
"""
And then we're going to create a new snake object from that class.
"""
snake = Snake()
"""
And once this line gets triggered, then we're going to be calling
create_snake and our three-segment snake will show up on screen like this.
"""

## Step 8
"""
Now the next step is: while the game is on, the screen is going to update every 0.1 second.
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
"""
So that's essentially what this is doing. It's saying that delay for 0.1 second and then refresh the screen.
And every time the screen refreshes, we're going to get the snake to move forwards by one step.

Now at the moment, on snake184.py under the move(self) method 
"""
self.segments[0].forward(20)
"""
each step is defined here as 20.
"""

## Step 9
"""
So again, I want to extract that into a constant up here, on snake184.py so we're going to call it the MOVE_DISTANCE
and we can set that to 20 and then change this to use the constant here.
"""
def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
    self.segments[0].forward(MOVE_DISTANCE)
"""
And the reason why we have all these constants is so that if we wanted to tweak our game,
say if we wanted the snake to start at a different position or for it to move further each time, 
then we don't have to dig through the body of our code. All we have to do is look at the top,
look at all the things that we can change and then change it accordingly.
"""
from turtle import Turtle
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
"""

"""
## Recap
"""
So now coming back to our code on main184.py, 
all we now really have here is just these few lines of code and everything that is snake related,
creating the snake or moving the snake is now abstracted into it's own class.

This way when something goes wrong with our snake, we know who's responsible and which file to dig through
to figure out the reason. 

Now, at this point, if we go ahead and rerun our code, you can see that our program works exactly the same as before.

Nothing should have changed and nothing should have broken ow because our game

isn't yet able to go into the game over sequence,

there's no way of stopping the snake other than hitting the stop button.

So don't worry if at this stage inside your console

you see a lot of red and it says things like keyboard interrupt,

or trace back errors. All of these are normal.

The thing that you're more concerned about is whether if, when you run the game,

whether if it actually works like it used to,

so namely your snake moving across the screen.

If it does exactly what it used to and your main184.py is now much simpler and

all of your snake functionality and behavior and appearance is now inside its

own class, then you have successfully achieved the goal of this lesson.
"""