from turtle import Turtle

STARTING_X = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.segt = 2

    def create_snake(self):
        for position in STARTING_X:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def add_segment(self, position):
        segment_1 = Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        self.segments.append(segment_1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)

