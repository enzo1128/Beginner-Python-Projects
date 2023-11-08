from turtle import Turtle
from snake import Snake
import random

possible_locations = []
for i in range(-280, 280, 20):
    for j in range(-280, 220, 20):
        loc = (i, j)
        possible_locations.append(loc)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):

        self.goto(random.choice(possible_locations))

