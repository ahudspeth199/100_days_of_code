# Create a racing game or etch a sketch

"""Step 1"""
from turtle import Turtle, Screen

"""Step 2"""
tim = Turtle()
screen = Screen()

"""Step 6"""
# create a function called move_forwards
def move_forwards():
    """"This fuction will get tim to go forward"""""
    tim.forward(10)


"""Step 3"""
# in order to start listening for events you must get a hold of the screen object then tell it to start listening
screen.listen()


"""Step 4"""
# once it starts listening you must bind a function that will be triggered when a particular key is pressed on the keyboard
# in order to bind a keystroke to an event in our code we have to use an event listner
# the one we will be using is the onkey() method https://docs.python.org/3/library/turtle.html#turtle.listen
'''''
turtle.onkey(fun, key)
turtle.onkeyrelease(fun, key)

Parameters:
fun – a function with no arguments or None
key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
'''

"""Step 5"""
# screen.onkey()
# then you must bind some sort of function to this method

"""Step 7"""
# after creating the move_forward function go back to step 5 the onkey() method and have the space bar trigger the move_forward function
# basically when the space bar is pressed trigger the function move forward
screen.onkey(key="space", fun=move_forwards)

# when we use a function as an argument something that is going to be passed into another function
# we don't add the parentheses at the end the parentheses triggers the function to happen there and then
# but what we want is this method onkey() to listen for when the space bar is pressed and only when that happens to
# trigger the move forward function


"""Step 8"""
# the final thing I need to add is the exit on click so the screen doesn't disappear when you run the code
screen.exitonclick()


"""Notes"""
# what we have is a function that is being used as an input

"""Functions as Inputs"""
''''
def function_a(something):
    #Do this with something
    #Then do this
    #Finally do this
    
def function_b():
    #Do this
'''
# in this example lets say we have a function called function_a on a that take some kind of input
# then we have a function called function_b
# we can pass function_b into function_a like this:
"""function_a(function_b)"""
# notice when pass a fuction as an input we only pass the name without the parentheses at the end

# When using methods you have not created yourself like for example onkey() to use keyword arguments instead of Positional Arguments


"""Keyword Arguments"""
'''''
def my_function(a,b,d):
    #Do this with a
    #Then do this with b
    #Finally do this with c
    
my_function(c=3, a=1, b=2)
'''



"""Positional Arguments"""
'''''
def my_function(a,b,c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
    
my_function(1, 2, 3)
'''