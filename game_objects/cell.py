from objects.figure import Rect
from settings import Settings
from raylib import colors
"""
Класс клетки для отрисовки поля


Добавить в приложение класс клетки (Cell).
Клетка - это часть поля, внутри хранит тип (0 - пустое место, 1 - стена, 2 - комната для призраков, 3 - телепорт).
В зависимости от этого - её нужно отрисовывать разными цветными квадратами.
Добавить 4 объекта клетки (с разными типами) на первую сцену.
"""


class Cell(Rect):
    def __init__(self, x, y, tip=1, width=30, height=30):
        self.tip = tip
        real_x, real_y = self.get_real_pos(x, y)
        super().__init__(real_x, real_y, width, height, self.get_color(tip))

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

