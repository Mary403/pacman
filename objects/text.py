import pyray
from raylib import colors

from objects.base import BaseObject


class Text(BaseObject):
    def __init__(self, x, y, text, size, color=None, spacing=2):
        super().__init__(x, y)
        self.rect = pyray.Rectangle(x, y, 0, 0)
        self.text = text
        self.size = size
        self.spacing = spacing
        self.color = color if color else colors.RED

    def set_position(self, x, y):
        super().set_position(x, y)
        self.rect = pyray.Rectangle(x, y, 0, 0)

    def draw(self):
        pos = pyray.Vector2(self._x, self._y)
        pyray.draw_text_ex(pyray.get_font_default(), self.text, pos, self.size, self.spacing, self.color)
