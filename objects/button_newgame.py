from objects.button import Button
from settings import Settings

"""
Класс кнопки новой игры
"""


class ButtonNewGame(Button):
    def __init__(self, x, y, width, height, color=None, outline=False, text=None, color_text=None):
        super().__init__(x, y, width, height, color, outline, text, color_text)

    def click(self):  # событие клика
        super().click()
        Settings.newgame = True
        Settings.set_scene(2)
