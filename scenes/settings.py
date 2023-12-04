import pyray
import raylib
from raylib import colors

from objects.text import Text
from scenes.base import BaseScene
from settings import Settings

from objects.button_menu import ButtonMenu


class SettingsScene(BaseScene):  # Сцена 3
    def __init__(self):
        self.hello_text = Text(Settings.WIDTH // 2, Settings.HEIGHT // 2, "Settings", 32, colors.SKYBLUE)
        self.button_menu = ButtonMenu()
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)
        self.objects.append(self.button_menu)

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ZERO):
            Settings.set_scene(0)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_scene(1)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            Settings.set_scene(2)
