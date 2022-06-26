# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not  exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")


# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exist"]

#IndexError
#fruit_list = ["Apple", "Banana", "Pear"]
#fruit = fruit_list[3]

# TypeError
#text = "abc"
#print(text + 5)

"""
try:
    "Something that might cause an exception"

except:
    "Do this if there was an exception"
else:
    "Do this if there were no exceptions"
finally:
    "Do this no matter what happens"
"""
