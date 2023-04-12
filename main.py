# TODO 1: Move the turtle with keypress
# TODO 2: Create and move the cars
# TODO 3: Detect collision with cars
# TODO 4: Detect when turtle reaches the other side
# TODO 5: Create a scoreboard


from turtle import Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Cross The Road')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.run, 'Up')

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.next_level()
##    if player.ycor() > 280:
##        player.reset()
##        scoreboard.next_level()

screen.exitonclick()