import pyray
import raylib

from objects.text import Text
from scenes.base import BaseScene
from settings import Settings

from raylib import colors

from objects.button import Button
from objects.button_exit import ButtonExit


class MenuScene(BaseScene):  # Сцена 0
    def __init__(self):
        self.hello_text = Text(Settings.WIDTH // 2 - 90, Settings.HEIGHT // 2 - 200, "Welcome", 50,
                               (255, 255, 255, 255))
        self.button1 = Button(Settings.WIDTH // 2 - 1000, Settings.HEIGHT // 2 - 50, 2000, 100,
                              (20, 100, 20, 255), False, 'New game', (0, 255, 0, 255))
        self.button2 = ButtonExit(Settings.WIDTH // 2 - 1000, Settings.HEIGHT // 2 - 50 + 150, 2000, 100,
                                  (100, 20, 20, 255), False, 'Exit', (255, 0, 0, 255))
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)
        self.objects.append(self.button1)
        self.objects.append(self.button2)

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_G):
            Settings.set_scene(2)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_S):
            Settings.set_scene(3)
