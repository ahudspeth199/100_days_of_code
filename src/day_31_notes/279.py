from tkinter import *



BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

canvas = Canvas(height=600, width=900)
my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(526,800, image=my_image)
canvas.grid(row=0, column=1, columnspan=2)


#Labels



#Button
button = Button(image=my_image, highlightthickness=0)

window.mainloop()
