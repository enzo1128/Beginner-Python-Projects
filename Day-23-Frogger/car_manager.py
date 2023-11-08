from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, y):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.setx(260)
        self.sety(y)

    def move(self):
        self.forward(1)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(270, 0)
        self.active_cars = [Car(random.randint(-230, 230))]

    def generate(self):
        num = random.random()
        for car in self.active_cars:
            if car.xcor() < -300:
                del car
        if num < 0.05:
            new_car = Car(random.randint(-230, 230))
            self.active_cars.append(new_car)

    def move_cars(self):
        for car in self.active_cars:
            car.move()

