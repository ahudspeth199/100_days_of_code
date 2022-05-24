
from art import logo, vs
from game_data import data
import random
import os

def clear():
    os.system('cls')

def format_data(account):
    """"Format the account data into printable format."""
    account_name = account["name"]
    accout_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {accout_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """"Use if statement to check if user is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(account_a)
    print(f"Compare A: {format_data(account_a)}.")

    print(vs)
    print(account_b)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score} ")
    else:
        game_should_continue = False
        print(f"Wrong, Final score: {score} ")