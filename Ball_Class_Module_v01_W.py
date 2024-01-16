
from turtle import Turtle

#CONSTANTS:
AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME = 10

class Ball(Turtle):

    def __init__(self, ball_position):  # extras: shape, pensize=20, color="orange"
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setheading(45)
        self.goto(ball_position)
        self.x_move = AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME
        self.y_move = AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME
        # self.forward(AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME)


    def move(self):
        # self.forward(AMOUNT_OF_PIXELS_SNAKE_MOVES_EACH_FRAME)
        #or
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_off_y_vertical_walls(self):
        self.y_move *= -1    #inverts the negativity or positivity of a value.

    def bounce_off_x_axis_paddle(self):
        self.x_move *= -1


    def reset_position(self):
        self.goto(0, 0)