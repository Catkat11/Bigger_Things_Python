from turtle import Screen
from tkinter import *
from paddle import Paddle
from bot import Bot
from ball import Ball
from scoreboard import Scoreboard
import time


class Menu:
    def __init__(self):
        window = Tk()
        window.title("Pong")
        window.config(padx=50, pady=50)

        single_player_play_button = Button(text="Single Player", width=10, command=self.single_play)
        single_player_play_button.grid(row=1, column=1, columnspan=2)
        multiplayer_play_button = Button(text="Two PLayers", width=10, command=self.multi_play)
        multiplayer_play_button.grid(row=2, column=1, columnspan=2)

        window.mainloop()

    def single_play(self):
        screen = Screen()
        screen.bgcolor("black")
        screen.setup(width=800, height=600)
        screen.title("Pong")
        screen.tracer(0)

        r_paddle = Paddle((350, 0))
        l_paddle = Bot((-350, 0))
        ball = Ball()
        scoreboard = Scoreboard()
        screen.listen()

        screen.onkeypress(r_paddle.up, "Up")
        screen.onkeypress(r_paddle.down, "Down")

        l_score = 0
        r_score = 0
        game_is_on = True
        while game_is_on:
            time.sleep(ball.move_speed)
            screen.update()
            ball.move()
            up = 0
            down = 0

            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

            if 320 < ball.xcor() < 345 and ball.distance(r_paddle) < 50 or \
                    -320 > ball.xcor() > -345 and ball.distance(l_paddle) < 50:
                ball.bounce_x()

            if ball.ycor() > l_paddle.ycor() and up < 1:
                l_paddle.up_bot()

            if ball.ycor() < l_paddle.ycor() and down < 1:
                l_paddle.down_bot()

            if ball.xcor() > 380:
                ball.reset_position()
                scoreboard.l_point()
                l_score += 1

            if ball.xcor() < -380:
                ball.reset_position()
                scoreboard.r_point()
                r_score += 1

            if l_score > 9:
                scoreboard.game_over_single()
                break
            if r_score > 9:
                scoreboard.game_over_single()
                break
        screen.exitonclick()

    def multi_play(self):
        screen = Screen()
        screen.bgcolor("black")
        screen.setup(width=800, height=600)
        screen.title("Pong")
        screen.tracer(0)

        r_paddle = Paddle((350, 0))
        l_paddle = Paddle((-350, 0))
        ball = Ball()
        scoreboard = Scoreboard()
        screen.listen()

        screen.onkey(r_paddle.up, "Up")
        screen.onkey(r_paddle.down, "Down")

        screen.onkey(l_paddle.up, "w")
        screen.onkey(l_paddle.down, "s")

        l_score = 0
        r_score = 0
        game_is_on = True
        while game_is_on:
            time.sleep(ball.move_speed)
            screen.update()
            ball.move()

            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

            if 320 < ball.xcor() < 345 and ball.distance(r_paddle) < 50 or \
                    -320 > ball.xcor() > -345 and ball.distance(l_paddle) < 50:
                ball.bounce_x()

            if ball.xcor() > 380:
                ball.reset_position()
                scoreboard.l_point()
                l_score += 1

            if ball.xcor() < -380:
                ball.reset_position()
                scoreboard.r_point()
                r_score += 1

            if l_score > 9:
                scoreboard.game_over_multi()
                break
            if r_score > 9:
                scoreboard.game_over_multi()
                break
        screen.exitonclick()
