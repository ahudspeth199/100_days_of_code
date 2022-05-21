"""
Guys, we've already come really, really far.
We've done all of this and now we're on this stage, creating a scoreboard.
So what we want is to be able to write some text in our program that keeps track
of the score, of how many pieces of food we've actually managed to eat.
Now, the score should update every single time we hit a new piece of food and it's
going to stay there and keep updating itself every time we hit a new piece of food.

Now this scoreboard is also going to be a turtle.
So one of the things that you can do with your turtle is you can get it to write a piece of text.
And this is what the method looks like in the documentation:

turtle.write(arg, move=False, align,"left", font=("Arial",8,"normal"))
Parameters:| * arg - object to be written to the TurtleScreen
             * move - True/False
             * align - one of the strings "left", "center" or right"
             * font - a triple (fontname, fontsize, fonttype)

You can tell it what it should write, what kind of alignment you want, do you want it to be in the center of the screen,
on the left or right side of the screen?
And then what kind of font you want?
So the font name, font size and font type,
so normal or heavy or bold or underlined,
and we would call it more or less like this:

turtle.write("Home= ", True, align="center" )
"""

# Challenge
"""
So here's a challenge for you.
I want you to go ahead and create a new file called a scoreboard.py.
And inside this file, I want you to create a new scoreboard class.
Now, this scoreboard class is going to inherit from the turtle class, just as we did with the food class:
"""from turtle import Turtle"""
And then the scoreboard is going to be a turtle
which knows how to keep track of the score and how to display it in our program.
Feel free to choose whatever font you want, whatever size you want,
but the end outcome we're looking for is something that looks a bit like this:
# Score: 0
and the score is going to need to be tracked inside that scoreboard class.

And it needs to be increased by one every single time the snake eats a piece of food. 
You're going to need the help of the documentation,
you're going to need to read up on how this turtle.write method works,
and you're also probably going to need this """turtle.clear()""" 
so that you clear the writing every time you update the score.
Have a think about how you would solve this and then go ahead, pause the video and give it a go.
"""
# My Solution
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.write(arg="Score = ", move=False, align='center', font='Arial')


# Challenge Answer
"""
All right.
So the first thing I'm going to do is I'm going to create my scoreboard class.
"""class Scoreboard:"""

And as I mentioned, this class needs to inherit from the turtle class.
So from the turtle module,let's get hold of the actual turtle class so we can use it inside this file.
And then I'm going to add it to my scoreboard as the superclass:
"""
from turtle import Turtle
class Scoreboard(Turtle):
"""

Now, if I create my inits, I can go ahead and use this light bulb to insert the superclass call.
So now my scoreboard is a class that can do everything a turtle class do.
And one of the things I want it to do is I want it to keep track of the score. So let's say it starts out at zero,
"""
from turtle import Turtle
class Scoreboard(Turtle):
    def__init__(self):
        super().__init__()
        self.score = 0
"""
and we want to be able to write this onto the screen. So we can say self.write, and let's use an f-string to say score,
and then we can insert the self.score value in here. 
And then we can add whether if we want it to be aligned to the center,
for example, and then we can also add a font if we need to.
Let's use the same font as here, Arial, and then we're going to make the font size a bit bigger,
and then we're going to keep it as normal.
So I'm going to choose an Arial font, size 24, and then the style is going to be normal.
"""
        self.write(f"Score: {self.score}", align="center", font="Arial, 18, normal")
"""
And as you can see here, I'm getting a warning here and it's telling me that it expected a tuple,
but instead it just got a single string. So let's just compare this against the documentation code:
turtle.write(arg, move=False, align,"left", font=("Arial",8,"normal"))

##Note
I did not see that on the website it does not show the double parantheses:
turtle.write(arg, move=False, align,"left", font=("Arial",8,"normal")

## now back to the instructor
and you can see that this is meant to be a tuple instead of just a single piece of string. So let me go ahead and fix that.
Let's add some parentheses around this, and then this Arial is going to be a string,
this 24 is going to be a number and the normal is going to be a string. And now our errors have gone away.
"""
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
"""
So now going back to our main.py let's go ahead and create our scoreboard as an object from the scoreboard class,
"""scoreboard = Scoreboard()"""
which of course means that we need to import it into this file.

"""from scoreboard190 import Scoreboard"""
So from the scoreboard file import the Scoreboard class.
And now if I run this code, somewhere in the middle there I've got a scoreboard,
but because it's actually black, you can't really see it.

It's really important that we change the color of the scoreboard turtle before we write the text,
because if it was written as black and then we change it to white, you still won't notice a difference.
So if I change the self.color right here to "white" 
"""
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

