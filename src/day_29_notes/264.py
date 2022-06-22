from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

website_inputs = Entry(width=35)
website_inputs.grid(column=0, row=1, columnspan=2)

website_label = Label(text="Website:", font=("Arial",24))
website_label.config(text="Website:")
website_label.grid(column=0,row=1)

user_label = Label(text="Email/Username:", font=("Arial",24))
user_label.config(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial",24))
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

gen_password_button = Button(text="Generate Password",width=21)
gen_password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=36,highlightthickness=0 )
add_button.grid(column=2,row=4)

window.mainloop()
