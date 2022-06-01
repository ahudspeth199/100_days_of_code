"""
Now let's go ahead and tackle this challenge.

So the first thing I want to do is to get hold of all of the invited names and I want to turn them into a list.
"""
invited_names.txt
"""
Now I can, of course, rather tediously go and add some square brackets, add some quotation marks around
it, and then add it into my main.py. But I don't want to do that.

Instead, I'm going to get Python to read the file.
So using our classic syntax with open, I'm going to open up that file.
But in order to open it up, I need to specify a string which is going to be the path that leads me from here to here.

So let's think about how we might get there.
Now, this input, output folder is on the same hierarchical level as our current file where we're writing our code.
If we want to use a relative file path, we can simply say go into the current folder which is mail-merge-project-start 
and then find a folder called Input.
"""
with open("./Input")
"""

Inside this folder called Input, we're going to go to another folder called Names.
And then inside that folder of names, we're going to get a hold of that file called invited_names.txt.
"""
with open("./Input/Names/invited_names.txt")
"""

And PyCharm is super clever and it helps you out with a lot of typing. So it saves you some time as well.
And then I'm going to save it as names_file.
"""
with open("./Input/Names/invited_names.txt") as namesfile:
"""

Now that I've got this file open I'm going to go ahead and read it. So names_file.read. 
And once I've read it, I'm going to save it to a variable called names and then I'm going to print out my names.
"""
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read()
    print(names)
"""

So now if I go ahead and hit run my main.py, you can see that it prints out all of these names individually
because it's getting hold of everything that's in here and just printing it out.

Now, at this point, I would really like these names to be in the format of a list.

So if you remember, that's where this readlines method is going to be really helpful
"""
readlines()
"""
because it returns a list containing each line inside the file as a list item.

Now, instead of saying names_file.read, let's replace that with readlines.
"""
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
"""

Now, when I hit run, you can see it prints out names, and names is now magically turned into a list.
So now that we have our list of names which we've extracted from our invited_names.txt, 
then we can go ahead and proceed to the next step where we're going to replace this placeholder in our starting
letter with each of these names.
"""
[name]
"""

Let's go ahead and create a constant at the top which I'll call PLACEHOLDER, and I'm going to set
it as the string which is the square brackets and then the word name 
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
"""
because this is the string that we want to replace from our starting letter.

The next step is to open up our starting letter.
So again, I'm going to use open and then I'm going to specify the path.

So from here, I'm going to go into the folder that's at the same level as this file """main.py""",
so using the ./ and then I'm going to go into input again and then I'm going to go into instead of names, I'm going to go to letters.
And I'm going to get hold of my starting letter and I'm going to open this as the letter_file. 
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
"""

With the letter_file I'm simply just going to get a hold of the letter_contents by saying letter_file.read.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
"""

And this is going to be a normal read because I want all of the content inside that letter and it's
now going to be saved as a string inside my letter_contents.

The next step is to go through the letter contents and replace that placeholder with the actual name
that we've got in our list.

To do that we'll need the second method that I showed you which is the replace method. So we can get
hold of the text call, replace, and then the output of this method will be a new string which has modified
this text. I in our case we'll need a for loop. So we can say for name in our list of names, let's go through
each of the names in that list and then let's get the letter_contents and replace the placeholder,
so the old string, with a new string which is going to be the name.
And once we've replaced it, then we're going to save it into a new_letter.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
"""

Now that we have our new letter, let's go ahead and print it out and see what it looks like.

So you can see all the contents of each of the letters being printed, but other than the very last
letter that looks pretty normal, every other letter has a new line after the name.

So remember when we printed out each of these names, you can see that after each of the names that
they've extracted from this list of invited names, there's a new line that's being added, and you can see that with this \n.

The only one that doesn't have a new line is the very last one. What we need to do is to strip the new line. 

Does that remind you of something?

Well, we have a method that we saw called strip which can take away any of the spaces at the beginning and at the end of the string.
And then we can end up with an output which is the string without any of those leading and trailing spaces.

We're going to loop through each of the names and then we're going to take the name and we're going to call strip on each of those names.
And then we can save it to a variable called stripped_name. And now we can use that stripped_name instead of the name.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
"""
Now if I go ahead and print out our new_letter,
you can see that each of the letters look exactly like how we want them to be. 
All we need to do now is to write them into a new file. 

In previous lessons I mentioned that when you open a file that doesn't exist, Python will actually create that file for
you.

Again, using our with open, I'm going to navigate to this ReadyToSend folder. Going from where we are in main.py,
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open("./")
"""
we're going to go to the output folder and then we're going to go to the ReadyToSend folder.
And then inside the ReadyToSend folder is where we're going to create our new file.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open("./output/ReadyToSendd/")
"""
So let's think about what we want our file name to look like. In the intro I showed you
this is the format for each of the files; letter_for_Aang.txt.

And then this part is replaced by each of the names.
So let's write that letter_for_ the name and then .txt.
We can use an f string to replace this part with the stripped_name.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt")
"""
So now we should be creating a new letter for each of the names in our list of names.
So now let's refer to this file as the completed_letter.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt") as completed_letter:
"""

What we want to do with this completed_letter, which at the moment is blank, is we want to write to it.
So to do that, we have to change the open mode from default which is 'r' for read to 'w' for write.
And this will allow us to get our completed letter and write to it.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write()
"""

What do we want to write in there?

Well, we want to write the new letter that we've created, of course.
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
"""
That's pretty much the end of our code, and all we have to do is to go ahead and hit run. 

And once I hit run, you can see there's a whole bunch of letters that have been generated over here,
and if I click on each of them, you can see that the name placeholder has now been replaced
and I'm now ready to go to the printers and print all of these out.

So did you manage to figure out how to complete this project?
If not, be sure to review the relevant parts of the lessons today so that you're really confident with
what's going on and you understand all of this code.

If you want to take a look at the completed solution, then head over to the course resources and you'll
find a link to the final project code which actually works even within repl.it.
So you can delete all of these files and you can see it generate them from scratch.