from turtle import Screen
from paddle199 import Paddle
from ball201 import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        game_is_on
        ball.bounce()

screen.exitonclick()