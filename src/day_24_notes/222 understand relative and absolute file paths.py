"""
All right.
So we've seen how we can open and close files as well as read them and write to them.
But files don't just have a name.

They also have a path or a way of getting to them.

For example, here in this map, if we wanted this dinosaur to get to the golden egg, there's many paths that it could take.
But if we wanted to give it some directions as to how it might arrive on this path,
well we might say, you know, continue forwards at the volcano turn, right.

And then when you see a snake turn right again, and when you see the coconut tree
turn left and you will get to the cave with the egg.

Now on computers, it works quite similarly, but we have to remember that on the computer there's files and there's folders.
So files can live within folders and you can navigate through several folders deep in order to get to a particular file.

So let's think about what the file paths might be for a computer that has a structure that looks like this.
So the first thing to note is that at the very root of all of the files and the folders is basically the origin, right?

This is the root folder.

And on a Mac, you can see that our PyCharm projects live within my users folder,
inside a folder called users inside a folder called Macintosh HD.

So if I have this folder selected right here, I can say go to enclosing folder, which is this one.

And then if I keep doing this, you can see it keeps jumping up until it can go no further.

So the root on a Mac is the Macintosh HD, the hard drive. And that in terms of a path is represented by a single forward slash.

Now when you're on a Windows computer however, the root folder is usually your C drive.
So that becomes your root folder. Inside our root folder, our Macintosh HD or a C drive,
we have a folder called work. Inside that folder I've got a report Word document as well as a project folder.

And then inside that project folder, there's a PowerPoint called talk. Now, if we think about the file paths for each of these things,
this is what they might look like. The route is obviously just a /, the work folder will be
/work, report will be /work/ report.doc, project will be /work/project, and finally, the talk will be /work/project/talk.
ppt.

So this path is kind of like the direction that we were talking about previously.
It's a way for the computer to navigate to the file of interest which in this case might be the talk.ppt.

And we have to give it directions for which folder to go into and then which
folder, and then you'll find the file with this name.

Now, this is known as an absolute file path. Absolute file paths always start off relative to the root.
So you always see a forward slash to begin with, and sometimes you'll see C: or on a Mac
you'll just see the /. This absolute file path is basically a path that starts from the origin,
the route of the computer storage system.

Now there's also something called a relative file path. Taking this talk.ppt,

we know that the absolute file path is /work/project/ talk.ppt.

But what if we were actually inside this project folder?
So let's say that at the time when we're trying to get to this talk.ppt we're actually right here.

Now this, in computer-speak, is called the working directory.
It's basically the directory or folder that we're currently working from.

And once we've established a working directory, say that we are right here,
then we can use what's called a relative file path to get to a file that we're interested in.

So given that we're here and we're trying to get here, the relative file path is simply just ./talk.ppt.
The ./ signifies look in the current folder for this file.

If we switch up our working directory and let's say we are now working from the work folder,
how do we get to this talk.ppt? Well, the absolute file path would not change for this file,
but the relative file path would now be ./project/talk.ppt.
So we're walking from here to here to here.

Now, what if we wanted to go upwards in the directory tree?
Let's say we wanted to get a hold of this report.doc,
but we all currently working inside this project folder. How do we go one step up?
Well, we would right ..,

so two dots now, /report.doc.
So we're inside this project folder, we're coming out of it to the parent folder
which is the work folder, and then we're getting hold of this file.
So that two dots represents going one step up in the hierarchy to the parent folder,
which this case is the work folder.

Now what we've been doing is we've been writing code inside our main.py.
And that main.py has usually been inside some sort of project folder. When
we're trying to get hold of a file this is basically where we are at.
So our working directory is the work folder.

So that means if we wanted to get access to this report.doc file from our main.py,
all we need to do is write ./report.doc because we're working within
the same directory and we're just getting hold of this file.

Now, when you're using relative file path, you can use this ./
but you can also shorten it and get rid of it as well.

This is why we've been able to open this my_file.txt
"""
with open("my_file.txt") as file
"""
which is in the same folder as my main.py and notice how these two files are at the same hierarchical level. 

So let's do a quick challenge.

I'm going to delete the part where we write to the file and I'm going to change my file
so it just has one sentence and I'm going to locate this file by using 'Reveal in Finder' and on Windows that would be right-
click and Show in Explorer.

And it would show you the location of that file in your computer system.
Now, what we're going to do is we're going to move this file to the desktop.

And what I want you to do is I want you to go to the desktop, right-click on that file. 
And if you want a Mac, I want you to click on get info.

And if you are on a Windows, I want you to right-click and go to properties.

Now what you're looking for is this location here.

Now you can see that this current file, new_file, is located under the root folder, which in this case is the C:\Users\London
AppBrewery\Desktop\new_file.txt. 

On a Mac you can see that it's located under the root folder, 
which is Macintosh HD slash users slash Angela slash desktop slash my_file.txt. 

Here comes your challenge.
Now that we've moved our file away from our project, I want you to fix this code so that when you run it,
it won't give you this file not found error because at the moment there is no my_file.txt in the same working directory as our main.py.
It doesn't exist inside this folder.

Have a think about what you've learned so far and see if you can change this path so that our code works again.

And it's the same on Windows.
Use the location of the file on your computer and use the absolute path in the code to get it to work. 

Pause the video now.
"""
with open("C:\Users\ahudspeth\Desktop") as file:
    contents = file.read()
    print(contents)
