from objects.figure import Rect
from settings import Settings
from raylib import colors
from settings import Settings

"""
Класс клетки для отрисовки поля
"""


class Cell(Rect):
    def __init__(self, x, y, tip=1, width=30, height=30):
        self.tip = tip
        real_x, real_y = self.get_real_pos(x, y)
        super().__init__(real_x, real_y, width, height, self.get_color(tip), Settings.field_outline)

    @staticmethod
    def get_real_pos(x, y):
        real_x, real_y = ((Settings.WIDTH - 17 * 30)//2) + 30*x, ((Settings.HEIGHT - 21 * 30)//2) + 30*y
        return real_x, real_y

    @staticmethod
    def get_color(tip):
        if tip == 0:
            return colors.BLACK
        if tip == 1:
            return colors.BLUE
        if tip == 2:
            return colors.DARKBLUE
        if tip == 3:
            return colors.GREEN
        if tip == 4:
            return colors.YELLOW
        if tip == 5:
            return colors.RED

