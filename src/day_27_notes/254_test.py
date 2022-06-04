from tkinter import *

def button_clicked():
    print("Calculate")
    km_label = input.get()
    miles_label.config(text=km_label)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

#Label
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.config(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.config(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text=0, font=("Arial", 24, "bold"))
kilometer_result_label.config(text=0)
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="km", font=("Arial", 24, "bold"))
km_label.config(text="km")
km_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()
