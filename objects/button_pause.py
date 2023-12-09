from objects.button import Button
from settings import Settings

"""
Класс кнопки паузы
"""


class ButtonPause(Button):
    def __init__(self, x=Settings.WIDTH-20-150, y=20, width=150, height=50, color=(150, 150, 0, 255), outline=False,
                 text='Pause',
                 color_text=(0, 0, 0, 255)):
        super().__init__(x, y, width, height, color, outline, text, color_text)

    def click(self):  # событие клика
        super().click()
        if Settings.scene_index == 2:
            Settings.set_scene(1)
        elif Settings.scene_index == 1:
            Settings.set_scene(2)
