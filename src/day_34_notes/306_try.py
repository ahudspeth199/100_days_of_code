# create this user interface inside the init method of the quiz interface class

from tkinter import *

HEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        canvas = Canvas(height=250, width=300)
        canvas.grid(row=0,column=1)

        quizzler_label = Label(text="score")
        quizzler_label.grid(row=0, column=2)
        self.window.mainloop()
