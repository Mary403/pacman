import random

import pyray
import os
from objects.image import Image
from objects.base import BaseObject


class Cherry(Image):
    def __init__(self, size=48):
        super().__init__("image/cherry.png", pyray.Rectangle(0, 0, size, size))
        self.map_position = (0, 0)  # Левый верхний угол
        self.show_time = 2
        self.hide_time = 1
        self.current_left_time = self.hide_time
        self.is_show = False

    def logic(self):
        self.current_left_time -= pyray.get_frame_time()
        if self.current_left_time >= 0:
            return None
        if self.is_show:
            self.current_left_time = self.hide_time  # Можно добавить рандома
        else:
            self.current_left_time = self.show_time
            # Функцию должен написать тот, кто разрабатывал поле
            # self.map_position = из_настроек_карты_взять_data_и_найти_рандомное_свободное_место()
            """
            map можно прокинуть:
            1. Доп. методом
            2. Через поле вишни
            3. Статическое поле карты и импорт
            """
            map = [
                [0, 0, 1],
                [0, 1, 0],
                [1, 0, 0],
            ]
            free_cords = [(x, y) for y in range(len(map)) for x in range(len(map[y])) if map[x][y] == 0]
            self.map_position = random.choice(free_cords)

            """
            Потом, с учетом размера ячейки (self.size) карты, отрисовать в нужных координатах
            WARNING! self._x, self._y <- с нижним подчеркиванием (protected)
            """
            padding = 100
            self.set_position(self.map_position[0] * self.width + padding, self.map_position[1] * self.height + padding)
        self.is_show = not self.is_show

    def draw(self):
        if self.is_show:
            super().draw()