"""
and I hit run, then you can see that scoreboard showing up.

But if I move this line of code to after we've written it,
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.color("white")
"""
then it won't actually make a difference. It's still written in black somewhere on there. 

Now, in addition, we want to get rid of the turtle that shows up when we create our scoreboard
because all we want it to do is we want it to write, we don't want it to actually show up a turtle. 
Self.hideturtle, 
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()
"""
and now that little arrow disappears.

And we probably don't want this scoreboard to be in the middle. So let's move it.
Let's tell it to go to a particular X and Y position.
"""
        self.goto()
"""
Now, in example, here, I've got it in the center, right at the top.
So we can keep the X as zero, but let's move the Y further up to the top. So let's say something around 270. 
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()
        self.goto(0, 270)
"""
And now if we test it again, you can see that the turtle went to the top, but this happened after this line was already written. 

So again, this needs to happen before we write.
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()
"""
And now if we refresh, you can see it's moved to the top, but it's also drawn on a path to do that. 

So instead of doing that we can tell it to self.penup before it moves to this location.
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()
"""
There we have it. We've got our score showing up at the top. 

Now, all that's left to do is to keep track of the score and to increase it whenever the snake hits a new piece of food.

main190.py
So we know that that happens inside this if statement:
"""
    if snake.head.distance(food) < 15:
        food.refresh()
"""
when the snake head collides with the food, then we refresh the food, but we also want to increase the score.

On scoreboard190.py
So let's go ahead and create a function inside our scoreboard class called increase_score.
And this function is going to take the self.score and add one to it.
"""
    def increase_score(self):
        self.score += 1
"""
And then it's going to call self.write.
"""
    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
"""

So now back inside our main.py, we can get whole of our scoreboard object and tell it to increase score
whenever the snake collides with the food. 
"""
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
"""
So let's test this again. And if I manage to hit the food, then you can see that the score is being updated,
but what's happening is that the score is being written on top of the previous scores. 

So it's just all overlapping with each other. So instead, what we need to do is between each time we update the scoreboard,

we actually have to delete what was previously on there.
And because we've now got these two lines which are pretty much identical in two places:
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
"""

let's go ahead and create a function instead. We'll call update_scoreboard,
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        self.hideturtle()

    def update_scoreboard(self):

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
"""

and inside this function, we'll have our self.write.
And we can call self.update_scoreboard here and also here:
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
"""
So now before we increase the score and call update scoreboard,

we can call self.clear to clear the previous text that was written by this turtle, which is the scoreboard. 
"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
"""
Now, if we run this again you can see that when I do score, my scoreboard is wiped and then the new text code is written.
So it doesn't overlap with the previous scoreboard.

The final thing I want to do just as a finishing touch is I don't like having
these hard-coded pieces of text inside the body of my programs.

So instead it would be much better if we could take these pieces of texts out and create constants with them.

So we could have one that's called ALIGNMENT set to center, and then another one called a FONT,
which is going to be set to this tuple. And then I can use these constants down here,
so align = ALIGNMENT, font = FONT. 
"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
"""
That way, when I decide that I want to change something about the alignment or the font,so for example instead of Arial,
I might go for something that is a little bit more video-gamey sort of font like courier,
then I don't have to dig through the body of my program to find out where it was defined. I can just look at the top
which contains all the constants and then fix it right here. 
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
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
"""
That shouldn't have changed any of the functionality. It's just made our scoreboard look a bit more
video-gamey, and you can see how it works perfectly.
"""