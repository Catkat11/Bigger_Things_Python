import pygame
from paddle import Paddle


class Bot(Paddle):

    def __init__(self, x, y, width, height, level):
        if level:
            self.bot_velocity = self.VEL_BOT_NOR
        else:
            self.bot_velocity = self.VEL_BOT_EASY
        super().__init__(x, y, width, height)

    def move_bot(self, up=True):
        if up:
            self.y -= self.bot_velocity
        else:
            self.y += self.bot_velocity

