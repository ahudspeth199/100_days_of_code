"""
It's time for your challenge.

You've already seen how we've managed to get the snake game to keep track of the high score.
And when the user scores a number that's greater than the high score, then we replace that high score with the new value.

But unfortunately as you saw previously, at the moment when we run this game and we achieve a new
high score, the next time that we run the game again that is completely lost.

So the first thing I want you to do is to right click on your project, create a new file and call it data.txt.
So we're going to create a data text file.

Now this data text file is just going to contain a single number, zero.
And we're going to use the data that's in this data.txt file to keep track of the high score.

And it's your job to figure out how you can convert this simple attribute here, high score,

on scoreboard221.py
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

to instead of using a number that we've just created in the code, I want you to use the number that's inside data.txt.

So you'll need to read from it here
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

and then later on, you'll need to write to it when we reset the game and check if there is a new high score. 
"""
def reset(self):
    if self.score > self.high_score:
        self.high_score = self.score
    self.score = 0
    self.update_scoreboard()
"""
Everything going well, you should be able to run the game, achieve a new high score and then stop and rerun the game and still see that
high score showing up. 

Think about what you learned in the last lesson, 
have a think about how you can convert the text in here 
"""
data.txt
"""
into a number using what you've learned in previous lessons and pause the video and give this challenge a go.


All right.

So we know that we've already got this file, data.txt, and it already contains the number zero. 
So instead of using this line of code,
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

we're going to be reading from that file to get that zero.

Let's delete this line of code. And instead, I'm going to open my file with the file name that is data.txt. 
And the file name is, of course, a string like you see here wrapped in quotation marks,
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        open("data.txt")
"""
and we're going to use the with keywords so that we don't have to bother about closing the file again.
We can get Python to manage it for us.
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt")
"""

with opening this file, and I'm going to save that file to a variable called data.
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:

"""
Now I'm going to use that data and read from it. 
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            data.read()
"""
Now, once I've read from it, I should end up with some sort of string that's going to represent the contents of this file.
So that string will need to be converted to an integer if we want to use it as a number
which we can increase and change in our game. So I'm going to type convert it into an integer. 
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            int(data.read())
"""
And then finally, I'm going to save that as the value for our new attribute, self.high_score. 
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
"""

That's the reading part done and if we run our code as it is, it should already work as it did before,
but it won't have the feature that we want which is to be able to quit out of the game, stop and rerun.

So it still not saving the latest high score to that data.txt.
You can see it's still zero. So where do we want to save it? Well, it's got to happen every time we adjust the high score.
When the score is greater than the current high score, we set the high score to the new score. 
"""
def reset(self):
    if self.score > self.high_score:
        self.high_score = self.score

    self.score = 0
    self.update_scoreboard()
"""
But in addition, we're going to read from a file data.txt.

So let's use our syntax with, and then open, again, and let's pass in the name of our file, data.txt.
And remember that we also need to change the mode to 'w' for write 
because otherwise, it's not going to let us write to that file. 
"""
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w")
        self.score = 0
        self.update_scoreboard()
"""
Now, once we've opened it and we've saved it as a variable called data, then we can write to that data using data.write.
"""
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write()
        self.score = 0
        self.update_scoreboard()
"""
And what are we going to write to it? Well, we have to write a string.
So let's use an f-string to convert our current self.high_score into a string, and then write that into our file, data.txt.
"""
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
"""
Now notice what happens when I run my code.

So I'm going to achieve a new high score of, um, 2, which I'm very proud of. And now if I hit stop,
take a look at data.txt. It's been updated, it's been rewritten by these two lines of code.

So now if I rerun my program, you can see it already is showing my previous high score of 2,
and I can keep playing this game and accumulate my high score and all of that data will be saved to my file data.txt, like that.

So did you manage to get this right? And by the way,
if you see this keyboard interrupt, don't worry. That's just because we clicked on the stop button to stop our 
program because it wants to keep on going forever until we achieve the highest score of them all. 
The point of this exercise is to try and get you to review what we learned
in the last lesson, which is opening a file, reading the file,
and also writing to the file and remembering the mode that we have to change.
And hopefully, you'll start to see how this could be really useful in terms of
improving the usability of our programs in our games.

Now in the next lesson, we're going to talk more than just about files.
We're going to talk about file paths and directories.

So for all of that and more, I'll see you there.