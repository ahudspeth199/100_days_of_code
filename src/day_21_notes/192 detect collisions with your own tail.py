"""
All right guys, we're at the final stretch.
All we have left to do now is to figure out how we can detect when the snake collides with its own tail.
As a snake gets longer and longer, it's more likely that at some point the head might hit some part of the tail.
And in the snake game, this means it's game over.

So we have to figure out how we can detect this and then trigger the game over sequence.

One of the things that we've left until now is a way of extending the snake every time it gets some food,
because at the moment what's happening is our snake is staying the same size with only three segments.
But now we need to change that.

We need to add a segment to the snake every single time it hits the food so that
it grows in length and we can start detecting collision with the tail.

The place we're going to do that is inside our snake class. (snake192.py)
So we're going to create a function that's going to be called extend.
"""
    def extend(self):
"""

And this extend function is going to add a new segment to the snake.
"""
    def extend(self):
        #add a new segment to the snake
"""

So we're probably going to need another function, which is going to be called add_segment,
and this is going to require the position to add the segment to essentially.
"""
    def add_segment(self, position):
"""

Notice how this is the part of the code where we actually add the segment (from snake190.py):
"""
    def create_snake(self):
        for positions in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(positions)
            self.segments.append(new_segment)
"""
So lets take it out of the for loop and put it into the add_segment (go back to snake192.py):
"""
    def create_snake(self):
        for positions in STARTING_POSITIONS:

    def add_segment(self, position):
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(position)
            self.segments.append(new_segment)
"""
And so we can now call this function, self.add_segment and then pass in this position that we're looping through.
These two functions together are going to create our snake:
"""
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)
"""
But in addition, we're going to use this add_segment() when we want to extend the snake:
"""
    def extend(self):
        self.add_segment()
"""

But what position do we want that last piece to go to? 

Well, we're going to get hold of the list of segments and we're going to get hold of the last one:
"""
    def extend(self):
        self.add_segment(self.segments[-1])
"""
Remember that with lists in Python, you can write a negative number so that you start counting from the end of the list.

For example, if our list was [1, 2, 3]
then this list at minus one position would be 3

Effectively we're getting hold of the last segment in our list 
"""
        self.add_segment(self.segments[-1])
"""
and then we're going to get hold of it's position:
"""
        self.add_segment(self.segments[-1].position())
"""
And remember, this is a method that comes from the turtle class and we can call it by writing
position and then parentheses and we'll get the position of that segment.
And then we're going to add this new segment to the same position as the last segment.

So now if inside our main.py (main192.py) every time our snake collides with the food, then not only are we going to refresh the food,
but we're also going to get the snake to extend itself:
"""
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
"""
So lets go ahead and run this game again. 
And notice how this time, once I hit the food, the snake actually extends itself and it gets longer each time.

So now we're able to think about how to detect tail collision because as the
snake gets longer, this tail collision becomes more of a problem.
We're more likely to get tangled with our own tail.

(on main192.py) Let's go ahead and add a comment here which will say 'Detect collision with tail.
And the way that we want to check this is we wanna say if the head collides with any segment in the tail:
"""
    #if the head collides with any segment in the tail:
        #trigger game_over
"""
then this means that we're going to trigger the game over sequence.

So how can we detect if the head collides with any segment in the tail?

Well, we could loop through our list of segments in the snake.
So we could say for segment in snake.segments
"""
    for segment in snake.segments:
"""
so out of all the snakes segments, let's go through each one of them.

And then we can say that well, if the snake.head has a distance of, let's say less than 10 
from any of those segments that we're currently looping through, 
well that probably is a collision, right? 
"""
    for segment in snake.segments:
        if snake.head.distance(segment) < 10:
"""
So in that case, we're going to set the game_is_on to false and we're going to get the
scoreboard to trigger the game over sequence.
"""
    for segment in snake.segments:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
"""
Now there's just one problem with this. If we go ahead and run the code
as it is, you can see that immediately we get game over.
And the reason is because out of all of the snake segments, the head is the first segment.
So when we loop through each of the segments, the first segment is going to be the snake head.
And so we're detecting if the snake head has a distance to
the snake head of less than 10, which of course it is going to.

So we need some sort of way of bypassing the snakehead.

So we could say if the current segment that we're looping through is equal to, so double equal, to the snake.head, 
"""
    for segment in snake.segments:
        if segment == snake.segments:
            pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
"""
well, in this case, we're going to pass. 
But if this is not the case, so in the elif after the if statement,
then we can check to see if the snake head has a distance to the segment of less than 10. 
"""
    for segment in snake.segments:
        if segment == snake.segments:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
"""
Now, if we rerun this code, you'll see that it works exactly as we expect it to.

We can move our snake around and as soon as the head hits the body, then it's game over for us.

We've pretty much now completed the snake game. But in the next lesson,
I want to talk about a special functionality in Python which is called slicing.
And this is something that you will often see in code in the wild, 
and we'll use that to improve our code just a little bit more. 

So for all of that and more, I'll see you there.