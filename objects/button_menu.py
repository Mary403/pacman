from objects.button import Button
from settings import Settings

"""
Класс кнопки меню
"""


class ButtonMenu(Button):
    def __init__(self, x=20, y=20, width=150, height=50, color=(150, 150, 0, 255), outline=False, text='<- Menu',
                 color_text=(0, 0, 0, 255)):
        super().__init__(x, y, width, height, color, outline, text, color_text)

    def click(self):  # событие клика
        super().click()
        Settings.set_scene(0)
