import turtle
from turtle import Turtle, Screen

screen = Screen()

STARTING_POSITIONS = [(0, -20), (0, 0), (0, 20), (0, 40)]    #will ALWAYS start here, so using Tuples is PERFECT!! Constants = Tuples, so this goes in ALL CAPS!
AMOUNT_OF_PIXELS_SNAKE_MOVES_EACH_FRAME = 20
#to prevent from cheating and doing a 180 turn:
UP = 90
DOWN = 270
# LEFT = 180
# RIGHT = 0


class Paddle(Turtle):
    
    def __init__(self, position):           # extras: shape, pensize=20, color="orange"
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):  # NOT (self) in this case!!!
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):  # NOT (self) in this case!!!
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def create_paddle(self):
    #     self.shape("square")
    #     self.color("white")
    #     self.shapesize(stretch_wid=5, stretch_len=1)
    #     self.penup()
    #     self.goto(350, 0)



        # new_segment = Turtle(shape="square")    # this info (and lines below it) was moved from create_snake (above) to the add_segment function definition
        # new_segment.pensize(20)
        # new_segment.color("purple")
        # new_segment.penup()
        # new_segment.goto(position)
        # self.segments.append(new_segment)
                                                #This above and this below are used together to add an extra block to the snake body, once passed through a food block.

    # def extend_snake_body(self):   #add new segment to the snake.
    #     self.add_segment(self.segments[-1].position())                         #get ahold of the last segment, and it's position)


    # def move(self):     #anytime you're within your Class, you have to put (self) in the parenthesis and a self. in front of any variable names!
    #     for seg_num in range(len(self.segments) - 1, 0, -1):   #if you want (1, 2, 3), then start=1, stop=3, step=1. BUT in reverse order (3, 2, 1): start=3, stop=1, step=-1. We actually want to go from 2, 1, 0 because of the 3 starting positions and segments[2] seg[1] and seg[0], which we apply here!
    #         new_x = self.segments[seg_num - 1].xcor()        #get ahold of the x-coordinate of the 2nd to last segment here
    #         new_y = self.segments[seg_num - 1].ycor()        #get ahold of the y-coordinate of the 2nd to last segment here
    #         self.segments[seg_num].goto(new_x, new_y)          #get ahold of the last segment here
        # self.head.forward(AMOUNT_OF_PIXELS_SNAKE_MOVES_EACH_FRAME)                  #OUTSIDE of the For Loop, get ahold of the first segment, and move that forward, so all the other code trails behind the front moving block.
