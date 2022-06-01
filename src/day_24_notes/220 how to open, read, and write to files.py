"""
In this lesson, I want to talk about the file system and how you could use Python to open up
files, read files, write to the files, and also close them down again, all without touching the mouse
So that way we can start saving our high scores into a file and retrieve it the next time we open up our program.

Let's start out by trying to do some of the simplest things with a file, reading and writing.

Now I've created a new project using PyCharm called day-24, and I've created my main.py where we're going to write our Python code.
But in addition, I'm also going to create a new file which is going to be called my_file.txt.

So this is going to be a text file. Now, inside this text file, I'm going to write some text.
Hello, my name is Angela. And if you want, you can actually find this text file inside your project folder,
and you can actually open it up with your native text editing software. So TextEdit on Mac or Notepad on Windows.

And you can see it's just a bunch of text. There's nothing really special here.
But what we can do using Python is that we can actually open up that file.

So, notice how this method, open, is a inbuilt method.

So you don't have to import anything, you can use it directly. And it takes a number of inputs;
the file that you want to open, the mode that you want to open that file in,
and a whole bunch of other optional things that you can specify.
In our case, I'm going to specify the name of my file as a string, so my_file.txt.
"""
file = open("my_file.txt")
"""

So remember that extension. And then I'm going to open this file and I'm going to save it inside a variable called file.
So when we hit run right now, nothing's really going to happen.
You're not going to see anything happening, but behind the scenes,

Python has already opened up this file and its ready for the next operation that you might want to do on that file.

So the next thing I wanna do is I wanna read the file and this read method returns the contents of that file as a string.
"""
contents = file.read()
"""

So we can now save it inside a variable called contents and I can go ahead and print out this contents.
"""
file = open("my_file.txt")
contents = file.read()
print(contents)
"""
So when I hit run right now, you can see what gets printed out is the content from my_file.txt.
And if I go ahead and modify my file to add some more lines and I hit run again,
you can see that all of the lines are being printed once we've opened the file, we've read the file,

and we print the contents that we have read. At the end of all of our work,
what we have to do once we're done with that file that we've opened we also have to close it. If there's an open,
there's probably going to be a close. 
"""
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()
""""

Now, why do we need to close the file?

Well, once Python opens up that file, it basically takes up some of the resources of your computer.
And at some point later on, it might decide to close it and free up those resources,
but we don't know when that's going to happen and if it will happen.

So instead, we're going to tell it to close down the file manually using this line of code.
"""
file.close()
"""

It's a similar concept to having lots and lots of tabs open in your browser.
While it's kind of convenient to have all of these tabs open, if you actually want your computer to perform at its best
you actually want to only use as many tabs as you need.
Every extra tab is going to add a little bit of burden to your computer and especially if you're using a very heavy application like Chrome
which likes to take up a lot of resources of your CPU and your computer. If you have more than 20 or 30 tabs,
you'll notice a significant decrease in the speed of your computer. So here's a computer tip as well as Programming tip,
always close down tabs that you've opened and always close out on files that you've opened. 

Now because it's kind of hard to remember to close a file because
we might be doing lots of other things in between the open and close, right?
We might be writing to the file, we might be modifying it or reading it line by line or doing lots of different things. 

So instead, what many Python developers opt for is a different way of opening the file.
We can use a 'with' keyword. And 'with' we can open this file and then we can open it as whatever it is we decide to name. 
"""
with open("my_file.txt")
contents = file.read()
print(contents)
file.close()
""""
So this you can name to anything. You can name it as f, you can name it as file.
"""
with open("my_file.txt") as file:
contents = file.read()
print(contents)
file.close()
""""
It's basically the equivalent to that variable that we created earlier on which stored the opened file.

Now we can indent the rest of this and I can delete this file.close. 
"""
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
""""

And you can see that it works exactly the same as before,

but now we no longer have to remember to close our file just by adding some keywords here.
This 'with' keyword is going to manage that file directly.
So as soon as it notices that we're done with it, it'll close down the file.

It kinda makes me wish that something similar for tabs existed,

but let's get back to our Python code.

So now that we've opened up my_file.txt, we've saved into a variable called file,
we've read that file and saved the contents that we read into a variable called contents, 
and then we've printed it. 

Now, what if instead of reading the file, I wanted to write to it? Well, it's just as simple. 

So we can get hold of our file and then call write.
"""
with open("my_file.txt") as file:
    file.write("")
"""
And we can put any sort of string inside this write method to put into our file.
So let's put some text, let's call it new text.
"""
with open("my_file.txt") as file:
    file.write("New Text")
"""
And I want this new text to be written into my_file.txt.

And if we run the code as it is, you'll notice that it doesn't work
cause it says that unsupported operation, this file is not writable.

And this is because we opened up the file in read-only mode.
So remember when we took a look at some of the parameters for this method open,
one of them was called mode and by default, it's set to read-only,
so 'r.' 
"""
with open("my_file.txt", mdoe="r") as file:
    file.write("New Text")
"""

Now if we want to write to it, so make it editable, we have the change, the mode to 'w' for write.
"""
with open("my_file.txt", mdoe="w") as file:
    file.write("New Text")
"""

So now if I run the code again, you can see that process finished with exit code zero
which we know to mean that everything was successful. And if I take a look inside my_file.txt, all of the previous text
got magically deleted and replaced with the new text that I wanted to write.

Now, if you don't want to delete everything that is in the file but you just want to add to it,
then you can change this mode from 'w' to 'a' and 'a' stands for append.
"""
with open("my_file.txt", mdoe="a") as file:
    file.write("New Text")
"""
So just as we like to use list.append and then we can add something to the end of the list, well,
the same thing happens with appending and writing. 
So I can write my new text and I can add a new line, remember we can use \n to
add a new line, and then add the new text.

And now take a look at the after version when I hit run and we write this new line and new text by appending it to my file.
It's gone at the very end of the file here. 

Now, one of the important things you need to know when you're writing files is when
you try to open a file in write mode and that file doesn't exist, then it's going to actually create it for you from scratch.

So let's go ahead and create a file which I'll call new_file.txt,
make sure you've got the extension in there. And we have the mode as write set. Because this new_file.txt doesn't exist
in this folder, then it's actually going to create it for us.
"""
with open("new_file.txt", mdoe="w") as file:
    file.write("New Text")
"""
So now when I hit run, you can see that once this goes through,
that new file gets created and the new text has been written inside.

Now, remember this only works when you're in the write mode and when that file doesn't currently exist.

So those are some basic ways of working with the file system. We can open and read, we can open and
write. And by using these different modes, append, read, or write, we can define what it is that we want to do with that file that we've opened.

Now that we've learned how to work with the file system, in the next lesson
I want to show you how we can fix our snake game so that we can write to
a text file our high score. And every time we open up and run our game,
we fetch that file and see what the previous high score was so that we can load
it into our game. So for all of that and more, I'll see you in the next lesson.
"""