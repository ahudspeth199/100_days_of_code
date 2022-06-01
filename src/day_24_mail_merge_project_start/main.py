#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""
with open("output/ReadyToSend/example.txt") as file:
    contents = file.read()
    print(contents)
"""


#f = open("input/letters/starting_letter.txt", "r")

with open("input/letters/starting_letter.txt") as file:
    contents = file.read()
    txt = "name"
    x = txt.replace("name", "input/")
    print(x)


