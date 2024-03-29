# calculator clean version
from art import calculator

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

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    # add a while loop
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)


        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

'''''
    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(calculation_function(num1, num2), num3)

    print(f"{answer} {operation_symbol} {num3} = {second_answer}")
'''