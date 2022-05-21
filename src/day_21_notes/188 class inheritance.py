"""
Let's talk about another feature of Object Oriented Programming that's really, really handy.

And it's something that we call class inheritance.
"""
class inheritance
"""
How does this work?

Well, let's say that you code up a robot chef and you give it a bunch of functionality.
You tell it how to bake, how to stir, how to measure:
"""
bake()
stir()
measure()
"""

And then at some point you decide actually, you know, in my restaurant, I also need a pastry chef.
Now this pastry chef will need to know some of the things that a chef knows how to do, but it also needs something extra.
So you don't want to create this pastry chef entirely from scratch. 

Instead, what you want to do is you want to be able to take the methods you've already defined for the chef class:
"""
bake()
stir()
measure()
"""
and then just add to it, add a few other relevant methods like how to knead dough or how to whisk some eggs.
"""
knead()
whisk()
"""
So it's process of inheriting behavior and appearance from an existing class is known as class inheritance. 

When we're talking about class inheritance, you can inherit both appearance, so attributes, like for example, 
if you inherited the same eyes as your mother, or if you inherited the same nose as your grandfather,
but you can also inherit behavior.

So maybe you chop tomatoes in the same way that your dad chops tomatoes. And if you believe my mother, 
I'm lazy in the same way that my dad is lazy. So not only can inherit appearance, but we can also inherit behavior. 

Now, how does inheritance actually work in terms of the code? Well, we can define a class, let's call it Fish,
"""
class Fish:
"""
and it has an initializer.
"""
class Fish:
    def __init__(self):
"""

Now in order to get this Fish class to inherit from another class, all we have to do is to
add a set of parentheses after the name of the class and then provide the class that we want to inherit from.
"""
class Fish(Animal):
    def __init__(self):
        super().__init__()
"""

So in this case our fish is inheriting from the animal class.
And then in order to get a hold of everything that an animal has and is, so its attributes and methods, 
all we have to do is inside the init, add this 
"""
        super().__init__().
"""
And the super refers to the superclass.

So basically, initialize everything that the superclass: (Animal) can do in our fish class. 

Let's take a look at this in terms of real code.

First, I'm going to create a animal class 
"""
class Animal:
"""
and this animal class is going to have an initializer where we're able to define some attributes, right?
"""
    def __init__(self):
"""
So let's say that all animals have, um, two eyes. So num_eyes = 2.
"""
        self.num_eyes = 2
"""

Now at the same time, I'm also gonna define a method associated with this animal class.
Let's say that all animals know how to breathe.
"""
    def breathe(self):
"""
So inside this breathe method, I'm going to keep it quite simple. I'm just going to say inhale, exhale.
"""
        print("Inhale, exhale.")
"""
#Note
"""
class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale.")
"""
So that's breathing done. 

Now later on, I decide to define a fish class 
"""
class Fish:
"""
and this fish class probably also knows how to do certain things. So for example, maybe it knows how to swim, right?
"""
    def swim(self):
        print("moving in the water.")
"""

Right now, if I create a object from this Fish class, 
let's say I create an object called nemo that's created from the Fish class,
"""
nemo = Fish()
"""
then I can say: 
"""
nemo.swim()
"""
"""
class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale.")

class Fish:
    def swim(self):
    print("moving in the water.")
nemo = Fish()
nemo.swim()
"""
And you can see when I run this code, it says that Nemo is moving in water.

Now, what if I wanted this Fish class to inherit everything that the animal class can do,
including the attribute number of eyes and also the method breathe.

All I have to do is to add this animal class after the name of the fish class inside parentheses,
"""
class Fish(Animal):
"""

and then I have to add the initializer
"""
    def __init__(self):
"""

and inside the initializer, I have to trigger a call to the superclass, which is in this case, the animal class.
"""
        super()
"""
And then I'm going to call the initializer, like this:
"""
        super().__init__()
"""

So now what these two parts of the code: the (Animal) and super().__init__()
"""
class Fish(Animal):
    def __init__(self):
        super().__init__()
"""
 
does is it allows anything that's created from my fish class to inherit all of the attributes and methods from the

superclass, which is the animal class.

"""
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()

"""
Now I can get my Nemo to start breathing. 
"""
nemo.breathe()
"""
And you can see if I hit run, then it will also inhale and exhale.
And in addition, if I wanted to print nemo.num_eyes,
"""
print(nemo.num_eyes)
"""
then you can see this is also going to print 2.

So now my object that's created from the Fish class now has access to all the
attributes and methods from the superclass that inherited from the animal class.

Now, what if I wanted to inherit a method?

So get all the things that it does, for example, the breathe method.
But what if I wanted to modify it a little bit? So for example,
a fish does, in fact, breathe, but it kind of breathes underwater. So let's say I want to define the breathe function
and I wanted to have the same functionality as the superclass which I'm inheriting from. 
So I want to print inhale, exhale, but I also want to do something extra. 
"""
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):

    def swim(self):
        print("moving in water.")
"""

Well, in this case,we would get hold of the superclass and then call breathe on it.
"""
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()

    def swim(self):
        print("moving in water.")
"""

This means we're going to do everything that the breathe method from the superclass does, so all of this, 
"""
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
"""        
but afterwards we're going to do something a little bit more special. So we're going to say we're doing this underwater. 
"""
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")
"""

Now, when this line 
"""
nemo.breathe()
"""
gets run, you can see what happens is it will print out inhale, exhale
and this comes from the super class' breathe method here:
"""
        super().breathe()
"""
And then afterwards, it will print its own unique twist on breathing, which is doing this underwater. 

By learning about inheritance, what it allows us to do is to take an existing class that we've created or
somebody else has created, and then build on top of it without having to reinvent the wheel and redefine
everything that's in that class. 

So in the next lesson, I'm going to show you how we can inherit from the turtle class to upgrade the turtle
to be able to do extra things such as creating a piece of food or creating a scoreboard. 

For all of that and more, I'll see you on the next lesson.
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

"""