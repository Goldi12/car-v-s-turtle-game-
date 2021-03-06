import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic('8.gif')
screen.tracer(0)
car_manager = CarManager()
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    # detect car collision with turtle """CAR VS TURTLE COLLISION""

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score_level_up()

"""collision between turtle and wall """

screen.exitonclick()
