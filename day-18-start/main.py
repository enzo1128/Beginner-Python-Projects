# import turtle
# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.speed(0)
#
# screen = Screen()
# screen.exitonclick
# day 18-1
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#################################################
# day 18-2
# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.speed(0)
#
# screen = Screen()
#
# for i in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# screen.exitonclick()
#################################################
# day 18-3
# import random
# shapes = 7
# sides = 1
#
# for i in range(shapes):
#     tim.pencolor(random.choice(["red", "blue", "green"]))
#     for i in range(sides):
#         tim.forward(50)
#         tim.right(360/sides)
#     sides += 1

#################################################
# day 18-4 random walk
# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# tim.speed(0.5)
# tim.pensize(10)
# turtle.colormode(255)
# screen = Screen()
#
# angles = [0, 90, 180, 270]
# moves = 2000
#
# for i in range(moves):
#     tup = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     tim.pencolor(tup)
#     tim.forward(20)
#     tim.right(random.choice(angles))
#
# screen.exitonclick()
#################################################
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(0)
turtle.colormode(255)
screen = Screen()

heading = 0
while heading <= 360:
    tup = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    tim.pencolor(tup)
    tim.circle(100)
    tim.setheading(heading)
    heading += 0.5

screen.mainloop()