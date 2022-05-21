
#188 A feature of Object Oriented Programming called class inheritance
"""
By learning about inheritance, what it allows us to do is to take an existing class that we've created or
somebody else has created, and then build on top of it without having to reinvent the wheel and redefine
everything that's in that class.
"""
"""
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
"""

# 189 I'm going to show you how we can inherit from the turtle class to upgrade the turtle
# to be able to do extra things such as creating a piece of food or creating a scoreboard.
"""


"""