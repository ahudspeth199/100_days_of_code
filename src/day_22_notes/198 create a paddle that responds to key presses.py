"""
So now that we've created the screen we're ready to go ahead and create and move a puddle.
So the paddle that we're going to create is going to be on the right side.

It's going to have a width of 20, a height of 100 and be positioned at 350 pixels on the X-axis and then 0 on
the Y-axis. So this is the sort of positioning we're looking for.

And additionally, we should be able to hit the up and down keys on a keyboard to move the paddle.
Each key press should move the paddle up or down by 20 pixels.
Have a think about how you might create the code for this and pause the video and complete the challenge.
"""
# My Solution
import turtle
from turtle import Turtle
#starting_position = (350,0)
x_pos = 350
y_pos = 0

turtle.shape('square')
turtle.shapesize(stretch_wid=20,stretch_len=100)
turtle.color('white')
turtle.goto(x_pos,y_pos)
"""

All right. So to create this paddle, it's going to be created as a turtle.
So let's go ahead and create our paddle from the turtle class and I'm going to
set the paddles shape to a square.
In order to stretch it so that it's 20 by 100 pixels, remember that all turtles start off as 20 by 20
so that means in the width we have to stretch it by five, and in the length, we leave it as it is in order to
make it 100 by 20. So let's go ahead and hid up paddle.shapesize
which is what we've been using so far. And then in terms of the stretch width,
we're going to make that five. And then the stretch length is going to be one.

Now we have to make sure that our paddle has a color of white
so that it's actually visible when we run our code. And you can see there it is, there's our paddle. And as always,
it gets initialized in the center at the coordinate (0, 0).

So in order to move it to the position we want to, we have to get it to go ahead and pen up,
and then we can tell it to go to the position that is 350 by 0, so 350 on the X-axis and 0 on the Y-axis, like that.
"""
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

screen.exitonclick()
"""

Now, the next thing we need to do is figure out how to get it to move up and down.
So, of course, we need some sort of way of getting our screen to listen for keystrokes. We're gonna call screen.listen
and then we're going to call onkey in order to listen for the "Up" key.
And then when that happens, we're going to get the paddle to go up. 
Now, remember as always, when you were using a function as a parameter, you don't want to add the parentheses. 
If you do, it won't work. 
"""
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

screen.listen()
screen.onkey(go_up, "Up")

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

screen.exitonclick()
"""

Now let's create our go_up function. And this function is going to take our paddle and move it so that it goes to a new position. 
"""
def go_up():
    paddle.goto()
"""

The new exposition is X not going to change, The only one that's going to change is the Y position. 
So the Y position is going to be the paddles current ycor, but it's going to go up, so it's going to need to plus let's say by 20.
"""
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto()
"""

Now we can tell the paddle to go to its current paddle.xcor.
So we're not changing that. And then to go to the new Y position.
"""
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
"""

Now, this go_up function is going to be called whenever the Up key is detected.
"""
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

screen.exitonclick()
"""

And if we copy this and we make a similar version of this function,
which is called go_down and we can subtract 20 instead.
So now we can copy this line and make it call go_down when the down arrow key is detected.
"""
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, 'Down')

screen.exitonclick()
"""

So now we've created our paddle and when I hit up, it goes up, when I hit down it goes down. 
And this completes the first part of the challenge.

But here's a question. 
When I hit run, you can see that the paddle first gets created in the center,
and then it moves to the location where it needs to go to, which is 350 on the X-axis, 0 on the Y-axis.

How can we get rid of this animation so that we don't have to look at the paddle move to the position?
Have a think about what you've learned in previous lessons and see if you can solve this problem. 
"""
# My Solution
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(2)
"""
# Instructors solution 

All right. So you might remember from previous lessons that there is a tracer method on the screen which controls the animation.
And in order to turn off the animation, we can put a zero in that method.

But when we run our code, as it is right now, you'll see that there's no animation.
There's not even a paddle of showing up anymore. Remember that when you turn off the animation,
you have to manually update the screen and refresh it every single time. 
To do that, we'll need some sort of a while loop.

And the while loop is going to check for some sort of variable.
So let's create a variable called game_is_on and set it to true and while the game is on,

then we're going to call screen.update. Now, if I run the code again, you'll see that my paddle
now goes directly from the center to the position because the first thing
that happens is the animation gets turned off, the paddle then gets created in the background
and then finally it gets to this point where we actually update the screen and
show everything that's happened in the background so far.
"""
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(0)

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
"""

Did you manage to complete this challenge and create the paddle and get it to move up and down using the keystrokes?
If not be sure to review some of these methods in the turtle documentation and
have a play around with the code until you're fully happy with what's going on so far. 

Now, if you had created the paddle in a separate file as a separate class, don't worry. We're going to do that next.
We're going to refactor this code so that it's fully compliant with Object Oriented Programming. 

But if you've already done it, then you're just one step ahead. And that is where we're heading to in the next lesson.