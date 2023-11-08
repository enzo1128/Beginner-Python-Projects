from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=('Courier', 30, 'normal'))

    def point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier', 30, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=('Courier', 30, 'normal'))