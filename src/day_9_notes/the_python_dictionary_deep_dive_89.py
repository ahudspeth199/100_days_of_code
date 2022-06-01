# Notes on python Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",

}

# Retrieving items from dictionary.
#print(programming_dictionary["Function"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

#create an empty dictionary.
#empty_dictonary = {}

#Wipe an existng dictonary
#programming_dictionary = {}
#print(programmng_dictionary)

#Edit an item in a dictionary
#programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
# Only gives you the Keys not the values
for thing in programming_dictionary:
    print(thing)

# to get the values from a key in a Loop you will need to enter the retrieval code
for key in programming_dictionary:
    print(programming_dictionary[key])