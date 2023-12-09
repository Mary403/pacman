import pyray

from objects.base import BaseObject
from objects.image import Image
from settings import Settings


class Turn:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


"""
Класс изображения Пакмена
"""


class Pacman(Image):
    def __init__(self, x, y, size=30):
        self.real_x, self.real_y = self.get_real_pos(x, y)
        super().__init__("image/pacman1.png", pyray.Rectangle(self.real_x, self.real_y, size, size))
        self.turn = Turn.UP
        self.radius = size // 2

        self.tick = 10

        self.pictures = [
            "image/pacman1.png",  # 0
            "image/pacman2.png",  # 1
            "image/pacman3.png",  # 2
        ]
        self.index_pic = 0

    def logic(self):
        super().logic()
        self.animation()

    def animation(self):
        self.tick += 1
        if self.tick >= 15:
            self.tick = 0

            self.index_pic += 1
            if self.index_pic > len(self.pictures) - 1:
                self.index_pic = 0

            self.set_picture(self.pictures[self.index_pic])

    def get_real_pos(self, x, y):
        self.real_x, self.real_y = ((Settings.WIDTH - 17 * 30) // 2) + 30 * x + 15, (
                (Settings.HEIGHT - 21 * 30) // 2) + 30 * y + 15
        return self.real_x, self.real_y

    def set_pos(self, x, y):
        self.x, self.y = self.get_real_pos(x, y)

    def get_center(self):
        return self.real_x + 5, self.real_y + 5

    def get_radius(self):
        return self.radius


"""
Класс логики Пакмена (движение, управление)
"""


class PacmanLogic(BaseObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.turn = Turn.UP
        self.image_pacman = Pacman(8, 15)

    def move(self, data):
        x, y = self.x, self.y
        if self.turn == Turn.UP and data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
            self.y -= 1
            self.image_pacman.set_rotation(270)
        if self.turn == Turn.RIGHT and data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
            self.x += 1
            self.image_pacman.set_rotation(0)
        if self.turn == Turn.DOWN and data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
            self.y += 1
            self.image_pacman.set_rotation(90)
        if self.turn == Turn.LEFT and data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
            self.x -= 1
            self.image_pacman.set_rotation(180)

        if self.turn == Turn.RIGHT and data[y][x + 1] == '!':
            self.x = 1
        if self.turn == Turn.LEFT and data[y][x - 1] == '!':
            self.x = 15

        self.image_pacman.set_pos(self.x, self.y)

    def logic(self):
        self.image_pacman.logic()
        super().logic()

    def draw(self):
        self.image_pacman.draw()
        super().draw()

    def event(self):
        self.image_pacman.event()
        keys = {
            pyray.KeyboardKey.KEY_W: Turn.UP,
            pyray.KeyboardKey.KEY_A: Turn.LEFT,
            pyray.KeyboardKey.KEY_S: Turn.DOWN,
            pyray.KeyboardKey.KEY_D: Turn.RIGHT,
        }
        for key in keys:
            if pyray.is_key_pressed(key):
                self.turn = keys[key]
