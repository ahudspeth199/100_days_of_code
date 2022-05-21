"""
The first challenge is pretty simple. We're just going to create the starting screen.
It's going to be a screen that has a height of 600 pixels and a width of 800 pixels.
It should be black in terms of the background color, and it should stay on the screen until we click on it.

So using what you've learned so far, go ahead and set up the starting code for our project.
"""

# my solution

from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')

# Instructors solution
"""
All right. So I've created a brand new project which I've called pong-game, and I've created a main.py. Now,
the first thing I'm going to do is I'm going to import a screen from the turtle module.
And then I'm going to create a screen object from the Screen class, and then I'm going to set the background color to black.
And then, of course, we'll need to set up the screen so that it has a width of 800 and a height of 600.
So now if I run this code as it is, you'll see that it flashes up and it disappears.
So of course we need that exitonclick method.
As well as a final finishing touch, this is completely optional but it helps to identify the program,
we can change the screens title to say Pong.
And now when I run the code, you can see that this window now says pong.
So we now have our 800 by 600 screen, and we're now ready to head to the next step where we create our paddles.
"""
from turtle import Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

screen.exitonclick()




