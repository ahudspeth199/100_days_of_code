import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.all_cars = []


    def new_cars(self):
        random_chance = random.randint(1,7)
        if random_chance == 2:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
            self.move_speed = 0.1

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)