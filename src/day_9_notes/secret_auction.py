from art import logo2
import os

print(logo2)

print("Welcome to the secret auction program.")

should_continue = True

while should_continue:
    name = input("What is your name?:\n")
    price = int(input("What's your bid?:\n$"))


    def add_entry(bidders_name,bid_amount):
        bidders_log = {}
        bidders_log[bidders_name] = name
        bidders_log[bid_amount] = price

        #bidders_log.append(bidders_log)
        print(bidders_log)

        add_entry()

    result = input("Are there any other bidders? Type 'yes' or 'no'.")
    if result == "no":
        should_continue = False

print(add_entry(bidders_name=name,bid_amount=bid))