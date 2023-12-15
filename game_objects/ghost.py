import random

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
Класс изображения призрака
"""


class Ghost(Image):
    def __init__(self, x, y, size=30):
        self.real_x, self.real_y = self.get_real_pos(x, y)
        super().__init__("image/ghost_down0.png", pyray.Rectangle(self.real_x, self.real_y, size, size))
        self.turn = Turn.UP
        self.radius = size // 2

        self.tick = 0

        self.down_pictures = [
            "image/ghost_down0.png",  # 0
            "image/ghost_down1.png",  # 1
        ]
        self.up_pictures = [
            "image/ghost_up0.png",  # 0
            "image/ghost_up1.png",  # 1
        ]
        self.left_pictures = [
            "image/ghost_left0.png",  # 0
            "image/ghost_left1.png",  # 1
        ]
        self.right_pictures = [
            "image/ghost_right0.png",  # 0
            "image/ghost_right1.png",  # 1
        ]
        self.bust_pictures = [
            "image/ghost_bust0.png",  # 0
            "image/ghost_bust1.png",  # 1
        ]

        self.now_pictures = self.down_pictures

        self.index_pic = 0

        self.start_x = x
        self.start_y = y

    def newgame(self):
        self.turn = Turn.UP
        self.set_pos(self.start_x, self.start_y)

    def logic(self):
        super().logic()
        self.animation()

    def animation(self):
        self.tick += 1
        if self.tick >= 15:
            self.tick = 0

            self.index_pic += 1
            if self.index_pic > len(self.now_pictures) - 1:
                self.index_pic = 0

            self.set_picture(self.now_pictures[self.index_pic])

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
Класс логики призрака (движение, управление)
"""


