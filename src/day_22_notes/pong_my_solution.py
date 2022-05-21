## Create the screen
from turtle import Screen
from paddle import Paddle
#import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
#screen.tracer(0)

"""
paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    paddle.move()
"""
screen.exitonclick()