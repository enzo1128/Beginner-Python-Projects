from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-260, 240)
        self.hideturtle()
        self.score = 1
        self.write(f"Level: {self.score}", align="left", font=FONT)
        self.speed = 0.02

    def keep_score(self, player):
        if player.ycor() > 270:
            self.clear()
            self.score += 1
            player.goto(0, -280)
            self.write(f"Level: {self.score}", align="left", font=FONT)
            self.speed /= 1.5
            #need to fix this formula

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.write("Game Over", align="center", font=FONT)
