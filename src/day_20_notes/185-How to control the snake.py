"""
So we've now managed to create a snake body, move the snake,
and we've even managed to put our snake related code into a separate class.
"""

"""
Now the next step is to figure out how to control the snake.
Now we're going to control the snake by using the up, down, left, and right arrow keys.


And we're going to be using our key bindings that we learned in yesterday's lessons 
to be able to translate this into a change in direction of the snake. 

In our code right after we create our snake: snake = Snake() 
we're going to call the screen.listen() method to start listening for keystrokes.

And the keystrokes """screen.onkey()""" that we're going to listen for are the up, down, left, and right arrow keys. 

Now those keys are described by a string. So it's a uppercase 'U' and then a 'p' so this would be up.
And then it's again, uppercase 'Down', 'Left', and 'Right'.
"""
screen.listen()
screen.onkey("Up")
screen.onkey("Down")
screen.onkey("Left")
screen.onkey("Right")
"""
These are the keys that it will detect, obviously the up, down, left, and right arrow keys on the keyboard.

The function that you're going to bind it to is going to be a function in the 
snake object and it's going to have the same name. So for example, it'd be snake.up,
and that will be triggered when the up key is pressed.
And then the same thing happens with snake.down when the down key gets pressed and then again with left and right.
"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
"""
"""

## Challenge 1
"""
Your job is to have a think about how you can create these methods up, down, left, and right, in the snake class
so that when the up key or the down key is detected, you can move the snake and change its heading accordingly.

## Note
So remember that up is going to be towards North, down is going to be South, left is going to be towards the left 
of the screen and right is going to be towards the right of the screen.

So have a think about the headings that we spoke about in previous lessons.

And if you need to, it might be worth just setting up a brand new project,
getting a turtle up and running and then setting it's heading from zero all the way to 360, 
just to see which direction it's actually facing.

If you managed to complete the challenge, you should be able to control the snake 
and even though it's going to continue moving forward,
you now determine which direction it moves in by using the arrow keys.

Pause the video now and see if you can complete this challenge.
"""

## Answer to Challenge
"""
All right. So I've already created all of these lines of code on the main.py:
"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
"""
 
which is going to get the screen to listen for these key strokes. And then when it detects it,
it's going to call these methods in the snake class.
"""

## Step 1
"""
So inside our snake class, let's go ahead and create those methods.

So we've got up,
"""def up(self):"""

down,
"""def down(self):"""

left, and right.
"""def left(self):"""
"""def right(self):"""
"""

## Step 2
"""
Let's think about how we can turn the snake up. In order to turn the snake,
the segment that we're most interested in is the first segment. That's basically the head of the snake.
So we could tap into self.segments and then get hold of the zeroth segment,
which is the first one, and then change its heading by calling setheading.
"""
def up(self):
    self.segments[0].setheading()
"""
"""

## Step 3
"""
And then we can tell it to, for example, if it's up, then it should actually be turning to the 90-degree direction,
which is actually towards North. 
"""
def up(self):
    self.segments[0].setheading(90)
"""
"""

## Step 4
"""
Now I'm going to go ahead and put a pass on all of these other methods,
just so that we can actually test our code and it doesn't give us any errors
because these functions are currently empty. Now, if you don't have the pass,
it won't like it because Python doesn't like the idea of empty functions. 
But now we can at least just test this one thing. 
"""
def down(self):
    pass

def left(self):
    pass

def right(self):
    pass
"""

So when we run our code, we should be able to hit the up key and you can see the snake changed direction. 
Let me just do that again. And this is because we managed to get the first segment, the head of the snake, to change
it's heading to 90 degrees and then the rest of the body will follow 
because it's continuously moving on every tick of the clock. So using this: """self.segments[0].setheading(90)"""
we can now set the rest of the methods.
"""

## Step 5
"""
But because we're going to need the head of the snake quite a few times in our
code, it might make sense to actually create a separate attribute.
So after we've created the snake, after we've got some segments inside this list, 
we can create an attribute called head: """self.head""" which is going to be the head of the snake:
"""
def __init__(self):
    self.segments = []
    self.create_snake()
    self.head
"""

And this can be equal to self.segments at index zero:  """self.head = self.segments[0]"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

