from turtle import Screen, Turtle

## Step 6
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

## Step 4
screen.tracer(0)

"""
Now in this lesson, we're going to move on to the next step where we actually move our snake
automatically across the screen without having to do anything.
So this way the snake is continuously moving forwards and all we have to do as the user is just to change its direction.
"""

""" 
Now, how would we go about moving the snake?
"""

"""
Well, we've already got these different segments that are created, but at the moment, 
there's no way of organizing all the segments. They're kind of just created and placed on screen.
"""

## Step 1
"""
So let's put them into a list called segments,
and let's start out that list as an empty list. 
And then later on, once we've created each new segment, we go ahead and append it to this list.
"""


starting_positions = [(0, 0),(-20, 0),(-40, 0)]

## Step 1
'''
segments = []

for positions in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(positions)
    segments.append(new_segment)
'''

segments = []

for positions in starting_positions:
    new_segment = Turtle('square')
    ## Step 3 pull the penup
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(positions)
    segments.append(new_segment)



## Step 2
"""
If we want something to continuously happen in our program,
the way that we've usually done that is through a while loop.

So let's create a new variable called game_is_on and let's set it to true.

And while game is on, then we're going to move each of the segments.

The simplest way that I could think of to move this segment is to loop through 
each of the segments in our list of segments.

And then to get each of these to go ahead and move forward. So let's say we move forwards by 20 pixels. 
Let's go ahead and run this program and see what we get.
"""
## Step 2
game_is_on = True
while game_is_on:

    ## Step 7
    screen.update()

    ## Step 8
    #time.sleep(1)
    ##############

    ## Step 9
    time.sleep(0.1)
    ###############
    #for seg in segments:
        #seg.forward(20)

        ## Step 5
        #screen.update()

        ## Step 6
        #time.sleep(1)

    ## Step 10
    #segments[0].left(90)

    ## Step 12
    #for seg_num in range(start= 2, stop=0 , step=-1):

    ## Step 15
    for seg_num in range(len(segments) - 1, 0, -1):


        ## Step 12
        # segments[seg_num].goto()

        ## Step 13
        # segments[seg_num - 1]

        ## Step 14
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    ## Step 16
    segments[0].forward(20)

    ## Step 17
    #segments[0].left(90)

## Step 3
"""
The first thing we notice is that the behavior is very weird. 

We've got a line that's being drawn and that comes from each of the segments which are individual turtles.

And they're all drawing this line as they're moving.
"""

## Step 3
"""
The first thing we want to fix is that line.

So when we create each new segment, before we tell it to go to its position,
let's go ahead and tell it to pull the pen up .penup(). This way it won't actually draw

and all that we'll see is the actual turtle pieces.
"""

## Step 4
"""
So now we see our three turtle pieces scurrying along like some sort of weird Caterpillar, 
but definitely not in a snake like way.

How can we fix this?
"""

## Step 4
"""
One of the things that you notice about turtle is it will first create the turtle when it runs this line,
the turtle will get created at the center positions, so coordinate (0, 0).

And then it will be moved to whatever position we tell it to go to. For example, for the third segment, 
it starts out life at (0, 0)

And then as soon as it gets told to go to this position, it goes to (-40, 0). Now we can see that happening on screen.

When we created our snake body, you could see each individual piece being created and then moved to their location. 

Now, if we wanted to turn off that animation, then we would have to use one of the screen class' methods called tracer. 

And tracer takes a number as a input, and it turns the animation on or off.

And when the tracer is turned off, then we can use the update method to tell our program when to refresh and redraw
the screen. 

Think of how the old TV monitors operated by painting on a strip of color line by line slowly covering the entire screen.
And then once it's done one screen, it's going to go back to the top
and then it's going to paint the pixels for the next scene.
"""

## Step 4
"""
In our game what we could do is we could describe each of these scenes and tell our program
when it should redraw each picture. So that way we could start out with one picture and then hit update and then do
something else on screen, maybe move each of our segments and then tell the screen to update again
to show the user the new result. And then each time we make the changes we want to happen and then call that 
update method to tell the screen to show a new image each time.
"""

