import turtle
from turtle import Turtle
import random
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def random_color():
    """Changes the colour of your turtle to a random one based on rgb"""
    rr = random.randint(0, 255)
    gr = random.randint(0, 255)
    br = random.randint(0, 255)
    r_color = (rr, gr, br)
    return r_color


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """creates a 3 segment long snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds an extra segment to the snake"""
        new_segment = Turtle("square")
        turtle.colormode(255)
        new_segment.color(random_color())
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ extend snake by one segment"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """Reset your snake so the new snake starts every time you lost a life"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """moves your snake forwards"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """moves your snake up when it is not facing down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """moves your snake down when it is not facing up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """moves your snake left when it is not facing right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """moves your snake right when it is not facing left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
