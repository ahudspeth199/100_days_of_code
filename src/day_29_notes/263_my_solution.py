from tkinter import *
# challenge 1
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#title_label = Label(text="Password Manager", font=("Courier", 50))
#title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=200, highlightthickness=0)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=my_pass_img)
canvas.grid(column=1, row=1)


window.mainloop()

