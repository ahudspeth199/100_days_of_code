from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('turtle')
        #self.shapesize(1,1)
        self.color('black')
        self.penup()
        self.left(90)
        self.goto(position)

    def move_forward(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(0,-280)

    def hit_by_car(self):
        pass


