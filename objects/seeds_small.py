import pyray
from raylib import colors
from objects.base import BaseObject
from objects.text import Text
from objects.figure import Ellipse
from raylib import colors

class Counter(Text):
    def __init__(self, x, y, text, size, color=None, spacing=2, score=0):
        super().__init__(x, y, str(score), size, color=color, spacing=spacing)
        self.score = score

    def score_change(self, points):
        self.score += points
        self.text = str(self.score)
class Seeds(Ellipse):
    def __init__(self, x, y, radius_w=10, radius_h=20, color=colors.YELLOW):
        super().__init__(x,y, radius_w,radius_h, color)
        self.weight = 10
        self.cnt = 0

    def set_position(self, x, y):
        self._x= x
        self._y=y


