from game_data import data
from art import logo
from art import vs
import random

score = 0
a = random.choice(data)
b = random.choice(data)

'''''
def start_game():

    print(logo)
    print(compare_a)

    name = compare_a['name']
    description = compare_a['description']
    country = compare_a['country']
    follower_count = compare_a['follower_count']
    print(f"Compare A: {name}, a {description}, from {country}")

    print(vs)
    print(against_b)

    name2 = against_b['name']
    description2 = against_b['description']
    country2 = against_b['country']
    follower_count2 = against_b['follower_count']
    print(f"Against B: {name2}, a {description2}, from {country2}")

    user_chose = input("Who has more followers? Type 'A' or 'B': ")
    follower_a = follower_count
    follower_b = follower_count2
start_game()
'''


should_continue = True

while should_continue:
    compare_a = a
    against_b = b

    print(logo)
    print(compare_a)

    name = compare_a['name']
    description = compare_a['description']
    country = compare_a['country']
    follower_count = compare_a['follower_count']
    print(f"Compare A: {name}, a {description}, from {country}")

    print(vs)
    print(against_b)

    name2 = against_b['name']
    description2 = against_b['description']
    country2 = against_b['country']
    follower_count2 = against_b['follower_count']
    print(f"Against B: {name2}, a {description2}, from {country2}")

    if compare_a == against_b:
        print(f"Compare A is the same as Aginst B ")
        compare_a = random.choice(data)

    user_chose = input("Who has more followers? Type 'A' or 'B': ")

    follower_a = follower_count
    follower_b = follower_count2

    if user_chose == "A" or user_chose == "a":
        if follower_a > follower_b:
            a = compare_a
            score = score + 1
            print(f"You're right! Current score: {score} ")

        else:
            should_continue = False
            print(f"Wrong, Final score: {score} ")

    elif user_chose == "B" or user_chose == "b":
        if follower_b > follower_a:
            score = score + 1
            print(f"'You're right!' Current score: {score} ")
            a = against_b

        else:
            should_continue = False
            print(f"Wrong, Final score: {score} ")


