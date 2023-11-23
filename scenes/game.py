import pyray
import raylib
from raylib import colors

from objects.text import Text
from scenes.base import BaseScene
from settings import Settings

from game_objects.pacman import PacmanLogic
from game_objects.pole import LogicPole


class GameScene(BaseScene):  # Сцена 2
    def __init__(self):
        self.hello_text = Text(Settings.WIDTH // 2, Settings.HEIGHT // 2, "Game", 32, colors.GREEN)
        self.pacman = PacmanLogic(0, 0)
        self.pole = LogicPole()
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)
        self.objects.append(self.pacman)
        self.objects.append(self.pole)

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_M):
            Settings.set_scene(0)

