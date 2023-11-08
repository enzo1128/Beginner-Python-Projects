from turtle import Screen
from scoreboard import Line, ScoreBoard
from time import sleep
from paddle import Paddle
from ball import Ball
game = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball = Ball()
line = Line()
line.draw_line()
board = ScoreBoard()


screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

while game:
    screen.update()
    sleep(0.02)
    ball.move()
    ball.bounce(l_paddle.span, r_paddle.span)
    board.track(ball)
screen.mainloop()