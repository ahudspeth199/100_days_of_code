from turtle import Turtle


class End_of_game(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.goto(0,0)
        self.hideturtle()

    def end(self):
        self.color('black')
        self.goto(0, 90)
        self.hideturtle()