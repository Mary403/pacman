import pyray

from objects.base import BaseObject
from objects.image import Image


class Turn:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


"""
Класс логики Пакмена (движение, управление)
"""


class PacmanLogic(BaseObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.turn = Turn.RIGHT

    def move(self, data):
        x, y = self.x, self.y
        if self.turn == Turn.UP and data[y - 1][x] != '#':
            self.y -= 1
        if self.turn == Turn.RIGHT and data[y][x + 1] != '#':
            self.x += 1
        if self.turn == Turn.DOWN and data[y + 1][x] != '#':
            self.y += 1
        if self.turn == Turn.LEFT and data[y][x - 1] != '#':
            self.x -= 1

    def event(self):
        keys = {
            pyray.KeyboardKey.KEY_W: Turn.UP,
            pyray.KeyboardKey.KEY_A: Turn.LEFT,
            pyray.KeyboardKey.KEY_S: Turn.DOWN,
            pyray.KeyboardKey.KEY_D: Turn.RIGHT,
        }
        for key in keys:
            if pyray.is_key_pressed(key):
                self.turn = keys[key]


"""
Класс Пакмана, наследуемый от Image
"""


"""class Pacman(Image):
    def __init__(self, x, y, path, size):
        super().__init__("", x, y, path, size)
        self.turn = Turn.RIGHT

    def event(self):
        keys = {
            pyray.KeyboardKey.KEY_W: Turn.UP,
            pyray.KeyboardKey.KEY_A: Turn.LEFT,
            pyray.KeyboardKey.KEY_S: Turn.DOWN,
            pyray.KeyboardKey.KEY_D: Turn.RIGHT,
        }
        for key in keys:
            if pyray.is_key_pressed(key):
                self.turn = keys[key]"""
