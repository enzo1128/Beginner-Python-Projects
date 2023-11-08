import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard, GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()

screen.listen()
screen.onkey(player.move, "w")
screen.onkey(player.move, "Up")

manager = CarManager()
board = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(board.speed)
    for car in manager.active_cars:
        if car.distance(player) < 20:
            game_is_on = False
        if car.xcor() < - 300:
            del car
    manager.generate()
    manager.move_cars()
    board.keep_score(player)
    board.keep_score(player)

if not game_is_on:
    game_over = GameOver()
screen.exitonclick()
