# I want you to have a think about what you just saw in the slides
# and see if you can create a function called add
# where you can pass in as many numbers as you want
# and it will always add together all of the numbers that are being passed into the function as the input,
# and then return the total sum.

"""
here is my code
def add(*args):
    print(args)
    return sum(args)


add(10,4,3)
"""

def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,6, 2, 1))


