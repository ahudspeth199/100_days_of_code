"""
Now, hopefully you've already downloaded the starting project, so you can go ahead and click open in PyCharm,
find the location where you've downloaded your turtle-crossing-start and make sure that you've unzipped that zip file
and you've got the actual folder, which contains all of the starting files.
So select the folder and then click open and we have to configure a Python
interpreter and make sure that your Python interpreter is at a minimum of Python 3.8. So you can use 3.9 or above,
but if it's lower than 3.8, you might get some errors and some problems. Refer back to when we first started
out using PyCharm and we installed Python if you get stuck on this.

Now, if you take a look at inside our project folder, you can see I've already created four files for you.
These files are pretty bare bones, but if you take a look at the main.py file which is your starting point
for your program, you can see that I've written a little bit of code that we learned about in previous lessons.

So we've created a screen object and we've set up the screen to be 600 by 600 pixels.
And then we've turned off the tracer by doing the tracer(0), and instead, we're getting the screen to update every 0.1 seconds.

So within the while loop, the code is going to run every 0.1 seconds.

So whatever it is that you put inside this while loop, it's going to be refreshed every 0.1 seconds.

Now, you'll also see that I've imported some classes from these files; player, car_manager, and scoreboard.

Now, inside these files,

I've created the starting point for each of the classes.

The player class is going to be the turtle which we're controlling to cross the road,
the car manager is going to generate all of the random cars and move them across the screen,
and then the scoreboard is just going to write the level that we're currently on and also the game over a sequence.

Now, inside each of these classes, I've got pass written here just so that the linter will stop screaming at me.

So, as we mentioned before, Python doesn't like things are empty, so empty functions, empty classes, and you'll get these errors.

Instead of getting these errors, all I've done is simply written pass which essentially just makes this an empty class.

So when you're creating these classes, just delete the pass and you can create it as you would normally.

Now,in addition, we've got all of these constants in here.

For example, the starting position of the player turtle,
how much the turtle should move each time and where the finish line is on the Y-axis.

In the car_manager we've got the colors of the cars, we've got the move distance of each of the cars on each refresh,
and we've also got how much the move distance should increase every time the user levels up.

Finally, we've got the scoreboard which just contains the font that you are going to use to write out the score board.

That's pretty much an introduction to the starting file.

So once you're ready, feel free to head over to the next lesson and get started with each step of the game.