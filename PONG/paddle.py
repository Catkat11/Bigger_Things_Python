from turtle import Turtle

MOVE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def up(self):
        if not self.ycor() > 250:
            self.forward(MOVE)

    def down(self):
        if not self.ycor() < -230:
            self.back(MOVE)