## Step 4
"""
Let's first turn off the tracer.

So the tracer is a method in the screen class and in order to turn it off, we're going to set it to zero.
So now once the tracer is off, if we actually try to run our program,
you can see it's just a black screen and nothing will happen.
"""

## Step 5
"""
So let's say that we decide to call update after all of the segments have been created and put it below 
segments.append(new_segment) you'll notice that pretty much immediately. As soon as you run the program,
our snake body will show up, not piece by piece,

Now, if on the other hand I move our screen.update line of code into the while loop so that once each segment moves, 
I get the screen to update, then this is what you're going to see. You see each of the pieces moving along one by one.
but in its entirety.
"""

## Step 6
"""
So I'm going to slow it down a little bit. And I'm going to do this by importing the time module.

Now I'm going to add the time.sleep and I'm going to get it to sleep by one second.

So this basically just add a one-second delay after each segment moves.

So each segment moves, the screen updates, and then we sleep for a second before the next time this happens.
Notice how in this case, our snake is moving piece by piece. So first this first piece, and then the second piece,
the third piece with a one-second delay between each movement.
"""

## Step 7
"""
Now, what happens if we move this screen.update to outside this for-loop?

So basically we only update the screen once all of the segments have moved forwards.
Now notice how our snake is moving forwards as an entire piece. It's going to move all three segments 
forward before the update gets triggered and we refresh the graphics.

So it looks like as if the whole snake is moving as one piece. 
"""

## Step 8
"""
instead of getting it to delay by one second after each segment has moved, if I move this above the for loop 
then it's only going to be delayed by one second after all three segments have moved. This way our snake is moving 
a little bit faster.
"""

## Step 9
"""
And we can make it move faster still if we cut the amount of time that we're sleeping.

So let's change it to 0.1 second sleep and you can see our snake is now moving at a reasonable speed.
"""

## Step 10
"""
Now you might think that we've solved the challenge and we've now got our snake to move automatically forwards, 
but there's a problem.

How do we turn our snake?

Let's see what would happen if we control the snake head and change direction. 

Let's say that at some point, we want to turn the snake so that it turns left.

Well, what happens then?

So this first piece is now facing up, the second piece is going to continue moving forwards as does the third piece.
Now on the next iteration of that for loop, that first piece is going to keep moving towards North while the second and
third pieces are going to keep moving forward because they're not going to change their own heading. 

We'll get this strange behavior because our snake segments are not linked. 

To illustrate this, let me go ahead and change the first segment,
so the segment at index zero, and get it to turn left by 90 degrees.
And notice when I run the code, you see how that head is moving in a circle all by itself,
and the body has completely left the head and has continued to go forward. 
"""

## Step 11
"""
So how can we solve this?

we have to rethink the way that we move our segments. Again, 
we have our three segments, but if instead of moving everything forwards, what if we get our last segment, so segment_3
in this case, to move to the position of the second to last segment, 
and then the second segment to move to the position of the first segment, and then the first segment itself 
to go forward by 20 paces

And if we go back to that situation where we're trying to turn our snake, then in this method, 
it will still continue to work.
So we've got our three segments, one, two, and three. Our third segment goes to where the second segment used to be,
second goes to where the one used to be, and then the one is going to turn and then move to the left.

Now the next turn is the interesting part

because at this point we saw how if these two pieces just continue moving forward, 
they're going to move away from the head of the snake and it's going to move in opposite directions. 
But using this method, our third segment is going to move to where the second segment used to be, 
the second goes to where the first used to be, and the first continues moving forward. This way,
our snake has pretty much straightened out as you would expect this snake to behave.
"""

## Step 11
"""
Now, it's just the matter of actually implementing this, which is the hard part.

So I'm going to go ahead and delete the part where I told the snake to turn left and I'm going to delete this for loop
which just moved each of the segments in our list of segments forward by 20 paces.
"""

