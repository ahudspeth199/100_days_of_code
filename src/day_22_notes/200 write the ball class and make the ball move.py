"""
Now that we've created both paddles the next obvious step is to create the ball and get it to move.

So this ball is going to be created as a separate ball class and the ball object
that we're going to create from it will have a width of 20, height of 20, and it's
X and Y position will start out at the center of the screen,
so (0, 0). Now when the screen refreshes, the ball is automatically going to move on the screen and it's going to move up
and also to the right. So it's X and Y positions will change on every refresh of the screen.

So this is going to be a little bit more challenging and will require a little bit of thinking from your part.
But I want you to pause the video and give this problem a bit of thought and see
how far you can get in trying to get the ball to move to the top-right edge of the screen.
Pause the video and give that a go.
"""
# My Solution

from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):


        self.goto()
"""
"""

# Instructors solution
"""
All right. So to start off, this time I'm going to create a ball.py file and inside
this ball.py is where we're going to create our ball object.

So firstly, I'm going to import my turtle class and then I'm going to create my ball class
which is going to inherit from the turtle class. And then I'm going to do all of the usual initialization.

And now we're ready to create our ball class. This ball is going to, firstly, have a white color.
And in addition, it's going to have a shape that is going to be a circle. Now I know that in the original pong game,
the table tennis ball is actually a square. So you can keep it a square
if you want to be historically accurate, or you can change it to
a circle like I have here to make it look more like a ping pong ball.

Now, in addition, we're going to need to get it to pen up so that it doesn't end up drawing across the screen.
"""
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
"""

And now all we need is to initialize our ball from the ball.py and we're going to do that just below our paddles.
So I'm going to create a new ball object from the ball class.
"""
from turtle import Screen
from paddle199 import Paddle
from ball200 import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
"""
And now if I hit run, you'll see our circular ball show up in the center of the screen.

The next problem is how do we get the ball to move towards the top right corner of the screen?
So that's going to involve a change in the X coordinate as well as the Y coordinate. 

In our while loop here (on main200.py):
"""
game_is_on = True
while game_is_on:
    screen.update()
"""
where our screen is updating, we're going to call a method in the ball class which is going to be called move. 
"""
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
"""

And this move method (go to ball200.py) which we'll define now is going to be responsible for moving our ball.
"""
def move(self):
"""
And the way that it's going to move is it's going to increase on the X and also increase on the Y.
Let's create a new X coordinate which is going to be the current self.xcor plus a arbitrary amount. So let's say increase by 10.
And then the new Y is going to be the self.ycor increased by the same arbitrary amount. And then finally,
we can get our ball to go to this new X and new Y.
"""
def move(self):
    new_x = self.xcor() + 10
    new_y = self.ycor() + 10
    self.goto(new_x, new_y)
"""

So now when we run our code, you can see that our ball immediately goes off the screen to the top right corner. 

If we want the ball to slow down a little bit, we can do one of two things. 

Either we can go into the move method and change this 10 here to say a 1.
"""
def move(self):
    new_x = self.xcor() + 1
    new_y = self.ycor() + 10
    self.goto(new_x, new_y)
"""

That way, every time our loop runs, our ball will only move one pixel.
Alternatively, we can pause the loop for a short time during each iteration.vMoving the ball at a tiny amount does work,

but I'm going to go with the second option and import our time module.
Then I'm going to get our while loop to sleep for a little bit in between each of the updates.
So, I normally start off with just a 0.1 second sleep, and you can see now a ball moves at a more reasonable pace
and we actually have a chance of catching it with one of the paddles.
"""
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
"""

That's all there is to it. We've now created on the ball class, initialized a ball object and we've got the ball to move 
on every refresh of the screen.
"""