import pyray

from objects.text import Text
from objects.cherry import Cherry
from scenes.base import BaseScene
from settings import Settings


class CherryTest(BaseScene):
    def __init__(self):
        super().__init__()

    def set_up_objects(self):
        self.objects = [
            Text(100, 25, "Check class Cherry", 24),
            Cherry(),
        ]

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
