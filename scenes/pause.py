import pyray
from raylib import colors

from objects.text import Text
from scenes.base import BaseScene
from settings import Settings
from game_objects.seeds import Energizer


class PauseScene(BaseScene):
    def __init__(self):
        self.hello_text = Text(Settings.WIDTH // 2, Settings.HEIGHT // 2, "<- Energizer (big seed)", 32, colors.YELLOW)
        self.seed = Energizer(Settings.WIDTH // 2 - 100, Settings.HEIGHT // 2 + 10)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)
        self.objects.append(self.seed)

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(0)
