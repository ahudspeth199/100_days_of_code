"""
In the last step, we figured out how to detect when the player turtle hits a car and to stop the
while loop which stops the game at that point. Now we're going to figure out how we can detect when the turtle reaches the
other side of the screen so that once our turtle makes a successful crossing,
then we can return the turtle to the starting position and speed up all the cars.

So I'm going to do that right here (on main.py)
"""
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()
"""
and I'm going to detect a successful crossing.
"""
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detect a successful crossing

screen.exitonclick()
"""
So what is a successful crossing? Well, the player turtle has the reach the finish line, right?
Which we've defined the Y value for as 280 here in the constant:
FINISH_LINE_Y = 280

Now you could do this in a number of ways.
You could define a method here or simply just get hold of the player's position
and then figure out if it's over 280 inside our main.py.

Now I'm going to create a method here instead (player.py) and I'm going to call the method is_at_finish_line.
"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
"""
This method is going to return true if the turtle is at the finish line and false while it's not.
So how do we detect this? Well, we can get our self.ycor and we can see if that is greater than 280, which is our finished line Y value.
What that means we've pretty much gone over the finish line, right?
So if this is the case, then we're going to return true.
But while that's not the case, any other time when we check this, we're going to return false.
"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
"""

So now coming back to our main.py, we can call our player.is_at_finish_line and we can say, if this is true, well in that case
we're going to get the player to go back to the starting position.
"""
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detect a successful crossing
    if player.is_at_finish_line():

screen.exitonclick()
"""
So inside our player class (on player.py) let's create yet another method which I'm going to call go_to_start.
And this just involves getting our player to go to the starting position which we've defined here in a constant:
STARTING_POSITION = (0, -280)

"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
"""

So notice how we've got a little bit of repetition here:
"""
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
"""        

so we can actually delete this line and simply call self.go_to_start. 
"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
"""

Back in our main.py once the player is at the finish line, we're going to get the player to go to the start 
player.go_to_start()
"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()

screen.exitonclick()
"""

And if we go ahead and run our code as it is right now,
you can see that once the turtle makes it across the road, it goes back to the starting position.

Now the very last thing we need to do is to increase the speed of the cars when the player reaches the other side,
because effectively they've just gone to the next level.

What we can do is when the player reaches the finish line,
we can get the car_manager to increase the speed of the cars.

Let's create a method inside our CarManager class (on car_manager.py)
which we'll call level_up. And in this method, we're going to get the cars' speed to increase by 10 every time.

"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_wid=2,stretch_len=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250,250)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
"""

So if we have an attribute called car_speed and we initially set it as the starting move distance: STARTING_MOVE_DISTANCE
and then we use this car_speed to determine how far it should move backward each time.
Well then when we level up, we can say self.car_speed now increases by the increment that we've defined here: MOVE_INCREMENT
which is the move increment.
"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_wid=2,stretch_len=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250,250)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed *= MOVE_INCREMENT
"""

So now when our player reaches the other side at the finish line, (on main.py)
then in addition to getting the player to go to the start,
we're going to get the car_manager to level up our cars as well.
"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()

screen.exitonclick()
"""

So now when my turtle reaches the other side of the screen, not only does the turtle go back to the original position,
but the cars also increase in speed.
"""