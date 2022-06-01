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
my_label.pack(side='left')

#Button
button = Button(text="Click Me", command=button_clicked)
button.pack(side='left')

#Entry
input = Entry(width=10)
print(input.get())
input.pack(side='left')

window.mainloop()
