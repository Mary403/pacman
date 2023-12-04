"""
Класс отрисовки поля
"""
from game_objects.pole import LogicPole
from game_objects.cell import Cell

from objects.base import BaseObject


class FieldDrawer(BaseObject):
    def __init__(self, pole_data):
        self.data = pole_data
        super().__init__(0, 0)

    def draw(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0]) - 1):
                if self.data[i][j] == '.':
                    Cell(j, i, 0).draw()
                elif self.data[i][j] == '#':
                    Cell(j, i, 1).draw()
                elif self.data[i][j] == '=':
                    Cell(j, i, 2).draw()
                elif self.data[i][j] == '!':
                    Cell(j, i, 3).draw()
                elif self.data[i][j] == '@':
                    Cell(j, i, 4).draw()
