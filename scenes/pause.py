import pyray
from raylib import colors

from objects.text import Text
from scenes.base import BaseScene
from objects.button_pause import ButtonPause
from settings import Settings


class PauseScene(BaseScene):  # Сцена 1
    def __init__(self):
        self.hello_text = Text(Settings.WIDTH // 2, Settings.HEIGHT // 2, "Pause", 32, colors.YELLOW)
        self.button_pause = ButtonPause()
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)
        self.objects.append(self.button_pause)

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ZERO):
            Settings.set_scene(0)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            Settings.set_scene(2)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_THREE):
            Settings.set_scene(3)
