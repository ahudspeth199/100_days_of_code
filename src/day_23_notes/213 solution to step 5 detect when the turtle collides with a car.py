"""
Now in the last lesson we created these rectangular cars randomly along the Y-axis.
And then we managed to get them to move across to the left side of the screen.
The next step is to detect when the turtle collides with the car.
So that way, when the turtle hits one of the cars,
we can stop the game and prevent further cars from moving. Inside our while loop
I'm going to detect the collision with the car here:
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
"""

So I'm going to get hold of all the cars in the car_manager object and I'm
going to use a for loop to loop through each of the cars in that list of cars.
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
"""

And then we're going to detect whether if the car has a distance to the player object that is less than 20.
"""
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        car.distance(player) < 20
"""

Remember that our cars are 20 pixels in height by 40 pixels in width.
If the player is less than 20 pixels from the center of the car, then it probably means that it's collided with the car.

So if this distance is less than 20, then we're going to stop the game.
And the way that we stopped the game is of course, by turning this game_is_on from true to false.
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
"""

Let's run our code again and let's see this in action. So we can move our turtle,
we've got randomly generated cars moving across and let's just park our turtle right here. 
When that car hit our turtle it immediately stopped the game. Now, if we want to take a look at what's happening
so for the screen to stay open instead of closing once the process is finished, we can tell it to exitonclick.
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

screen.exitonclick()
"""

So now let's run our code again and notice this time if we collide with one of the cars
you can see that it stops and it waits for further instruction,
which eventually is going to be just the game over text showing up on screen
and we also the final level showing up on screen. 
That's it. That's how we detect collision between the car and our player.
"""