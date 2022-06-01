"""
All right. So just as previously, we've split up this large problem of building the game into five smaller sub-parts.
Firstly, moving the turtle, controlling it with the keypress, creating and moving the cars automatically across the screen,
detecting a collision with the car and detecting when the turtle reaches the
other side.

Finally,we create a scoreboard that keeps track of which level we're on and also that shows game over at the end.
So the first step is to move the turtle using a keypress.
The turtle can only go forwards, and every time we hit the Up key
the turtle moves forward by a set amount until it reaches the other side of the screen.
This is the first thing that we're going to tackle.

Now, because this is related to the functionality of the player, let's go ahead and create this inside the player class.

I'm going to delete that pass and I'm also going to import the turtle class from the turtle module.
Now, our player is going to inherit from this turtle class. So inside our init, we're going to need to add the super.init
or you can add it automatically using the light bulb.
So now this player class can do everything that a turtle class can do and we can make it do even more.
"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
"""

The first thing we're going to do is we're going to set the shape of our player and we're gonna set it to a turtle.
The next thing we're going to do is we're going to call penup so that this turtle just remains a shape and it doesn't draw. 
Finally, we need to get it to the starting position and get it to face North.

We can do that by setting self.goto and then we can set it to go to the starting position,
which you can see is a tuple because it's enclosed inside parentheses and you've got values separated by a comma. 
STARTING_POSITION = (0, -280)

Finally, we're going to set the heading of our turtle so that it faces North, which is 90 degrees.
"""
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
"""

So now all we have to do is go back into our main.py,after we've set up our screen,
let's go ahead and create a new player from the player class.
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

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
"""
Let's go ahead and run this code.

...

And you can see that we've got our little turtle showing up here at the center of the bottom of the screen and it's facing North.

So now the next thing we need to do is to get that turtle to move upwards every time we hit the Up key.
That means we're going to need to get our screen to listen for events. 

After calling screen.listen, we're going to get the screen to listen to a keystroke. So we can use onkey to
set the Up key as the key to listen to. And then when that happens, then we're going to call player.
go_up. And remember that when we're calling methods inside the listener,
we don't want to add the parentheses because this will trigger it at the point where it evaluates this line of code. 
Instead, we want to trigger this function only when this Up key is detected.
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

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
"""
So now all that's left to do is to go into our player.py and define that function go_up.
"""
    def go_up(self):
"""

So how can we move our turtle up? Well,

we can get our turtle so self, and then we can get it to move forwards by a distance.
and the distance is going to be the move distance that's set in this constant here: MOVE_DISTANCE = 10

This means that later on when we want to change the move distance if we want it to go further each time,
we can just edit it at the top of the file instead of digging through the code.
"""
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
"""

Now let's run our code again and let's just make sure that it works.

So now every time I hit the Up key my turtle moves up and it keeps on going until it reaches the other side of the screen. 
So that's the first step completed. 

Now, if you think you can complete the next step by yourself,
then head back to that list of problems broken down and see if you can tackle the next one by yourself. 
If you can't or if you need some extra help, then you can always come back to the videos and I'll walk you through the steps
one by one.