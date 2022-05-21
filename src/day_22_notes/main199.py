from turtle import Screen
from paddle199 import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((350,0))
top_paddle = Paddle((100, 100))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()