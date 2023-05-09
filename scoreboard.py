from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over_single(self):
        if self.l_score > 9:
            self.goto(0, 0)
            self.write("BOT WIN!", align="center", font=("Courier", 55, "normal"))
        elif self.r_score > 9:
            self.goto(0, 0)
            self.write("YOU WIN!", align="center", font=("Courier", 55, "normal"))

    def game_over_multi(self):
        if self.l_score > 9:
            self.goto(0, 0)
            self.write("LEFT PLAYER WIN!", align="center", font=("Courier", 55, "normal"))
        elif self.r_score > 9:
            self.goto(0, 0)
            self.write("RIGHT PLAYER WIN!", align="center", font=("Courier", 55, "normal"))