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
        self.tick_gho = 0
        self.tick_pac = 0
        self.pacman = PacmanLogic(0, 0, self.data)
        self.ghost = GhostLogic(0, 0)
        self.read_level("levels/level1.txt")
        self.speed = 5

    def newgame(self):
        self.read_level("levels/level1.txt")

    def event(self):
        self.pacman.event()

    def logic(self):
        self.tick_pac += self.speed
        self.tick_gho += self.speed
        ghost_move = True
        if self.tick_pac >= Settings.FPS // self.pacman.speed:
            if not Settings.is_gameover:
                self.change_pole_data_pacman()

            self.tick_pac = 0

        if self.tick_gho >= Settings.FPS // self.ghost.speed:
            if not Settings.is_gameover:
                self.change_pole_data_ghost()

            self.tick_gho = 0
            # TODO: Вывод поля
            for row in self.data:
                print(*row, end='')
            print()
            print(self.pacman.x, self.pacman.y)
            print("-*-"*30)

        if self.ghost.is_die:
            for i in range(len(self.data)):
                for j in range(len(self.data[0]) - 1):
                    if self.data[i][j] == '1':
                        self.data[i] = self.data[i][:j] + ' ' + self.data[i][j + 1:]
                    if i == 9 and j == 7:
                        self.data[i] = self.data[i][:j] + '1' + self.data[i][j + 1:]
                        self.ghost.x, self.ghost.y = j, i

    def change_pole_data_pacman(self):
        pac_x, pac_y = self.pacman.x, self.pacman.y
        self.data[pac_y] = self.data[pac_y][:pac_x] + '.' + self.data[pac_y][pac_x + 1:]
        self.pacman.move(self.data)
        pac_x, pac_y = self.pacman.x, self.pacman.y
        self.data[pac_y] = self.data[pac_y][:pac_x] + '@' + self.data[pac_y][pac_x + 1:]

    def change_pole_data_ghost(self):
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
            for j in range(len(self.data[0]) - 1):
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
