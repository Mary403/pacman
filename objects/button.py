import pyray
from pyautogui import Point
from raylib import colors
from objects.figure import Rect
from objects.text import Text

"""
Класс кнопки
"""


class Button(Rect):
    def __init__(self, x, y, width, height, color=None, outline=False, text=None, color_text=None):
        super().__init__(x, y, width, height, color, outline)
        self.colorText = color_text
        self.text = Text(x + width // 2 - 18 * len(text) // 2, y + height // 2 - 18, text, 32, color_text)  # ООО ДАААА ТЕКСТ ПО СЕРЕДИНЕ

    def set_size(self, w, h):
        self.width = w
        self.height = h

    def draw(self):
        super().draw()
        self.text.draw()

    def event(self):
        if self.is_click():
            self.click()

    def is_click(self):  # проверка нажата ли кнопка
        point = (pyray.get_mouse_position().x, pyray.get_mouse_position().y)
        rec = pyray.Rectangle(self.x, self.y, self.width, self.height)
        if pyray.check_collision_point_rec(point, rec):
            if pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                return True
            return False
        return False

    def click(self):  # событие клика
        print('Кликнулось')