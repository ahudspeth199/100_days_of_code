# # Describe Problem

#def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
#my_function()

# code does not print
# range did not include 20 it is up to 20

# # Reproduce the Bug
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)
#print(dice_imgs[dice_num])

# randint is different from range in that both end points are considered
# notice that the error message only happens on 6
# randint counts from 0


# # Play Computer
#year = int(input("What's your year of birth?"))
#if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
#elif year > 1994:
#   print("You are a Gen Z.")

# you have to enter a = on either 1994


# # Fix the Errors
#age = int(input("How old are you? "))
#if age > 18:
#    print(f"You can drive at age {age}.")
#else:
#    print(f"You can't drive at age {age}")


# #Print is Your Friend
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page = int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)


# #Use a Debugger
#def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

#mutate([1,2,3,5,8,13])

# to fix this code the b_list.append is outside the loop





