"""
In the last lesson we created and managed to move a paddle up and down.

Now in this lesson, we're going to figure out how we can create another paddle,
but we don't want to repeat all the code that we've written so far.

So we're probably going to need the help of a separate paddle class.
So if you haven't already created your paddle inside a separate file and a separate class,
then this is the time to refactor your code so that you can create
another paddle object from the puddle class easily and effortlessly.
Here's what we're aiming for.

We're aiming to get rid of all of this paddle related code and move it into a separate paddle class.
"""
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
"""

And then subsequently we want to be able to create a right paddle simply by creating it from the paddle class.
And then we can create a left paddle from the panel of class. 
"""
r_paddle = Paddle()
l_paddle = Paddle()
"""

Now because the right paddle has a different coordinate from the left paddle,
we'll need to pass in the position of the right and left paddle as a tuple.
So we might say something like the X will be 350 and the Y will be 0.
And on the left paddle, the X will be -350 and the Y will be 0.
"""
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
"""

So have a think about how you can make this code work:
"""
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
"""
and refactor this code:

"""
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
"""

into a separate paddle class
and this paddle class should inherit from the turtle class.

Overall, our program should work pretty much the same as before. The only difference being that we now have a left pedal
which can move up and down with the w and s keys on the keyboard.
Pause the video and try to complete this challenge.



All right. So the first thing we're going to need is a new file,
which is going to be called """paddle.py""" and paddle.py is going to need the
turtle class from the turtle module. So let's go ahead and import it.
And then I'm going to create this Paddle class, and of course, all classes start off with a capital letter.

Now, this class is going to take all of this paddle creation code and it's going to carry it out 
when we initialize a new paddle object. This paddle object, in order for it to be a turtle object, 
we're going to get it to inherit from the turtle class like this. And in order to get all of the abilities, the methods, 
and the attributes of the turtle class,

we need to get this superclass to initialize itpaddle.

The next thing we're going to do is figure out how we can get our paddle to

change its shape, change its color and all of these other things.
"""
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        paddle = Turtle()
        paddle.shape('square')
        paddle.color('white')
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(350,0)
"""
So we can get rid of this line entirely because our paddle class is now the same as a turtle class. 
"""
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        paddle.shape('square')
        paddle.color('white')
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(350,0)
"""


And then for the rest of these, instead of writing paddle.shape or paddle.color,
we're going to hit command R or simply go to edit, find, and then replace,
and you can take a look at the shortcut on your computer of how to get hold of this replace screen. 
So what I want to replace is everything that is paddled. here in my code, and I'm going to replace it with paddle.,
"""
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_self()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350,0)
"""
because now we're inside the paddle class which is effectively the same as a turtle class with some added extras.
We can tap into our methods and our attributes by simply using the self keyword.

Now, the very last thing we need to do in order to make this work is to go ahead and import our paddle from the paddle.py.
And once we've imported it, we need to address this warning.

Notice how it's highlighting this area and it's telling us that this is an unexpected argument because the paddle
class doesn't actually take any inputs when it's initialized.

It's just got the self here. But in fact, we do need a position being passed over.
"""
class Paddle(Turtle):
    def __init__(self, posistion):
        super().__init__()
        self.create_self()
"""

So this position is going to determine where the paddle is going to go to,
"""
class Paddle(Turtle):
    def __init__(self, posistion):
        super().__init__()
        self.create_self()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posistion)
"""
because remember the left paddle is going to have a different coordinate from the right paddle.
So now that we fixed that, this is now completely valid code.
And if we run our code as it is, you'll see our paddles being created and looking exactly the same way as before
but now we've got one extra paddle. Going down here with our go up and go down methods,
ideally, we would want them to live within our paddle class.

So we want them to be methods inside this class.
And remember that methods always have a first attribute as the paddle.
Now, in addition, we have to, again, replace this paddle. with paddle. so that it's actually referring to the object
that's created from this class to get its Y coordinate or get its X coordinate.
"""
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, posistion):
        super().__init__()
        self.create_self()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posistion)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
"""
Now, coming back to our main.py, we'll have to modify this code a little bit because this go_up and go_down
function is now gone, and instead, we now have the r_paddle.go_up and r_paddle.go_down.

So the right paddle is going to be controlled by the up and down keys,

but the left paddle, we can get it to be controlled by some other keys. Now, in our case,
I'm going to choose the 'w' to go up and the 's' key to go down.
So we're going to need another set of these screen.onkey method calls.

But in this case,this is going to get the left paddle to go up and the left paddle to go down. And
to go up is controlled by the 'w' key and to go down is controlled by the 's' key. So now,
if we run our code, you can see that when I moved w it goes up, when I move
s it goes down, and up and down moves the right side of the paddle.
"""
r_paddle = Paddle((350,0))
l_paddle = Paddle((350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
"""

So notice how now that we've refactored our paddle related code into a completely separate class, 
firstly, our main.py is now a lot simpler. It's clear of all of this paddle related code.

And on top of that, if I wanted to create a third paddle let's say I wanted you to create a top paddle for some reason,
then all I have to do is just call the paddle class and then pass in a tuple for the location of this paddle.
So let's put it at, I dunno, 100 by 100. If I hit run,
"""
from turtle import Screen
from paddle199 import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((350,0))
top_paddle = Paddle((100, 100))
"""

you can see there's a third random paddle and I didn't have to write
any of this extra code or any of the related methods. We can create as many of
these paddles as we want because we've now got this paddle class.

So with these examples, I hope you're getting the sense of how important classes are and just how
important they are when it comes to the development of a more complex project like this pong game. 

Now in the next lesson, we're going to continue building out our program and we're going to create our
ball class and get the ball moving.