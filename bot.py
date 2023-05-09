from paddle import Paddle
MOVE_BOT = 9


class Bot(Paddle):
    def up_bot(self):
        if not self.ycor() > 250:
            self.forward(MOVE_BOT)

    def down_bot(self):
        if not self.ycor() < -230:
            self.back(MOVE_BOT)
