import sys

from objects.button import Button

"""
Класс кнопки выхода из игры
"""


class ButtonExit(Button):
    def __init__(self, x, y, width, height, color=None, outline=False, text=None, color_text=None):
        super().__init__(x, y, width, height, color, outline, text, color_text)

    def click(self):  # событие клика
        super().click()
        sys.exit()