Now, remember if you have this line of code:"""self.head = self.segments[0]""" above the create_snake: self.create_snake
it's probably going to error out because at this point the segments is empty
and if you try to get the first item from it, it's not going to allow you to.
So look at the positioning of the code here: 
        self.segments = []
                self.create_snake()
                self.head = self.segments[0]
"""

## Step 6
"""
Now, once we've got this set, we can go down here: """self.segments[0].forward(MOVE_DISTANCE)"""  and change everywhere
where we need to use the head of the snake. 
So for example, when we're moving the head forwards and when we're moving it up, left, down, and right. 
"""before
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)
"""
"""after
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
"""
"""

## Step 7
"""
Now we can set each of these headings.
Up is going to be a heading of 90, down is going to be 270, left is 180 and right is 0.
"""
    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
"""

These directions are just simply counter-clockwise.
So the turtle starts out pointing towards East and that's a heading of zero,
and then going anticlockwise, up is 90, left is 180, down as 270.
This can be easily verified just by testing out some numbers, right?
You could just put some numbers in there and then just try it out and see which
direction it goes and then you'll be able to figure it out.
But we've also mentioned this in previous lessons
so you could also go back and take a look at when we looked at the heading of the turtle. 

So now if I go ahead and run this, then you should see that I can now freely control the snake by going left or
right or down or up. And if you managed to do this, then you should consider yourself successful. 
"""

## Part 2
"""
Now, while I was testing this code, I realized that there's something about the snake game that we haven't really
accounted for. And it's the fact that the snake can't move back on itself.
It can't go forwards and then go the opposite direction because that requires the head to change directions.

And this is not allowed in the official snake game. So how can we code this into our game? 
"""

## Step 1 of part 2
"""
Well, we have to figure out when the head is pointing towards down direction, then we shouldn't allow it to go up. 
"""
    def up(self):
        self.head.setheading(90)
"""
        
And similarly, when it's pointing up, we shouldn't let it go down, when it's pointing right we shouldn't left it go left. 
"""
    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
"""
So at the top here, I'm going to create some constants.
I'm going to create a UP direction and it's going to be 90, DOWN direction is going to be 270, 
LEFT is going to be equal to 180 and RIGHT is going to be equal to 0. 
"""
from turtle import Turtle
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
"""
"""

## Step 2 of part 2
"""
So now that I've got all of these as constants, 
I can go in here and set the heading to instead say UP when it needs to go up, DOWN, LEFT and RIGHT. 
"""
    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)
"""
"""

## Step 3 of part 2
"""
In addition, we're going to do an if check. So we're going to say if the current self.head.heading
is not equal to down, well, in that case, it's allowed to move up. 
"""
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
"""

So this way, it just means that if the current heading is pointed down, it can't move up. But for all other directions,
if it's already moving up or left or right, then it can change the heading to up.

Now be really careful here because it's not just self.head.heading()
it's actually heading as a method because remember that the head of the snake is the first segment of our 
list of segments and each segment is a individual turtle.

The turtle has a heading method which will give you a direction in terms of these 360-degree numbers,
and then we can use that to check to see if it's equal to down. And if it is, then it's not allowed to go up.
"""

## Challenge 2
"""
So using this logic, see if you can complete the rest of the three methods so that when you run your
code, you can turn in all directions.

But when you're facing one direction, you can't go backwards, like this.
"""


## Challenge 2 Answer
"""
Okay? Alright. So it's going to be pretty straightforward.

If it's already going up, then it's not allowed to go down. 
If it's already going right, then it's not allowed to go left. 
And finally, if it's already going left, then it's not allowed to go right.
"""
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
"""

So this way, even though our snake can move freely through the space, it can't go back on itself. And there we have it.
We've now managed to create our snake, get it to move and control it using our key presses.

Even though it seems like our game is still not quite there, we've already come so far. 
So this comes up to our hour mark and it's now time to take a break, refresh your minds,

look at some of the concepts that you might be confused about that we covered today,
especially this concept on main.py of using the update to refresh the screen, as well as using the timer
to delay the refresh so that we can control how often it happens.
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
"""

And then using our key bindings 
"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
"""


as well as separating all classes.


We looked at a lot of things today. Now, tomorrow, once you're rested and fresh and ready,
we're going to be finishing up the snake game. And we're going to be learning about inheritance as well as slicing
and we're going to be building out the full functionality of this game. So I hope you're looking forward to it. 
I certainly am. I'll see you tomorrow.
"""