class GhostLogic(BaseObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.turn = Turn.UP
        self.image_ghost = Ghost(7, 9)
        self.start_x = x
        self.start_y = y

        self.is_die = False
        self.tick_die = 0
        self.time_die = 300

        self.speed = 1
        self.weight = 100

    def move(self, data, pac_x, pac_y):
        self.new_turn(data, pac_x, pac_y)
        x, y = self.x, self.y
        if self.turn == Turn.UP and data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
            self.y -= 1
            # self.image_ghost.set_rotation(270)
        if self.turn == Turn.RIGHT and data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
            self.x += 1
            # self.image_ghost.set_rotation(0)
        if self.turn == Turn.DOWN and data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
            self.y += 1
            # self.image_ghost.set_rotation(90)
        if self.turn == Turn.LEFT and data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
            self.x -= 1
            # self.image_ghost.set_rotation(180)

        """if self.turn == Turn.RIGHT and data[y][x + 1] == '!':
            self.x = 1
        if self.turn == Turn.LEFT and data[y][x - 1] == '!':
            self.x = 15"""

        self.image_ghost.set_pos(self.x, self.y)

    def newgame(self):
        self.turn = Turn.DOWN
        self.speed = 1
        self.is_die = False
        self.tick_die = 0
        """self.x = self.start_x
        self.y = self.start_y"""

    def logic(self):
        if Settings.bust:
            self.speed = 0.25

        if self.is_die:
            self.tick_die += 1
            # print(self.tick_die)
            if self.tick_die >= self.time_die:
                self.tick_die = 0
                self.is_die = False
                # print('is die = False')
                Settings.bust = False
                # print('bust = False')
                turn = self.turn

                self.speed = 1

                if not Settings.bust:
                    if turn == Turn.UP:
                        self.image_ghost.now_pictures = self.image_ghost.up_pictures
                    elif turn == Turn.DOWN:
                        self.image_ghost.now_pictures = self.image_ghost.down_pictures
                    elif turn == Turn.LEFT:
                        self.image_ghost.now_pictures = self.image_ghost.left_pictures
                    elif turn == Turn.RIGHT:
                        self.image_ghost.now_pictures = self.image_ghost.right_pictures
                else:
                    self.image_ghost.now_pictures = self.image_ghost.bust_pictures

        if not Settings.bust:
            self.speed = 1

        if not self.is_die:
            self.image_ghost.logic()
            super().logic()

    def draw(self):
        turn = self.turn
        if not Settings.bust:
            if turn == Turn.UP:
                self.image_ghost.now_pictures = self.image_ghost.up_pictures
            elif turn == Turn.DOWN:
                self.image_ghost.now_pictures = self.image_ghost.down_pictures
            elif turn == Turn.LEFT:
                self.image_ghost.now_pictures = self.image_ghost.left_pictures
            elif turn == Turn.RIGHT:
                self.image_ghost.now_pictures = self.image_ghost.right_pictures
        else:
            self.image_ghost.now_pictures = self.image_ghost.bust_pictures

        if not self.is_die:
            self.image_ghost.draw()
            super().draw()

    def event(self):
        if not self.is_die:
            self.image_ghost.event()

    def new_turn(self, data, pac_x, pac_y):
        x, y = self.x, self.y
        turns = []

        if not Settings.bust:
            if data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
                if y > pac_y:
                    if self.turn != Turn.DOWN:
                        turns.append(Turn.UP)

            if data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
                if y < pac_y:
                    if self.turn != Turn.UP:
                        turns.append(Turn.DOWN)

            if data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
                if x > pac_x:
                    if self.turn != Turn.RIGHT:
                        turns.append(Turn.LEFT)

            if data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
                if x < pac_x:
                    if self.turn != Turn.LEFT:
                        turns.append(Turn.RIGHT)

            if len(turns) == 0:
                # print('000')

                if data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
                    if self.turn != Turn.DOWN:
                        turns.append(Turn.UP)

                if data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
                    if self.turn != Turn.UP:
                        turns.append(Turn.DOWN)

                if data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
                    if self.turn != Turn.RIGHT:
                        turns.append(Turn.LEFT)

                if data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
                    if self.turn != Turn.LEFT:
                        turns.append(Turn.RIGHT)

                if len(turns) == 0:
                    if data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
                        turns.append(Turn.UP)

                    if data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
                        turns.append(Turn.DOWN)

                    if data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
                        turns.append(Turn.LEFT)

                    if data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
                        turns.append(Turn.RIGHT)
        else:
            if data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
                if y < pac_y:
                    # if self.turn != Turn.DOWN:
                    turns.append(Turn.UP)

            if data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
                if y > pac_y:
                    # if self.turn != Turn.UP:
                    turns.append(Turn.DOWN)

            if data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
                if x < pac_x:
                    # if self.turn != Turn.RIGHT:
                    turns.append(Turn.LEFT)

            if data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
                if x > pac_x:
                    # if self.turn != Turn.LEFT:
                    turns.append(Turn.RIGHT)

            if len(turns) == 0:
                # print('000')

                if data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
                    if self.turn != Turn.DOWN:
                        turns.append(Turn.UP)

                if data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
                    if self.turn != Turn.UP:
                        turns.append(Turn.DOWN)

                if data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
                    if self.turn != Turn.RIGHT:
                        turns.append(Turn.LEFT)

                if data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
                    if self.turn != Turn.LEFT:
                        turns.append(Turn.RIGHT)

                if len(turns) == 0:
                    if data[y - 1][x] != '#' and data[y - 1][x] != '=' and data[y - 1][x] != '!':
                        turns.append(Turn.UP)

                    if data[y + 1][x] != '#' and data[y + 1][x] != '=' and data[y + 1][x] != '!':
                        turns.append(Turn.DOWN)

                    if data[y][x - 1] != '#' and data[y][x - 1] != '=' and data[y][x - 1] != '!':
                        turns.append(Turn.LEFT)

                    if data[y][x + 1] != '#' and data[y][x + 1] != '=' and data[y][x + 1] != '!':
                        turns.append(Turn.RIGHT)

        # print('turns', *turns)
        turn = (random.choice(turns))
        # print('turn:', turn)

        self.set_turn(turn)

    def set_turn(self, turn):
        if not Settings.bust:
            if turn == Turn.UP:
                self.image_ghost.now_pictures = self.image_ghost.up_pictures
            elif turn == Turn.DOWN:
                self.image_ghost.now_pictures = self.image_ghost.down_pictures
            elif turn == Turn.LEFT:
                self.image_ghost.now_pictures = self.image_ghost.left_pictures
            elif turn == Turn.RIGHT:
                self.image_ghost.now_pictures = self.image_ghost.right_pictures
        else:
            self.image_ghost.now_pictures = self.image_ghost.bust_pictures

        self.turn = turn

    def die(self, counter):
        # print('DIE')
        self.is_die = True
        Settings.bust = False
        # print('is die = True')
        # print('bust = False')
        self.image_ghost.set_pos(7, 9)

        counter.score_change(self.weight)
