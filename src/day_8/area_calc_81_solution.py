# Area Calc

#Write your code below this line 👇
import math

# instuctors solution
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area/cover)
    print(f"You'll need {num_of_cans} cans of paint.")

# my solution
#def paint_calc(height, width, cover):
 #   num_of_cans=(height * width)/cover
  #  return num_of_cans

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#print(f"You will need {round(paint_calc(height=test_h,width=test_w, cover=coverage))} cans.")
