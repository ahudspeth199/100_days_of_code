"""
Now while our snake game works now with all of the functionality that we set out to create,
there's just one thing that bothers me a little bit about this code, and it's how wordy this section is:
"""
#Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.segments:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
"""
All that we're trying to do is make sure that we're detecting the distance from
all of the segments that we're looping through in snake.segments other than the first one.
Surely there's an easier way of doing this rather than writing all of these lines of code. 

And indeed there is. But in order to use it, we have to learn about a Python concept known as "slicing".

Let's say that we had a list of piano keys all the way from a to g:
"""
piano_keys = (a,b,c,d,e,f,g)
"""
and we wanted to get hold of a small section of this list.
Let's say we wanted to slice the list so that we only get the c, d, and e keys from this list. 

How would we do that using Python? 

Well, one way of doing that is you could write a for loop and you could check, well,
is it c, is a d, is it d. If so, then add it to a new list. But that's really convoluted. 

We have a much, much better way of doing that in Python. And it's known as slicing.

This is what the syntax would look like. 
We would get hold of our lists, piano_keys, and then we would use a set of square brackets:
"""
piano_keys[2:5]
"""
but instead of accessing just one item with a position, we get a set of items by slicing it from position 2 to position 5.

This might be a little bit confusing because we know that "a" is that position 0, "b" is at 1, "c" is at 2,
but the one at position 5 is actually "f", so how does this get us c, d, and e?

Well, you have to visualize it like this:
piano_keys = a,b,c,d,e,f,g
 posistion  0 1 2 3 4 5 6 7
Imagine that zero position is actually at the beginning of the list before where "a" starts. 
And at the end of the list, we're actually at the slicing position of 7.

If we think about it this way, then the way that we're slicing this list is going all the way from position 2
to position 5 then of course, we would end up with c, d, and e.

If you take a look at this code in my Repl.it:
"""
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:5])
"""
I've essentially got the same code that we saw in the slides
and we're slicing this list of piano keys from position 2 to 5.
When I hit run, you will see that what gets printed is c, d, and e, exactly the slice that we wanted.
"""
['c','d','e']
"""

Now, there's other things that you can do with slicing that's pretty cool. 

So, for example, if you wanted to slice from position 2, which remember is right here
"""
piano_keys = a,b,c,d,e,f,g
 posistion  0 1 2 3 4 5 6 7
"""
because we're starting at 0, 1, and 2, and you want to slice it all the way to the end of the list, well,
you can just emit the second number. 
"""
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:])
"""
You can have two and then a colon.
"""
['c','d','e','f','g']
"""
Now, when you slice this you get all of the rest of the list starting from the position that you specified.

And this works in the opposite direction as well.
Let's say that we want to get hold of everything up to position 5. 

Well, we could omit the first number, add a colon, and then after the colon specify the end slice position:
"""
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[:5])
"""
And now we get all of the items in the list up to that position 5.

In addition to just slicing between two numbers, we can actually specify a third number after another colon.
And what this number does is it sets the increment. For example, we wanted the slice from a position 2 to position 5,
but we want to only get every other item:
"""
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[2:5:2])
"""
So then it would give 'c', it would skip over the second one, and then it would give us 'e'. 
And if I hit run, this is exactly what you see:
"""
["c", "e",]
"""

So let's say I wanted to get hold of everything in this list but I wanted every second item. 
Well, then this is what my code would look like:
"""
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[::2])
"""
go from the beginning to the end and then skip every second one.
And I end up with a, c, e, and g.
"""
["a", "c", "e", "g"]
"""

Now to extend this a little bit further, we can actually use this neat trick to specify a -1 as the increment
and what this does is it will actually reverse this list for us going from right to the end to the beginning. 
"""
piano_keys = ["a","b","c","d","e","f","g"]
print(piano_keys[::-1])
"""
So essentially the increments are by one, but it's by -1, so that way we get the list starting from the end
all the way back to the beginning.

And this is a really neat trick that you'll see a lot of people use when it comes to manipulating lists and tuples. 

So speaking of tuples, this method of slicing also works for tuples.
So let's say we had a piano tuple, which remember is defined by a set of parentheses with items inside separated by
commas. 
"""
piano_keys = ["a","b","c","d","e","f","g"]
piano_tuple = ("do", "re", "mi", "fe", "so", "la", "ti")
print(piano_keys[])
"""

Well, we can use the same method of slicing to work with our tuple.
So we use our square brackets, let's get hold of the items from section 2 to 5:
"""
piano_keys = ["a","b","c","d","e","f","g"]
piano_tuple = ("do", "re", "mi", "fe", "so", "la", "ti")
print(piano_keys[2:5])
"""
Then when we hit run, you'll see it gives us "mi", "fa", "so"
"""
["mi", "fa", "so"]
"""

"""
### Challenge
"""
So coming back to our code main193.py, I have a challenge for you.
Can you figure out how to use what we've just learned about slicing to change this code so that we get rid of this
if statement 
"""
    for segment in snake.segments:
        if segment == snake.segments:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
"""
where we're passing over the snake head so that we are in fact only
checking that the snake head has a distance to every segment other than the first segment, less than 10 

If you managed successfully to do this, you should be able to get rid of this if statement, 
change this to a single if statement and somehow figure out a way of making this code work using slicing.
"""
    for segment in snake.segments:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
"""
Pause the video and give this a go.
# My Solution
"""
# Detect collision with tail.
for segment in snake.segments:
    if snake.head.distance(segment[1:]) < 10:
        game_is_on = False
        scoreboard.game_over()
"""

Alright, so we know that we want to loop through every segment in snake.segments other than the first one. 
Well, all we need to do is simply slice this list of segments. 
"""
for segment in snake.segments[]:
    if snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()
"""
So we can get hold of everything that starts off from position 1 to the end, by writing 1: nothing.
"""
for segment in snake.segments[1:]:
"""
This will give us everything inside the list other than the first item, like so.
"""
piano_keys = ["a","b","c","d","e","f","g"]
piano_tuple = ("do", "re", "mi", "fe", "so", "la", "ti")
print(piano_keys[1:])
"""

And then we can use that segment to loop through it and then check every segment 
in the tail against the distance to the head. 
"""
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()
"""
And now when you run the code, you can see that it works just as perfectly as before,
but we've now vastly simplified our code using the power of Python slicing.

Have fun playing with your snake game and be sure to let me know your highest score because I can't seem to get past 10.
And you've pretty much seen in this tutorial how bad I am at this game, but I'm sure you can do much better. And on top of that,

think about ways that you might want to customize your snake game.
Maybe you want to change the food to have a different color or a different
shape, maybe your snake is actually going to eat turtles, I don't know. The world is your oyster.

Now that you've learned about so many more concepts in Programming
including inheritance in OOP as well as slicing lists and tuples.
So I hope you've had fun building this game and I'll see you tomorrow.