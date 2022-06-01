"""
The big topic that we're going to explore today is a concept known as a list comprehension.
And as I mentioned before, this is something that's really unique to the Python language.

In many other programming languages, you don't actually have access to something like this.

There's nothing that really compares to it.

And it's something that Python developers really, really love because it cuts down on the amount of typing and it just makes the
code a lot shorter, and in most cases, a lot easier to read.

So what exactly is a list comprehension? Well, it's a case where you create a new list from a previous list.
So far we've been doing that using for loops.

So for example, if I have a list of numbers, 1, 2, 3,
"""
numbers = [1,2,3]
"""
and I want to create a new list where each number is increased by one,

well then I would use a for loop creating a new empty list and then looping through
each of the numbers in that list in order to add one to each of those numbers.
And then I would append each of those increased numbers to my new list.
"""
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
"""
And I would end up with a new list that consists of three items,and it will be 2, 3, and 4. Now using list comprehension

we can take these four lines of code and turn it into one.

And the way that we create a list comprehension looks something like this.
"""
new_list = [new_item for item in list]
"""
I like to use the keyword method where you type out the list comprehension keywords,
and then replace each of the words with the actual item in your code.

The way that we would create any list comprehension is we will create the name
of the new list and instead of creating a empty list and then having to append
to it or populate it, we actually going to create it straight in the same line.

So we open up a set of square brackets to denote that we're creating a new list,
and then we have this new _item for item in list keyword pattern. 

Here's how it would work.
Let's take that same thing that we did before where we took you a list of numbers
and we created a new list where each number is increased by one,
and let's see how we would do it using list comprehension.

So the first keyword I'm going to replace is the list.

So this is the list that we're going to iterate through. And in our case,

it's this list of numbers. So let's replace that list

keyword with the actual list, which is numbers.

The next thing that is easy to understand is each item in the list.

So we can call this anything we want. In the for loop here,

we called it n, so why don't we go ahead and call it n again?

This n is going to represent each of the numbers in that list of numbers

just as it does in this for-loop.

And the final keyword that we haven't yet replaced is the new_item.

So what do we want each of the new items to be in this new list?

Well,

each of the new items is basically calculated by taking n and then adding one

to it.

So this line is the expression or the code that we need to execute in order to

get a new_item. So this becomes our final list

comprehension. We have our lists of numbers

and then we create a new list where we loop through each of the numbers, n,

inside this list of numbers

and then for each of the n, we add one to it in order to create the final list.

So when you look at a list comprehension just like this as in the real code,

it can be a little bit confusing to see how would you read it,

which order does it happen.

But when you're using this keyword method that I often use

where you just type out what you need to have inside a list comprehension,

you need a name for the new list, you need a set of square brackets

and then inside the square brackets, you have new_item for item in list.

Then you go through it replacing each of the keywords, list item

and new_item. So I want you to have a go at actually writing out this code.

Go ahead and create a new PyCharm project,

and I want you to go into the Python console.

We're not actually going to be writing code inside our main.py.

And the reason is because the console allows us to write code line by line

and then we can view our variables really easily on the right-hand side pane

here. For example, if I have my list of numbers, 1, 2, 3,

and then I have to write out my list comprehension

where we create our new list which I'll call new_numbers,

and then we have to create our list comprehension.

So the way to remember it is new_item for item in list.

So now go ahead and write this out and see if you can remember how we actually

structure our list comprehension and see if you can get it to work within your

PyCharm console. So pause the video, give that a go.

All right. So our list is of course, this list of numbers.

So let's replace that first.

And then for each of the items in that list of numbers, well,

we can call it anything we want. So I'm just going to call it n or num,

it doesn't matter. But as long as you're consistent in using it

when you create the new item

because each new item is going to be the n,

which is each number in the list, +1.

So now when I hit enter,

you can see I've got this new list called new_numbers created from the previous

list, numbers, and this now has the same number of items

but each item is now increased by one.

Now it's important to remember that when we say list comprehension,

it doesn't strictly mean that you can only work with list.

You can work with other sequences like strings, for example.

So here I've got a variable called name, which is just a string. It's the word

Angela.

And I'm creating a new list by using a list comprehension that has this kind of

code. Now,

I want you to pause for a second and think about what would be in this new list,

what would it look like? And then I want you to try it out inside PyCharm.

So pause the video now. All right.

So name equals Angela, this is the variable that we're working with.

And then I'm going to create a new list

which I'll call letters_list.

This new list is going to be created using my list comprehension.

So it's going to be letter for letter in name. And what this does is it takes

this sequence, this string,

it goes through each of the letters in that string

and then it adds each of the letters into this new list.

So when I hit enter, you can see, this is what letters_list

looks like. It's just split off my string into individual letters

and it's added it into a brand new list.

As I mentioned, these things in Python

like a list or a string or a range or tuple, they're called sequences because

they have a specific order. And when you perform a list comprehension,

it's going to take that sequence and it's going to go through it in order either

be it the letters in the string or the items in a list.

And then it's going to take each of those items in that correct order

and then do something with it, either add one to it, or in this case,

do nothing and just add it to a new list. Here's a challenge for you.

Can you take the range,

which is also a sequence that we can iterate through, and then create a range

between 1 and 5?

And remember that the way that the range works is it's going to take 1 and

then 2, and then 3 and then 4, but it's not going to go up to 5.

I want you to loop through this range and then create a list where each of the

numbers in the range is doubled.

And the final list should look like this. It will be 2, 4, 6,

and 8. Pause the video and see if you can complete this challenge.

All right. So let's create our new lists

which I'm just going to call range_list.

And we're going to use that keyword pattern to remind ourselves.

So it was going to be new_item for item in list.

And this list, in this case, is actually not going to be a list,

it is going to be a range between 1 and 5.

And then each of the items, we get to give it a name, which I'll just call num.

And then in this new list, what is each new item going to be? Well,

it's going to be num multiplied by 2. So now when I hit enter,

I get my range_list, which is 2, 4, 6, 8.

So its loop through each of the numbers in the range

and its multiplied each of those numbers by 2,

and then its created a new list using each of those numbers.

Now the final thing I want to show you regarding list comprehensions is that

there's also such a thing as a conditional list comprehension.

This takes our keywords a little bit further.

Whereas previously we stopped right here,

new_item for item in list. We can also tag on two more keywords;

if and a test.

What this is going to allow us to do is to only add this new item and only to

perform this code if the test actually passes.

Here's an example. I've got a bunch of names here; Alex, Beth, Caroline,

Dave, Eleanor, and Freddy. Now,

one of the neat things that you can actually do with the Python console is not

only can you view what all of the variables are equal to,

but you can also edit them if you have an issue.

The sharp-eyed amongst you will know that I've actually made a typo in this

name, it's not Elanor, its actually spelled a little bit differently.

So what I can do on the right-hand pane here is I can right-click on that piece

of data that I want to change and then click set value,

and then actually change the data here.

Now that I've got that spelled out correctly, if I type names and hit enter,

you can see it's now been corrected and this is my new list of names.

So using this list of names,

I'm going to try and create a new list of names,

but I only want the short names.

I only want the names which is made up of four letters or less, like Alex or

Beth.

The way I would do this is I would create a new list,

which is called short_names. And then I would use my list comprehension.

And remember, in this case, the keywords are new_item

for item in list. And then if and a test.

So let's fill in the easy parts first.

The list is going to be our list of names, the item I can call it

anything I want. I'll just call it name in terms of the singular form of names.

And then once I loop through each of the names inside my list of names,

what is the new item going to be? Well, it's actually going to be unmodified.

It's just going to be that same name. But in this case,

I'm only going to add that name to the list if it passes this test.

And this test is going to look at the length of the name

which I created here,

so if I named this n then I would be testing it against n and it would be adding

n as well. But because I've called it name

so I'm going to use that name right here in the condition.

So if the length of the name is less than five,

so it has four or less characters,

then I'm going to add that name to my new list. Now, when I hit enter,

you can see that I've got this new list of short names and it only contains the

names, Alex, Beth and Dave.

So this list comprehension is now a little bit more complex because the first

thing it does is it goes through each of the names inside this list of names,

it checks each of those names for its length. And if the length is five,

then it adds the name to this new list.

Now here's a challenge for you.

I want you to take all of the names from this list of names

which are made up of five letters or more, so basically Caroline,

Eleanor and Freddie,

and I want you to turn each of these names to the uppercase version.

What you should end up with is a list where you have CAROLINE in all caps,

ELEANOR in all caps and FREDDIE in all caps.

But of course, you're not going to just type this out,

you're going to use list comprehension.

Pause the video and see if you can complete this challenge.

All right. I'm going to call this new list long_names,

cause I haven't eaten for a while and I lack imagination. Now,

in order to create this list of long names,

I'm going to use that new keyword pattern that we learned,

which is new item for item in list

if test. The list is, again, going to be our list of names.

Each of the items we can call it anything we want,

but I'm going to call it name. And if you find that this is too similar to this,

you can call anything you want.

Nom, you can use French or you can just write n or you can do anything you want.

This name that we're looping through is going to be tested in order to see if

we're actually going to create a new item.

So the test, in this case, is we're checking to see if the length of the name is

now greater than five.

And if this name that we're currently looping through passes this test,

then we get to specify what the new item should be.

So the new item is going to be that particular name that passed the test,

but then it's going to be uppercased,

so we're going to call name.upper in order to create the new item

that's going to be added to the list. So now once I hit enter,

you can see the new list that I've created, long_names, has Caroline,

Eleanor and Freddy, all in uppercase.

Essentially, we looped through each of the names in the list,

we took each of those names and checked that they'ree longer than five.

If they were, in fact, longer than five,

then we looked at this part of the code to see what we should do with each of

those names. And in our case, we've turned it into uppercase.

So there's quite a lot of theory covered in today's lesson.

And if you want to see the code that I've been writing so far,

then you can always head over to the day-26-end Repl.it in order to either

download it or just read through the code that I've been typing. Now,

in order to be able to fully understand what's going on,

you can't just watch me talk about it. You have to practice.

So in the coming lessons,

I've got a whole bunch of exercises for you to practice using and creating list

comprehensions for yourself. And that way, once you've done the drills,

you've done the code press-ups, then you'll be able to show off your list

comprehension muscles. For all of that and more, I'll see you on the next lesson.