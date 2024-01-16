
from turtle import Screen, Turtle
from Paddle_Class_Module import Paddle
from Ball_Class_Module_v01_W import Ball
from Scoreboard_Class_Module_v01_W import Scoreboard

import time

#CONSTANTS:
ball_speed_modifier = 0.1   #0.2 is slower, 0.1 is average speed.

################################################
# TODO: Classes to create
# Scoreboard (for both sides)
# Paddle for p1 and p2
#the ball

# TODO: Objects to create
# separator down the middle
# gameboard and wall boundaries

# TODO: Movement:
# player 1 and player 2 controls, physics of the ball and the bouncing off the side walls

#updating the scoreboards (both of them)


# TODO: Angela's Version:
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create paddle for p2
# 4. Create the ball and make it move
# 5. detect collision with wall and bounce
# 6. Detect collision with a paddle
# 7. Detect when paddle misses
# 8. Keep score

################################################



# time_modifier_for_snake_speed = 0.1   #0.2 is slower, 0.1 is average speed.

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)                    # for this line to work: game_on = True
screen.title("Siris's Pong Game")                   #  while game_on:
                                                    #     screen.update()
p1_r_paddle = Paddle((350, 0))   #paddle object for player 1
p2_l_paddle = Paddle((-350, 0))    #paddle object for player 2
# top_paddle = Paddle((0, 270))
ball = Ball((0, 0))           #ball object, at starting position

# scoreboard = Scoreboard()
# p1_scoreboard_location = (100, 270)
p1_scoreboard = Scoreboard(100, 270)

# p2_scoreboard_location = (-100, 270)
p2_scoreboard = Scoreboard(-100, 270)
# p2_scoreboard_location = (-100, 270)
# p2_scoreboard = Scoreboard(p2_scoreboard_location)


screen.listen()

screen.onkey(fun=p1_r_paddle.go_up, key="Up")
screen.onkey(fun=p1_r_paddle.go_down, key="Down")

screen.onkey(fun=p2_l_paddle.go_up, key="w")
screen.onkey(fun=p2_l_paddle.go_down, key="s")

counter_p1 = 0
counter_p2 = 0

game_on = True
while game_on:
    time.sleep(ball_speed_modifier)
    screen.update()
    ball.move()

    # (width=800, height=600)

    # bouncing off verticle walls:
    if ball.ycor() > 280 or ball.ycor() < -280:  # or ball.xcor() >= 375 or ball.xcor() < -375 or
        ball.bounce_off_y_vertical_walls()


    # Detect collision with paddles:
    # (2 criteria):
    # 1. You will want to check if it will go past a certain x-axis point (x=340)
    # 2. If it will be within 50 pixels of the middle of the paddle (half of 100 distance)

    # if ball.xcor() >= 325 and ball.distance(p1_r_paddle) <= 50 or ball.distance(p2_l_paddle) <= 50 and ball.xcor() < -325:
    #     ball.bounce_off_x_axis_paddle()  #made contact with ball print("made contact")

    if (ball.xcor() >= 325 and ball.distance(p1_r_paddle) <= 50) or (
            ball.distance(p2_l_paddle) <= 50 and ball.xcor() < -325):
        ball.bounce_off_x_axis_paddle()


    #GAME OVER FOR P1:
    # GAME OVER FOR P1:
    if ball.xcor() > 380:
        # p1_scoreboard.clear()
        ball.reset_position()
        ball.bounce_off_x_axis_paddle()
        p1_scoreboard.l_point()
        screen.update()
        # p1_scoreboard.clear()
        # p1_scoreboard.r_point()  # Assuming this is the correct method to increment and update the score
        # screen.update()

    # if ball.xcor() > 380:
    #     ball.reset_position()
    #     ball.bounce_off_x_axis_paddle()
    #     p1_scoreboard.clear()
        # p1_scoreboard.r_point()
        # p1_scoreboard.update_scoreboard()
        # p1_scoreboard.r_p1_score += 1
        # p1_scoreboard.r_p1_score
        # p1_scoreboard.write(f"P1 Score: {p1_scoreboard.r_p1_score}", align="center", font=("Courier", 16, "normal"))
        # self.write(f"P1 Score: {self.r_p1_score}", align=ALIGNMENT, font=("Courier", 16, "normal"))
        # p2_scoreboard.score += 1
        # p2_scoreboard.clear()
        # p2_scoreboard.write_the_scoreboard_for_p2()
                # game_on = True
            # return game_on
    if ball.xcor() < -380:
        # p2_scoreboard.clear()
        ball.reset_position()
        ball.bounce_off_x_axis_paddle()
        p2_scoreboard.r_point()
        screen.update()
        # p2_scoreboard.l_p2_score += 1
        # p2_scoreboard.clear()
        # p2_scoreboard.r_p1_score
    #     p1_scoreboard.score += 1
    #     p2_scoreboard.write(f"P2 Score: {p2_scoreboard.l_p2_score}", align="center", font=("Courier", 16, "normal"))
    #
    #     p1_scoreboard.write_the_scoreboard_for_p1()
    #     screen.clear()

    #     game_on = True

            # p2_scoreboard.game_over_display_for_p2()
            # game_on = False






screen.exitonclick()