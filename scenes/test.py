import pyray
from raylib import colors

from objects.animated import Animated
from objects.text import Text
from scenes.base import BaseScene
from settings import Settings


class TestScene(BaseScene):
    def __init__(self):
        self.pacman = Animated(Settings.WIDTH // 2, Settings.HEIGHT // 2, 40, 40)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.pacman)
    

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)