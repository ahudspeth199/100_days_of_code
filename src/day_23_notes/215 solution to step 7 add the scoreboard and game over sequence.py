"""
In the last lesson, we figured out how to detect when our turtle reaches the other side of the screen.
And when this happens, we return the turtle player to its original position
and we also increase the speed of the cars by the move increment that we defined as a constant.

So in this lesson, what we're going to do is the final step, which is to create a scoreboard that keeps track of which level the turtle
player is on, and also when the turtle hits one of the cars to display
the words game over in the center of the screen.

To do that, we're of course going to go inside our scoreboard class (scoreboard.py) and again
we're going to need the help of the turtle class.
So let's import that from the turtle module and I'm going to make my scoreboard a subclass of the turtle class.

So it's now inheriting from the turtle class.
And once we've defined our init and managed to get it

to inherit everything from the superclass,

then our scoreboard is now able to do everything a turtle class can do.

What do we want it to do? Well,

we have to initialize it with a couple of things first. For example,

we probably want to start out by hiding the turtle,

we just want to use it as a pen to draw. And in addition,

we don't want it to move and draw. So we're going to pull the pen up.

We're going to be using the write method instead.

And what we want to write is the level, right?

So the current level that the player is on. In order to do that,

we also have to keep track of the level.

So let's go ahead and create a new attribute

which I'll call level and let's start at level 1.

So then we can insert this right here with self.level

and in addition to writing this text,

we can define what we want the alignment to be.

So I want this to be on the left and also what the font to be.

So I'm going to use this font that was declared up here as a constant. Now,

inside our main.py next to where we've defined our player and our car_

manager

I'm going to create this new scoreboard object and that's going to be created

from the scoreboard class. Now notice when I run the code as it is,

you can see that our level is left-aligned,

it's got the font that we defined and it's writing the text that we want,

but it's not in the right position. To define the position

we have to do that right before we tell the scoreboard to write,

so right here, but after where we've got our penup.

So this way we don't draw a path to where we're going to.

So now we're going to define self.goto,

and I'm just going to get it to go to probably the top left corner.

So that's going to be probably -280 and then it's going to be

+280 on the Y. Now, if we just check the positioning,

you can see that it's a little bit too far up on the Y-axis.

So it lets move it down a little bit and you can tweak these things until you

get to the point where you're happy with its positioning.

So I think this looks pretty good. Now,

in addition to writing the level,

we actually have to update it every time the player levels up, right?

And they do that when there's a successful crossing.

So at some point here,

we should be able to call scoreboard and we should be able to get the scoreboard

to increase the level.

So let's go into scoreboard and let's define that function, increase_

level.

And the first thing to do when we're increasing the level is of course getting

hold of this self.level and then adding one to it each time.

In addition, we're going to need the level to be rewritten again.

So let's cut this out of the init and let's instead define a custom method

which we'll call update_scoreboard.

Yeah.

Inside this update_scoreboard, we can write the current level.

So now inside the init

we can call self.update_scoreboard

and also when we increase the level,

we can call self.update_scoreboard.

Now at the moment, as it is,

it's going to overwrite what used to be on the scoreboard.

So at the moment it's on level 1,

but once I make a successful crossing,

you can see that level 2 is going to be overwritten over level 1.

To prevent that when we update the scoreboard,

we have to get the scoreboard to clear itself

so that it deletes all the previous stuff that it wrote. This way

when we actually run our code

you can see that our scoreboard will refresh and clear the previous text and

write the new text each time.

So now the final thing to do is to write the words game over in the middle of

the screen when the game ends. To do that, I'm going to create

another method here

which I'll call game_over. And inside this method,

we're going to get our turtle to go to the center.

So we're going to say self.goto and the center is, of course, at

(0, 0), and then we're going to get it to write,

but this time we're not going to write the level anymore. Instead,

we're going to just write the words GAME OVER in all caps.

And I want the alignment to be centered and I want the font to be the default

font. Now, when we actually detect a collision,

not only is game_is_on going to be false,

but also we're going to get the scoreboard to show the game over sequence.

So now we can run our code and you can see that when my turtle collides with a

car,

then it says game over in the center.

And because when we wrote game over, we didn't clear any of the previous texts,

the user can see at the highest level that they managed to reach.

That's it. That's the entire game.

Hopefully you've managed to build this entire game by yourself and you're just here

to check a few niggling issues. But if you struggled with this code,

then I really recommend to review the previous lessons where we created the

snake game or when we created this turtle crossing game

and try to see if you can create these two games from scratch by yourself

by looking at how the game works. Because if you continue forward,

things are only gonna get more complex.

And I'm assuming that you're going to take the time to review and revise before

you continue.

So have fun playing with the turtle crossing game and be sure to let me know in

the Q/A what your highest level is that you managed to reach and also

remember to attach a picture or it didn't happen.

And this is a great project for you to customize.

So think about what you might want to change

like the colors or the shapes and make the game really your own and then take a

screenshot of it and share it with us in the Q/A so that we can all

appreciate and congratulate you on your work.