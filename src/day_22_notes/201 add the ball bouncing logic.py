"""
Now we've done most of the easy parts, getting a paddle and a ball up and running on our screen.
The next few parts are going to be a little bit more tricky.

And the first thing we're going to tackle is how to detect collision when the
ball hits the wall at the top and the bottom and getting the ball to bounce.

Now, we only need to detect collision on the top and the bottom walls
because when the ball hits the right or of the left edges of the program,
it should actually be caught by one of the paddles. And if it isn't, then that means that player has missed the ball
and it's a point to the other side.

So we need to focus on how can we detect when the ball has collided with the top or bottom walls,
when has its position gone past a certain point that it probably is going to
collide with the wall.

We've done something similar in snake, but it's again
time to revisit this topic. Now on top of that, we have to figure out how do we get the ball to actually bounce?

And what does bouncing actually mean in terms of changing the position of the ball?
When the ball is constantly going up in the Y value and going up in the X value
in order to travel in this direction, what actually happens to the X and Y values when it bounces?

Which one gets reduced and which one stays constant?
Have a think about those questions and play around with some of those numbers
and see if you can complete this challenge by yourself.

If you get stuck or if you just want to check the answer,
then come back and I'll go through the solution with you.

## Note: The screen is 600px tall. Detect collisions with the top and bottom walls. Change the ball's movement direction
upon collision
"""
# My solution
"""


"""

"""
All right. So it's going to be inside our while loop where I'm going to be detecting the collision with the wall.
And in order to detect the collision with the wall, essentially,
what I'm going to say is that if the screen is 600 by 800, when the ball is at a Y position that is above 300,
remember 300 is half of 600, and the Y-axis goes from 0 to 300 and 0 to -300.

So once the ball is past 300,

then it's going to be way past the wall, right? So at that point,

I can be pretty sure that it's going to hit the wall

or it has it already hit the wall.

So that will be my criteria for detecting collision.

So it can say if the ball.ycor is greater than 300,

well in that case it's basically gone too far up and it's hit the top wall. Now,

in addition, I can add a or statement to say

if the ball.ycor is less than -300,

then that means it's gone too far down and it's hit the bottom wall.

So in this case, it needs to bounce.

So we need to figure out how to get our ball to bounce.

And we're going to create a bounce method in our ball class in order to tell it

how to do this. Firstly,

we're going to need to figure out a new Y because the Y coordinate needs to

essentially reverse. So,

whereas previously our Y coordinate was going up and up and up increasing each

time, when it hits the wall it needs to reverse direction.

So if it was increasing,

it needs to decrease. If it was decreasing, it needs to increase.

So basically we need the opposite of what it currently is. To do that,

the easiest way is to create a attribute

which I'm going to call x_move and another

which I'm going to call y_move.

These are going to start out at 10,

and every time we move our ball we're going to say,

self.xcor + self.x_move,

and plus self.y_move.

This basically hasn't changed anything.

It's just that every single time the ball moves,

it's going to increase in the X coordinate by 10 pixels

and also increased by 10 pixels in the Y coordinate. Now,

when we bounce however,

we need to change our y_move

so that it's the opposite in terms of direction of what it used to be.

So if it used to be +10 we want it to be now -10,

and if it used to be -10, we want it to be now +10. To do that,

all we need to do is multiply it by - 1.

So that means if y_move is currently equal to 10 and 10 is being added to the Y

coordinate, then this ball is moving upwards.

But when we reverse the direction by multiplying it by -1,

now that is now -10.

So we're now adding -10 to the Y coordinate

which is the same as subtracting 10. So this is some basic high school math

that's going to get our pong program to start moving in the right direction.

Now, back in the main.py under these conditions

when the ball has hit the top or the bottom,

we're going to get the ball to bounce.

And now if I hit run, you should see that when the ball hits the top screen,

it comes right back, exactly in the way that we want it to.

But the only thing that we might need to tweak

is look at how far it's gone before it actually bounces. It completely disappeared

of the screen before it actually makes a bounce.

So we can adjust these values accordingly.

So I think it works best that when we actually have it as 280.

So remember that the width of the ball is 20 pixels

so if we're 20 pixels away from the wall,

then that's pretty much where we need to bounce. So if I run this again,

you can see that the ball hits close to the wall and then it comes right back.

So this will take a little bit of thinking to get your head around it.

The best way to really understand this is to print out the values of the new_y

and also of the y_move

and also after you've modified the move in the bounce. Look at those numbers

and you'll eventually be able to understand what's actually happening to the

position of the ball. But effectively,

all that we're doing is we're defining an amount that the ball is going to move

by in the X and the Y axis.

We're adding that amount to the X and Y coordinates in order to move the ball.

And when the ball needs to bounce off the top and bottom walls,

we reverse the y_move number so that we get it to subtract instead of add.

And that moves it in the opposite direction.