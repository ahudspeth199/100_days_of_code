from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text='New Text')
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)

window.mainloop()
