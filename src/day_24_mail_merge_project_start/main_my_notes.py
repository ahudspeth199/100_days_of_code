"""
step 1: turn all of the invited names (invited_names.txt) into a list

- Get python to read the file using open syntex
- use a relative file path (Input, Output folders are on the same hierarchical level as our current file: invited_names)
  """
  with open("./Input")
  """

- Get a hold of the file invited_names.txt
  """
  with open("./Input/Names/invited_names.txt")
  """

- Save it as names_file
  """
  with open("./Input/Names/invited_names.txt") as names_file:
  """

- Now that the file is open you can read it, save it to a variable called (names) and then print out the names.
  """
  with open("./Input/Names/invited_names.txt") as names_file:
      names = names_file.read()
      print(names)
  """
  So now if I go ahead and hit run my main.py, you can see that it prints out all of these names individually
  because it's getting hold of everything that's in here and just printing it out.

- Format these names in a list using readlines method readlines()
  Now, instead of saying names_file.read, let's replace that with readlines.
  """
  with open("./Input/Names/invited_names.txt") as names_file:
      names = names_file.readlines()
      print(names)
  """
Now, when I hit run, you can see it prints out names we have our list of names which we've extracted from our invited_names.txt
"""

"""
Step 2: replace this placeholder in our starting letter with each of these names [names].

- Create a constant at the top which I'll call PLACEHOLDER 
  set it as the string which is the square brackets and then the word name 
  """
  PLACEHOLDER = "[name]"

  with open("./Input/Names/invited_names.txt") as names_file:
      names = names_file.readlines()
      print(names)
  """
  this is the string that we want to replace from our starting letter.
"""

"""
Step 3: Open up our starting letter

- So again, use open syntex and then I'm going to specify the path.
  go into the folder that's at the same level as main.py using the ./ then go into input folder, then Letters folder, 
  to get hold of my starting letter and I'm going to open this as the letter_file.
  """
  PLACEHOLDER = "[name]"

  with open("./Input/Names/invited_names.txt") as names_file:
      names = names_file.readlines()
      print(names)

  with open("./Input/Letters/starting_letter.txt") as letter_file:
  """

- With the letter_file I'm simply just going to get a hold of the letter_contents by saying letter_file.read.
  """
  PLACEHOLDER = "[name]"

  with open("./Input/Names/invited_names.txt") as names_file:
      names = names_file.readlines()
      print(names)

  with open("./Input/Letters/starting_letter.txt") as letter_file:
      letter_contents = letter_file.read()
  """
  I want all of the content inside that letter and it's now going to be saved as a string inside my letter_contents.
"""

"""
Step 4: Go through the letter contents and replace that placeholder with the actual name
that we've got in our list.

- Need the replace method
  we can get hold of the text call, replace, and then the output of this method will be a new string which has modified
  this text.

- Need a for loop
  we can say for name in our list of names, let's go through
  each of the names in that list and then let's get the letter_contents and replace the placeholder,so the old string, with a new string which is going to be the name.
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
  when we printed out each of these names, you can see that after each of the names that
  they've extracted from this list of invited names, there's a new line that's being added, and you can see that with this \n.

  The only one that doesn't have a new line is the very last one. What we need to do is to strip the new line. 
  
- We have to use a method called strip which can take away any of the spaces at the beginning and at the end of the string.
  We're going to loop through each of the names and then we're going to take the name and we're going to call strip 
  on each of those names. then we can save it to a variable called stripped_name. 
  And now we can use that stripped_name instead of the name.
  
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

- 
