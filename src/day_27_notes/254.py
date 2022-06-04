from tkinter import *

def button_clicked():
    print("Calculate")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.config(text='is equal to')
my_label.grid(column=0, row=1)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.config(text=0)
my_label.grid(column=1, row=1)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.config(text="Km")
my_label.grid(column=2, row=1)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.config(text="Miles")
my_label.grid(column=2, row=0)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()
