from objects.text import Text
from raylib import colors

"""
    Класс счётчика
"""


class Counter(Text):
    def __init__(self, x, y, text='Score: 0', size=30, color=colors.WHITE, spacing=2, score=0):
        super().__init__(x, y, text, size, color=color, spacing=spacing)
        self.score = score

    def score_change(self, points):
        self.score += points
        self.text = 'Score: ' + str(self.score)
