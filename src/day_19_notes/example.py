"""example of how the onkey fuction works """
# using the calculator program we will give an example of passing a function into another function

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# lets say we create a final function called calculator that will take three parameters

def calculator(n1, n2, func):
    return func(n1, n2)

# your going to take in the function name that was passed in (func) then call that function by adding the parentheses
# then passing in n1, and n2
# so now you a calculator function which can take any function as an input
# and once that function has been passed in there then that function will get triggered passing in n1 and n2
# then you can return that result as an output

# now you need to call your calculator function and pass in some numbers
# save it into a variable then print that variable

result = calculator(2, 5, multiply)
print(result)

# this is called higher order function
"""Higher Order Function"""
# it is a function that can work with other functions
# in this case our calculator is a higher order function because it is taking anothe function as an input then working
# with it inside the body of the function
# there are certain programming languages you can't do this at all but in python it is commonly used
# it is used to listen for events then trigger a function