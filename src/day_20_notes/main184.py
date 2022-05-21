from turtle import Screen
## Step 6
from snake184 import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

## Step 7
snake = Snake()

## Step 8
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()

