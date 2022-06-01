"""
First, let's start by improving our snake game, getting it to be able to keep track of the high score that we attain each time
we play the game so that we can see what our high score is and keep striving to etter ourselves.

Open up the snake game in PyCharm that you created a few days back. Now,
if you can't find your snake game project, or if you've made some significant changes to it where it might be confusing to
follow along with the tutorial, then simply just head over to this URL which is in the course resources
and then you can go ahead and hit download as a zip, unzip the downloaded file, and then open it inside PyCharm
and you should end up with the same project as I have here.

And once you've done that, then we can begin to start adding the functionality to keep track of the high score.

Firstly, I'm going to add another attribute to my scoreboard, which is going to be called high_score.
And again, it's going to start out as zero.
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
"""

Now, the next thing I'm going to do is I'm going to replace this game over method
with a new method. We're not going to stop the game and write game over anymore.
Instead, we're going to reset the scoreboard.
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
"""
So what happens when we reset the scoreboard? Well,
we need to figure out if the current score that the user has attained is greater than the high score of all time. 
And if that is the case, then we're going to update the high score with the value of the current score.
So the code for that would look something like this.

If self.score is greater than self.high_score,
well in that case then self.high_score is going to be equal to self.score.
"""
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
"""
Now, this looks a little bit confusing at first,
but if you just go through the logic and think about how you would create a high score saving mechanism,
then you'll pretty quickly understand what's going on here. 

Now, once we've updated the high score, the next thing to do is to reset the score. So I'm going to reset it down to zero. 
"""
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
"""

Now, remember the order of your code matters a huge deal because if you first set the score to zero,
then it's never going to be greater than the current high score.
"""
    def reset(self):
        self.score = 0
        if self.score > self.high_score:
            self.high_score = self.score
"""

So this will never get triggered:
"""
        self.high_score = self.score
"""

So as always, be careful where you're writing your code. 

Now, after we've set the score, then we need to update the scoreboard.
"""
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
"""

Now, one thing that I've changed about the scoreboard is previously when we increased the score,
I've used the self.clear and then self.update_scoreboard.
"""
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
"""
But it actually makes more sense for this clear to happen every single time we update the scoreboard.
So I've added this method call here before we actually write the score.
"""
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.update_scoreboard()
"""

The reason why I couldn't do this previously is because when we wanted to show game over,
we wanted to keep the score on the screen and then for the score board turtle to go to the center and write game over so that both of
these things show up on screen.

But now that we're getting rid of our game over method, then we can go ahead and move that clear to update scoreboard
and then we don't have to call it twice, both in reset and increase_score.

on scoreboard.py
"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
"""

Now, in addition to writing the score, I'm now also going to write the high score,
and this is going to be using an f-string to insert self.high_score.

"""
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
"""

Now, if we run this game as it is, you can see it says score 0, high score 0 using these initial values.

But as soon as it hits the wall, it ends because in our main.py
we change this game_is_on to false and that ends our while loop.

on main.py
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
"""

Instead, what I'm going to do is I'm going to delete this game_is_on equals false and also delete it when we collide with the tail.
And I'm also going to delete the part where we call game over from the score board. 
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:



    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
"""

Instead, I'm going to get the scoreboard to reset itself.
So that way the score gets reset to zero and we're ready with the next round.
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
"""

So now if I run this game again, you can see it says, score is 0,
and then as soon as we get a higher score and we end up dying, like so, then our high score goes to 2.
But our snake kind of just disappears because it continues moving in the same
direction and it's now probably somewhere, all the way down to the left. What we do instead? 

Well, our snake also needs to be reset.
So let's create a reset method inside the snake class as well.

And all we're going to do is we're going to get all of the segments to clear.

on snake.py
"""
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        self.segments.clear()

    def extend(self):
        self.add_segment(self.segments[-1].position())
"""

And when I hover over this clear,
you can see what it does is it's going to remove all of the items from that list.

So all of the segments that we've added already to the list of segments is going to be deleted. 
And then once we've gotten rid of all the segments, we're going to call self.create_snake again,
so that we create another three-segment snake in the starting position.
on snake.py
"""
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        self.segments.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.segments[-1].position())
"""
Now, in addition, I'm also going to set the self.head as the zeroth element from that list of segments.
on snake.py
"""
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())
"""
So basically we're doing everything that is in the init because we're going to initialize the snake again, back at the center.

So now if I go back to main.py, and in addition to resetting the scoreboard,
I also get my snake to reset,

on main.py
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
"""

At this point, when I run the code, you'll notice that it's not behaving quite the way you expect it to. So I can go
ahead and score, and when I die, I get the high score, but my old snake is still lingering on screen.
So even though we've cleared the segments, we don't actually get rid of the turtles that are still onscreen.
And in order to get rid of them, we actually have to send them to a different location. 

In our snake reset method, just before we clear our segments, so while we still have access to all of them,
we're going to use a for loop to loop through all of the segments in the list of
segments and tell each of them to go to a place that is off the screen.

on snake.py
"""
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())
"""
So our screen is only 600 by 600 and I'm going to tell it to go to 1000 X, 1000 Y.
So it's gonna disappear off the screen. 

So this way, notice how when the snake hits one of the walls or when it hits its tail, instead of sort of just staying there,
it actually disappears into a location that's off the screen.

So that way we can keep track of our high scores, we can continue to get higher scores,
and if we get a score that's not quite as high as the high score
and we end up dying, then the high score stays as the previous value.

Now, the only thing about this game is that in order to end it, we have to hit the stop button here. 

But once we've done that, it also reveals the crucial flaw in our code. Because if I run our program again, you can see that, wait,
what happened to the high score? We had a high score of 3 previously. So, huh? What exactly is happening? 

Well, the reason is actually quite simple. We know that if we create a variable, let's say we create a variable called a
set it to equal 3, and then at some point we set a to be from the input.
a = 3
a = input("What do you want a to equal?:")

So now when I run this code, you can see that initially a is equal to 3,
but then the next line I asked the user, 'what do you want a to equals?'
I'm going to make it equal to 12. 

Now at this point, if I go ahead and access this variable a inside the console
just by typing a and then hitting enter, you can see it's equal to 12.

Now, similarly, I can add some print statements here.
I can print the value of a and then also print the value of a after we modify it. 
a = 3
print(a)
a = input("What do you want a to equal?:")
print(a)

So again, you can see initially it's equal to 3, but then I decided to change it to 12.
So now it's equal to 12.

Now what happens if I rerun the code. A is equal to 3 again.
Its reset itself because the code is being rerun and the previous state is not being remembered. 
In our case, we've got this high score variable which initially starts out as zero.
high_score = 0

And at some point during the game as we progress, we modify this high score variable to equal a new value,
let's say three.

So now if I go ahead and print my high score, you can see that it's equal to 3. But as soon as I rerun the code and this goes through,
then all of that progress gets reset. And now if I print the value of high score, you can see it's again,
equal to zero. 

So this is what's happening in our program as well. So how might you keep track of the score if you weren't using Python?

Well, you might open up a word document and then write down your high score in that document, close it down, 
and then the next time you play the game, open up that file again and see what your previous high score is.
We're going to try and do the same thing, but using Python to read and write to a file so that we can save our progress
and be able to retrieve our previous high scores each time we play the snake game. 

To find out how to do that and to solve this problem, head over to the next lesson and we'll talk about how to use 
Python to open, read, write, and close files on your system.