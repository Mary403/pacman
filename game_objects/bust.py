import pyray

from objects.base import BaseObject
from settings import Settings


class Bust(BaseObject):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

        self.tick = 0
        self.time_activ = 300

    def logic(self):
        super().logic()

        if Settings.bust:
            self.tick += 1
            if self.tick >= self.time_activ:
                self.tick = 0
                Settings.bust = False
        else:
            self.tick = 0