"""

my solution
"""
with open(r"C:\Users\ahudspeth\Desktop\my_file.txt") as file:
    contents = file.read()
    print(contents)
"""

Instructors solution

All right. Here's how you would use the absolute path. So we know that our,
my_file.txt is located in the root folder and then it's users, angela, desktop. 
So let's go ahead and change this string.
Let's start at the root and then let's add the next folder, which is users.
And then let's add another slash and then we go to the next folder, which is Angela. 

Now of course, this will be different for you, but finally we go to our desktop and then we can get to our, my_file.txt.
So this is the full path to get to this file.
"""
with open("\Users\ahudspeth\Desktop\my_file.txt") as file:
    contents = file.read()
    print(contents)
"""
So now if I run this code again, you can see it's able to read the file,
there is no errors, and it's getting hold of the contents of the file.

Now on Windows, it's a similar story.
So we know that the location of the file is root, then users, then LondonAppBrewery, then desktop. 
Again, this of course will be different for you depending on your username, but you should see it in your location
when you take a look at the file properties. So let's change this.

Let's start out at the root, which is the C drive, and then let's go to users.
And then we go to our username which is LondonAppBrewery,
and then we go to our desktop and that is where it should find this new_file.txt. So now when I hit run,

you can see that it's able to fetch that file and print the content without any errors. 

Now, one of the peculiarities about file paths in Windows and Mac is that in a Mac, the path,
each of the folders are separated by a / whereas on Windows,
they're separated by a \. 

But as you've noticed, when we're writing Python code, we don't care about that.
We can just write it as / and making sure that we have the root,
which represents the C drive, so this entire part, and then we have our folder, the next folder, the next folder,
the next folder, et cetera. 

So now comes the next challenge.

You can see that this path follows from the root folder, which is the C drive and on the Mac, it's also from the Macintosh HD.

So what if we wanted to change this so that it's relative to our current main.py? 

Our main.py if we go to 'Show in Explorer', you can see that the path for this file is the following.

It's under Users/LondonAppBrewery/PyCharmProjects/WindowsDemo.
So that's the name of my project. 

And then afterwards, it's my main.py. So this is a bit of a tricky question.

Given that this file is inside this current folder or whatever it is that you have as your folder which contains this file,
how can you get it to use a relative file path so that it jumps back two folders
to the LondonAppBrewery folder and then goes to Desktop and then to new file?
On our Mac, it's a similar story. So we go to 'Reveal in Finder'.

We can see this is where we are currently.
So our current working directory is this day-24 project folder.

So if we go one level up and the shortcut is command + up,

we go to our day-24 folder. So this is our working directory.

Now, if we want to go up one level,

we can go to go, and then go to including folder,

so one level up that gets us to PyCharm projects.

And then if we go one level up further, we get to our Angela folder

at which point we can then navigate downwards to Desktop/my_file.txt.

This is your challenge.

Figure out what the relative path to the text file on your desktop should be
then modify the code and get it to work. 

Pause the video now.

The way that we would modify this is in order to get to this Angela folder where we can continue to our Desktop and then to my file,
we have to go up two levels.
So that translates to ../../ and now we're inside the Angela folder.
"""
with open("../../") as file:
    contents = file.read()
    print(contents)

"""
So we can start going down. And PyCharm is smart enough to know what your

folder structure looks like. So it will start giving you hints as to what folders are accessible at this level.
So I can get to Desktop and then I can get to my_file.txt.
"""
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
"""

And if I go ahead and run my code, you can see it's able to read and print the content of that file.
The main difference between an absolute file path and a relative file path is
the absolute file path is always relative to the root of your computer. On Windows that's the C drive, usually anyways
unless you've changed it. And on a Mac, it is the Macintosh HD.

Now the relative file path is relative to your current working directory.
So it depends on where you are and where you're trying to get to. 

Now, depending on the situation and where that file you are interested in is located,
you might decide to use the absolute file path or the relative file path.

And you can see that in this case it's not necessarily that much shorter or that much more easier to understand.

So if you know how to do both, then you can adapt to the situation and figure out which one is most
appropriate. 

Now I know that paths can be confusing. So that's why I've come up with a whole bunch of quiz exercises for you in the
next lesson for you to get more the practice with file paths so that you can feel confident leaving this lesson.

So for all of that and more, I'll see you on the next lesson.