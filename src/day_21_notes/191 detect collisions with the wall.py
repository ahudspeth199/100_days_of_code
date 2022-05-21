"""
We've coded up the majority of this game now already.
All that's left to do is to define the two situations where we might get game over.
and that is detecting collision with wall and detecting collision with tail.
So let's tackle the easier one first.

We want the snake once it gets past a certain point
that's very close to the four walls to trigger the game over sequence.

So we know that we have a 600 by 600 screen and the X and Y axis go to 300 and -300 at all four sides.

So if we create a boundary box that say 280 here,280 here, -280 and -280, then as soon as the snake head touches that
position, then once it zoomed past it, then we can say that the snake has pretty much hit the wall.

Now this number is not perfect, it's just what I found to work after doing a lot of testing.
And this is the case with a lot of games, you have to test it, run it, see if it works the way you want it to.

But let's go ahead and add a comment, detect collision with a wall, (this is on the main191.py)
and let's create our if statement.
So what we want to say is if the snake.head has a X coordinate that is greater than 280, so it's gone too far to the right,
or if it has a X coordinate that is less than -280, so it's gone too far to the left, or if it has a Y coordinate
that's greater than 280, so too far to the top, or if it has a Y coordinate that is less than -280
so it's gone too far to the bottom,
if any of these four situations occur then it basically means that the snake has hit the wall.
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 200 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
"""
So what do we want to happen when the snake hits the wall?

Well, we want to change this game_is_on to false
"""
    #Detect collision with wall.
    if snake.head.xcor() > 200 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
"""
because what that's going to allow us to do is to exit the while loop and basically end the snake movement and end the game.

Let's go ahead and test this out.

So let's let the snake hit the wall and you can see it no longer continues moving forward. 
But for the user, this might be a little bit confusing. It doesn't seem like it's actually game over. 
It seems like it's just crushed.

So let's go ahead into our scoreboard (scoreboard191.py)
which does a lot of the writing and let's create a new function which is going to be called game_over
"""
    def game_over(self):
"""
And this game_over function is going to simply just write some texts, not the score,
but instead it's just going to write 'GAME OVER' onto the screen using the same alignment and the same font.
"""
        self.write("GAME OVER", align=ALIGMRNT, font=FONT)
"""

But instead of it at the position which we initially defined which is right at the top,
let's go ahead and get it to go to the center, which is at (0, 0). """self.goto(0,0)"""
"""
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMRNT, font=FONT)
"""
So now when the snake hits the wall, not only does the snake stop moving,
but we're also going to get the scoreboard to trigger the game over a sequence.
"""
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
"""
So that means when it hits the wall, game over shows up in the middle of the
screen, and you can still see the score that was written previously
because we don't actually hit clear before we write this game over.

And this means that the user can see that the game is over, the snake has stoppedmoving, and they can see their final score.

So let's try to score some points. And once I've done that,
I'm gonna hit a wall and it's game over and I can see that my score was 2.
"""