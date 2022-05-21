from game_data import data
from art import logo, vs
import random
import os

def clear():
    os.system('cls')

def format_data(account):
    """"Format the account data into printable format."""
    name = account["name"]
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(user_chose, follower_a, follower_b):
    if follower_count > follower_count2 and user_chose == "a":
        return True
    elif follower_count2 > follower_count and user_chose == "b":
        return True
    else:
        return False


score = 0
should_continue = True
against_b = random.choice(data)

while should_continue:
    print(logo)

    compare_a = against_b
    against_b = random.choice(data)

    while compare_a == against_b:
        compare_a = random.choice(data)

    print(compare_a)
    print(f"Compare A: {format_data(compare_a)}")



    print(vs)
    print(against_b)
    print(f"Against B: {format_data(against_b)}")

    user_chose = input("Who has more followers? Type 'A' or 'B': ")

    follower_count = compare_a['follower_count']
    follower_count2 = against_b['follower_count']

    is_correct = check_answer(user_chose, follower_count, follower_count2)

    clear()

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score} ")
    else:
        should_continue = False
        print(f"Wrong, Final score: {score} ")
