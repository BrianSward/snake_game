from turtle import Turtle

POINTS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for point in POINTS:
            self.add_segment(point)

    def add_segment(self, point):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(point)
        self.body.append(new_snake)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            self.body[part].goto(self.body[part - 1].xcor(), self.body[part - 1].ycor())
        self.body[0].forward(SPEED)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    # basically everything in init is here because this is like
    # re-init-ing it, i'n't cool?

    def reset(self):
        for bod in self.body:
            bod.goto(800, 800)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]