# Calculator
# Build a calculator where you enter a number, pick an operation, then pick the next number, finally it will calculate the results
# clear the screen to start a new calculation
from art import calculator

#add
def add(n1, n2):
    return n1 + n2

# substract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# create a dictionary that includes the math symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))


# my solution
if operation_symbol == "+":
    answer = add(num1,num2)
    print(answer)

elif operation_symbol == "-":
    answer = subtract(num1,num2)
    print(answer)

elif operation_symbol == "*":
    answer = multiply(num1,num2)
    print(answer)

else:
    answer = divide(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

#instructors solution

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")


operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]



# instead of passing over calculation_function we are going to pass over the answer
# so now num1 is the previous answer and num2 will now be num3
# now when calling this calculation_function you are passing over the results or outputs of this calculation: calculation_function(num1, num2)
answer = calculation_function(answer, num3)

# another what to look at the answer step is:
# answer = calculation_function(calculation_function(num1, num2), num3)



# you can also rename the answer to make it easier

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {first_answer}")


operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")