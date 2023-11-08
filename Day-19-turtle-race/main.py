from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Betting Time", prompt=f"Which color turtle will win?")

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
names = ["red", "orange", "yellow", "green", "blue", "violet"]
racers = []

for c, n in zip(colors, names):
        n = Turtle(shape="turtle")
        n.color(c)
        n.speed(0)
        racers.append(n)

y_pos = -125
for t in racers:
    t.penup()
    t.goto(x=-230, y=y_pos)
    y_pos += 10

race = True
while race:
    current_racer = random.choice(racers)
    current_racer.forward(random.randint(1,2))
    if current_racer.xcor() >= 230:
        winner = current_racer
        race = False
        screen.bye()

if winner.color()[0] == bet:
    print(f"You win! The {winner.color()[0]} turtle was the first to cross the finish line")
else:
    print(f"You lose. The {winner.color()[0]} turtle won")

screen.mainloop()