from objects.figure import Ellipse
from raylib import colors
from objects.base import BaseObject
from settings import Settings

"""
    Классы большого и маленького зерна
"""


class Energizer(Ellipse):
    def __init__(self, x, y, radius_w=10, radius_h=10, color=colors.WHITE):
        self.real_x, self.real_y = self.get_real_pos(x, y)
        super().__init__(self.real_x, self.real_y, radius_w, radius_h, color)
        self.weight = 50
        self.radius_w = radius_w
        self.radius_h = radius_h

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_center(self):
        return self.real_x, self.real_y

    def get_radius(self):
        return self.radius_w

    @staticmethod
    def get_real_pos(x, y):
        real_x, real_y = ((Settings.WIDTH - 17 * 30) // 2) + 30 * x + 15, ((Settings.HEIGHT - 21 * 30) // 2) + 30 * y + 15
        return real_x, real_y

    def eaten(self, counter):
        # TODO: Включается режим bust
        counter.score_change(self.weight)


class Seed(Ellipse):
    def __init__(self, x, y, radius_w=5, radius_h=5, color=colors.WHITE):
        self.real_x, self.real_y = self.get_real_pos(x, y)
        super().__init__(self.real_x, self.real_y, radius_w, radius_h, color)
        self.weight = 10
        self.radius_w = radius_w
        self.radius_h = radius_h

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_center(self):
        return self.real_x, self.real_y

    def get_radius(self):
        return self.radius_w

    @staticmethod
    def get_real_pos(x, y):
        real_x, real_y = ((Settings.WIDTH - 17 * 30) // 2) + 30 * x + 15, ((Settings.HEIGHT - 21 * 30) // 2) + 30 * y + 15
        return real_x, real_y

    def eaten(self, counter):
        counter.score_change(self.weight)


class SeedsLogic(BaseObject):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.data = []
        self.seeds = []
        self.read_level("levels/level1.txt")

    def newgame(self):
        self.data = []
        self.seeds = []
        self.read_level("levels/level1.txt")

    def set_data(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0]) - 1):
                if self.data[i][j] == '.':
                    if (i == 3 and j == 1) or (i == 15 and j == 15) or (i == 15 and j == 1) or (i == 3 and j == 15):
                        seed = Energizer(j, i)
                        self.seeds.append(seed)
                    elif not (i == 11 and j > 13) and not (i == 7 and j > 13) and not (i == 8 and j == 15):
                        seed = Seed(j, i)
                        self.seeds.append(seed)

    def read_level(self, path):
        fin = open(path, "r")
        self.data.clear()
        for line in fin:
            self.data.append(line)
        self.set_data()

    def event(self):
        for i in range(len(self.seeds)):
            self.seeds[i].event()

    def logic(self):
        for i in range(len(self.seeds)):
            self.seeds[i].logic()

    def draw(self):
        for i in range(len(self.seeds)):
            self.seeds[i].draw()
