'''''
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('green')

for turtle in range(4):
    timmy_the_turtle.forward(109)
    timmy_the_turtle.right(90)
'''

'''''
timmy_the_turtle.forward(109)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(109)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(109)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(109)
'''
'''''
screen = Screen()
screen.exitonclick()
'''

# Get turtle to draw dash line
'''''
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color('green')

for t in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
'''

# I misunderstood the challenge and had the turtle draw dash then stright line
'''''
def draw_dash_stright():
    for t in range(3,15):
        tim.forward(20)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    for i in range(3,15):
        tim.forward(20)

should_continue = True

while should_continue:
    draw_dash_stright
'''


# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# found this solution on https://willbroad.hashnode.dev/turtle-graphics-for-beginners
'''''
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

tim.penup()
#tim.goto(-150,150)
tim.pendown()

colors = ['green', 'CornflowerBlue', 'DarkOrchid', 'purple', 'black','blue','purple', 'yellow','orange','red','grey']

def draw_shapes(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random.choice(colors))
    draw_shapes(i)
'''

# Draw a Random Walk
# My Solution
'''''
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.speed(3)
tim.pensize(10)

colors = ['green', 'CornflowerBlue', 'DarkOrchid', 'purple', 'black','blue','purple', 'yellow','orange','red','grey',
          "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_walk(num_of_walks):
    for i in range(3, 30):
        directions = [0,90,180,270]
        while True:
            tim.forward(30)
            tim.setheading(random.choice(directions))
            tim.color(random.choice(colors))

random_walk(30)
screen = Screen()
screen.exitonclick()
'''

# Instructors solution
'''''
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.speed('fastest')
tim.pensize(10)

directions = [0,90,180,270]
colors = ['green', 'CornflowerBlue', 'DarkOrchid', 'purple', 'black','blue','purple', 'yellow','orange','red','grey',
          "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
'''

# Generate random RGB Colours
'''''
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # See if you can return from this function a tuple that consist of the three random integers (r,g,b) and use that
    # random color to color that color drawing instead of tim.color(random.choice(colors))
    my_tuple = (r,g,b)
    return my_tuple


directions = [0,90,180,270]

tim.shape("turtle")
tim.speed("fastest")
tim.pensize(10)


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
'''

# Draw Spirograph circle

import turtle as t
import random


#My solution
tim = t.Turtle()
tim.shape("turtle")
tim.speed('fastest')
tim.pensize(1)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r,g, b)
    return my_color


for i in range(35):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)


t.hideturtle()

screen = t.Screen()
screen.exitonclick()
