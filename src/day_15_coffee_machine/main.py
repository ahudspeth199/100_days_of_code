
from menu import MENU
import math

# TODO: 1. Print report of all coffee machine resources

def format_data(coffee):
    coffee_choice = coffee[MENU]

# coffee
espresso = MENU['espresso']
latte = MENU['latte']
cappucino = MENU['cappuccino']

#coffee cost
espresso_cost = espresso['cost']
latte_cost = latte['cost']
cappucino_cost = cappucino['cost']

should_continue = True

while should_continue:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    quarters_enter = int(input("how many quarters?: "))
    dimes_enter = int(input("how many dimes?: "))
    nickles_enter = int(input("how many nickles?: "))
    pennies_enter = int(input("how many pennies?: "))

    quarter = .25 * quarters_enter
    dime = .10 * dimes_enter
    nickle = .05 * nickles_enter
    penny = .01 * pennies_enter
    total = float(quarter + dime + nickle + penny)
    drink = MENU[user_choice]
    drink_cost = drink['cost']
    print(f"This is the total coins entered in the machine: ${total} ")
    print(f"This is how much the {user_choice} cost ${drink_cost} ")

    def coins_enter():
        total_coins = float(quarter + dime + nickle + penny)
        return total_coins


    if user_choice == 'espresso':
        if total >= drink_cost:
            refund = total - drink_cost
            should_continue = False
            print(f"Here is ${refund} in change.")
            print("Here is your espresso. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded. ")

    elif user_choice == 'latte':
        if total >= drink_cost:
            refund = total - drink_cost
            should_continue = False
            print(f"Here is ${refund} in change.")
            print("Here is your latte. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded. ")

    elif user_choice == 'cappuccino':
        if total >= drink_cost:
            refund = total - drink_cost
            should_continue = False
            print(f"Here is ${refund} in change.")
            print("Here is your cappuccino. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded. ")

    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")