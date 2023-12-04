"""
    Добавить в приложение класс большого зерна (Energizer)
    Объект этого класса должен уметь отображаться в виде картинки (пока что жёлтый круг радиусом в 20 пикселей).
    Объект этого класса должен хранить в себе вес малого зерна (по умолчанию 50).
"""
from objects.figure import Ellipse
from raylib import colors


class Energizer(Ellipse):
    def __init__(self, x, y, radius_w = 20, radius_h = 20, color = colors.YELLOW):
        super().__init__(x, y, radius_w, radius_h, color)
        self.weight = 50

    def set_position(self, x, y):
        self.x = x
        self.y = y


