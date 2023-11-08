import colorgram

# numberofcolors = 21
# colors = colorgram.extract("Hirst photo.jpeg",numberofcolors)
#
# tup_all = []
# for i in range(0,numberofcolors):
#     list_col = []
#     list_col.append(colors[i].rgb.r)
#     list_col.append(colors[i].rgb.g)
#     list_col.append(colors[i].rgb.b)
#     tup_col = tuple(list_col)
#     tup_all.append(tup_col)
#
# print(tup_all)

import turtle
from turtle import Turtle, Screen
import random
from time import sleep

colors = [(235, 234, 231), (234, 229, 232), (237, 34, 108), (221, 232, 237), (147, 26, 66), (230, 238, 233), (240, 74, 34),
       (8, 147, 91), (222, 170, 42), (181, 160, 46), (26, 126, 193), (43, 192, 234), (250, 221, 22), (84, 24, 87),
       (125, 193, 77), (31, 169, 118), (185, 35, 104), (253, 223, 0), (211, 63, 25), (24, 183, 223), (168, 21, 18)]

tim = Turtle()
screen = Screen()
turtle.colormode(255)
tim.up()
tim.speed(0)
tim.hideturtle()

rows = 0
y = -200
for _ in range(10):
       tim.setx(-200)
       for _ in range(10):
              tim.sety(y)
              tim.dot(20, random.choice(colors))
              tim.forward(50)
              tim.dot(20, random.choice(colors))
       y += 50


screen.mainloop()
