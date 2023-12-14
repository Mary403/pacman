from objects.base import BaseObject
from settings import Settings
from game_objects.pacman import PacmanLogic
from game_objects.ghost import GhostLogic

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
        self.ghost = GhostLogic(0, 0)
        self.read_level("levels/level1.txt")
        self.speed = 5

    def newgame(self):
        self.read_level("levels/level1.txt")

    def event(self):
        self.pacman.event()

    def logic(self):
        self.tick += self.speed
        if self.tick >= Settings.FPS:
            # TODO: Все двигаются на одну клетку
            if not Settings.is_gameover:
                self.change_pole_data()

            self.tick = 0
            # TODO: Вывод поля
            """for row in self.data:
                print(*row, end='')
            print()
            print(self.pacman.x, self.pacman.y)
            print("-*-"*30)"""

    def change_pole_data(self):
        pac_x, pac_y = self.pacman.x, self.pacman.y
        # self.data[y][x] = ' '
        self.data[pac_y] = self.data[pac_y][:pac_x] + '.' + self.data[pac_y][pac_x+1:]
        self.pacman.move(self.data)
        pac_x, pac_y = self.pacman.x, self.pacman.y
        # self.data[y][x] = '@'
        self.data[pac_y] = self.data[pac_y][:pac_x] + '@' + self.data[pac_y][pac_x + 1:]

        gho_x, gho_y = self.ghost.x, self.ghost.y
        self.data[gho_y] = self.data[gho_y][:gho_x] + '.' + self.data[gho_y][gho_x + 1:]
        self.ghost.move(self.data, self.pacman.x, self.pacman.y)
        gho_x, gho_y = self.ghost.x, self.ghost.y
        self.data[gho_y] = self.data[gho_y][:gho_x] + '1' + self.data[gho_y][gho_x + 1:]

    def read_level(self, path):
        fin = open(path, "r")
        self.data.clear()
        for line in fin:
            self.data.append(line)
        for i in range(len(self.data)):
            for j in range(len(self.data[0])-1):
                if self.data[i][j] == '@':
                    self.pacman.x, self.pacman.y = j, i
                if self.data[i][j] == '1':
                    self.ghost.x, self.ghost.y = j, i


"""def main():
    logic = LogicPole()
    logic.read_level("../levels/level1.txt")
    for line in logic.data:
        print(line, end='')
    print(len(logic.data), len(logic.data[0]))


if __name__ == '__main__':
    main()
"""