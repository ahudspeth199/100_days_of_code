#Doc string

format_name()
print(format_name(input("what is yor first name?\n "), input("What is your last name?\n ")))

#Already used functions with outputs.
length = len(formatted_name)

def format_name(f_name, l_name):
    """"Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not enter a name"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

'''''
format_name()
print(format_name(input("what is yor first name?\n "), input("What is your last name?\n ")))
'''