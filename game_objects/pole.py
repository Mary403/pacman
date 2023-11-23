from objects.base import BaseObject
from settings import Settings
from game_objects.pacman import PacmanLogic
import levels

"""
Класс Поля
"""


class LogicPole(BaseObject):
    def __init__(self):
        super().__init__(0, 0)
        self.n = 0
        self.m = 0
        self.data = []  # поле
        self.tick = 0  # таймер
        self.pacman = PacmanLogic(0, 0)
        self.read_level("./level1.txt")

    def event(self):
        self.pacman.event()

    def logic(self):
        self.tick += 1
        if self.tick >= Settings.FPS:
            # TODO: Все двигаются на одну клетку
            # self.pacman.move(self.data)
            self.change_pole_data()

            self.tick = 0
            # TODO: Вывод поля
            for row in self.data:
                print(*row, end='')
            print(self.pacman.x, self.pacman.y)
            print("-*-"*30)

    def change_pole_data(self):
        x, y = self.pacman.x, self.pacman.y
        # self.data[y][x] = ' '
        self.data[y] = self.data[y][:x] + ' ' + self.data[y][x+1:]
        self.pacman.move(self.data)
        x, y = self.pacman.x, self.pacman.y
        # self.data[y][x] = '@'
        self.data[y] = self.data[y][:x] + '@' + self.data[y][x + 1:]

    def read_level(self, path):
        fin = open(path, "r")
        self.data.clear()
        for line in fin:
            self.data.append(line)
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == '@':
                    self.pacman.x, self.pacman.y = j, i


def main():
    logic = LogicPole()
    logic.read_level("../level1.txt")
    for line in logic.data:
        print(line, end='')


if __name__ == '__main__':
    main()
