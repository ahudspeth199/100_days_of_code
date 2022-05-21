from turtle import Turtle
STARTING_POSITIONS = [(-388, 0),(-388, 20),(-388, 30),(-388,40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270



class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            #new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(UP)


