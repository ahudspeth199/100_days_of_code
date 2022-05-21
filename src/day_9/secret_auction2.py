from art import logo2
import os

print(logo2)

def clear():
    clear = lambda: os.system('cls')

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    #bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?:\n")
    price = int(input("What is our bid?:\n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        bidding_finished = False
        clear()