from turtle import Turtle
MOVE_DISTANCE = 20
starting_positions = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.all_segs = []
        self.generate_snake()
    def generate_snake(self):
        for pos in starting_positions:
            self.add_seg(pos)
    def add_seg(self, pos):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.all_segs.append(new_seg)
    def grow(self):
        self.add_seg(self.all_segs[-1].position())
    def move(self):
        for seg_num in range(len(self.all_segs) - 1, 0, -1):
            new_x = self.all_segs[seg_num - 1].xcor()
            new_y = self.all_segs[seg_num - 1].ycor()
            self.all_segs[seg_num].goto(new_x, new_y)
        self.all_segs[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.all_segs[0].heading() != 270:
            self.all_segs[0].setheading(90)
    def down(self):
        if self.all_segs[0].heading() != 90:
            self.all_segs[0].setheading(270)
    def left(self):
        if self.all_segs[0].heading() != 0:
            self.all_segs[0].setheading(180)
    def right(self):
        if self.all_segs[0].heading() != 180:
            self.all_segs[0].setheading(0)

