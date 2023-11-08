from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.headoptions = [40, 130, 320, 220]
        self.setheading(random.choice(self.headoptions))

    def move(self):
        self.forward(5)

    def bounce(self, l, r):
        if self.ycor() > 280:
            if any(self.heading() == angle for angle in range(90, 180)):
                self.setheading(180 + (180 - self.heading()))
            elif any(self.heading() == angle for angle in range(0, 90)):
                self.setheading(360 - self.heading())
        elif self.ycor() < -280:
            if any(self.heading() == angle for angle in range(180, 270)):
                self.setheading(180 - (180 + self.heading()))
            elif any(self.heading() == angle for angle in range(270, 360)):
                self.setheading(0 + (360 - self.heading()))
        elif self.xcor() <= -350 and any(int(self.ycor()) == cor for cor in range(l[0], l[1])):
            if any(self.heading() == angle for angle in range(180, 270)):
                self.setheading(360 - (self.heading() - 180))
            elif any(self.heading() == angle for angle in range(90, 180)):
                self.setheading(0 + (180 - self.heading()))
        elif self.xcor() >= 350 and any(int(self.ycor()) == cor for cor in range(r[0], r[1])):
            if any(self.heading() == angle for angle in range(0, 90)):
                self.setheading(180 - (self.heading()))
            elif any(self.heading() == angle for angle in range(270, 360)):
                self.setheading(180 + (360 - self.heading()))
        else:
            self.forward(10)
