import pyray
from objects.image import Image
from objects.base import BaseObject


class Animated(BaseObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.data = [
            Image("images/image1.png", pyray.Rectangle(x, y, w, h)),
            Image("images/image2.png", pyray.Rectangle(x, y, w, h))
        ]
        self.current_frame = 0
        self.fps = 60
        self.tick = self.fps

    def logic(self):
        self.tick -= 5
        if self.tick <= 0:
            self.tick = self.fps
            self.current_frame = (self.current_frame+1) % len(self.data)

    def draw(self):
        self.data[self.current_frame].draw()
