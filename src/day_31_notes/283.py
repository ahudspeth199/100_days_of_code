# After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.

# The card image should change to the card_back.png and the text colour should change to white.
# The title of the card should change to "English" from "French".

# HINTS:
"""
 1. To change the canvas image, you'll need a reference to the image, like what you have with the text created in the canvas. Then you can set the image attribute using itemconfig(). e.g.

 new_image = PhotoImage(file="new_image.png")
 old_image = PhotoImage(file="old_image.png")
 canvas_image = canvas.create_image(300, 300, image=old_image)
# #To change the image:
# canvas.itemconfig(canvas_image, image=new_image)
# IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.

To change the color of the text in a canvas element, use the fill parameter. e.g. https://stackoverflow.com/questions/41030973/how-can-i-change-the-color-of-text-in-tkinter

3. Remember in the mainloop() you should not create additional delayed loops e.g. with time.sleep() but instead, use window.after() e.g. Tkinter Reference Manual: .after() method

4. You can cancel a window.after() loop using window.after_cancel() e.g. Tkinter Reference Manual: .after_cancel() method

"""


from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

def card_flip():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word,text=current_card["English"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan= 2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
