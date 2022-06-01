import time
from turtle import Screen
from player210 import Player
from car_manager210 import CarManager
from scoreboard210 import Scoreboard
from end_of_game import End_of_game

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

turtle = Player((0,-280))
car_manager = CarManager()
end_of_game = End_of_game()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    turtle.clear()
    car_manager.new_cars()
    car_manager.move_cars()

    # Detect Turtle reaching the top
    if turtle.ycor() > 280:
        end_of_game.write("You made it!!", align='center',font=('Courier', 40, 'normal'))
        turtle.reset_position()
        scoreboard.point()
        end_of_game.clear()
        car_manager.move_speed *= 0.9

    # Detect Collision with cars
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            end_of_game.write("Squish!!", align='center',font=('Courier', 40, 'normal'))
            end_of_game.end().write(f'Your score is: {scoreboard.point()}')
            game_is_on = False



screen.exitonclick()