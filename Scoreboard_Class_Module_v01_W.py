
from turtle import Turtle
# from __2x__Pong_Game_Main_v02_W__231027 import p1_scoreboard_location, p2_scoreboard_location

#CONSTANTS:
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # global r_p1_score, l_p2_score
        self.hideturtle()
        self.penup()
        self.color('white')
        self.r_p1_score = 0
        self.l_p2_score = 0
        # self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        # self.write_the_scoreboard_for_p1()
        # self.clear()
        self.write(f"P1: {self.r_p1_score}", align="center", font=("Courier", 30, "normal"))
        self.goto(100, 230)
        # self.clear()
        self.write(f"P2: {self.l_p2_score}", align="center", font=("Courier", 30, "normal"))
        # self.write_the_scoreboard_for_p2()


    def l_point(self):
        # self.clear()
        self.l_p2_score += 1
        self.update_scoreboard()
    #     self.clear()
    #     self.write_the_scoreboard()


    def r_point(self):
        # self.clear()
        self.r_p1_score += 1
        self.update_scoreboard()

    # def r_point(self):
    #     self.clear()
        # self.r_p1_score += 1
        # self.update_scoreboard()
    #     self.clear()
    #     self.write_the_scoreboard()

    #
    # def game_over_display_for_p1(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER PLAYER 1. PLAYER 2 WINS.", move=False, align=ALIGNMENT, font=FONT)
    #
    # def game_over_display_for_p2(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER PLAYER 2. PLAYER 1 WINS.", move=False, align=ALIGNMENT, font=FONT)

scoreboard = Scoreboard()

