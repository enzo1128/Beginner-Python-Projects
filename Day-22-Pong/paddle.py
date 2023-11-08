from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if pos == "left":
            self.goto(-380, 0)
        if pos == "right":
            self.goto(380, 0)
        self.span = [self.ycor() + 51, self.ycor() - 51]

# basically every time the paddle moves, it generates tuples of what it spans
    def set_span(self):
        self.span = [self.ycor() + 50, self.ycor() - 50]
        self.span.sort()

    def up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 50)
            self.set_span()


    def down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 50)
            self.set_span()




