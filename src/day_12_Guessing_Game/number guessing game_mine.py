from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")

chosen_number = random.randint(0,100)
end_of_game = False
print("I am thinking of a number between 1 and 100. ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
print(f'Pssst, the correct answer is {chosen_number}.')



if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    easy_guesses = 10
    while not end_of_game:
        user_guess = int(input("Make a guess: "))
        if user_guess == chosen_number:
            end_of_game = True
            print("You Guessed Correct!")
            print("You Win!!!!!!!!!")

        else:
            if user_guess != chosen_number:
                easy_guesses -= 1
                print(f"You have {easy_guesses} attempts remaining to guess the number.")
                if easy_guesses == 0:
                    end_of_game = True
                    print("You Ran out of guess attempts")
                    print("You Lose. ")
                elif user_guess < chosen_number:
                    print("you are less than the number")
                    print("Guess again")
                else:
                    if user_guess > chosen_number:
                        print("You are higher than the number")
                        print("Guess again")


else:
    if difficulty == "hard":
        print("You have 5 attempts remaining to guess the number. ")
        hard_guesses = 5
    while not end_of_game:
        user_guess = int(input("Make a guess: "))
        if user_guess == chosen_number:
            end_of_game = True
            print("You Guessed Correct!")
            print("You Win!!!!!!!!!")

        else:
            if user_guess != chosen_number:
                hard_guesses -= 1
                print(f"You have {hard_guesses} attempts remaining to guess the number.")
                if hard_guesses == 0:
                    end_of_game = True
                    print("You Ran out of guess attempts")
                    print("You Lose. ")
                elif user_guess < chosen_number:
                    print("you are lower then the number")
                    print("Guess again")
                else:
                    if user_guess > chosen_number:
                        print("You are higher then the number")
                        print("Guess again")






