from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')


"""
I want you to think about how we can create this. Here we have three separate squares
which are each a turtle object and they're shaped like a square and they have a white color. 

Now, they're positioned so that the first one is (0, 0),
the next one is 20 pixels to the left and the next one is again
20 pixels to the left so that none of the squares overlap with each other,
"""
# My solution
'''
tim = Turtle()
tim.shape('square')
tim.color('white')
tim.shapesize(2, 2)
tim.goto(x=0,y=0)

tom = Turtle()
tom.shape('square')
tom.color('white')
tom.shapesize(2, 2)
tom.goto(x=-8,y=0)
'''

# Instructors solution
'''
segment_1 = Turtle('square')
segment_1.color('white')
segment_1.goto(x=0,y=0)

segment_2 = Turtle('square')
segment_2.color('white')
segment_2.goto(x=-20,y=0)

segment_3 = Turtle('square')
segment_3.color('white')
segment_3.goto(x=-40,y=0)
'''

# a much easier way to do this is using a for loop
"""
could have created a list of starting positions and this could contain some tuples.
"""

"""
So we know that in order to specify where the segment should go to, we have to provide a tuple, 
which is a X and a Y value.

Python Tuples
(1, 2, 3)
"""

"""
And we know that we can create a tuple just by using a set of parentheses and then adding values in there, 
separated by commas.
"""

"""
So if the first segment has to be at the center, then that's going to be (0, 0) 
And then the second piece is going to be at (-20, 0),
And the third piece is going to be at (-40, 0).
"""
starting_positions = [(0, 0),(-20, 0),(-40, 0)]

"""
Now we can create a for loop. So for position in starting_positions,
let's loop through starting_positions list and create a new segment for each of those positions.
"""

for positions in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    """we're going to get the segment to go to the position that we're currently looping on."""
    new_segment.goto(positions)
"""
"""
starting_positions = [(0, 0),(-20, 0),(-40, 0)]
for positions in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')

    new_segment.goto(positions)

screen.exitonclick()