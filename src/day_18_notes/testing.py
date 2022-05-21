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

