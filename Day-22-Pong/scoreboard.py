from turtle import Turtle
import random

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setpos(0, 300)
        self.pensize(5)
        self.setheading(270)

    def draw_line(self):
        for i in range(0, 50):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.setpos(0, 200)
        self.l_score = 0
        self.r_score = 0
        self.headoptions = [40, 130, 320, 220]
        self.hideturtle()

    def track(self, ball):
        if ball.xcor() < -400:
            self.r_score +=1
            ball.setheading(random.choice(self.headoptions))
            ball.setpos(0,0)
        elif ball.xcor() > 400:
            self.l_score += 1
            ball.setheading(random.choice(self.headoptions))
            ball.setpos(0, 0)
        self.clear()
        self.write(f"{self.l_score}\t{self.r_score}", align='center', font=("Bit5x3", 60, 'normal'))