## Step 12
"""
Now, instead, I'm going to create a for loop,
but this time I'm going to loop through each of the segments going from the last segment to the first segment,
so basically in reverse order. Now to do this, I'm going to use the range type of for-loop.

So I'm going to say for segment number or seg_num in the range, and this range is going to have a start, a stop, 
and also a step.

So the start is the number that we're going to start the range from, the stop is where the range is going to end,
and the step is how we're going to get from the start to the stop. 

For example, if we wanted a range of 1, 2, 3, then of course start is going to be 1,
stop is going to be 3 and step is going to be +1.

Now, if we wanted a range of 3, 2, 1, however, then the start is going to be 3,
the stop is going to be 1 and the step is going to be -1.

In our case, what we actually want is actually to go from 2, 1, 0. 
(going back to the starting_positions tuplits 2 = (-40, 0), 1 = (-20, 0), and 1 = (0,0)
So the start will be 2, the stop will be 0, and the step will be -1.
Now, unfortunately, even though we have these named parameters,
because the range function in Python is actually something that's not quite pure Python, 
it's something that comes from the C language, it doesn't actually let us use these names.

But for the time being, it's actually much easier to visualize this as we write the code inside this for-loop.

So in this case, the segment number is going to be equal to 2, and then 1, and then finally 0.

Now we're going to use that to get hold of the last segment from our list of segments.

So we can tap into that list and then get hold of the last one using that seg_num.
And then we're going to set it to goto() a particular X and Y position.
"""

## Step 13
"""
Now the X and Y position that we want it to go to is going to be the second to last segment's position.

So how can we get hold of the second to last segment? 
Well, we're going to get hold of the segments and then pass in seg_num but then -1. 
So when we first start out, we start out with 2.
So the segment at position two is going to be the last segment.
And then the segment at 2 - 1 is going to be the second to last segment.
"""

## Step 14
"""
Now this one we're going to get hold of it's X coordinate and we're going to set this to a variable called new_x,
and then we're going to do the same and get hold of the new_y.
So we're going to get hold of the second to last segment's Y coordinate,
and then we're going to use these coordinates, 
new_x and new_y to tell this last segment to go to the position of the second to last segment.

Now, as I mentioned before, this range function comes from the C language.
So if we run it with these keyword arguments it's actually going to give us an error
and it tells us that this range function takes no keyword arguments.
So while it's really nice to use it to visualize it, 
if we actually want it to work, we have to delete (start= 2, stop=1, step=0).
"""

## Step 15
"""
But just before I delete it, I want to this so that we're no longer using these hard-coded numbers. 
So instead of going from 2 to 0, we want to go to the length of the segments. 
So in the future, if we had 10 segments or 20 segments, that our code would still work.

Now, the length of the segment is actually three to begin with. And we know that lists start counting from zero, 
so 0, 1, 2, ... the last position is going to be the length - 1, and then we're going to stop at the zeroth segment.

So now we can go ahead and delete these named arguments. And we end up with this:
for seg_num in range(len(segments) - 1, 0, -1)
"""

## Step 16
"""
Notice how all three of the segments went to the same position, the position of the first segment. 
So in addition to moving these segments, remember that we also have to move the very first segment actually forwards by
say, 20 paces. 

So at the very end of all of this code outside of the four loop, we're going to get hold of the first segment, 
so segment at position zero, and then we're going to get it to move forward by 20 paces.

So now when I run this again, you can see our snake is now moving freely forwards. 
"""

## Step 17
"""
even if at some point, the snake needed to turn, let's say it turned left by 90 degrees segments[0].left(90), 
then our code is still going to work.

Notice how our snake is now turning in a circle and all of the subsequent pieces are following the head along its path. 
"""

## The End
"""
That's it. 

This is the code that will get our snake to automatically move forwards.

Now, there was quite a few concepts mentioned in here, 
and you have to think about the segments in terms of how they move in the graph
and also this idea of getting hold of the last segment and then telling it to go
to the position of the second to last segment and then doing this for all of the segments.
So it's a little bit mind-bending and it might be worth just taking a second
look at this code and going back in the video where I explain how this worked in the slides, 
just so that you're really clear with how this works. 
Once you are, then you can move forward and head over to the next lesson.
"""