import pyray
import raylib
from raylib import colors

from objects.text import Text
from scenes.base import BaseScene
from settings import Settings


class SettingsScene(BaseScene):  # Сцена 3
    def __init__(self):
        self.hello_text = Text(Settings.WIDTH // 2, Settings.HEIGHT // 2, "Settings", 32, colors.SKYBLUE)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_M):
            Settings.set_scene(0)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_G):
            Settings.set_scene(2)

