import pyray
from raylib import colors

from objects.text import Text


class Counter(Text):
    def __init__(self, x, y, text, size, color=None, spacing=2, score=0):
        super().__init__(x, y, str(score), size, color=color, spacing=spacing)
        self.score = score

    def score_change(self, points):
        self.score += points
        self.text = str(self.score)

#a = Counter(100, 100, "0", 20, pyray.WHITE, 2, 0)