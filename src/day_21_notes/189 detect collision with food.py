"""
All right. So now that we've learned all about inheritance, it's time to apply the theory to our snake game,

and we're going to use it to detect collision with food.

Our snake should be able to head a piece of food,

which is just going to be a blue circle. And every time it touches the food,

the circle moves to a new, random location on the screen.

If we take a look at our code,

you can see that the main.py controls the entire game.

It dictates how the screen should behave and how the snake behaves.

Now, everything that's to do with a snake,

it's a parent's and behavior, is all captured inside a class.

So everything snake related is inside the snake class.

So what we want to be able to do is to create a new food.py file

and this food.py is going to be its own class.

And the food class is going to know how to render itself as a small circle on

the screen. And then every time the snake touches the food,

then that food is going to move to a new random location.

So let's create the initializer for this food class.

And one of the things that we're going to need to do is we're going to need to

import turtle. So from the turtle module,

let's import the turtle class.

And this piece of food that we're going to see onscreen is going to be a turtle

object. Instead of creating it as an attribute in this class,

so self.food = turtle like this,

what we want to be able to do is we actually want this class, food, to inherit

from the turtle class.

So that way this food class is going to have all of the capabilities of the

turtle class,

but it's also going to have some specific things that we're going to tell it

how to do so that it behaves like an actual piece of food.

Here's a quick challenge. From what you learned in the last lesson,

can you figure out how to make this food class inherit from the turtle class?

Pause the video and give that a

go.

All right.

So we mentioned that there's only two steps we need to do. First is after the

name of the class

we add some parentheses and then put in the name of the class that we want to

inherit from. So in this case, it's the turtle class.

And then the next thing we need to do is we need to call the turtle's init

method inside the food's init method.

And you can see that as soon as you've added this inheritance here, this init

starts giving us a warning. And when you click on it, you can see

it says call to __init__ of superclass is missed.

So it actually knows what we need to do next.

That means if we click on the light bulb,

we can actually automatically just add in the superclass' call. This,

of course, you could just type it out and it's good for practice,

but in case you're ever wondering if you get these warnings,

you can always take a look at what PyCharm is recommending.

Now we've actually created our food class and we've inherited from the turtle

class.

What that means is we can now start using things that are from the turtle class.

For example, I can straight up say self.shape,

and it knows what shape is.

This is a method that the turtle class has that I'm now going to modify in my

food class. So when I initialize a new piece of food,

I'm going to make sure that it has a circular shape,

and I'm also going to get it to pen up so that it doesn't draw.

And then I'm going to define it's size.

And there's something called a shape size which I can use.

And what this allows me to do is to stretch the turtle along its length and

along its width. Now I'm not actually going to stretch it bigger than it is.

It's normally 20 by 20 pixels,

but I wanna turn it into 10 by 10 pixels.

So I'm going to stretch the length by 0.5,

so I'm basically going to half it.

And then I'm going to stretch the width also by 0.5.

So now it should be a 10 by 10 circle

which I've created by defining the shape size. Now,

remember all of these methods, shape, size,

pen up, shape, comes from this turtle superclass and we're only able to use it

because we're inheriting from the superclass so that our food class is now also

sort of a turtle, but it's more like a souped-up turtle. Finally,

it let's go ahead and define the color which I'm going to set as blue,

but of course, feel free to set it as anything you like.

And I'm also going to set the speed of my turtle to fastest. This way

I don't have to look at the animation of the food being created at the center of

the screen, and then moving to the location that I want it to.

Speaking of moving, we're going to need to use the goto to get it

to go to a random X, Y location.

So let's import the random module and let's create a random X,

which is going to be random.randint. Remember that our screen is 600 by 600

so that means our X-axis goes from -300 to +300

and our Y-axis goes from +300 to -300.

Now we don't want our food to be right at the edge of the screen,

cause it will be really hard to get the snake to go to right at the edge.

It'll probably just die on the wall.

So we want to maybe subtract this a little bit.

So we can go from -280 to +280 and the same on the Y-axis.

So let's generate a random integer from -280 to +280

and let's generate a random Y-integer in the same range.

So now we can tell our food to go to a random X and a random Y. All of this

is going to happen

as soon as we create a new food object from the food class.

Remember, whenever you initialize a new object from the class, the

init gets called. Back in our main.py

right below where we initialized our snake, we're going to initialize our food.

So food equals the food class and then parentheses.

And of course we need to get hold of our Food class from the food file,

like this.

Another thing you'll notice is that this turtle is now grayed out because we're

not using that class anywhere inside the main.py. So we can delete that

which gets rid of all our warnings on this page

and we get the green checkmark. Our food.py looks good,

our snake.py looks good,

and we're now ready to go ahead and run this code.

Notice how we've got our snake moving around on screen.

And at this point it doesn't really matter about the walls.

It's just moving around anywhere it likes. But more importantly,

we've got our food being randomly generated on the screen right here.

Now the next step is how can we detect when the snake and the food have come

into contact and then to tell the food to move itself to a new

random location? Well, we're going to do that inside our main.py.

Right after we've got our screen updating, our snake moving,

then we're going to detect

collision with food.

And we're going to do that by using a method from the turtle class called

distance.

The distance method works by comparing the distance from this turtle to whatever

it is that you put inside the parentheses.

So the X could be a pair of numbers, X and Y,

or it could simply just be a turtle instance.

So you're comparing this turtle against another turtle,

and you're trying to get hold of the distance between the two turtles.

So what that means is we can check to see if the distance from the first segment

of the snake,

so it remember that would be snake.head.distance,

and then the distance that we want to know is what is the distance from the

snake's head to the food. At this point,

you can check to see if it is less than a certain amount,

then it's pretty likely that the snake head is now colliding with the food.

So we know that the food is 10 by 10.

So if we add a bit of a buffer, let's just say,

if this snake head is within 15 pixels of the food or even closer,

so if the distance is less than 15,

then we can be pretty much certain that they've collided.

So let's go ahead and print something. I'll just write nom nom nom.

So if we go ahead and run our code and let's just get our snake back into view,

and if I now go and touch this piece of food, if I can,

then you can see nom nom nom being printed in the console.

Now let's go ahead and touch it again. You can see,

as soon as I collide with that food,

I get that print statement executing.

So now, instead of just writing nom nom nom,

let's figure out what we need to do next.

What we want to happen is the food should go to a new random location.

And, of course, that comes from this part of the code.

So why don't we go ahead and create a new method which we'll call refresh.

And this refresh method is going to create a new random X,

a new random Y, and then get the food to go to that new, random location.

Then inside our init, we can simply just call self.refresh.

So be careful that you didn't right reset because that's one of the methods from

the turtle class that we're inheriting from.

But what we actually want is to call this refresh method so that the food goes

to a new random location. And then back inside our main.py,

when the snake head collides with the food,

then we're going to get the food to refresh its own location.

So check this out. Now, when I hit the food,

then you can see the food now appears at a new,

random location. Like that. Now,

depending on how accurate you want the snake to hit the food,

so it might need to hit it dead on,

or if you're happy with it just gliding past and counting that as a collision,

then you could decrease the number here from 15 to 10.

Now I've done a bit of testing and this number seems to be the best distance in

order to get a valid collision,

but feel free to tweak around with the number and see how it goes. There we go.

We've managed to figure out how to create a piece of food by inheriting from the

turtle class, get the food to be generated,

and then to move to a new random location

every time the snake head collides with the food.

Now I know that in the snake game,

the snake segments increase once it hits a piece of food,

but we're only going to add that functionality at the very end of this project

when we're detecting collision with the snake tail.

So don't worry about that for now.