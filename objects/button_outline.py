import sys

from objects.button import Button
from settings import Settings
from raylib import colors

"""
Класс кнопки в настройках. Вид поля
"""


class ButtonOutline(Button):
    def __init__(self, x=Settings.WIDTH//2 - 350//2, y=Settings.HEIGHT//2 - 150//2 + 100, width=350, height=150, color=colors.RED,
                 outline=False, text='Outline: OFF', color_text=(255, 255, 255, 200)):
        super().__init__(x, y, width, height, color, outline, text, color_text)

    def click(self):  # событие клика
        if Settings.field_outline:
            Settings.field_outline = False
            self.set_color(colors.RED)
            self.set_text('Outline: OFF')

        elif not Settings.field_outline:
            Settings.field_outline = True
            self.set_color(colors.GREEN)
            self.set_text('Outline: ON')

        super().click()

