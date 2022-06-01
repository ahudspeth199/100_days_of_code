"""
In the last lesson, we managed to figure out how to get the turtle to move with a keypress and that's with every
press of the Up key the turtle moves further towards North.

Now the next task is to create and move the cars. The cars need to move from right to left and they need to be
randomly generated along the Y-axis here.

So they need to be generated right to the right edge of the screen and they can appear anywhere along this line,
and then they're going to move automatically towards the left at a fixed pace.

Each of these cars,you can see, are going to be turtles and they're going to be 20 by 40 pixels.
So we mentioned that by default every turtle that we create is 20 by 20 pixels.

So we'll need to stretch the turtle to make it into this shape.

Now that we are concerned with the cars let's create our code inside the car_manager.

The first thing we'll need to do is to import the turtle class from the turtle
module and our car manager is going to have a init where we create all of our cars.

So I'm going to create a list called all_cars, and it's going to start out being an empty list.
"""
class CarManager:
    def __init__(self):
        all_cars = []
"""

Now, at some point, our main.py is going to call a function from the car_manager called create_cars.
And this method is going to create a random car somewhere along the Y-axis with a given dimension. 
"""
class CarManager:
    def __init__(self):
        all_cars = []

    def create_cars(self):
"""
Each of these cars, so let's call it a new_car, is going to be a turtle object and it's going to be created in a square shape.
Now, in addition, we're going to have to change the dimensions of this turtle and we're going to use that method that we used before
which is this one, shapesize.

Now, what shapesize allows us to do, if you remember, is it allows us to stretch our turtle along the width and along the length.

So we want the width to be double the original size,
so two times 20 pixels is 40 pixels and the length we don't want to be stretched at all.
So we're going to say it's one times the original length.
In addition our new_car is not going to draw, so we're going to get it to penup.
And also our new car is going to have a random color.
So we can set the color and then we can import the random module so that we can use one of these colors in this list.
And we can say random.choice and then pass in our list of colors from this COLORS constant.
Finally, we're going to define where it's going to go on the screen.
To do that we need to define a random_y position.
So this again is going to be created from the random module and we're going to
use the randint and then we're going to define somewhere along this Y-axis, which is the vertical,
somewhere for this call to be generated at.
So we know that our screen is 600 by 600, so that means the Y-axis goes from +300 to -300.
But we don't want the car to be generated all the way to the edge because remember the turtle needs a bit of starting space
and also a bit of ending space. So you can play around with this number,
but I've ended up going with -250 to +250.
This means that we get a good range in the middle of the screen and that the
turtle has a bit of empty space at the beginning and also at the end when it
needs to move across. So now that we've defined our random_y, we can tell our new_car to go to the x position
which is going to be the very edge of the right screen,

so that's going to be +300, right to the edge.

And then the y position is going to be the random_y that we just created.
And finally, once we've created our new_car, we're going to append it to our list of all_cars which of course,
because it's defined in a class, it has to have the self in front of it.
So self.all_cars.append, and then we're going to append this new car that we've just created.
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
"""

Now, coming back to our main.py, let's create our car_manager from the CarManager class,
and then we're going to use it inside our game loop here so that on every refresh of the screen, every 0.1 seconds,
we're going to get the car_manager to create a new car.
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

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
"""

And strictly this probably shouldn't be plural because each time we call this method, it only creates one new car.
So let's change that method so that it only creates one car, but it creates one car every 0.1 seconds.
(she changed the methed from car_managers() to car_manager()

Now at this point in time if we run our code, you'll actually see nothing happen because the cars are being created at this
right edge here and it's not yet visible on the screen. To make it visible we have to move our cars across the screen.

Let's create another method which we'll call move_cars because this method is going to go through our list of cars,
so for car in self.all_cars,and for each of those cars, 
it's going to move it towards the left by the move distance that we've defined up here.
"""
    def move_cars(self):
        for car in self.all_cars:
"""

So to do that, all we need is to get the car to move backwards by the starting move distance.
"""
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
"""
Now it's going to loop through our list of all_cars that were created and then for each of the cars,
it's going to move it backwards by five paces: STARTING_MOVE_DISTANCE = 5

So now in addition to getting the car manager to create a new car on every refresh of the game loop,
we're also going to get it to move all of the cars by five paces.
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

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
"""

Let's hit run
now and you should see that we've got our cars being generated,
but notice how I've made a slight error in the stretch. Instead of stretching it along the length, I've stretched it along the width
and this is why we've got this random array of shapes moving.
So let's go back to our car manager and change the width to stretch by one and stretch to the length by two. 
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
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250,250)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)
"""

So now if we rerun our code, you can see the cars are now the right shape,
a rectangle that looks like it's moving to the left.

Now notice how, in my case, the cars are being generated far too frequently.
We've got way too many calls and it's impossible for our turtle to cross the road.

So we need to figure out a way of how we can reduce the number of cars that are being made. 
Instead of creating a car every 0.1 seconds at every refresh of the game, we need to slow this down a little bit.
And one way we can do this is by using a random number.

Let's say that we create a random_chance which is going to be a one in six chance,
so it's almost like throwing a dice. If you get a one on the dice, then we create a car.

We can do this by getting hold of our random module, creating a random int between one and six
and then we can say that if the random_chance is equal to one, then, and only then do we actually create a new car.
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
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
"""

So this basically ensures that every six times the while loop runs a new car will be generated.
Now it's not going to be precisely every six times because there's some degree of chance involved. 

But notice when we run our program now, see how the cars are now being created much less frequently.
And we've actually got some space for our turtle to cross.

So that is how we create and move our cars across the screen and make sure that
they don't occur so frequently that our turtle has no chance of crossing the road. 

I hope this walkthrough was helpful. Don't worry if your code doesn't look the same as mine, it doesn't have to.
What matters is if you're able to achieve the desired functionality of the game.
There are a million different ways that you can solve this problem.
And as long as it works, whatever way you choose will be the best way.
"""


