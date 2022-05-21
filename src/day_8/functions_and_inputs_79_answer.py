# create a simple function then call the function

#def greet():
    #print("hello")
    #print("nice to meet you")
    #print("don't know another greeting")

#greet()

# create a function that allows inputs
#name = input("Enter your name:\n")
#def greet_with_name(name):
    #print(f"Hello {name}")
    #print(f"nice to meet you {name}")

#greet_with_name(name)

name = input("Enter your name:\n")
location = input("Enter your city:\n")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name, location)